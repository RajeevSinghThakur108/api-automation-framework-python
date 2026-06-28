def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {response.status_code}"
    )


def assert_json_value(response, key, expected_value):
    data = response.json()

    assert key in data, f"Key '{key}' not found in response"

    assert data[key] == expected_value, (
        f"Expected '{key}' = {expected_value}, "
        f"but got {data[key]}"
    )


def assert_response_time(response, max_time):
    assert response.elapsed.total_seconds() <= max_time, (
        f"Response took {response.elapsed.total_seconds()} seconds"
    )


def assert_content_type(response, expected_type):
    actual = response.headers.get("Content-Type", "")

    assert expected_type in actual, (
        f"Expected Content-Type '{expected_type}', "
        f"but got '{actual}'"
    )