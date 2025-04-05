// This Jenkinsfile is for a Python-based Azure Function App deployment pipeline.
// It includes stages for checking out code, installing dependencies, running tests, building the package, and deploying to Azure.
pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:/Users/singp/AppData/Local/Programs/Python/Python311/python.exe"
        PATH = "${env.PATH}:${PYTHON_PATH}"
        
        AZURE_SUBSCRIPTION_ID = credentials('azure-subscription-id')
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
    }

    triggers {
        githubPush()
    
    } // This trigger will start the pipeline when a push is made to the GitHub repository.

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code from Git'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh '"C:/Users/singp/AppData/Local/Programs/Python/Python311/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '${PYTHON_PATH} -m pytest test_hello.py''
            }
        }

        stage('Deploy to Azure') {
            steps {
                echo 'Deploying to Azure...'
                    sh '''
                        az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                        az account set --subscription $AZURE_SUBSCRIPTION_ID
                        az functionapp deployment source config-zip \
                          --name myfunctionapp8910481 \
                          --resource-group azure_pipeline \
                          --src function_package.zip
                    '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
        }

        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
