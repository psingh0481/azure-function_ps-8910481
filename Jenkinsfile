pipeline {
    agent any

    environment {
        // Set Python and pip path explicitly (adjust based on your Python installation path)
        PYTHON_PATH = "C:/Users/singp/AppData/Local/Programs/Python/Python311"
        PIP_PATH = "pip 23.2.1 from C:/Users/singp/AppData/Local/Programs/Python/Python311/Lib/site-packages/pip"
        PATH = "${PYTHON_PATH};${PIP_PATH};${env.PATH}"
        
        // Azure Service Principal credentials (These should be stored in Jenkins as secrets)
        AZURE_SUBSCRIPTION_ID = credentials('azure-subscription-id') // Replace with your Jenkins secret ID
        AZURE_CLIENT_ID = credentials('azure-client-id') // Replace with your Jenkins secret ID
        AZURE_CLIENT_SECRET = credentials('azure-client-secret') // Replace with your Jenkins secret ID
        AZURE_TENANT_ID = credentials('azure-tenant-id') // Replace with your Jenkins secret ID
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
                script {
                    // Use full path to pip to ensure it's found
                    bat "${PYTHON_PATH}/python.exe -m pip install -r requirements.txt"
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                script {
                    // Run your tests (adjust if needed)
                    bat "${PYTHON_PATH}/python.exe -m pytest"
                }
            }
        }

        stage('Deploy to Azure') {
            steps {
                echo 'Deploying to Azure...'
                script {
                    // Set Azure credentials environment variables
                    withCredentials([usernamePassword(credentialsId: 'azure-service-principal', usernameVariable: 'AZURE_CLIENT_ID', passwordVariable: 'AZURE_CLIENT_SECRET')]) {
                        // Login to Azure using Service Principal
                        bat """az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID"""
                        
                        // Set the Azure subscription to use
                        bat "az account set --subscription $AZURE_SUBSCRIPTION_ID"
                        
                        // Deploy your Azure Function
                        bat 'az functionapp deploy --name myfunctionapp8910481 --resource-group azure_pipeline'
                    }
                }
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