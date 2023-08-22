from pymongo.mongo_client import MongoClient
import config
import openai
from gpt_scraper import identify_sponsor

def scrape_all_emails(uri, client, db, collection):
    openai.api_key = config.gpt
    client = MongoClient(uri)
    db = client.sponsorScraper
    collection = db.Emails 

    all_records = collection.find({"sponsor": "Pending"})

    for record in all_records:
        sponsor_result = identify_sponsor(record)
        
        if "no sponsor found" in sponsor_result.lower():
            collection.update_one({"_id": record["_id"]}, {"$set": {"sponsor": "no sponsor found"}})
            print('No Sponsor Found')
        else:
            collection.update_one({"_id": record["_id"]}, {"$set": {"sponsor": sponsor_result}})
            print(f"Identified sponsor for {record['from']}: {sponsor_result}")

    client.close()
