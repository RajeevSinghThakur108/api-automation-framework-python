from src.utils.assertions import assert_status_code


def test_delete_post(client):

    response = client.delete("/posts/1")

    assert_status_code(response, 200)