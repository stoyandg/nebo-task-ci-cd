pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/stoyandg/nebo-task-ci-cd.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'export PATH=$PATH:/usr/local/bin && docker build -t my-image .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh {
                    'export PATH=$PATH:/usr/local/bin && docker run -d -p 6001:6001 my-image'
                }
            }
        }
    }
}