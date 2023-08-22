import gspread
from pymongo.mongo_client import MongoClient
import config

uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.sponsorScraper
collection = db.Emails 
unexported_emails = collection.find({'exported': False})

def update_sheet(emails):
    sa = gspread.service_account(filename="sheets_secret.json")
    sh = sa.open("Email Sponsors")
    wks = sh.worksheet("Sponsors")

    for email in emails:
        row = [email['date'], email['from'], email['sponsor']]
        wks.append_row(row)
        collection.update_one({'_id': email['_id']}, {'$set': {'exported': True}})



update_sheet(unexported_emails)