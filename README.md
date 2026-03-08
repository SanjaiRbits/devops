# ACEest Fitness & Gym — DevOps CI/CD Pipeline

## Project Overview

This project implements a **Flask-based REST API** for managing ACEest Fitness & Gym services.
It demonstrates a complete **DevOps workflow** including:

* Git version control
* Automated testing using Pytest
* Docker containerization
* CI pipeline using GitHub Actions
* Jenkins build automation

The goal is to showcase how modern DevOps practices automate **build, test, and deployment workflows**.

---

# Local Setup & Execution

## Prerequisites

Install the following tools before running the project:

* Python 3.10+
* pip
* Docker Desktop
* Git

---

## Clone the Repository

```bash
git clone https://github.com/SanjaiRbits/devops.git
cd devops
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Flask Application

```bash
python ACEest_Fitness_Gym/app.py
```

The application will run at:

```
http://localhost:5000
```

---

# API Endpoints

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | `/`               | Health check                |
| GET    | `/programs`       | List available gym programs |
| GET    | `/program/<name>` | Get program details         |
| POST   | `/calories`       | Calculate calories burned   |
| GET    | `/clients`        | List all registered clients |
| POST   | `/clients`        | Add a new client            |

---

# Running Tests

This project uses **Pytest** for automated testing.

Run all tests:

```bash
pytest ACEest_Fitness_Gym/tests
```

Expected result:

```
9 passed
```

---

# Docker

## Build Docker Image

```bash
docker build -t aceest-gym-app .
```

---

## Run Docker Container

```bash
docker run -p 5000:5000 aceest-gym-app
```

Application will be available at:

```
http://localhost:5000
```

---

## Run Tests Inside Container

```bash
docker run --rm aceest-gym-app pytest ACEest_Fitness_Gym/tests
```

---

# GitHub Actions CI/CD Pipeline

**Workflow File**

```
.github/workflows/main.yml
```

## Pipeline Trigger

The CI pipeline runs automatically on:

* Push to the **main branch**
* Pull requests targeting **main**

---

## CI Pipeline Stages

| Stage                | Description                           |
| -------------------- | ------------------------------------- |
| Checkout Code        | Retrieves latest code from repository |
| Setup Python         | Installs Python environment           |
| Install Dependencies | Installs required Python packages     |
| Run Pytest           | Executes unit tests                   |
| Docker Build         | Builds Docker container image         |

The pipeline ensures that **tests pass before Docker images are built**.

---

# Jenkins Build Automation

Jenkins is executed locally using Docker.

Start Jenkins:

```bash
docker run -p 8080:8080 -p 50000:50000 --name jenkins jenkins/jenkins:lts
```

Access Jenkins at:

```
http://localhost:8080
```

---

## Jenkins Pipeline Job

**Job Name**

```
gym-devops-build
```

### Configuration

| Setting        | Value                                     |
| -------------- | ----------------------------------------- |
| Source Control | GitHub Repository                         |
| Repository URL | https://github.com/SanjaiRbits/devops.git |
| Branch         | main                                      |

---

## Jenkins Build Script

```bash
pip install -r requirements.txt
pytest ACEest_Fitness_Gym/tests
```

Jenkins acts as an **additional quality gate** ensuring all tests pass before builds succeed.

---

# Project Structure

```
devops/
│
├── ACEest_Fitness_Gym/
│   ├── __init__.py
│   ├── app.py
│   └── tests/
│       └── test_app.py
│
├── Dockerfile
├── requirements.txt
├── README.md
├── .dockerignore
├── .gitignore
│
└── .github/
    └── workflows/
        └── main.yml
```

---

# DevOps Workflow

```
Developer pushes code to GitHub
        ↓
GitHub Actions CI pipeline runs
        ↓
Dependencies installed
        ↓
Pytest executes automated tests
        ↓
Docker image is built
        ↓
Jenkins pulls repository and verifies build
```

---

# Student Details

**Student ID:** 2024tm93548
**Course:** Introduction to DevOps (CSIZG514 / SEZG514)
**Institution:** BITS Pilani WILP
