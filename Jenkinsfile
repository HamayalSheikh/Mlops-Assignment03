pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = 'nuzhat059' 
        ML_IMAGE = "${DOCKERHUB_USERNAME}/ml-model:latest"
        AIRFLOW_IMAGE = "${DOCKERHUB_USERNAME}/airflow:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build ML Docker Image') {
            steps {
                bat "docker build -f Dockerfile -t %ML_IMAGE% ."
            }
        }

        stage('Build Airflow Docker Image') {
            steps {
                bat "docker build -f models\\Dockerfile -t %AIRFLOW_IMAGE% ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin
                        docker push %ML_IMAGE%
                        docker push %AIRFLOW_IMAGE%
                    """
                }
            }
        }
    }

    post {
       success {
    echo 'Docker images built and pushed successfully.'
}
failure {
    echo 'Build or push failed.'
}
    }
}
