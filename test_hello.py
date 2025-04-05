import requests

def test_response_code():
    res = requests.get("http://localhost:7071/api/HelloWorld")
    assert res.status_code == 200

def test_response_text():
    res = requests.get("http://localhost:7071/api/HelloWorld")
    assert res.text == "Hello, World!"

def test_invalid_method():
    res = requests.post("http://localhost:7071/api/HelloWorld")
    assert res.status_code in [200, 405]
