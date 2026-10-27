from fastapi import FastAPI
import csv

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

    with open("data/movies.csv", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            movie = Movie(
                row["movieId"],
                row["title"],
                row["genres"]
            )

            movies.append(movie.__dict__)

    return movies


@app.get("/links")
def get_links():

    links = []

    with open("data/links.csv", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            link = Link(
                row["movieId"],
                row["imdbId"],
                row["tmdbId"]
            )

            links.append(link.__dict__)

    return links


@app.get("/ratings")
def get_ratings():

    ratings = []

    with open("data/ratings.csv", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            rating = Rating(
                row["userId"],
                row["movieId"],
                row["rating"],
                row["timestamp"]
            )

            ratings.append(rating.__dict__)

    return ratings


@app.get("/tags")
def get_tags():

    tags = []

    with open("data/tags.csv", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:
            tag = Tag(
                row["userId"],
                row["movieId"],
                row["tag"],
                row["timestamp"]
            )

            tags.append(tag.__dict__)

    return tags