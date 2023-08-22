from pymongo.mongo_client import MongoClient
import config
import openai
from gpt_scraper import identify_sponsor
from scrape_all_emails import scrape_all_emails
from read_emails import read_emails
from clean_database import clean_database
from update_sheet import update_sheet


#Common Variables
uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.sponsorScraper
collection = db.Emails


print("App Started")
print("------- Reading Emails -------")
read_emails(uri, client, db, collection)
print("------- Scraping Sponsors -------")
scrape_all_emails(uri, client, db , collection)
print("------- Cleaning DB -------")
clean_database(uri, client, db, collection)
print("-------Updating Sheet -------")
update_sheet(uri, client, db, collection)
print("App Complete")


