import json

import requests
from bs4 import BeautifulSoup as soup
from fake_headers import Headers

from src.db import db, Movie

with open('../data/sites.json') as f:
    data = json.load(f)

def scrape(name, site):
    # execute parser
    header = Headers(headers=False)
    fetch_uri = f"{site.host}{site.query}{name}"
    res = requests.get(fetch_uri ,headers=header.generate())

    # save to url db 

    # return 

def fetchMovieUrl(name):
    # check in db
    header = Headers(headers=False)
    fetch_uri = f"{site.host}{site.query}{name}"
    res = requests.get(fetch_uri ,headers=header.generate())
    # return else launch scraper