/**
 * Centralized API & WebSocket Endpoint Resolver for Senate AI
 * Defaults to the local development environment unless explicitly configured.
 */

export function getApiBaseUrl(): string {
  const envUrl = import.meta.env.VITE_API_URL;
  if (envUrl && envUrl.trim().length > 0) {
    return envUrl.replace(/\/$/, "");
  }

  return "http://localhost:8000";
}

export function getApiUrl(endpointPath: string): string {
  const base = getApiBaseUrl();
  const cleanPath = endpointPath.startsWith("/") ? endpointPath : `/${endpointPath}`;
  return `${base}${cleanPath}`;
}

export function getWsUrl(): string {
  const envWs = import.meta.env.VITE_WS_URL;
  if (envWs && envWs.trim().length > 0) {
    return envWs;
  }

  return "ws://localhost:8000/ws/chat";
}
