# MLOps CI/CD Pipeline

A lightweight MLOps project demonstrating an automated CI pipeline for a containerized FastAPI service using **GitHub Actions, Docker, Pytest, and Flake8**.

The project focuses on software quality and deployment automation by validating code, running unit tests, building a Docker container, launching the API, and performing an end-to-end smoke test automatically after each push to the `main` branch.

## CI Pipeline

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ▼
Install Dependencies
   │
   ▼
Run Unit Tests (Pytest)
   │
   ▼
Lint Code (Flake8)
   │
   ▼
Build Docker Image
   │
   ▼
Run FastAPI Container
   │
   ▼
Smoke Test /predict Endpoint
```

A failed step stops the pipeline, helping prevent broken code from progressing further.

## Features

- FastAPI REST API
- Deterministic feature hashing
- Input validation
- Automated unit testing with Pytest
- Code quality checks with Flake8
- Docker containerization
- Automated GitHub Actions workflow
- API smoke testing after container startup
- Stop-the-line CI behavior when a validation step fails

## API

The application exposes a simple prediction-style endpoint:

```http
GET /predict?text=mlops
```

Example response:

```json
{
  "bucket": 4
}
```

The endpoint converts text into a deterministic bucket using MD5-based feature hashing. It serves as a lightweight application for demonstrating the CI and containerization workflow rather than as a trained machine-learning model.

## Project Structure

```text
mlops-cicd-pipeline/
│
├── .github/
│   └── workflows/
│       └── main.yml
│
├── app/
│   ├── features.py
│   └── main.py
│
├── tests/
│   └── test_features.py
│
├── Dockerfile
├── requirements.txt
├── smoke_test.py
├── .gitignore
└── README.md
```

## Testing

The unit tests verify:

- Deterministic hashing for identical inputs
- Bucket values remain within the expected range
- Invalid non-positive bucket counts are rejected

Run the tests locally:

```bash
python -m pytest tests/test_features.py
```

Run linting:

```bash
python -m flake8 app tests
```

## Run Locally

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the API:

```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## Docker

Build the Docker image:

```bash
docker build -t mlops-app .
```

Run the container:

```bash
docker run -p 8000:8000 mlops-app
```

Then run the smoke test:

```bash
python smoke_test.py
```

## Technologies

- Python
- FastAPI
- Uvicorn
- Pytest
- Flake8
- Docker
- GitHub Actions
- REST API

## What This Project Demonstrates

This project demonstrates practical CI and MLOps engineering concepts including:

- Continuous Integration
- Automated quality gates
- Unit and smoke testing
- Containerized application delivery
- Reproducible application environments
- Automated validation on Git pushes
- Fail-fast / stop-the-line development practices
