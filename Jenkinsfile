pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Data Preparation') {
            steps {
                sh 'source venv/bin/activate && python3 src/data_preparation.py'
            }
        }
        stage('Model Training') {
            steps {
                sh 'source venv/bin/activate && python3 src/model_training.py'
            }
        }
        stage('Model Evaluation') {
            steps {
                sh 'source venv/bin/activate && python3 src/model_evaluation.py'
                archiveArtifacts artifacts: 'metrics.txt, model.pkl', fingerprint: true
            }
        }
    }
    post {
        always {
            cleanWs()
        }
        success {
            emailext (
                subject: "SUCCESS: Pipeline '${env.JOB_NAME}' (${env.BUILD_NUMBER})",
                body: "Пайплайн успешно выполнен!<br>Просмотреть сборку: ${env.BUILD_URL}",
                to: 'darrenshen02@gmail.com'
            )
        }
        failure {
            emailext (
                subject: "FAILED: Pipeline '${env.JOB_NAME}' (${env.BUILD_NUMBER})",
                body: "Ошибка в выполнении пайплайна!<br>Просмотреть сборку: ${env.BUILD_URL}",
                to: 'darrenshen02@gmail.com'
            )
        }
    }
}