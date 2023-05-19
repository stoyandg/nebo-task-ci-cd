pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Stop previous container') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'export PATH=$PATH:/usr/local/bin && docker stop my_container'
                    sh 'export PATH=$PATH:/usr/local/bin && docker rm my_container'
                }
            }
        }
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/stoyandg/nebo-task-ci-cd.git'
            }
        }
        stage('Check Changes') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    script {
                        def changeset = checkout([$class: 'GitSCM']).poll()
                            if (changeset != null && changeset.any()) {
                            input(
                                id: 'manual-approval',
                                message: 'Changes detected. Manual approval required to proceed.',
                                ok: 'Proceed',
                                submitterParameter: 'APPROVER'
                            )
                        } else {
                             echo 'No changes detected. Automatically building.'
                        }
                    }
                }    
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
