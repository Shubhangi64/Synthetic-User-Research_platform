# 🤖 Generation of AI-Powered Synthetic Users for Product Research

A Python-based Generative AI research prototype for generating synthetic
user personas, simulating product-research surveys and interviews,
checking question relevance and persona consistency, evaluating response
quality, extracting insights, and exporting a PDF research report.

**Python** · **Streamlit** · **FastAPI** · **Pydantic** · **LangGraph /
modular agents** · **Ollama / Gemini** · **ReportLab**

> **Important:** Synthetic users are AI-generated simulations, not real
> participants. Their responses can help explore hypotheses but are not
> statistically representative and do not replace research with real
> users.

## 📖 Table of Contents

-   [Overview](#-overview)
-   [Problem Statement](#-problem-statement)
-   [Project Objectives](#-project-objectives)
-   [Key Features](#-key-features)
-   [Case Study](#-case-study)
-   [Target Audience](#-target-audience)
-   [System Architecture](#-system-architecture)
-   [Research Workflow](#-research-workflow)
-   [AI Agent Architecture](#-ai-agent-architecture)
-   [Persona Model and Consistency](#-persona-model-and-consistency)
-   [Technology Stack](#-technology-stack)
-   [Project Structure](#-project-structure)
-   [API Design](#-api-design)
-   [Development Status and
    Milestones](#-development-status-and-milestones)
-   [Example Research Scenario](#-example-research-scenario)
-   [Security and Reliability](#-security-and-reliability)
-   [Research Limitations](#-research-limitations)
-   [Future Improvements](#-future-improvements)
-   [Local Development on Windows](#-local-development-on-windows)
-   [Running Tests](#-running-tests)
-   [Git Workflow](#-git-workflow)
-   [Documentation](#-documentation)
-   [Project Vision](#-project-vision)
-   [Disclaimer](#-disclaimer)
-   [License](#-license)

## 📌 Overview

Product teams often want to understand how potential users might react
to a product concept before investing substantial time and resources in
development. Traditional research may involve recruiting participants,
designing surveys, scheduling interviews, collecting responses,
reviewing qualitative feedback, and preparing reports. These activities
are valuable, but they can be costly and time-consuming during early
product exploration.

This project explores how Generative AI can support **early-stage
exploratory product research** by generating synthetic personas and
simulating their responses to research questions. A researcher defines a
product, target audience, and research objective. The application uses a
small panel of synthetic personas to simulate survey answers and
conversational interviews, then applies question checks, consistency
checks, response evaluation, insight extraction, and report generation.

The current demonstration is based on an **AI Personal Shopping
Platform** for online shoppers aged 18--40.

## ❗ Problem Statement

Early-stage product teams may need to explore questions such as:

-   Which product features might potential users value?
-   What concerns could reduce trust or adoption?
-   How might people with different preferences respond to the same
    feature?
-   Are research questions clear, relevant, and answerable?
-   What themes appear across a collection of exploratory responses?

The project investigates a workflow that combines:

``` text
Generative AI
     +
Synthetic Personas
     +
Survey and Interview Simulation
     +
Question and Consistency Checks
     +
Response Evaluation
     +
Insight Extraction and Reporting
```

## 🎯 Project Objectives

1.  Generate structured synthetic personas with different backgrounds,
    preferences, and behaviors.
2.  Provide a research workspace for defining the product, audience, and
    research objective.
3.  Simulate survey responses from multiple personas for side-by-side
    comparison.
4.  Support multi-turn interviews with a selected synthetic persona.
5.  Check question relevance, clarity, and answerability.
6.  Identify possible persona inconsistencies and provide
    response-quality indicators.
7.  Summarize themes, sentiment tendencies, concerns, and
    willingness-to-use results.
8.  Save structured results and generate a downloadable PDF report.
9.  Keep the implementation modular for incremental testing and
    improvement.

## ✨ Key Features

### 👤 Synthetic Persona Panel

The current Streamlit prototype runs with **four personas per research
run**. Persona records can include demographic details, occupation,
personality, shopping behavior, goals, motivations, preferences, pain
points, and concerns. These profiles are generated or stored as
synthetic examples; they do not represent verified real people.

### 📋 Survey Mode

Survey Mode asks the same research questions to the persona panel and
organizes responses for comparison. It can help explore differences in
feature preferences, price sensitivity, trust, privacy concerns, and
possible product adoption. The current Streamlit workspace accepts **up
to three research questions per run**.

### 💬 Interview Mode

Interview Mode supports follow-up questions to a selected persona. The
persona profile and recent session history are used to guide responses
across multiple turns. Active interview sessions are held in backend
application memory; this is not a durable, production-grade memory
store.

### 🔎 Question Relevance and Answerability

The workflow checks whether research questions appear relevant to the
product and objective and whether they are clear enough to answer.
Questions that fail the configured checks may be blocked for revision
before the research run continues.

### 🧩 Persona Consistency Validation

An automated validation step checks generated responses against persona
details and can flag possible inconsistencies. It is an indicator for
review, not a guarantee of perfect consistency.

### 📊 Response Evaluation and Insight Extraction

The workflow can produce response-quality indicators and summarize:

-   Common themes and sentiment tendencies
-   User concerns and pain points
-   Feature preferences and behavioral patterns
-   Willingness-to-use scores and their distribution
-   Potential product opportunities

These are exploratory, automated outputs rather than ground-truth
measurements of a real population.

### 📄 Research Report Export

The prototype saves structured results locally and can generate a PDF
research report. Outputs are stored under `results/`, organized by
research run. Example outputs are provided under `data/demo_results/`.

### 🔌 Language-Model Provider Options

The LLM adapter supports provider modes configured for the project:

-   **Ollama** for local inference (default example model: `llama3.2`)
-   **Gemini** when a valid API key and model are configured
-   **Demo mode** for basic workflow checks without depending on a live
    model response

Provider availability depends on configuration, model installation,
network connectivity, API quotas, and provider service status.

## 💡 Case Study

### AI Personal Shopping Platform

The demonstration product is an AI-powered personal shopping platform
for online shoppers aged 18--40. The product concept includes:

-   AI product recommendations
-   Price comparison
-   Personalized shopping feeds
-   Review summarization
-   Virtual try-on
-   Price-drop alerts
-   Budget-based shopping
-   Brand comparison and alternative product suggestions

**Research objective:** Understand online shoppers' preferences,
expectations, concerns, and behavioral responses toward an AI-powered
personal shopping platform.

Example research themes include recommendation usefulness, feature
preferences, privacy and data-sharing concerns, trust in sponsored
results, price sensitivity, and willingness to use the platform.

## 👥 Target Audience

**Platform users:** product researchers, student project teams,
early-stage product teams, and developers exploring AI-assisted research
workflows.

**Synthetic audience in the demonstration:** online shoppers aged
**18--40**. The personas represent simulated perspectives and are not a
statistically sampled panel.

## 🏗️ System Architecture

The project separates the Streamlit interface, FastAPI backend, research
services, model adapter, local data files, and report outputs.

``` text
                 PRODUCT RESEARCHER
                         |
                         v
              +------------------------+
              |      Streamlit UI      |
              | Research workspace     |
              | Personas and interview|
              | Results and run guide  |
              +-----------+------------+
                          | REST API
                          v
              +------------------------+
              |     FastAPI Backend    |
              | Health and configuration|
              | Personas               |
              | Research execution     |
              | Interview sessions     |
              | PDF report download    |
              +-----------+------------+
                          |
                          v
              +------------------------+
              | Research Service Layer |
              | Question checks        |
              | Survey simulation      |
              | Validation and scoring |
              | Insight extraction     |
              | Report generation      |
              +-----------+------------+
                          |
                          v
              +------------------------+
              |       LLM Adapter      |
              | Ollama / Gemini / Demo |
              +------------------------+

            Local JSON data and run results
```

This is a functional overview of the prototype, not a claim that every
component is deployed as an independent production service.

## 🔄 Research Workflow

``` text
Define Product and Target Audience
                 |
                 v
       Define Research Objective
                 |
                 v
       Prepare Research Questions
                 |
                 v
        Load Four Personas
                 |
                 v
       Check Question Relevance
                 |
                 v
        Simulate Survey Answers
                 |
                 v
       Validate Persona Consistency
                 |
                 v
        Evaluate Response Quality
                 |
                 v
        Extract Research Insights
                 |
                 v
       Save Structured Run Results
                 |
                 v
          Generate PDF Report
```

Interview Mode is available as a separate interaction flow.

## 🤖 AI Agent Architecture

The codebase contains modular agent and workflow components. Actual
outputs depend on the configured provider and the selected workflow.

1.  **Persona Generation Agent** --- creates or supports structured
    persona information based on the experiment context and target
    audience.
2.  **Survey Agent** --- generates answers to research questions using
    persona characteristics and product context.
3.  **Question Agent** --- checks research question relevance, clarity,
    and answerability; it can stop a run when a question needs revision.
4.  **Validation Agent** --- checks responses against persona details
    and flags possible inconsistencies.
5.  **Evaluation Agent** --- produces response-quality indicators using
    configured evaluation logic. Scores are not ground truth.
6.  **Insight Agent** --- summarizes response patterns, themes,
    sentiment tendencies, and willingness-to-use results.
7.  **Workflow Orchestration and Report Generation** --- coordinates the
    research steps and generates a structured result and PDF report.

## 🧑‍🎭 Persona Model and Consistency

A persona record can include:

-   Name, age, occupation, and location
-   Income or budget preference
-   Personality traits and communication style
-   Decision-making style
-   Shopping frequency and price sensitivity
-   Brand loyalty and review dependence
-   Technology adoption and impulse buying
-   Goals, motivations, pain points, and concerns
-   Preferred categories, brands, and product factors
-   A profile summary

Illustrative example (not necessarily a record in the current dataset):

``` text
SYNTHETIC PERSONA
-----------------
Name: Example Shopper
Age: 29
Occupation: Working Professional
Personality: Practical and price-conscious
Shopping behavior: Compares prices and reads reviews
Goal: Find suitable products within a budget
Concern: Inaccurate recommendations and sponsored results
```

Consistency is supported by combining the selected persona profile with
recent interview history:

``` text
Core Persona Profile
         +
Recent Interview History
         |
         v
    Interview Logic
         |
         v
   Persona Response
```

Active interview sessions currently live in backend memory. Persistent
storage across restarts, advanced memory retrieval, and long-term memory
summarization are potential future improvements. Automated checks can
flag contradictions but cannot guarantee every response will be
consistent.

## 🛠️ Technology Stack

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  Python                              Main programming language and
                                      research workflow

  Streamlit                           Research user interface

  FastAPI                             Backend REST API

  Pydantic                            Request and response schema
                                      validation

  LangGraph / modular agents          Organizing research and agent
                                      workflow components

  Ollama                              Local LLM inference option

  Gemini API                          Optional hosted model provider

  Pandas                              Tabular result handling

  ReportLab                           PDF report generation

  Requests                            HTTP communication between UI and
                                      backend

  pytest                              Automated test framework

  JSON                                Experiment, persona, and structured
                                      result files
  -----------------------------------------------------------------------

The documented local workflow does **not** require React, Vite, or
PostgreSQL. Experiment settings and persona examples are stored in local
JSON files.

## 📁 Project Structure

``` text
synthetic-user-research-platform/
|
├── app.py                       # Streamlit entry point
├── backend/
│   └── main.py                  # FastAPI endpoints
├── frontend/
│   └── app.py                   # Streamlit interface implementation
├── src/
│   ├── agents/
│   │   ├── persona_agent.py
│   │   ├── survey_agent.py
│   │   ├── question_agent.py
│   │   ├── validation_agent.py
│   │   ├── evaluation_agent.py
│   │   ├── insight_agent.py
│   │   └── orchestrator.py
│   ├── llm/client.py            # Ollama/Gemini/demo adapter
│   ├── models/schemas.py
│   ├── config.py
│   ├── experiment.py
│   ├── personas.py
│   ├── survey.py
│   ├── interview.py
│   ├── question_validator.py
│   ├── validation.py
│   ├── evaluation.py
│   ├── insights.py
│   ├── report.py
│   └── service.py
├── data/
│   ├── experiment.json
│   ├── personas.json
│   ├── personas_generated.json
│   └── demo_results/
├── results/                     # Local run outputs
├── tests/
│   ├── test_core.py
│   ├── test_research_workflow.py
│   └── test_llm_client.py
├── docs/
│   ├── MILESTONE_1.md
│   ├── MILESTONE_2.md
│   └── MILESTONE_3.md
├── .env.example
├── .gitignore
├── requirements.txt
├── PROJECT_ROADMAP.md
├── RUN_IN_VSCODE.md
├── Dockerfile.api
├── Dockerfile.ui
├── docker-compose.yml
├── LICENSE
└── README.md
```

Generated files may be created locally after running the application;
the tree highlights the main source and documentation files.

## 🔌 API Design

The current FastAPI backend exposes these routes:

  -----------------------------------------------------------------------
  Method                  Endpoint                Purpose
  ----------------------- ----------------------- -----------------------
  `GET`                   `/health`               Check API and LLM
                                                  provider health

  `GET`                   `/config`               Return experiment and
                                                  provider configuration

  `GET`                   `/personas?limit=4`     Load personas; limit
                                                  must be between 1 and 4

  `POST`                  `/research/run`         Run the research
                                                  workflow

  `POST`                  `/interview/ask`        Ask a question to a
                                                  selected persona

  `GET`                   `/report/{run_id}`      Download a PDF report
                                                  for a completed run
  -----------------------------------------------------------------------

Interactive API documentation is available at
`http://localhost:8000/docs` when the backend is running.

## 🚧 Development Status and Milestones

The project is organized into three milestones. The descriptions below
summarize the prototype's scope; they do not imply that every possible
scenario has passed end-to-end testing.

### Milestone 1 --- Planning and Design

-   Define the problem and research use case.
-   Identify the product, target audience, and research objective.
-   Document system architecture and research workflow.
-   Plan persona attributes and evaluation approach.

### Milestone 2 --- Synthetic-User Foundation

-   Set up the Python project structure.
-   Create experiment and persona data structures.
-   Implement the Streamlit research workspace.
-   Add backend endpoints and the LLM provider adapter.
-   Support synthetic personas and interview context.

### Milestone 3 --- Simulation, Insights, and Reporting

-   Coordinate survey and interview workflows.
-   Add question relevance and answerability checks.
-   Add persona consistency validation.
-   Add response-quality evaluation indicators.
-   Extract insights and willingness-to-use summaries.
-   Save structured outputs and generate a PDF report.
-   Run automated tests and verify the workflow locally.

**Current prototype constraints:** four personas per research run and up
to three questions in the Streamlit workspace. Model calls can fail due
to provider availability, configuration, network problems, or quota
limits. See `PROJECT_ROADMAP.md` and `docs/MILESTONE_1.md`,
`docs/MILESTONE_2.md`, and `docs/MILESTONE_3.md` for more detail.

## 🧪 Example Research Scenario

**Product:** AI Personal Shopping Platform\
**Target audience:** Online shoppers aged 18--40\
**Research objective:** Understand preferences, expectations, concerns,
and likely responses to an AI-powered personal shopping platform.

Example questions:

1.  How useful would AI-powered product recommendations be when shopping
    online?
2.  Which features would be most useful: personalized feeds,
    budget-based shopping, or alternative product suggestions?
3.  How comfortable would you be sharing shopping preferences and
    personal data with an AI shopping platform?

The four synthetic personas respond according to their stored profile
and the experiment context. The workflow can then check questions and
persona consistency, evaluate response quality, summarize themes and
willingness-to-use scores, and prepare a report. Potential themes
include convenience, price comparison, trust, privacy, sponsored
placement, and review quality; actual findings should be taken from each
run's output rather than assumed in advance.

## 🔐 Security and Reliability

-   Store API keys and private configuration in `.env`, not in committed
    source files.
-   Use `.env.example` as a template and configure values locally.
-   Do not submit real personal or sensitive participant data to an LLM
    provider without appropriate permission and safeguards.
-   Check provider configuration and model availability before starting
    a run.
-   Review generated outputs instead of treating them as verified facts.
-   Label personas and results clearly as synthetic.

This is an academic prototype, not a production system with a complete
authentication, authorization, and privacy-governance layer.

## ⚠️ Research Limitations

Synthetic responses are affected by model behavior, prompt design,
persona attributes, product descriptions, and conversation context.
Potential limitations include model-generated bias, repetitive answers,
prompt sensitivity, inaccurate claims, limited representation of
uncommon experiences, and evaluation scores that disagree with human
judgment.

Use results to develop hypotheses and improve research questions.
Validate important findings with real participants before making
significant product decisions.

## 📈 Future Improvements

-   Compare synthetic responses with responses from real participants.
-   Evaluate automated quality scores against human ratings.
-   Improve persona diversity and persona-generation validation.
-   Add persistent interview memory and conversation retrieval.
-   Make insights traceable to source responses.
-   Add richer visualizations and cross-run comparisons.
-   Expand evaluation metrics, logging, and error handling.
-   Add experiment history and more robust storage.
-   Improve model/provider selection and usage tracking.
-   Increase automated test coverage and reproducibility.

## 🖥️ Local Development on Windows

### Prerequisites

-   Python 3.10 or newer recommended
-   VS Code or another Python editor
-   Git (optional, for version control)
-   Ollama with a compatible local model **or** a configured Gemini API
    key
-   Internet access to install packages or call a hosted provider

### 1. Open the project

Open the `synthetic-user-research-platform` directory in VS Code. Run
commands from the project root in PowerShell.

### 2. Create the virtual environment and install dependencies

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

If `.env` already exists, do not overwrite it. Compare its settings with
`.env.example` instead.

### 3. Configure the model provider

For local Ollama, confirm that Ollama is running and the model is
installed:

``` powershell
ollama list
ollama pull llama3.2
```

Review `.env` and set the provider you want to use. The project supports
`ollama`, `gemini`, and `demo` modes. For Gemini, configure a valid API
key and model. Never commit `.env` or API keys to Git.

### 4. Start the FastAPI backend

Open **Terminal 1** in VS Code and run:

``` powershell
.venv\Scripts\Activate.ps1
python -m uvicorn backend.main:app --reload --port 8000
```

-   API health: `http://localhost:8000/health`
-   Interactive API documentation: `http://localhost:8000/docs`

### 5. Start the Streamlit interface

Open **Terminal 2** in the project root:

``` powershell
.venv\Scripts\Activate.ps1
streamlit run app.py
```

Open the URL printed in the terminal, usually `http://localhost:8501`.
Keep both terminals running while using the application.

### 6. Check backend and model status

Use **Check backend and model** in the Streamlit sidebar or open
`http://localhost:8000/health`. If a research run fails, check the
FastAPI terminal and confirm that the selected model provider is
available.

## 🧪 Running Tests

With the virtual environment active, run from the project root:

``` powershell
python -m pytest -q
```

If pytest is not installed:

``` powershell
pip install pytest
python -m pytest -q
```

Record the actual local test result. Do not report tests as passing
unless they have been executed successfully.

## 🌿 Git Workflow

A typical workflow is:

``` powershell
git status
git add .
git commit -m "Describe the change"
git push
```

Before committing, confirm `.env`, `.venv/`, Python cache files, and
secrets are excluded by `.gitignore`. Pushing to GitHub requires a
configured remote repository and suitable authentication.

## 📚 Documentation

-   `PROJECT_ROADMAP.md` --- three-milestone roadmap and future work.
-   `docs/MILESTONE_1.md` --- planning and design.
-   `docs/MILESTONE_2.md` --- synthetic-user foundation.
-   `docs/MILESTONE_3.md` --- simulation, insights, and reporting.
-   `RUN_IN_VSCODE.md` --- Windows/VS Code setup and troubleshooting.
-   `data/demo_results/README.md` --- example output information.

## 🗺️ Project Roadmap

``` text
Milestone 1: Planning and Design
              |
              v
Milestone 2: Synthetic-User Foundation
              |
              v
Milestone 3: Simulation, Insights, and Reporting
              |
              v
Future Work: Human Validation, Better Memory,
             Expanded Evaluation, and Experiment History
```

## 🌟 Project Vision

The long-term vision is to provide an accessible environment for product
teams and student researchers to explore possible user perspectives
before conducting formal research with real participants.

``` text
Product Idea
     |
     v
Research Objective
     |
     v
Synthetic Personas
     |
     v
Survey / Interview Simulation
     |
     v
Response Checks and Evaluation
     |
     v
Research Insights
     |
     v
Structured Report
```

## 📜 Disclaimer

This project is an academic research prototype. Synthetic personas and
their responses are AI-generated simulations. They are not real people,
real survey participants, or statistically representative samples of a
target population. Automated evaluations and insights may contain errors
or bias. Validate important conclusions through appropriate research
with real users.

## 📄 License

This project is distributed under the MIT License. See the `LICENSE`
file for the license text.

------------------------------------------------------------------------

**Project:** Generation of AI-Powered Synthetic Users for Product
Research\
**Status:** Academic prototype developed across three milestones\
**Demonstration use case:** AI Personal Shopping Platform
