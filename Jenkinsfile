
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Install Test Dependencies') {
            steps {
                sh 'python --version'
                sh 'python -m pip install --no-cache-dir pytest'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                echo 'Tests passed. Continuing to the build stage.'
                sh 'echo "Build simulation completed."'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline passed.'
        }
        failure {
            echo 'CI pipeline failed. Review the test or build output.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}