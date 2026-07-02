// pipeline {

//     agent any

//     stages {

//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }

//         stage('Create Virtual Environment') {
//             steps {
//                 sh '/opt/homebrew/bin/python3.13 -m venv venv'
//             }
//         }

//         stage('Install Dependencies') {
//             steps {
//                 sh '''
//                 ./venv/bin/python -m pip install --upgrade pip
//                 ./venv/bin/pip install -r requirements.txt
//                 '''
//             }
//         }

//         stage('Run API Tests') {
//             steps {
//                 sh './venv/bin/pytest -v'
//             }
//         }
//     }
// }


pipeline {

    agent any

    environment {
        IMAGE_NAME = "api-framework"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Run API Tests') {
            steps {
                sh "docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }
    }
}