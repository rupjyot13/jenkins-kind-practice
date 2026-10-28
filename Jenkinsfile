
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git...'
                checkout scm

                sh 'echo "Current workspace:"'
                sh 'pwd'

                sh 'echo "Checked-out Git commit:"'
                sh 'git rev-parse --short HEAD'

                sh 'echo "Repository files:"'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application from source control...'
                sh 'echo "Build simulation completed."'
            }
        }

        stage('Test') {
            steps {
                echo 'Running test simulation...'
                sh 'echo "Tests passed."'
            }
        }
    }

    post {
        success {
            echo 'Git-based Jenkins pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed. Check the checkout and stage logs.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
