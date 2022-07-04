from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from src.db import PyObjectId

class DeviceModel(BaseModel):
    name: str
    id: Optional[PyObjectId] = Field(alias='_id')
    device_id: str
    host: str
    user_agent: str
    hash_key: str
    date: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "Device Name",
                "device_id": "9488439w434",
                "host": "localhost:8000",
                "user_agent": "curl/7.68.0",
                "hash_key": "84d8e5389c67a826b683ff167",
                "date": "2022-06-18T22:48:04.688117"
            }
        }

class UpdateDeviceModel(BaseModel):
    name: str
    device_id: str
    host: str
    user_agent: str
    hash_key: str
    date: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Device Name 2",
                "device_id": "948843239w434",
                "host": "localhost:8080",
                "user_agent": "curl/7.68.0",
                "hash_key": "84d8e826b683ff167",
                "date": "2022-06-19T22:48:04.688117"
            }
        }
