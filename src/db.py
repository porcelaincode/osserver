import os
from pathlib import Path
import motor.motor_asyncio
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, List
from dotenv import load_dotenv
# from pymongo import MongoClient

path = Path(".env")
load_dotenv(dotenv_path=path)

MONGO_HOST = os.environ.get("DATABASE_HOST")
MONGO_PORT = os.environ.get("DATABASE_PORT")
MONGO_URI = os.environ.get("DATABASE_URI")
ENV = os.environ.get("ENVIRONMENT")

database_url = MONGO_URI if ENV == 'production' else f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

# client = MongoClient(host=database_url)
client = motor.motor_asyncio.AsyncIOMotorClient(database_url)

db = client.openstream

'''
Helpers

1) Device
TODO:2) Response
TODO:3) Media
TODO:4) Room
'''

def device_helper(device) -> dict:
    return {
        "id": str(device["_id"]),
        "device_id": device["device_id"],
        "name": device["name"],
        "user_agent": device["user_agent"],
        "host": device["host"],
        "hash_key": device["hash_key"],
        "date": device["date"],
    }

'''
Models

1) Device
2) Response
TODO:3) Media
TODO:4) Room
'''

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}