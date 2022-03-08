from .common_utils import database


# Custom request: Retrieve a data with a matching Field
async def get_artisans_category(category: str):
    try:
        list_data = []
        data_collection = database.get_collection("Artisan")
        async for data in data_collection.find({"categorie": category}):
            list_data.append(data)
        return list_data
    except ValueError:
        print("error")
