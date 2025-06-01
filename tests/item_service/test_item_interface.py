import pytest
from _pytest.fixtures import fixture
from fastapi.testclient import TestClient
from services.item.app import app as user_app


client = TestClient(user_app)
ITEM_BASE_PATH = "/items/"


@fixture(scope="module")
def get_item_dict():
    yield {"item_id": "123", "name": "Laptop"}


def test_create_item(get_item_dict):
    response = client.post(ITEM_BASE_PATH, json=get_item_dict)
    assert response.status_code == 201
    assert response.json()["item_id"] == "123"


def test_get_items(get_item_dict):
    client.post(ITEM_BASE_PATH, json=get_item_dict)
    response = client.get(ITEM_BASE_PATH)
    assert response.status_code == 200
    assert "123" in [item["item_id"] for item in response.json()]


def test_create_item_exists(get_item_dict):
    client.post(ITEM_BASE_PATH, json=get_item_dict)
    response = client.post(ITEM_BASE_PATH, json=get_item_dict)
    assert response.status_code == 400
    assert response.json() == {"error": "Item already exists with id 123"}
