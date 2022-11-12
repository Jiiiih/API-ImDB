# imdb_request.py

import requests
from imdb_module.response import Response
from dotenv import load_dotenv
import json
import os

# load the .env file
load_dotenv()
api_key = os.getenv("api_key")


class ImdbRequest:

    def get_title(movie_title):
        url = f"https://imdb-api.com/en/API/SearchTitle/{api_key}/{movie_title}"
        response = requests.get(url)
        return Response(status_code=response.status_code, content=json.loads(response.content))

    def get_ratings(movie_id) -> [Response]:
        url = f"https://imdb-api.com/en/API/Ratings/{api_key}/{movie_id}"
        response = requests.get(url)
        return Response(status_code=response.status_code, content=json.loads(response.content))
