import os
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_URL = os.environ.get("MONGODB_ADDON_URI")

db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = db.brzto7idtuqprth

async def retrieve_datas(collection:str):
    list_data = []
    data_collection = database.get_collection(collection)
    async for data in data_collection.find():
        data.append(list_data)
    return data

# Retrieve a data with a matching ID
async def retrieve_data(collection:str, id:str):
    data_collection = database.get_collection(collection)
    data = await data_collection.find_one({"_id": id})
    if data:
        return data

# Add a new data into to the database
async def insert_data(collection:str,add_data:dict):
    data_collection = database.get_collection(collection)
    data = await data_collection.insert_one(add_data)
    new_data = await data_collection.find_one({"_id": data.inserted_id})
    return new_data


# Update a data with a matching ID
async def update_data(collection:str, id: str, data_update: dict):
    # Return false if an empty request body is sent.
    data_collection = database.get_collection(collection)
    if len(data_update) < 1:
        return False
    data = await data_collection.find_one({"_id": id})
    if data:
        updated_data = await data_collection.update_one(
            {"_id": id}, {"$set": data}
        )
        if updated_data:
            return True
        return False


# Delete a data from the database
async def remove_data(id: str):
    data_collection = database.get_collection(collection)
    data = await data_collection.find_one({"_id": id})
    if data:
        await data_collection.delete_one({"_id": id})
        return True
