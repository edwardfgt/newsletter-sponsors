from simplegmail import Gmail
from simplegmail.query import construct_query
from pymongo.mongo_client import MongoClient
import config
import newsletters
import re

def read_emails(uri, client, db, collection):
    # Connect to Mongo and Gmail API
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
    print(f"{len(messages)} Unread messages retrieved")
    index = 0
    for message in messages:
        from_email = re.search(r'<([^>]+)>', message.sender).group(1)
        matching_newsletter = None

        for newsletter_email in newsletters.all_newsletters:
            if from_email.lower() in newsletter_email.lower():
                matching_newsletter = newsletters.all_newsletters[newsletter_email]
                print(matching_newsletter)
                break

        if matching_newsletter:
            data_entry = {
                "from": matching_newsletter,
                "subject": message.subject,
                "date": message.date,
                "body": message.plain,
                "sponsor": "Pending",
                'exported': False,
            }

            collection.insert_one(data_entry)
            index += 1
        message.mark_as_read()

    client.close()
    print(f"{index} records successfully added to the database")
