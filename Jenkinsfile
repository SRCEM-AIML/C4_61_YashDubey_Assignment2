pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yashdubey2004/studentproject"
    }

    stages {
        stage('Clone Repo') {
            steps {
                // Use SSH with github-ssh credentials
                git credentialsId: 'github-ssh', url: 'git@github.com:SRCEM-AIML/C4_61_YashDubey_Assignment2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the Docker image using bat for Windows
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Login to Docker Hub using Jenkins credentials
                withDockerRegistry([credentialsId: 'YashDubey', url: 'https://index.docker.io/v1/']) {
                    bat "docker push %DOCKER_IMAGE%"
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build and push completed successfully!'
        }
        failure {
            echo '❌ Build or push failed. Check the logs.'
        }
    }
}
