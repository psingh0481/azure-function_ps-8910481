// This Jenkinsfile is for a Python-based Azure Function App deployment pipeline.
// It includes stages for checking out code, installing dependencies, running tests, and deploying to Azure.
pipeline {
    agent any
 
    environment {
        // Python environment configuration
        PYTHON_VERSION = "3.11.5"
        PYTHON_PATH = "C:/Users/singp/AppData/Local/Programs/Python/Python311/python.exe"
        PATH = "${env.PATH}:${PYTHON_PATH}"
        
        // Azure credentials - these should be configured in Jenkins Credentials Manager
        AZURE_SUBSCRIPTION_ID = credentials('azure-subscription-id')
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        
        // Azure resource configuration
        RESOURCE_GROUP = 'azure_pipeline'
        FUNCTION_APP_NAME = 'myfunctionapp8910481'
    }
 
    triggers {
        githubPush()
    }
 
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code from Git'
                checkout scm
            }
        }
 
        stage('Build') {
            steps {
                script {
                    echo 'Setting up Python environment...'
                    sh '''
                        # Verify Python version
                        python --version | grep "${PYTHON_VERSION}" || { echo "Python ${PYTHON_VERSION} is required. Aborting."; exit 1; }
                        
                        # Create and activate virtual environment
                        python -m venv venv
                        . venv/Scripts/activate
                        
                        # Upgrade pip and install dependencies
                        python -m pip install --upgrade pip
                        python -m pip install --no-cache-dir -r requirements.txt
                    '''
                }
            }
        }
 
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh '''
                        . venv/Scripts/activate
                        python -m pytest test_hello.py -v
                    '''
                }
            }
        }
 
        stage('Package') {
            steps {
                script {
                    echo 'Creating deployment package...'
                    sh '''
                        # Create deployment directory
                        mkdir -p deploy
                        
                        # Copy necessary files
                        cp __init__.py deploy/
                        cp requirements.txt deploy/
                        cp host.json deploy/
                        cp local.settings.json deploy/
                        
                        # Create deployment package
                        cd deploy
                        zip -r ../function_package.zip .
                        cd ..
                        
                        # Clean up
                        rm -rf deploy
                    '''
                }
            }
        }
 
        stage('Deploy to Azure') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    sh '''
                        # Login to Azure
                        az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                        az account set --subscription $AZURE_SUBSCRIPTION_ID
                        
                        # Deploy function app
                        az functionapp deployment source config-zip \
                            --name $FUNCTION_APP_NAME \
                            --resource-group $RESOURCE_GROUP \
                            --src function_package.zip
                            
                        # Verify deployment
                        az functionapp show --name $FUNCTION_APP_NAME --resource-group $RESOURCE_GROUP
                    '''
                }
            }
        }
    }
 
    post {
        always {
            cleanWs()
            echo 'Cleaning up workspace...'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
            // You might want to add notification steps here (email, Slack, etc.)
        }
    }
}