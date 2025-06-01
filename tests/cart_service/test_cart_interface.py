import pytest
from fastapi.testclient import TestClient
from services.cart.app import app as cart_app

client = TestClient(cart_app)
CART_BASE_PATH = "/users"


def test_add_item_to_cart():
    response = client.post(f"{CART_BASE_PATH}/456", json={"item_id": "424", "quantity": 1})
    assert response.status_code == 201
    assert "424" in [item["item_id"] for item in response.json()["items"]]


def test_add_item_to_cart_increase_quantity():
    client.post(f"{CART_BASE_PATH}/456", json={"item_id": "789", "quantity": 5})
    response = client.post(f"{CART_BASE_PATH}/456", json={"item_id": "789", "quantity": 5})
    assert response.status_code == 201
    actual = [item["quantity"] for item in response.json()["items"] if item["item_id"] == "789"][0]
    expected = 10
    assert expected == actual


def test_get_cart():
    client.post(f"{CART_BASE_PATH}/789", json={"item_id": "999", "quantity": 1})
    response = client.get(f"{CART_BASE_PATH}/789")
    assert response.status_code == 200
    assert response.json()["user_id"] == "789"
    assert response.json()["items"] == [{'item_id': '999', 'quantity': 1}]
