pipeline {
    agent any
    environment {
        AZURE_SUBSCRIPTION_ID = credentials('AZURE_SUBSCRIPTION_ID')
        AZURE_CLIENT_ID = credentials('AZURE_CLIENT_ID')
        AZURE_CLIENT_SECRET = credentials('AZURE_CLIENT_SECRET')
        AZURE_TENANT_ID = credentials('AZURE_TENANT_ID')
        RESOURCE_GROUP = 'MyResourceGroup'
        FUNCTION_APP_NAME = 'myfunctionapp8910481'
    }
    stages {
        stage('Build') {
            steps {
                bat '''
                    python -m venv .venv
                    call .venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                bat '''
                    call .venv\\Scripts\\activate
                    pytest tests\\ -v
                '''
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([azureServicePrincipal(
                    credentialsId: 'azure-credentials',
                    subscriptionIdVariable: 'AZURE_SUBSCRIPTION_ID',
                    clientIdVariable: 'AZURE_CLIENT_ID',
                    clientSecretVariable: 'AZURE_CLIENT_SECRET',
                    tenantIdVariable: 'AZURE_TENANT_ID'
                )]) {
                    bat '''
                        az login --service-principal -u %AZURE_CLIENT_ID% -p %AZURE_CLIENT_SECRET% -t %AZURE_TENANT_ID%
                        func azure functionapp publish %FUNCTION_APP_NAME%
                    '''
                }
            }
        }
    }
}
