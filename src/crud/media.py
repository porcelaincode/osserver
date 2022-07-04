
from src.db import media_helper, db
from bson.objectid import ObjectId

media_collection = db.get_collection("media")

# Retrieve all medias present in the database
async def retrieve_medias():
    medias = []
    async for media in media_collection.find():
        medias.append(media_helper(media))
    return medias


# Add a new media into to the database
async def add_media(media_data: dict) -> dict:
    media = await media_collection.insert_one(media_data)
    new_media = await media_collection.find_one({"_id": media.inserted_id})
    return media_helper(new_media)


# Retrieve a media with a matching ID
async def retrieve_media(id: str) -> dict:
    media = await media_collection.find_one({"_id": ObjectId(id)})
    if media:
        return media_helper(media)


# Update a media with a matching ID
async def update_media(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    media = await media_collection.find_one({"_id": ObjectId(id)})
    if media:
        updated_media = await media_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_media:
            return True
        return False


# Delete a media from the database
async def delete_media(id: str):
    media = await media_collection.find_one({"_id": ObjectId(id)})
    if media:
        await media_collection.delete_one({"_id": ObjectId(id)})
        return True