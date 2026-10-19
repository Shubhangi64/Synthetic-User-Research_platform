# Generation of AI-Powered Synthetic Users for Product Research

A Python research prototype that generates synthetic personas and simulates product-research surveys and interviews. It includes question checks, persona consistency checks, response-quality indicators, insight summaries, and downloadable research reports.

> **Research limitation:** synthetic responses are simulations, not real participant data. Treat findings as hypotheses and validate important conclusions with human participants.

## Demonstration use case

- **Product:** AI Personal Shopping Platform
- **Audience:** Online shoppers aged 18–40
- **Goal:** Explore shopper preferences, expectations, concerns, and responses to AI-powered shopping features.
- **Streamlit defaults:** four personas and up to three research questions.

## Main features

- Synthetic persona profiles
- Survey Mode for comparing responses
- Interview Mode with multi-turn context
- Question relevance and persona consistency checks
- Response-quality indicators
- Theme, sentiment, and willingness-to-use summaries
- JSON/CSV results and PDF research report
- Configurable Ollama, Gemini, or demo provider (depending on `.env` settings)

## Three milestones

1. **Planning and design** — problem definition, use case, requirements, and system plan.
2. **Synthetic-user foundation** — research workspace, persona structure/generation, and interview context.
3. **Simulation, insights, and reporting** — survey/interview workflows, checks, evaluation indicators, insights, PDF export, and basic end-to-end verification.

See `docs/MILESTONE_1.md`, `docs/MILESTONE_2.md`, and `docs/MILESTONE_3.md` for details.

## Requirements

- Python 3.10 or newer recommended
- VS Code or another Python editor
- Ollama with a model such as `llama3.2` for local runs, or a configured Gemini API key. Demo mode can be used for basic UI/pipeline checks.

## Run locally on Windows

Open the project folder in VS Code. In the terminal, run these commands from the project root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

If `.env` already exists, do not overwrite it. Check its settings against `.env.example`. For Ollama, ensure the configured model is installed:

```powershell
ollama list
ollama pull llama3.2
```

Start the backend in Terminal 1:

```powershell
python -m uvicorn backend.main:app --reload --port 8000
```

Start Streamlit in Terminal 2:

```powershell
.venv\Scripts\Activate.ps1
streamlit run app.py
```

Open `http://localhost:8501`. API health and documentation are available at `http://localhost:8000/health` and `http://localhost:8000/docs`.

## Run tests

```powershell
python -m pytest -q
```

If pytest is missing, install it with `pip install pytest`.

## Project structure

- `backend/` — FastAPI application
- `frontend/` — Streamlit research interface
- `src/` — research workflow, agents, model clients, insights, and reports
- `data/` — example experiment and persona data
- `tests/` — automated tests
- `docs/` — the three milestone summaries

## Responsible interpretation

Themes, sentiment, and scores are exploratory automated indicators, not ground truth. Do not present generated personas as actual people. Keep API keys and other secrets out of source control; `.env` is excluded by `.gitignore`.

## License

Released under the MIT License. See `LICENSE`.
