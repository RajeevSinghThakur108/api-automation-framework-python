from src.utils.assertions import assert_status_code

def test_update_post(client):

    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = client.put("/posts/1", json=payload)
    assert_status_code(response, 200)

    