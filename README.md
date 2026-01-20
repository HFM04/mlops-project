# MLOps Project - Milestone 0

A reproducible Python environment with automated CI validation.

[![CI](https://github.com/HFM04/mlops-project/actions/workflows/ci.yml/badge.svg)](https://github.com/HFM04/mlops-project/actions/workflows/ci.yml)

## Setup

### Prerequisites
- Python 3.10
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/repo.git
   cd repo

2. Create a virtual environment:
python -m venv venv

3. Activate the environment:
Linux/macOS:
  source venv/bin/activate

Windows:
  venv\Scripts\activate

4. Install dependencies:
  pip install -r requirements.txt

5. Verify the installation by running tests:
  pytest -v

Successful test execution confirms that the environment has been created correctly.

## Environment Reproducibility and ML Lifecycle Reliability
Reliable machine learning systems depend on consistent software environments across experimentation, training, and deployment. Small differences in Python versions or library dependencies can lead to silent behavior changes, non-reproducible results, and production failures. This project addresses these risks by enforcing environment reproducibility as a first-class concern.

All Python dependencies are pinned to exact versions in requirements.txt, preventing dependency drift and ensuring deterministic environment recreation. Environment isolation is achieved through the use of virtual environments, which separate project dependencies from system-level Python packages and other projects. In addition, automated validation is implemented using GitHub Actions. The CI workflow provisions a clean Linux environment, installs dependencies from scratch, and executes a smoke test to verify that the environment boots correctly and required libraries load as expected.

By validating the environment early and automatically, these practices improve reliability across the ML lifecycle and increase confidence that models behaving correctly during development will behave consistently when deployed to production systems.

## Project Structure
```bash
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_smoke.py
├── requirements.txt
├── README.md
└── .gitignore
