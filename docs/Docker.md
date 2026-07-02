# Docker Guide

## Overview

Docker is used to package the API Automation Framework along with Python and all required dependencies into a container. This ensures the framework runs consistently on any machine without installing Python or creating a virtual environment.

---

# Why Docker?

Before Docker:

* Python had to be installed on every machine.
* Virtual environment had to be created.
* Dependencies had to be installed manually.
* Different environments could cause different results.

After Docker:

* Same environment everywhere.
* No Python installation required.
* No virtual environment required.
* Easy integration with Jenkins CI/CD.

---

# Prerequisites

* Docker Desktop installed
* Docker daemon running
* Project contains:

  * `Dockerfile`
  * `requirements.txt`

Verify Docker:

```bash
docker --version
docker info
```

---

# Dockerfile Used in This Project

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]
```

---

# Dockerfile Explanation

### FROM

Uses the official Python 3.12 image as the base image.

### WORKDIR

Creates and switches to the `/app` directory inside the container.

### COPY requirements.txt .

Copies only the dependency file.

This improves Docker build caching because dependencies usually change less frequently than source code.

### RUN pip install

Installs all project dependencies while building the image.

### COPY . .

Copies the complete project into the container.

### CMD ["pytest"]

Runs all API tests automatically when the container starts.

---

# Build Docker Image

```bash
docker build -t api-framework .
```

Explanation:

* `docker build` → Build an image.
* `-t` → Assign a name (tag) to the image.
* `.` → Use the current project directory as the build context.

---

# Verify Image

```bash
docker images
```

Expected image:

```
api-framework
```

---

# Run Tests Inside Docker

```bash
docker run --rm api-framework
```

Explanation:

* Creates a new container.
* Executes `pytest`.
* Removes the container automatically after execution because of `--rm`.

---

# Useful Commands

List images:

```bash
docker images
```

List running containers:

```bash
docker ps
```

List all containers:

```bash
docker ps -a
```

Run interactive container:

```bash
docker run -it python:3.12 bash
```

Start an existing container:

```bash
docker start <container_id>
```

Open terminal in a running container:

```bash
docker exec -it <container_id> bash
```

Remove container:

```bash
docker rm <container_id>
```

Remove image:

```bash
docker rmi <image_name>
```

---

# .dockerignore

File used in this project:

```text
.git
.gitignore
.dockerignore

.venv/
.env

**/__pycache__/
.pytest_cache/

*.pyc
*.pyo

logs/
reports/
htmlcov/
.coverage
```

Purpose:

* Reduces image size.
* Speeds up Docker build.
* Prevents unnecessary files from being copied.

---

# Docker + Jenkins

Pipeline Flow:

```
GitHub
   │
   ▼
Jenkins Checkout
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

Example Jenkins commands:

```groovy
sh "docker build -t api-framework:${BUILD_NUMBER} ."

sh "docker run --rm api-framework:${BUILD_NUMBER}"
```

---

# Best Practices Followed

* Use the official Python image.
* Copy `requirements.txt` before project files for better build cache.
* Use `.dockerignore`.
* Use `--rm` to clean up containers automatically.
* Tag images with the Jenkins build number.

---

# Common Issues

### Docker daemon is not running

Error:

```
Cannot connect to the Docker daemon
```

Solution:

Start Docker Desktop.

---

### Image not found

Error:

```
Unable to find image
```

Solution:

Build the image first.

```bash
docker build -t api-framework .
```

---

### Container exits immediately

Reason:

The default command (`pytest`) has finished executing.

Check logs if required:

```bash
docker logs <container_id>
```

---

# Interview Questions

### What is Docker?

Docker is a containerization platform that packages an application and its dependencies into a portable container.

### Difference between Image and Container?

* Image → Blueprint
* Container → Running instance of an image

### Why do we copy `requirements.txt` before `COPY . .`?

To reuse Docker's build cache and avoid reinstalling dependencies when only source code changes.

### Difference between RUN and CMD?

* `RUN` executes during image build.
* `CMD` executes when the container starts.

### Why use `--rm`?

It automatically removes the container after execution, preventing unused containers from accumulating.

---

# Commands Cheat Sheet

```bash
docker --version
docker info

docker images
docker ps
docker ps -a

docker build -t api-framework .

docker run --rm api-framework

docker run -it python:3.12 bash

docker start <container_id>
docker exec -it <container_id> bash

docker rm <container_id>
docker rmi <image_name>
```

---

# Summary

In this project, Docker is used to:

* Containerize the API Automation Framework.
* Install dependencies inside the image.
* Execute API tests using `pytest`.
* Integrate with Jenkins CI/CD.
* Ensure the framework runs consistently across different environments.
