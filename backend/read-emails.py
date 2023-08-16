from simplegmail import Gmail
from simplegmail.query import construct_query
from pymongo.mongo_client import MongoClient
import config


uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

gmail = Gmail()

query_params = {
    "newer_than": (1, "day"),
}

messages = gmail.get_messages(query=construct_query(query_params))

# for message in messages:
#     print("From: " + message.sender)
#     print("Subject: " + message.subject)
#     print("Date: " + message.date)
#     print("Preview: " + message.snippet)
#     print("Message Body: " + message.plain)


# {
#   "from": "Jane Doe",
#   "subject": "jane@abc.com",
#   "date": 26,
#   "body": "hello",
# }