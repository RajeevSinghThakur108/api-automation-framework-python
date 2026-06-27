from src.clients.api_client import APIClient
from src.utils.assertions import assert_status_code

client = APIClient()
def test_create_post():

    payload = {
        "title": "Python API",
        "body": "Learning API Automation",
        "userId": 1
    }

    response = client.post("/posts", json=payload)

    assert_status_code(response, 201)