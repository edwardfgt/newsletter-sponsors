from pymongo.mongo_client import MongoClient
import config


uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"

#Connect to Mongo and Gmail API
client = MongoClient(uri)

db = client.sponsorScraper
collection = db.Emails 

def clean_database(uri, client, db, collection):
    delete_query = {
        "$or": [
            {"sponsor": "no sponsor found"},
            {"sponsor": "Beehiiv"}
        ]
    }
    collection.delete_many(delete_query)

clean_database(uri, client, db, collection)

