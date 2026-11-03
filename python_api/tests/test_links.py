from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_links():

    response = client.get("/links")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_link():

    response = client.get("/links/1")

    assert response.status_code == 200

    link = response.json()

    assert link["movie_id"] == 1


def test_link_not_found():

    response = client.get("/links/999999")

    assert response.status_code == 404