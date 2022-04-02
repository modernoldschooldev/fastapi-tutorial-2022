from fastapi import FastAPI, Path, Query

from . import crud

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello, World"}


@app.get("/movie/{id}", summary="Get single movie from database by ID")
def get_movie(id: int = Path(..., description="Movie ID to retrive")):
    return crud.get_movie_by_id(id)


@app.get("/movies", summary="Retrieve list of movies from database")
def get_movies(
    limit: int = Query(
        5, description="Limit of how many results to return", gt=0, lt=11
    ),
    offset: int = Query(0, description="Offset to start fetching movies from", gt=-1),
):
    return crud.get_movies(limit=limit, offset=offset)
