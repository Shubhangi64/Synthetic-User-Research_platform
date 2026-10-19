# Run the Project in VS Code (Windows)

1. Open this folder in VS Code and choose **Terminal → New Terminal**.
2. Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

If `.env` already exists, do not overwrite it. Check its settings against `.env.example`.

3. For local Ollama, confirm the configured model is installed:

```powershell
ollama list
ollama pull llama3.2
```

4. Start the API in Terminal 1:

```powershell
python -m uvicorn backend.main:app --reload --port 8000
```

5. Start Streamlit in Terminal 2:

```powershell
.venv\Scripts\Activate.ps1
streamlit run app.py
```

Open `http://localhost:8501`. The demo defaults to four personas and up to three research questions. API health and docs are at `http://localhost:8000/health` and `http://localhost:8000/docs`.

6. Run tests if needed:

```powershell
python -m pytest -q
```

## Troubleshooting

- **API connection refused:** make sure the backend is running on port 8000.
- **Ollama connection refused:** start Ollama and check `ollama list`.
- **Model not found:** pull the model configured in `.env`.
- **Missing Python module:** activate `.venv` and run `pip install -r requirements.txt`.
- **PowerShell blocks activation:** run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate again.
