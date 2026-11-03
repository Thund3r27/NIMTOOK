from fastapi import FastAPI, HTTPException
import csv
import sqlite3

from models.movie import Movie
from models.link import Link
from models.rating import Rating
from models.tag import Tag

app = FastAPI()


@app.get("/")
def home():
    return {"hello": "world"}


@app.get("/movies")
def get_movies():

    movies = []

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies")

    rows = cursor.fetchall()

    movies = []

    for row in rows:
        movie = Movie(
            row[0],
            row[1],
            row[2]
        )

        movies.append(movie.__dict__)

    conn.close()

    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM movies WHERE id = ?",
        (movie_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    movie = Movie(
        row[0],
        row[1],
        row[2]
    )

    return movie.__dict__

@app.post("/movies")
def create_movie(movie: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO movies(id, title, genres)
        VALUES (?, ?, ?)
        """,
        (
            movie["id"],
            movie["title"],
            movie["genres"]
        )
    )

    conn.commit()
    conn.close()

    return movie

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE movies
        SET title = ?, genres = ?
        WHERE id = ?
        """,
        (
            movie["title"],
            movie["genres"],
            movie_id
        )
    )

    conn.commit()
    conn.close()

    return {"message": "updated"}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM movies WHERE id = ?",
        (movie_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "deleted"}

@app.get("/links")
def get_links():

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM links")

    rows = cursor.fetchall()

    result = []

    for row in rows:
        link = Link(
            row[0],
            row[1],
            row[2]
        )

        result.append(link.__dict__)

    conn.close()

    return result

@app.get("/links/{movie_id}")
def get_link(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM links WHERE movie_id = ?",
        (movie_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Link not found"
        )

    return {
        "movie_id": row[0],
        "imdb_id": row[1],
        "tmdb_id": row[2]
    }

@app.post("/links")
def create_link(link: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO links(movie_id, imdb_id, tmdb_id)
        VALUES (?, ?, ?)
        """,
        (
            link["movie_id"],
            link["imdb_id"],
            link["tmdb_id"]
        )
    )

    conn.commit()
    conn.close()

    return link

@app.put("/ratings/{movie_id}")
def update_rating(movie_id: int, rating: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE ratings
        SET rating = ?, timestamp = ?
        WHERE movie_id = ?
        """,
        (
            rating["rating"],
            rating["timestamp"],
            movie_id
        )
    )

    conn.commit()
    conn.close()

    return {"message": "updated"}

@app.put("/links/{movie_id}")
def update_link(movie_id: int, link: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE links
        SET imdb_id = ?, tmdb_id = ?
        WHERE movie_id = ?
        """,
        (
            link["imdb_id"],
            link["tmdb_id"],
            movie_id
        )
    )

    conn.commit()
    conn.close()

    return {"message": "updated"}

@app.delete("/links/{movie_id}")
def delete_link(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM links WHERE movie_id = ?",
        (movie_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "deleted"}

@app.get("/ratings")
def get_ratings():

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ratings")

    rows = cursor.fetchall()

    result = []

    for row in rows:
        rating = Rating(
            row[0],
            row[1],
            row[2],
            row[3]
        )

        result.append(rating.__dict__)

    conn.close()

    return result

@app.get("/ratings/{movie_id}")
def get_rating(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM ratings WHERE movie_id = ?",
        (movie_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Rating not found"
        )

    return {
        "movie_id": row[0],
        "rating": row[1],
        "timestamp": row[2]
    }

@app.post("/ratings")
def create_rating(rating: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO ratings(movie_id, rating, timestamp)
        VALUES (?, ?, ?)
        """,
        (
            rating["movie_id"],
            rating["rating"],
            rating["timestamp"]
        )
    )

    conn.commit()
    conn.close()

    return rating

@app.put("/ratings/{movie_id}")
def update_rating(movie_id: int, rating: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE ratings
        SET rating = ?, timestamp = ?
        WHERE movie_id = ?
        """,
        (
            rating["rating"],
            rating["timestamp"],
            movie_id
        )
    )

    conn.commit()
    conn.close()

    return {"message": "updated"}

@app.delete("/ratings/{movie_id}")
def delete_rating(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM ratings WHERE movie_id = ?",
        (movie_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "deleted"}

@app.get("/tags")
def get_tags():

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tags")

    rows = cursor.fetchall()

    result = []

    for row in rows:
        tag = Tag(
            row[0],
            row[1],
            row[2],
            row[3]
        )

        result.append(tag.__dict__)

    conn.close()

    return result

@app.get("/tags/{movie_id}")
def get_tag(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tags WHERE movie_id = ?",
        (movie_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Tag not found"
        )

    return {
        "movie_id": row[0],
        "tag": row[1],
        "timestamp": row[2]
    }

@app.post("/tags")
def create_tag(tag: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tags(movie_id, tag, timestamp)
        VALUES (?, ?, ?)
        """,
        (
            tag["movie_id"],
            tag["tag"],
            tag["timestamp"]
        )
    )

    conn.commit()
    conn.close()

    return tag

@app.put("/tags/{movie_id}")
def update_tag(movie_id: int, tag: dict):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tags
        SET tag = ?, timestamp = ?
        WHERE movie_id = ?
        """,
        (
            tag["tag"],
            tag["timestamp"],
            movie_id
        )
    )

    conn.commit()
    conn.close()

    return {"message": "updated"}

@app.delete("/tags/{movie_id}")
def delete_tag(movie_id: int):

    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tags WHERE movie_id = ?",
        (movie_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "deleted"}