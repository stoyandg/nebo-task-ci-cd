pipeline {
    agent any

    stages {
        stage('Stop previous container') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'export PATH=$PATH:/usr/local/bin && docker stop my_container && docker rm my_container'
                }
            }
        }
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
                sh 'export PATH=$PATH:/usr/local/bin && docker run -d --name my_container -p 6001:6001 my-image'
            }
        }
    }
}