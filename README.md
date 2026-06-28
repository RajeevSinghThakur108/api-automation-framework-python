# API Automation Framework (Python)

A scalable, maintainable, and production-ready API Automation Framework built using Python, Pytest, and Requests. This project demonstrates industry-standard automation practices, including authentication management, payload handling, reporting, database validation, CI/CD integration, and Docker support.

---

# Features

- REST API Automation
- Reusable API Client
- Session Management
- Configuration Management
- Custom Assertions
- Logging
- Authentication Support
- Environment Management
- Payload Management
- Response Validation
- JSON Schema Validation
- Database Validation
- Retry Mechanism
- Parallel Execution
- HTML & Allure Reporting
- CI/CD Integration
- Docker Support
- Enterprise Framework Architecture

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pytest | Test Framework |
| Requests | API Testing |
| Faker | Test Data Generation |
| JSON Schema | Response Validation |
| PostgreSQL / MySQL / SQLite | Database Validation |
| Git | Version Control |
| GitHub | Repository Hosting |
| GitHub Actions | CI/CD |
| Jenkins | CI/CD |
| Docker | Containerization |
| Allure | Reporting |
| HTML Report | Test Report |

---

# Project Structure

```
api-automation-framework-python/
│
├── src/
│   ├── clients/
│   ├── auth/
│   ├── config/
│   ├── database/
│   ├── exceptions/
│   ├── managers/
│   ├── models/
│   ├── payloads/
│   ├── utils/
│   └── validators/
│
├── testdata/
│
├── tests/
│   ├── smoke/
│   ├── sanity/
│   ├── regression/
│   └── integration/
│
├── reports/
├── logs/
│
├── .env
├── pytest.ini
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── README.md
└── .github/
```

---

# Framework Architecture

```
                Tests
                  │
                  ▼
             API Client
                  │
                  ▼
         Authentication Layer
                  │
                  ▼
         Request Builder
                  │
                  ▼
            REST API Server
                  │
                  ▼
        Response Validator
                  │
                  ▼
      Assertions & Reporting
                  │
                  ▼
          Database Validation
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/api-automation-framework-python.git
```

Move into the project

```bash
cd api-automation-framework-python
```

Create a virtual environment

### Windows

```bash
python -m venv venv
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Tests

Run all tests

```bash
pytest
```

Run with verbose output

```bash
pytest -v
```

Run a specific file

```bash
pytest tests/test_users.py
```

Run smoke tests

```bash
pytest -m smoke
```

Run tests in parallel

```bash
pytest -n auto
```

---

# Reporting

Generate HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

Generate Allure results

```bash
pytest --alluredir=reports/allure-results
```

Generate Allure report

```bash
allure serve reports/allure-results
```

---

# Environment Management

The framework supports multiple environments.

- DEV
- QA
- STAGE
- UAT
- PROD

Environment variables are managed using `.env`.

Example:

```env
BASE_URL=https://reqres.in
API_KEY=xxxxxxxx
TOKEN=xxxxxxxx
```

---

# Authentication Support

The framework supports

- Bearer Token
- JWT
- API Key
- Basic Authentication
- OAuth 2.0
- Session Authentication
- Refresh Token

---

# Response Validation

Reusable validators include

- JSON Key Validation
- JSON Value Validation
- JSON Schema Validation
- Header Validation
- Cookie Validation
- Status Code Validation
- Response Time Validation
- List Size Validation

---

# Payload Management

Supports

- JSON Payload Files
- Dynamic Payload Builder
- Faker Data
- UUID Generation
- Date Utilities
- Payload Templates

---

# Database Validation

Supports

- PostgreSQL
- MySQL
- SQLite

Example flow

```
API Request

↓

Database Validation

↓

Response Comparison

↓

Assertion
```

---

# Logging

Framework provides

- Console Logging
- File Logging
- Rotating Logs
- Pretty JSON Logs
- Request Logging
- Response Logging
- Execution Time Logging

---

# CI/CD

Supported

- GitHub Actions
- Jenkins

Pipeline

```
Git Push

↓

GitHub Actions

↓

Install Dependencies

↓

Run Tests

↓

Generate Reports

↓

Upload Reports
```

---

# Docker

Run the framework inside Docker

```bash
docker-compose up --build
```

---

# Coding Standards

- PEP 8
- SOLID Principles
- DRY
- KISS
- Layered Architecture
- Reusable Components

---

# Current Progress

| Phase | Status |
|--------|--------|
| Project Foundation | ✅ Completed |
| Core Framework | ✅ Completed |
| Authentication | ⏳ Planned |
| Payload Management | ⏳ Planned |
| Response Validation | ⏳ Planned |
| Advanced Pytest | ⏳ Planned |
| Logging & Reporting | ⏳ Planned |
| Environment Management | ⏳ Planned |
| Data Driven Testing | ⏳ Planned |
| Database Validation | ⏳ Planned |
| Schema Validation | ⏳ Planned |
| Utilities | ⏳ Planned |
| Retry Mechanism | ⏳ Planned |
| Parallel Execution | ⏳ Planned |
| CI/CD | ⏳ Planned |
| Docker | ⏳ Planned |
| Framework Design | ⏳ Planned |
| Enterprise Features | ⏳ Planned |
| Interview Preparation | ⏳ Planned |
| GitHub Polish | ⏳ Planned |

---

# Learning Objectives

This project is designed to demonstrate real-world API automation skills, including:

- Building a scalable automation framework
- Designing reusable API clients
- Implementing authentication strategies
- Managing test data and payloads
- Validating API responses and databases
- Integrating CI/CD pipelines
- Containerizing test execution with Docker
- Applying clean code and design principles

---

# Future Enhancements

- API Contract Testing
- Performance Testing
- GraphQL Automation
- gRPC Testing
- UI Automation Integration
- Slack/Email Notifications
- Kubernetes Deployment
- AI-assisted Test Data Generation

---

# Author

**Rajeev Singh Thakur**

FullStack SDET | API Automation | Python | Pytest | Requests | CI/CD | Docker

