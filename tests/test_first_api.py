
# from src.clients.api_client import APIClient
from src.utils.assertions import (
    assert_status_code,
    assert_json_value,
    assert_response_time,
    assert_content_type
)




# client = APIClient()


def test_get_post(client):
    res = client.get("/posts/1")
    assert res.status_code == 200
    print("assertion")
    assert_status_code(res,200)
    assert_json_value(res, "id", 1)
    assert_response_time(res, 2)
    assert_content_type(res, "application/json")
    