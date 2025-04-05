import pytest
from __init__ import main
import azure.functions as func

@pytest.mark.asyncio
async def test_hello_world_response():
    # Test case 1: Check if response contains "Hello, World!"
    req = func.HttpRequest(
        method='GET',
        url='/api/hello',
        body=None
    )
    response = main(req)
    assert response.status_code == 200
    assert "Hello, World!" in response.get_body().decode()

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