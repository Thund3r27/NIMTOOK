import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genres TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS links (
    movie_id INTEGER,
    imdb_id INTEGER,
    tmdb_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ratings (
    user_id INTEGER,
    movie_id INTEGER,
    rating REAL,
    timestamp INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tags (
    user_id INTEGER,
    movie_id INTEGER,
    tag TEXT,
    timestamp INTEGER
)
""")

conn.commit()
conn.close()