// This Jenkinsfile is for a Python-based Azure Function App deployment pipeline.
// It includes stages for checking out code, installing dependencies, running tests, building the package, and deploying to Azure.
pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:/Users/singp/AppData/Local/Programs/Python/Python311"
        PIP_PATH = "pip 23.2.1 from C:/Users/singp/AppData/Local/Programs/Python/Python311/Lib/site-packages/pip"
        PATH = "${PYTHON_PATH};${PIP_PATH};${env.PATH}"
        
        AZURE_SUBSCRIPTION_ID = credentials('azure-subscription-id')
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
    }

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
                sh '${PYTHON_PATH} -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '${PYTHON_PATH} -m pytest'
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
