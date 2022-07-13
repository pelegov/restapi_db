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
                        bat 'python rest_app.py'
                    } else {
                        sh 'python rest_app.py'
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

