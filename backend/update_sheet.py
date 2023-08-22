import gspread
from pymongo.mongo_client import MongoClient
import config

def update_sheet(uri, client, db, collection):
    emails = collection.find({'exported': False})
    sa = gspread.service_account(filename="sheets_secret.json")
    sh = sa.open("Email Sponsors")
    wks = sh.worksheet("Sponsors")

    for email in emails:
        row = [email['date'], email['from'], email['sponsor']]
        wks.append_row(row)
        collection.update_one({'_id': email['_id']}, {'$set': {'exported': True}})


