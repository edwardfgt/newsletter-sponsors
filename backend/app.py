from pymongo.mongo_client import MongoClient
import config
import openai
from gpt_scraper import identify_sponsor

openai.api_key = config.gpt

uri = f"mongodb+srv://Edward:{config.mongoPw}@your-mongodb-uri"
client = MongoClient(uri)
db = client.sponsorScraper
collection = db.Emails 

all_records = collection.find()

num_records_to_process = 10
processed_records = 0

for record in all_records:
    if processed_records >= num_records_to_process:
        break
    
    sponsor_result = identify_sponsor(record)
    print(sponsor_result)
    processed_records += 1

client.close()
