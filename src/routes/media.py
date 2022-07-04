from fastapi import APIRouter, Body, Request
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from src.utils.movieapi import fetchSearchResults
from src.middleware.device import authDevice

from src.crud.media import (
    add_media,
    delete_media,
    retrieve_media,
    retrieve_medias,
    update_media,
)
from src.db import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

@router.get("/search/{name}&page={page}&limit={limit}")
def search(page: int, name: str, limit: str, request: Request):
    t = datetime.now()
    res = fetchSearchResults(name, page)
    print(request.headers["host"])
    #print(res["results"][:int(limit)])
    return {"data": {"res": res["results"][:int(limit)], "len": len(res["results"])}, "meta":{"date": datetime.now(), "elapsed": datetime.now() - t}}
    