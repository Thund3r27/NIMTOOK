from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_movies():

    response = client.get("/movies")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_movie_by_id():

    response = client.get("/movies/1")

    assert response.status_code == 200

    movie = response.json()

    assert movie["id"] == 1


def test_get_movie_not_found():

    response = client.get("/movies/999999")

    assert response.status_code == 404


def test_create_movie():

    payload = {
        "id": 99999,
        "title": "Test Movie",
        "genres": "Comedy"
    }

    response = client.post(
        "/movies",
        json=payload
    )

    assert response.status_code == 200

    response = client.get("/movies/99999")

    assert response.status_code == 200

    movie = response.json()

    assert movie["title"] == "Test Movie"


def test_update_movie():

    payload = {
        "title": "Updated Movie",
        "genres": "Drama"
    }

    response = client.put(
        "/movies/1",
        json=payload
    )

    assert response.status_code == 200

    response = client.get("/movies/1")

    movie = response.json()

    assert movie["title"] == "Updated Movie"
    assert movie["genres"] == "Drama"


def test_delete_movie():

    client.post(
        "/movies",
        json={
            "id": 77777,
            "title": "Delete Me",
            "genres": "Test"
        }
    )

    response = client.delete("/movies/77777")

    assert response.status_code == 200

    response = client.get("/movies/77777")

    assert response.status_code == 404