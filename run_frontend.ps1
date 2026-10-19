$ErrorActionPreference = 'Stop'
if (Test-Path '.venv\Scripts\Activate.ps1') { . '.venv\Scripts\Activate.ps1' }
Write-Host 'Starting Streamlit at http://localhost:8501' -ForegroundColor Cyan
streamlit run app.py
