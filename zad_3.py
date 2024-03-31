from fastapi import FastAPI
import csv


app = FastAPI()


# Przeniesienie endpointu pod /test
@app.get("/test")
async def read_test():
    return {"hello": "world"}


# Model danych filmu
class Movie:
    def __init__(self, movieId, title, genres):
        self.movirId = movieId
        self.title = title
        self.genres = genres


# Model danych linku
class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movirId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


# Model danych ratingu
class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movirId = movieId
        self.rating = rating
        self.timestamp = timestamp


# Model danych ratingu
class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movirId = movieId
        self.tag = tag
        self.timestamp = timestamp


# Endpoint zwracający listę filmów w formie obiektów JSON
@app.get("/movies")
async def read_movies():
    movies = []
    with open('database/movies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Movie(movieId=row['movieId'], title=row['title'], genres=row['genres'])
            movies.append(movie.__dict__)
    return movies


# Endpoint zwracający listę linków w formie obiektów JSON
@app.get("/links")
async def read_movies():
    movies = []
    with open('database/links.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Link(movieId=row['movieId'], imdbId=row['imdbId'], tmdbId=row['tmdbId'])
            movies.append(movie.__dict__)
    return movies


# Endpoint zwracający listę ratingów w formie obiektów JSON
@app.get("/ratings")
async def read_movies():
    movies = []
    with open('database/ratings.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Rating(userId=row['userId'], movieId=row['movieId'], rating=row['rating'], timestamp=row['timestamp'])
            movies.append(movie.__dict__)
    return movies


# Endpoint zwracający listę tagów w formie obiektów JSON
@app.get("/tags")
async def read_movies():
    movies = []
    with open('database/tags.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Tag(userId=row['userId'], movieId=row['movieId'], tag=row['tag'], timestamp=row['timestamp'])
            movies.append(movie.__dict__)
    return movies