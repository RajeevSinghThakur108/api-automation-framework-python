# GitHub Actions Guide

## Overview

GitHub Actions is GitHub's built-in CI/CD platform. It automates tasks such as building, testing, and deploying applications directly from a GitHub repository.

> **Status:** Planned for future implementation in this project.

---

# Why GitHub Actions?

* Built into GitHub.
* No separate Jenkins server required.
* Automatically triggers workflows on repository events.
* Easy integration with pull requests and branches.

---

# Planned Workflow

```text
Developer
    │
git push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions Workflow
    │
    ▼
Build Project
    │
    ▼
Run API Tests
    │
    ▼
Workflow Success / Failure
```

---

# Workflow File

Location:

```text
.github/workflows/api-tests.yml
```

---

# Planned Workflow

```yaml
name: API Automation

on:
  push:
    branches:
      - main

jobs:
  api-tests:
    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install -r requirements.txt

      - run: pytest -v
```

---

# Workflow Explanation

## Trigger

Runs whenever code is pushed to the `main` branch.

---

## Runner

Uses an Ubuntu virtual machine provided by GitHub.

---

## Checkout

Downloads the latest source code.

---

## Setup Python

Installs Python 3.12.

---

## Install Dependencies

Installs project packages from `requirements.txt`.

---

## Execute Tests

Runs the API test suite using Pytest.

---

# Planned Improvements

Future enhancements include:

* Docker-based execution
* Test reports
* Allure integration
* Workflow caching
* Artifact upload
* Scheduled workflows
* Matrix builds

---

# Jenkins vs GitHub Actions

| Jenkins                    | GitHub Actions            |
| -------------------------- | ------------------------- |
| Self-hosted                | Cloud-hosted              |
| Requires server            | Built into GitHub         |
| Highly customizable        | Easy to configure         |
| Suitable for enterprise CI | Great for GitHub projects |

---

# Interview Questions

### What is GitHub Actions?

GitHub's built-in CI/CD platform for automating workflows.

---

### What is a Workflow?

A YAML file that defines automated tasks.

---

### What is a Job?

A collection of steps executed on the same runner.

---

### What is a Runner?

The machine that executes the workflow.

---

### What is an Action?

A reusable unit of automation, such as checking out code or setting up Python.

---

# Summary

This project will use GitHub Actions in a future phase to automatically execute API tests whenever code is pushed to GitHub, providing an additional CI/CD solution alongside Jenkins.
