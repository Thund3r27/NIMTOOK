import sqlite3
import csv

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

with open("python_api/data/movies.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        cursor.execute("""
            INSERT INTO movies(id, title, genres)
            VALUES (?, ?, ?)
        """, (
            row["movieId"],
            row["title"],
            row["genres"]
        ))

conn.commit()
conn.close()

with open("data/links.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT INTO links(movie_id, imdb_id, tmdb_id)
            VALUES (?, ?, ?)
        """, (
            row["movieId"],
            row["imdbId"],
            row["tmdbId"]
        ))

with open("data/ratings.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT INTO ratings(user_id, movie_id, rating, timestamp)
            VALUES (?, ?, ?, ?)
        """, (
            row["userId"],
            row["movieId"],
            row["rating"],
            row["timestamp"]
        ))

with open("data/tags.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        cursor.execute("""
            INSERT INTO tags(user_id, movie_id, tag, timestamp)
            VALUES (?, ?, ?, ?)
        """, (
            row["userId"],
            row["movieId"],
            row["tag"],
            row["timestamp"]
        ))

