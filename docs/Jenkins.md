# Jenkins Guide

## Overview

Jenkins is used to automate the execution of API tests whenever new code is pushed to GitHub. The pipeline builds a Docker image and runs the test suite inside a Docker container.

---

# Why Jenkins?

Before Jenkins:

* Tests were executed manually.
* Developers had to remember to run tests.
* No continuous integration.

After Jenkins:

* Automated test execution.
* Consistent build process.
* Immediate feedback after code changes.
* Easy integration with Docker.

---

# Prerequisites

* Jenkins installed
* Git installed
* Docker Desktop running
* GitHub repository connected to Jenkins

---

# Jenkins Pipeline

Pipeline Flow:

```text
GitHub
   │
   ▼
Checkout Source Code
   │
   ▼
Build Docker Image
   │
   ▼
Run Docker Container
   │
   ▼
Execute Pytest
   │
   ▼
Build Success / Failure
```

---

# Jenkinsfile Used

```groovy
pipeline {

    agent any

    environment {
        IMAGE_NAME = "api-framework"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Run API Tests') {
            steps {
                sh "docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }
    }
}
```

---

# Pipeline Explanation

## agent any

Runs the pipeline on any available Jenkins agent.

---

## environment

Stores reusable variables.

Example:

```groovy
IMAGE_NAME = "api-framework"
```

---

## Checkout Stage

Downloads the latest code from GitHub.

---

## Build Docker Image

Builds a Docker image for the current build.

```bash
docker build -t api-framework:${BUILD_NUMBER} .
```

---

## Run API Tests

Runs the Docker container and executes the test suite.

```bash
docker run --rm api-framework:${BUILD_NUMBER}
```

---

# Why BUILD_NUMBER?

Each Jenkins build creates a uniquely tagged Docker image.

Example:

```
api-framework:1
api-framework:2
api-framework:3
```

This avoids confusion between builds.

---

# Best Practices Followed

* Pipeline as Code (`Jenkinsfile`)
* Dockerized execution
* Build-specific image tags
* Automatic container cleanup using `--rm`
* Source code managed in GitHub

---

# Common Issues

## Docker daemon not running

Solution:

Start Docker Desktop.

---

## Docker command not found

Ensure Docker is installed and available in Jenkins PATH.

---

## Build failed during docker build

Verify:

* Dockerfile exists
* requirements.txt exists
* Internet connection is available for dependency installation

---

# Interview Questions

### What is Jenkins?

An automation server used for Continuous Integration and Continuous Delivery (CI/CD).

---

### What is Pipeline as Code?

A Jenkins pipeline defined using a `Jenkinsfile` stored in the repository.

---

### What is a Stage?

A logical section of the pipeline such as Checkout, Build, or Test.

---

### Why use Docker with Jenkins?

Docker provides a consistent execution environment, eliminating dependency issues on the Jenkins machine.

---

### What is BUILD_NUMBER?

A Jenkins environment variable that uniquely identifies each build.

---

# Commands Cheat Sheet

```bash
docker build -t api-framework:${BUILD_NUMBER} .

docker run --rm
```
