
from src.clients.api_client import APIClient


client = APIClient()


def test_get_post():
    res = client.get("https://jsonplaceholder.typicode.com/posts/1")
    assert res.status_code == 200
