import requests as r

def test_get_post():
    res = r.get("https://jsonplaceholder.typicode.com/posts/1")
    assert res.status_code == 200
