from typing import Dict, List

from .db import db


def get_movie_by_id(id: int) -> Dict[str, str]:
    return db[id - 1]


def get_movies(*, limit: int, offset: int) -> List[Dict[str, str]]:
    return db[offset : offset + limit]  # noqa: E203
