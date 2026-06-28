import pytest
from src.clients.api_client import APIClient

@pytest.fixture
def client():
    return APIClient()