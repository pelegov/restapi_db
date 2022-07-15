pipeline {
    agent any
    stages {
        stage('git_connect') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git branch: 'main', url: 'https://github.com/pelegov/restapi_db.git'
            }
        }
        stage('run rest_api_app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python3 rest_app.py'
                    } else {
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }
        }
        stage('run web_app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python3 web_app.py'
                    } else {
                        sh 'python3 web_app.py'
                    }
                }
            }
        }
        stage('run back_end_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python3 backend_testing.py'
                    } else {
                        sh 'python3 backend_testing.py'
                    }
                }
            }
        }
        stage('run clean_environment') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python3 clean_environment.py'
                    } else {
                        sh 'python3 clean_environment.py'
                    }
                }
            }
        }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}

