import pytest
from _pytest.fixtures import fixture
from fastapi.testclient import TestClient
from services.user.app import app as user_app

client = TestClient(user_app)
USER_BASE_PATH = "/users/"


@fixture(scope="module")
def get_user_dict():
    yield {"user_id": "12345", "name": "Alice"}


def test_create_user(get_user_dict):
    response = client.post(USER_BASE_PATH, json=get_user_dict)
    assert response.status_code == 201
    assert response.json()["user_id"] == "12345"


def test_create_user_exists(get_user_dict):
    client.post(USER_BASE_PATH, json=get_user_dict)
    response = client.post("/users/", json=get_user_dict)
    assert response.status_code == 400
    assert response.json() == {"error": "User already exists with id 12345"}
