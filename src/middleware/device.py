import hashlib

from bson import ObjectId

from src.db import db, Device
from src.redis import get, save

def authDevice(id, headers, auth_hash):
    device = get(id)
    if device != None:
        device = db.device.find_one({'hash_key': device})
        return {"error": False, device: device, "message": "Authentication successfull"}
    else:
        device = db.device.find_one({'_id':ObjectId(id)})
        if device != None:
            res = save(id, device.hash_key, 60*60*24)
            return {"error": False, device: device, "message": "Authentication successfull"}
        else:
            return {"error": True, device: None, "message": "Auth request unsuccessful. No device found."}
