pipeline {
    agent any
    environment {
        AZURE_CLIENT_ID = Credentials('azure-client-id')
        AZURE_CLIENT_SECRET = Credentials('azure-client-secret')
        AZURE_TENANT_ID = Credentials('azure-tenant-id')
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
                sh 'pytest tests/' // Add your test cases under the tests directory
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
