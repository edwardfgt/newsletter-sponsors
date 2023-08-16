from simplegmail import Gmail
from simplegmail.query import construct_query
from pymongo.mongo_client import MongoClient
import config


uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"

#Connect to Mongo and Gmail API
client = MongoClient(uri)
gmail = Gmail()

db = client.sponsorScraper
collection = db.Emails 

query_params = {
    "newer_than": (1, "day"),
}

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

messages = gmail.get_unread_inbox()

for message in messages:
    dataEntry = {
        "from": message.sender,
        "subject": message.subject,
        "date": message.date,
        "body": message.plain,
    }
    collection.insert_one(dataEntry)
    message.mark_as_read()

client.close()