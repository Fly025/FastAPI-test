# FastAPI Test Application

A simple FastAPI application with automated versioning and Docker image deployment.

## Application Overview

This is a simple FastAPI application with two endpoints:
- `/`: Returns a "Hello World" message
- `/hello/{name}`: Returns a personalized greeting

## Local Development

### Prerequisites
- Python 3.9+
- pip

### Setup
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   uvicorn main:app --reload
   ```
4. Access the application at http://127.0.0.1:8000

## Docker

### Building the Docker Image
```
docker build -t fastapi-test .
```

### Running the Docker Container
```
docker run -p 8000:8000 fastapi-test
```

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow that:

1. Automatically increments the version number (starting from v1.0.0)
2. Builds a Docker image
3. Pushes the Docker image to Docker Hub

### Workflow Details

The workflow is triggered on pushes to the main branch and consists of two jobs:

1. **Versioning**: Uses [github-tag-action](https://github.com/anothrNick/github-tag-action) to manage semantic versioning
2. **Build and Push**: Builds the Docker image and pushes it to Docker Hub with both `latest` and version-specific tags

### Required Secrets

To use the GitHub Actions workflow, you need to set up the following secrets in your GitHub repository:

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token

## Testing

You can test the API endpoints using the included `test_main.http` file if you're using an IDE that supports HTTP request files, or with tools like curl or Postman.