from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_tags():

    response = client.get("/tags")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_tag():

    response = client.get("/tags/1")

    assert response.status_code == 200


def test_tag_not_found():

    response = client.get("/tags/999999")

    assert response.status_code == 404