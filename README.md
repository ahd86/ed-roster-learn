   # Clinical Roster (learning project)

   A configurable rostering app for clinical services, built from scratch to learn
   FastAPI, Git/GitHub workflow, CI and deployment. ED is the first service
   configuration; HITH and others follow. All data is fictional.

   ## Run
       uv sync
       uv run uvicorn app.main:app --reload

   ## Test
       uv run pytest -q && uv run ruff check .

   See docs/PLAN.md for the plan and docs/services/ for each service's requirements.