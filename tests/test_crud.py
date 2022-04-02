import pytest
import tutorial.crud as crud


def test_get_movie_by_id():
    movie = crud.get_movie_by_id(1)
    assert movie["title"] == "Black Panther"


def test_get_movie_by_id_invalid_id():
    with pytest.raises(IndexError):
        crud.get_movie_by_id(12)


def test_get_movies():
    # check first 5 movies
    movies = crud.get_movies(limit=5, offset=0)
    assert len(movies) == 5
    assert movies[0]["title"] == "Black Panther"
    assert movies[4]["title"] == "Iron Man"

    # check last 5 movies
    movies = crud.get_movies(limit=5, offset=6)
    assert len(movies) == 5
    assert movies[0]["title"] == "Spider-Man"
    assert movies[4]["title"] == "Deadpool"

    # no results are returned if offset is beyond the end
    movies = crud.get_movies(limit=1, offset=11)
    assert movies == []

    # get all 11 movies, even if more are requested
    movies = crud.get_movies(limit=50, offset=0)
    assert len(movies) == 11
    assert movies[5]["title"] == "Avatar"
