pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Stop previous container') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'export PATH=$PATH:/usr/local/bin && docker stop my_container && docker rm my_container && docker image rm my_image'
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
                script {
                    def pyChanged = false
                    for (changeLogSet in currentBuild.changeSets) {
                        for (entry in changeLogSet) {
                            for (affectedFile in entry.affectedFiles) {
                                if (affectedFile.path == 'app.py') {
                                    pyChanged = true
                                    break
                                }
                            }
                            if (pyChanged) {
                                break
                            }
                        }
                    }
                    if (pyChanged) {
                        input(
                            id: 'manual-approval',
                            message: 'Manual approval is required.',
                            ok: 'Proceed',
                            submitterParameter: 'APPROVER'
                        )
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'export PATH=$PATH:/usr/local/bin && docker build -t my_image .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'export PATH=$PATH:/usr/local/bin && docker run -d --name my_container -p 6001:6001 my_image'
            }
        }
    }
}

