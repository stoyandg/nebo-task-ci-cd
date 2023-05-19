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
                script {
                    def changes = currentBuild.changeSets
                    def htmlChanged = false
                    def pyChanged = false
                    for (int i = 0; i < changes.size(); i++) {
                        def entries = changes[i].items
                        for (int j = 0; j < entries.length; j++) {
                            def entry = entries[j]
                            if (entry.path.toLowerCase().contains("index.html")) {
                                htmlChanged = true
                            }
                            if (entry.path.toLowerCase().contains("app.py")) {
                                pyChanged = true
                            }
                        }
                    }

                    if (pyChanged) {
                        input(message: "Changes detected in app.py, proceed?")
                    } else if (htmlChanged) {
                        echo("Changes detected in index.html, proceeding automatically.")
                    } else {
                        error("No relevant changes detected, skipping build.")
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
