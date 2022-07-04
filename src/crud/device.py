
from src.db import device_helper, db
from bson.objectid import ObjectId

device_collection = db.get_collection("devices")

# Retrieve all devices present in the database
async def retrieve_devices():
    devices = []
    async for device in device_collection.find():
        devices.append(device_helper(device))
    return devices


# Add a new device into to the database
async def add_device(device_data: dict) -> dict:
    device = await device_collection.insert_one(device_data)
    new_device = await device_collection.find_one({"_id": device.inserted_id})
    return device_helper(new_device)


# Retrieve a device with a matching ID
async def retrieve_device(id: str) -> dict:
    device = await device_collection.find_one({"_id": ObjectId(id)})
    if device:
        return device_helper(device)


# Update a device with a matching ID
async def update_device(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    device = await device_collection.find_one({"_id": ObjectId(id)})
    if device:
        updated_device = await device_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_device:
            return True
        return False


# Delete a device from the database
async def delete_device(id: str):
    device = await device_collection.find_one({"_id": ObjectId(id)})
    if device:
        await device_collection.delete_one({"_id": ObjectId(id)})
        return True