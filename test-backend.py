import pytest

from app import app as flask_app


@pytest.fixture
def client():
    test_client = flask_app.test_client()
    return test_client


def test_example(client):
    response_inventory = client.get("/inventory")
    response_product = client.get("/inventory/9f0d518206")
    assert response_inventory.status_code == 200
    assert response_product.status_code == 200
