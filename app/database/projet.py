import os
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_URL = os.environ.get("MONGODB_ADDON_URI")
MONGO_DB = os.environ.get("MONGODB_ADDON_DB")

db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = db.get_database(MONGO_DB)

# Retrieve a data with a matching Field
async def get_projet(id:str):
    try:
        list_data = []
        data_collection = database.get_collection("Projets")
        async for data in data_collection.find({"id": id}):
            list_data.append(data)
        return list_data
    except ValueError:
        print("error")