$ErrorActionPreference = "Stop"

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = "C:\Users\satvi\AppData\Local\Programs\Python\Python311\python.exe"

if (-not (Test-Path $pythonExe)) {
    throw "Python 3.11 was not found at $pythonExe. Install it first and rerun this script."
}

if (-not (Test-Path (Join-Path $repo ".venv\Scripts\python.exe"))) {
    Write-Host "Creating Python virtual environment..."
    & $pythonExe -m venv (Join-Path $repo ".venv")
}

$venvPython = Join-Path $repo ".venv\Scripts\python.exe"
Write-Host "Installing backend dependencies..."
& $venvPython -m pip install --upgrade pip | Out-Null
& $venvPython -m pip install -r (Join-Path $repo "backend\requirements.txt")

Write-Host "Installing frontend workspace dependencies..."
& "C:\Program Files\Git\bin\sh.exe" -lc "cd /c/Users/satvi/Downloads/Nexus-AI/Nexus-AI-main && pnpm install"

$backendCommand = @(
    "Set-Location '$repo';",
    "& '$venvPython' -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload"
) -join " "

$frontendCommand = @(
    "Set-Location '$repo';",
    "& 'C:\Program Files\Git\bin\sh.exe' -lc 'cd /c/Users/satvi/Downloads/Nexus-AI/Nexus-AI-main && pnpm --filter @workspace/nexus-ai dev -- --host 0.0.0.0 --port 5173'"
) -join " "

Write-Host "Starting backend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", $backendCommand

Write-Host "Starting frontend..."
Start-Process powershell -ArgumentList "-NoExit", "-Command", $frontendCommand

Write-Host ""
Write-Host "Project started."
Write-Host "Backend: http://localhost:8000"
Write-Host "Frontend: http://localhost:5173"
Write-Host ""
Write-Host "If the database is not configured, the backend will still start but DB features may not work."
