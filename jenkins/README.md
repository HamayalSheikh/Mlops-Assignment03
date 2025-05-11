# Jenkins CI/CD Pipeline

## Overview
This project automates the Docker image build and push using Jenkins.

## Steps Performed
1. **Checkout code**
2. **Build ML Docker image**
3. **Build Airflow Docker image**
4. **Push both images to Docker Hub**

## Setup Instructions

### Prerequisites
- Jenkins installed (Windows agent)
- Docker installed and running
- Jenkins credentials with ID `dockerhub-creds` (Docker Hub username/password)

### Creating Jenkins Job
1. Go to Jenkins dashboard → *New Item*
2. Choose *Pipeline*
3. Set pipeline definition to "Pipeline script from SCM"
4. Point to this GitHub repo and ensure the `Jenkinsfile` is in the root

## Environment Variables
- `DOCKERHUB_USERNAME` is added as nuzhat059
