
from src.clients.api_client import APIClient
from src.utils.assertions import assert_status_code




client = APIClient()


def test_get_post():
    res = client.get("/posts/1")
    # assert res.status_code == 200
    assert_status_code(res,200)
