import os
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_URL = os.environ.get("MONGODB_ADDON_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)

database = client.ufo_api
