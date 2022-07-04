import os
import requests
from pathlib import Path
from dotenv import load_dotenv

path = Path(".env")
load_dotenv(dotenv_path=path)

TMDB_URI = os.environ.get("MOVIESDB_URI")
TMDB_KEY = os.environ.get("MOVIESDB_KEY")

def fetchSearchResults(name, page):
    request_uri = f"{TMDB_URI}search/movie?query={name}&api_key={TMDB_KEY}&page={page}"
    res = requests.get(request_uri)
    return res.json()

def fetchMovieInfo(name, page):
    request_uri = f"{TMDB_URI}search/multi?query={name}&api_key={TMDB_KEY}&page={page}"
    res = requests.get(request_uri)
    return res.json()