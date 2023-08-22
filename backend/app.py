from pymongo.mongo_client import MongoClient
import config
import openai
from gpt_scraper import identify_sponsor
from scrape_all_emails import scrape_all_emails
from read_emails import read_emails
from clean_database import clean_database
from update_sheet import update_sheet

print("App Started")
print("------- Reading Emails -------")
read_emails()
print("------- Scraping Sponsors -------")
scrape_all_emails()
print("------- Cleaning DB -------")
clean_database()
print("-------Updating Sheet -------")
update_sheet()
print("App Complete")


