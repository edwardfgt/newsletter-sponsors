import gspread
from pymongo.mongo_client import MongoClient
import config

uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.sponsorScraper
collection = db.Emails 
emails = collection.find()


def update_sheet(emails):

    sa = gspread.service_account(filename="sheets_secret.json")
    sh = sa.open("Email Sponsors")
    wks = sh.worksheet("Sponsors")

    for email in emails:
        row = [email['date'], email['from'], email['sponsor']]
        wks.append_row(row)



update_sheet(emails)