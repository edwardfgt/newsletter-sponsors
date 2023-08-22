from pymongo.mongo_client import MongoClient
import config

def clean_database(collection):
    delete_query = {
        "$or": [
            {"sponsor": "no sponsor found"},
            {"sponsor": "Beehiiv"}
        ]
    }
    collection.delete_many(delete_query)

