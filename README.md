# azure-function_ps-8910481
Jenkins CI/CD Pipeline To Deploy Azure Functions

Azure Function CI/CD Pipeline Project
This project demonstrates a CI/CD pipeline using Jenkins to deploy a Python Azure Function to Azure Functions.

## Project Structure
__init__.py: Main Azure Function implementation
test_hello.py: Test cases for the Azure Function
requirements.txt: Python dependencies

## Jenkinsfile: Jenkins pipeline configuration
function.json: Azure Function configuration
host.json: Azure Functions host configuration
local.settings.json: Local development settings

## Prerequisites
Python 3.11.5 or higher
Azure CLI
Jenkins server with configured credentials
Azure Service Principal credentials
GitHub Personal Access Token
Azure Function App created in Azure Portal

## Local Development
Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run tests locally:

python -m pytest test_hello.py -v

## CI/CD Pipeline
The Jenkins pipeline consists of three stages:

Build: Sets up Python environment and installs dependencies
Test: Runs automated tests
Package
Deploy: Deploys the function to Azure Functions
Test Cases

## The project includes three test cases:

Verifies the response contains "Hello, World!"
Checks if the status code is 200
Validates the response type is correct
Deployment
The function is automatically deployed to Azure Functions when changes are pushed to the main branch. The deployed function returns "Hello, Priya Singh. Welcome to the world of Azure.


Author
Priya Singh
