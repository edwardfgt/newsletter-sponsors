from pymongo.mongo_client import MongoClient
import config
import newsletters
import re
from sponsor_scraper import find_sponsor

uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"

#connects to mongoDB
client = MongoClient(uri)
db = client.sponsorScraper
collection = db.Emails 

all_records = collection.find()

for record in all_records:
    body = record.get('body', '')  # Replace with the actual field name

    sponsor = find_sponsor(body)  # Replace with your sponsor extraction logic
    if sponsor:
        print(f"Sponsor: {sponsor}")
    else:
        print("Sponsor not found.")

# Close the MongoDB client connection
client.close()