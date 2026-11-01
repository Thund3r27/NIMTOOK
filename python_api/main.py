from fastapi import FastAPI
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