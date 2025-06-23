pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                // Установка зависимостей без активации окружения
                sh 'venv/bin/pip install --upgrade pip'
                sh 'venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Data Preparation') {
            steps {
                sh 'venv/bin/python data_preparation.py'
            }
        }
        stage('Model Training') {
            steps {
                sh 'venv/bin/python model_training.py'
            }
        }
        stage('Model Evaluation') {
            steps {
                sh 'venv/bin/python model_evaluation.py'
                archiveArtifacts artifacts: 'metrics.txt, model.pkl', fingerprint: true
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}