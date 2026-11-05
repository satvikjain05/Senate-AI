import asyncio

import httpx
import pytest
from fastapi import HTTPException

from backend.main import (
    PhishingAnalysisRequest,
    app,
    analyze_phishing_email,
    require_phishing_api_key,
)


def test_phishing_api_key_fails_closed_when_unconfigured(monkeypatch):
    monkeypatch.delenv("PHISHING_API_KEY", raising=False)

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(require_phishing_api_key("test-key"))

    assert exc_info.value.status_code == 503


def test_phishing_api_key_requires_matching_secret(monkeypatch):
    expected_secret = "expected-secret-" + ("x" * 32)
    monkeypatch.setenv("PHISHING_API_KEY", expected_secret)

    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(require_phishing_api_key("incorrect-secret"))

    assert exc_info.value.status_code == 401
    asyncio.run(require_phishing_api_key(expected_secret))


def test_phishing_endpoint_rejects_missing_api_key(monkeypatch):
    monkeypatch.setenv("PHISHING_API_KEY", "expected-secret-" + ("x" * 32))

    async def request():
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            return await client.post(
                "/api/phishing/analyze",
                json={"subject": "Test", "body": "Email body"},
            )

    response = asyncio.run(request())
    assert response.status_code == 401


def test_phishing_request_validates_body():
    with pytest.raises(ValueError):
        PhishingAnalysisRequest(body="")

    with pytest.raises(ValueError):
        PhishingAnalysisRequest(body="x" * 10_001)


def test_phishing_analysis_returns_structured_assessment(monkeypatch):
    captured = {}
    api_key = "expected-secret-" + ("x" * 32)
    monkeypatch.setenv("PHISHING_API_KEY", api_key)

    class FakeOrchestrator:
        def __init__(self):
            pass

        async def run_debate_and_synthesize(self, **kwargs):
            captured.update(kwargs)
            yield {
                "type": "agent_stances_complete",
                "agent_responses": [{"status": "success"}],
            }
            yield {
                "type": "debate_complete",
                "status": "success",
                "full_text": "The message is suspicious.",
                "conflict_analysis": {
                    "phishing_assessment": {
                        "verdict": "likely_phishing",
                        "confidence": 87,
                        "indicators": [
                            {
                                "type": "urgency",
                                "evidence": "It pressures the reader to act immediately.",
                            }
                        ],
                    },
                    "verdict_summary": "The message uses suspicious urgency.",
                    "points_of_agreement": ["The email is urgent."],
                    "points_of_disagreement": [],
                },
            }

    monkeypatch.setattr("backend.main.MultiAgentOrchestrator", FakeOrchestrator)
    async def request():
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            return await client.post(
                "/api/phishing/analyze",
                headers={"X-API-Key": api_key},
                json={"subject": "Act now", "body": "Verify your account."},
            )

    response = asyncio.run(request())
    assert response.status_code == 200
    result = response.json()

    assert result["risk_assessment"]["verdict"] == "likely_phishing"
    assert result["risk_assessment"]["confidence"] == 87
    assert result["risk_assessment"]["indicators"][0]["type"] == "urgency"
    assert result["summary"] == "The message uses suspicious urgency."
    assert "untrusted evidence" in captured["user_query"]
    assert "synthesis_instructions" in captured
    assert "untrusted data" in captured["analysis_system_instructions"]


def test_phishing_analysis_does_not_return_invalid_model_verdict(monkeypatch):
    class FakeOrchestrator:
        def __init__(self):
            pass

        async def run_debate_and_synthesize(self, **kwargs):
            yield {
                "type": "agent_stances_complete",
                "agent_responses": [{"status": "success"}],
            }
            yield {
                "type": "debate_complete",
                "status": "success",
                "full_text": "Model output",
                "conflict_analysis": {
                    "phishing_assessment": {
                        "verdict": "safe",
                        "confidence": 100,
                        "indicators": [],
                    }
                },
            }

    monkeypatch.setattr("backend.main.MultiAgentOrchestrator", FakeOrchestrator)
    with pytest.raises(HTTPException) as exc_info:
        asyncio.run(
            analyze_phishing_email(
                PhishingAnalysisRequest(body="Message body"),
                None,
            )
        )

    assert exc_info.value.status_code == 502
