import os
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_URL = os.environ.get("MONGODB_ADDON_URI")

db = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = db.brzto7idtuqprth

# Retrieve a data with a matching Field
async def get_artisans_category(category:str, ):
    data_collection = database.get_collection("Artisans")
    data = await data_collection.find({"categoryArtisan": category})
    if data:
        return data