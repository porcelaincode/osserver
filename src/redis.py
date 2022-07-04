import os
import json
from pathlib import Path
from datetime import datetime

import redis
from dotenv import load_dotenv

path = Path("./.env")
load_dotenv(dotenv_path=path)

REDIS_HOST=os.environ["REDIS_HOST"]
REDIS_PORT=os.environ["REDIS_PORT"]

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def save(key, value, t:int or 600):
    res = r.set(key, value, ex=t)
    if res:
        return True
    else:
        return False

def get(key:str):
   res = r.get(key)
   return res

def delete(key:str):
    res = r.delete(key)
    if res:
        return True
    else:
        return False