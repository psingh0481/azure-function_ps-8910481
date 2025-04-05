import pytest
from __init__ import main
import azure.functions as func
import json
from datetime import datetime
 
 
@pytest.mark.asyncio
async def test_hello_world_response():
    # Test case 1: Check if response contains "Hello, World!" and timestamp
    req = func.HttpRequest(
        method='GET',
        url='/api/hello',
        body=None
    )
    response = main(req)
    assert response.status_code == 200
    assert "Hello, World!" in response.get_body().decode()
    assert "Current time:" in response.get_body().decode()
 
 
@pytest.mark.asyncio
async def test_status_code():
    # Test case 2: Check if status code is 200
    req = func.HttpRequest(
        method='GET',
        url='/api/hello',
        body=None
    )
    response = main(req)
    assert response.status_code == 200
 
 
@pytest.mark.asyncio
async def test_response_type():
    # Test case 3: Check if response is of correct type
    req = func.HttpRequest(
        method='GET',
        url='/api/hello',
        body=None
    )
    response = main(req)
    assert isinstance(response, func.HttpResponse)
 
 
@pytest.mark.asyncio
async def test_cors_headers():
    # Test case 4: Check if CORS headers are present
    req = func.HttpRequest(
        method='GET',
        url='/api/hello',
        body=None
    )
    response = main(req)
    assert "Access-Control-Allow-Origin" in response.headers
    assert response.headers["Access-Control-Allow-Origin"] == "https://portal.azure.com"
    assert "Content-Type" in response.headers
    assert response.headers["Content-Type"] == "text/plain"
 
 
@pytest.mark.asyncio
async def test_options_request():
    # Test case 5: Check OPTIONS request handling
    req = func.HttpRequest(
        method='OPTIONS',
        url='/api/hello',
        body=None
    )
    response = main(req)
    assert response.status_code == 204
    assert "Access-Control-Allow-Methods" in response.headers
    assert "Access-Control-Allow-Headers" in response.headers
    assert "Access-Control-Max-Age" in response.headers
 
 
@pytest.mark.asyncio
async def test_post_with_name():
    # Test case 4: Check POST request with name parameter
    req = func.HttpRequest(
        method='POST',
        url='/api/hello',
        body=json.dumps({"name": "Test"}).encode('utf-8')
    )
    response = main(req)
    assert response.status_code == 200
    assert "Hello, Test" in response.get_body().decode()