from fastapi import FastAPI
import csv

app = FastAPI()

# Endpoint zwracający {'hello': 'world'}
@app.get("/")
async def read_root():
    return {"hello": "world"}

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
