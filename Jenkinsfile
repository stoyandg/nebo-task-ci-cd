pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/stoyandg/nebo-task-ci-cd.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build "my-image:${env.BUILD_ID}"
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    dockerImage.run("--name my-container")
                }
            }
        }
    }
}