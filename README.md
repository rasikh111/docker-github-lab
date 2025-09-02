# docker-github-lab
# Lab 22: Building from GitHub in Docker

This lab demonstrates how to integrate **Docker** with **GitHub** effectively by creating a simple Flask application, building a Docker image, running it locally, and automating builds using **GitHub Actions**.

---

## Objectives
- Understand how to integrate Docker with GitHub.
- Learn to create and configure a `Dockerfile` in a GitHub repository.
- Gain hands-on experience cloning, building, and running a Docker container.
- Explore automation strategies for Docker builds using CI/CD tools like GitHub Actions.

---

##  Prerequisites
Before starting, ensure you have:
- Basic understanding of **Git** and version control.
- Familiarity with **Docker** and Dockerfiles.
- A **GitHub account**.
- Installed **Docker Desktop**.
- Installed **git** on your local machine.

---

## 📝 Lab Tasks

### ✅ Task 1: Create a Simple Project in GitHub with a Dockerfile

1. **Create a new repository** on GitHub:
   - Name: `docker-github-lab`
   - Public visibility
   - Initialize with a README

2. **Add a simple Flask application** (`app.py`):

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello():
       return "Hello, Docker!"

   if __name__ == '__main__':
       app.run(host='0.0.0.0')

    Create a Dockerfile:

FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

Commit and push changes:

    git add .
    git commit -m "Add simple Flask app and Dockerfile"
    git push origin main

✅ Task 2: Clone Locally and Run Docker Build

    Clone the repo:

git clone https://github.com/your-username/docker-github-lab.git
cd docker-github-lab

Build the Docker image:

docker build -t my-flask-app .

Run the container:

docker run -p 5000:5000 my-flask-app

Now visit: 👉 http://localhost:5000
✅ Task 3: Automate Builds with GitHub Actions

    Add GitHub Actions workflow (.github/workflows/docker-image.yml):

name: Docker Image CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1

      - name: Build Docker image
        uses: docker/build-push-action@v2
        with:
          context: .
          file: ./Dockerfile
          push: false
          tags: my-flask-app:latest

Commit and push workflow:

    git add .github/workflows/docker-image.yml
    git commit -m "Add GitHub Actions workflow for Docker build"
    git push origin main

    ✅ Every push to the main branch will now automatically trigger a Docker build.

🏁 Conclusion

By completing this lab, you have learned how to:

    Create and run a Dockerized application directly from GitHub.

    Build and run Docker containers locally.

    Automate Docker builds with GitHub Actions.

This workflow enhances your DevOps pipeline and makes your application deployment more efficient and reliable. 🎉
📌 Repository Structure

docker-github-lab/
<pre><font color="#12488B"><b>.</b></font>
├── Dockerfile
├── README.md
└── app.py

1 directory, 3 files
</pre>
