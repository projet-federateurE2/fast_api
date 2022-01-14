import os
import motor.motor_asyncio

MONGO_URL = os.environ.get("MONGODB_ADDON_URI")
MONGO_DB = os.environ.get("MONGODB_ADDON_DB")

db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = db.get_database(MONGO_DB)

# Retrieve a data with a matching Field
async def get_artisans_category(category:str):
    try:
        list_data = []
        data_collection = database.get_collection("Artisan")
        async for data in data_collection.find({"categorie": category}):
            list_data.append(data)
        return list_data
    except ValueError:
        print("error")