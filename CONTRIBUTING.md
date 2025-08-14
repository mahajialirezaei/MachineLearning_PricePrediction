# Contributing

Thank you for your interest in contributing to this project! This document explains how to get started quickly, coding conventions, how to open issues and pull requests, and important notes about data and reproducibility.

---

## Quick Start
1. Fork and clone the repository:
   ```bash
   git clone https://github.com/<your-username>/MachineLearning_PricePrediction.git
   cd MachineLearning_PricePrediction

2. Create and activate a virtual environment (recommended: Python >= 3.9):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS / Linux
   .venv\Scripts\activate         # Windows (PowerShell)
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run basic tests:

   ```bash
   pytest -q
   ```

---

## Smoke Run (Quick check)

To ensure your changes don't break basic functionality, run a quick smoke test:

```bash
# Example: run a small training job if train.py exists
python train.py --sample 1000 --seed 42
```

If `train.py` is not present, add a reproducible script that reads a sample of data and trains a small model.

---

## Coding Style & Best Practices

* Commit frequently and keep commits focused. Use meaningful commit messages.
* Commit message convention: follow Conventional Commits. Examples:

  ```
  feat: add seed handling to train.py
  fix: handle missing values in preprocess
  chore: update requirements.txt
  ```
* Formatting:

  * Use `black` and `isort` for Python formatting. CI will enforce these rules.
  * Provide docstrings for public functions/classes (Google or NumPy style acceptable).
* Use type hints for public functions and methods.
* Separate concerns: put data loading in `data.py`, feature engineering in `features.py`, model code in `models.py`, and runnable scripts in `train.py` / `predict.py`.

---

## Tests & Continuous Integration

* Add tests for any significant change. Use `pytest`.
* Tests should be fast and deterministic (use fixed random seeds).
* CI (GitHub Actions) should run on every PR and include:

  * dependency installation
  * linting (`black --check`, `isort --check`, `flake8`)
  * running `pytest`
  * a small smoke test for the pipeline (if feasible)
* Target test coverage for core modules: 70%–80% (flexible for small PRs).

---

## Data & Large Files

* **Do not** commit large raw datasets directly to the repository.
* If a small sample dataset is permissible (e.g., 1000 rows), place it under `data/sample/` and list larger files in `.gitignore`.
* Consider DVC or external storage (Google Drive, AWS S3) for large datasets.
* Preprocessing should be reproducible and definable in scripts (i.e., running a pipeline command should reproduce the same cleaned data).
* If data is sensitive, document anonymization steps in `DATA_README.md`.

---

## How to Propose Changes (Issue → PR)

1. Open an Issue describing the bug or feature. Use the issue template if appropriate.
2. Create a new branch named `feat/<short-desc>` or `fix/<short-desc>`:

   ```bash
   git checkout -b feat/add-train-seed
   ```
3. Implement changes and add tests, then commit and push:

   ```bash
   git add .
   git commit -m "feat: add fixed seed to train.py"
   git push origin feat/add-train-seed
   ```
4. Open a Pull Request with a clear description. Use the PR template.

---

## Suggested Issue Template

(Place as `.github/ISSUE_TEMPLATE/bug_report.md` or similar)

```markdown
### Title
(Short summary of the issue or feature)

### Description
Full description of the bug or requested feature.

### Steps to reproduce (for bugs)
1. Step one
2. Step two

### Current and expected behavior
- Current:
- Expected:

### Environment
- OS:
- Python version:
- Dependencies (from requirements.txt):
```

---

## Suggested Pull Request Template

(Place as `.github/PULL_REQUEST_TEMPLATE.md`)

```markdown
## Type of change
- [ ] feat
- [ ] fix
- [ ] docs
- [ ] chore
- [ ] refactor
- [ ] test

## Summary of changes
(A concise description of changes)

## Pre-merge checklist
- [ ] Code formatted (`black` / `isort`)
- [ ] New tests added (if applicable)
- [ ] Tests run locally
- [ ] No large data files added
- [ ] README/NOTES updated (if applicable)

## How to test
(Example commands to run tests or a smoke-run)
```

---

## Pre-merge Checklist

* CI passes for the branch
* Relevant tests pass
* Commit messages follow conventional commits
* Documentation (README, DATA\_README, or NOTES) updated as needed
* Large data files are excluded via `.gitignore` or linked externally

---

## Notebooks & Results

* When adding EDA or experiment notebooks, include either:

  * the `.ipynb` file with a short HTML or markdown summary, or
  * an exported HTML version for easier review.
* Place experiment outputs (small CSVs, model artifacts) under `results/`. For large artifacts, provide download links instead of committing them.

---

## Reproducibility

* Always fix random seeds for experiments.
* Record environment dependencies in `requirements.txt` (or `environment.yml`).
* Provide scripts to reproduce experiments end-to-end (data preparation → training → evaluation).

---

## Contact & Help

If you need help:

* Open an Issue with the `help-wanted` label.
* For urgent matters, mention a maintainer (e.g., `@mahajialirezaei`) in the Issue or PR.

Thank you for contributing — even a small documentation fix or an extra test helps a lot!

```
::contentReference[oaicite:0]{index=0}
```
