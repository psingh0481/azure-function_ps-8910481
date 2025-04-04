pipeline {
    agent any
    environment {
        AZURE_CLIENT_ID = credentials('azure-client-id')  // Credentials ID for Client ID
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')  // Credentials ID for Client Secret
        AZURE_TENANT_ID = credentials('azure-tenant-id')  // Credentials ID for Tenant ID
        RESOURCE_GROUP = 'azure_pipeline'
        FUNCTION_APP_NAME = 'myfunctionapp8910481'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests/'  // Add your test cases under the tests directory
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying to Azure Function...'
                sh '''
                    zip -r function.zip *
                    az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                    az functionapp deployment source config-zip --resource-group $RESOURCE_GROUP --name $FUNCTION_APP_NAME --src function.zip
                '''
            }
        }
    }
}
