# ACEest Fitness & Gym DevOps Project

This project demonstrates a complete DevOps pipeline using:

- Flask Application
- Git & GitHub
- Pytest Testing
- Docker Containerization
- GitHub Actions CI Pipeline
- Jenkins Build Automation

--------------------------------------------------

## Running Application Locally

Install dependencies

pip install -r requirements.txt

Run application

python app.py

Open browser

http://localhost:5000

--------------------------------------------------

## Running Tests

pytest

--------------------------------------------------

## Docker Setup

Build Docker Image

docker build -t gym-app .

Run Container

docker run -p 5000:5000 gym-app

--------------------------------------------------

## GitHub Actions CI Pipeline

Pipeline automatically runs when code is pushed.

Steps:
1. Checkout Code
2. Install Dependencies
3. Run Pytest
4. Build Docker Image

--------------------------------------------------

## Jenkins Integration

Jenkins pulls latest code from GitHub and performs:

1. Dependency installation
2. Pytest execution
3. Docker image build

This ensures the application builds successfully in a separate environment.


## Folder Structure

ACEest-Gym-DevOps
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── tests
│   └── test_app.py
│
└── .github
    └── workflows
         main.yml