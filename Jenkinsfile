pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhubusername/studentproject"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-repo/StudentProject.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
    }
}
