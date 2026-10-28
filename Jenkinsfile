
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'echo "Latest commit:"'
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application after a Git change...'
                sh 'echo "Build completed."'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "Tests passed."'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed.'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
