from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_ratings():

    response = client.get("/ratings")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_rating():

    response = client.get("/ratings/1")

    assert response.status_code == 200


def test_rating_not_found():

    response = client.get("/ratings/999999")

    assert response.status_code == 404