import json
from fastapi import FastAPI, Request
from datetime import datetime

from src.utils.crypt import Crypt

from src.routes.device import router as DeviceRouter
from src.routes.device import router as MediaRouter

app = FastAPI()
crypt = Crypt()

app.include_router(DeviceRouter, tags=["Device"], prefix="/device")
app.include_router(MediaRouter, tags=["Media"], prefix="/media")

with open("app.json", "r") as f:
    data = json.load(f)

@app.get("/")
def root(request: Request):
    print(request.headers)
    data["date"] = datetime.now()
    return data
