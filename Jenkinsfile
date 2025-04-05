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
        stage('Cleanup') {
            steps {
                script {
                    echo 'Cleaning up existing resources...'
                    powershell '''
                        # Login to Azure
                        az login --service-principal -u $env:AZURE_CLIENT_ID -p $env:AZURE_CLIENT_SECRET --tenant $env:AZURE_TENANT_ID
                        az account set --subscription $env:AZURE_SUBSCRIPTION_ID
                        
                        # Delete existing function app if it exists
                        Write-Host "Checking if function app exists..."
                        $functionApp = az functionapp show --name $env:FUNCTION_APP_NAME --resource-group $env:RESOURCE_GROUP 2>$null
                        if ($functionApp) {
                            Write-Host "Deleting existing function app..."
                            az functionapp delete --name $env:FUNCTION_APP_NAME --resource-group $env:RESOURCE_GROUP --yes
                            Write-Host "Function app deleted successfully."
                        } else {
                            Write-Host "No existing function app found."
                        }
 
                        # Create new function app
                        Write-Host "Creating new function app..."
                        az functionapp create `
                            --name $env:FUNCTION_APP_NAME `
                            --resource-group $env:RESOURCE_GROUP `
                            --storage-account mystorage8910481 `
                            --runtime python `
                            --runtime-version 3.11 `
                            --functions-version 4 `
                            --os-type linux `
                            --consumption-plan-location australiaeast `
                            --https-only true `
                            --min-tls-version 1.2
 
                        # Configure Python settings
                        Write-Host "Configuring Python settings..."
                        az functionapp config appsettings set `
                            --name $env:FUNCTION_APP_NAME `
                            --resource-group $env:RESOURCE_GROUP `
                            --settings `
                            PYTHON_ENABLE_WORKER_EXTENSIONS=1 `
                            FUNCTIONS_WORKER_RUNTIME=python `
                            PYTHON_ISOLATION_LEVEL=ISOLATED
 
                        Write-Host "Function app created and configured successfully."
                    '''
                }
            }
        }
 
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
                    powershell '''
                        # Create deployment directory
                        New-Item -ItemType Directory -Force -Path deploy
                        
                        # Copy the hello directory with all its contents
                        Copy-Item -Path hello -Destination deploy/ -Recurse
                        
                        # Copy other necessary files
                        Copy-Item requirements.txt deploy/
                        Copy-Item host.json deploy/
                        Copy-Item local.settings.json deploy/
                        
                        # Create deployment package using Compress-Archive
                        Set-Location deploy
                        Compress-Archive -Path * -DestinationPath ../function_package.zip -Force
                        Set-Location ..
                        
                        # Verify package contents
                        Write-Host "Verifying package contents..."
                        Expand-Archive -Path function_package.zip -DestinationPath verify_package -Force
                        Get-ChildItem -Path verify_package -Recurse | ForEach-Object { Write-Host $_.FullName }
                        
                        # Clean up
                        Remove-Item -Path deploy -Recurse -Force
                        Remove-Item -Path verify_package -Recurse -Force
                    '''
                }
            }
        }
 
        stage('Deploy to Azure') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    powershell '''
                        # Login to Azure
                        az login --service-principal -u $env:AZURE_CLIENT_ID -p $env:AZURE_CLIENT_SECRET --tenant $env:AZURE_TENANT_ID
                        az account set --subscription $env:AZURE_SUBSCRIPTION_ID
                        
                        # Deploy function app
                        az functionapp deployment source config-zip `
                            --name $env:FUNCTION_APP_NAME `
                            --resource-group $env:RESOURCE_GROUP `
                            --src function_package.zip
                            
                        # Verify deployment
                        Write-Host "Waiting for function app to be ready..."
                        Start-Sleep -Seconds 30
                        
                        # List functions
                        Write-Host "Listing functions..."
                        az functionapp function list `
                            --name $env:FUNCTION_APP_NAME `
                            --resource-group $env:RESOURCE_GROUP
                            
                        # Show function app details
                        az functionapp show `
                            --name $env:FUNCTION_APP_NAME `
                            --resource-group $env:RESOURCE_GROUP
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
 