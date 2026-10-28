
pipeline {
    agent {
        kubernetes {
            defaultContainer 'python'
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: python
      image: python:3.12-slim
      command:
        - cat
      tty: true
'''
        }
    }

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    stages {
        stage('Check Python') {
            steps {
                sh 'python --version'
                sh 'python -m pip --version'
            }
        }

        
stage('Use Jenkins Credential') {
    steps {
        withCredentials([
            string(
                credentialsId: 'lab-api-token',
                variable: 'API_TOKEN'
            )
        ]) {
            sh '''
                set +x
                if [ -n "$API_TOKEN" ]; then
                    echo "Credential was retrieved successfully."
                else
                    echo "Credential is missing."
                    exit 1
                fi
            '''
        }
    }
}


        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
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
                echo 'Python tests passed. Continuing to build.'
                sh 'echo "Build simulation completed."'
            }
        }
    }

    post {
        success {
            echo 'Python CI pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed. Review the console output.'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
