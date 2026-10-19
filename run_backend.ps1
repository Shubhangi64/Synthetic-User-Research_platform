$ErrorActionPreference = 'Stop'
if (Test-Path '.venv\Scripts\Activate.ps1') { . '.venv\Scripts\Activate.ps1' }
Write-Host 'Starting FastAPI backend at http://localhost:8000' -ForegroundColor Cyan
python -m uvicorn backend.main:app --reload --port 8000
