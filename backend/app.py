from pymongo.mongo_client import MongoClient
import config
import os
import openai

openai.api_key = config.gpt

uri = f"mongodb+srv://Edward:{config.mongoPw}@emails.443qzuu.mongodb.net/?retryWrites=true&w=majority"

#connects to mongoDB
client = MongoClient(uri)
db = client.sponsorScraper
collection = db.Emails 

all_records = collection.find()

num_records_to_process = 10  
processed_records = 0

for record in all_records:
    if processed_records >= num_records_to_process:
        break
    
    newsletter = record.get('from', '')
    body = record.get('body', '')

    conversation = [
        {"role": "user", "content": f"Please read this email sent from {newsletter} and identify the sponsor, only return a single string with the sponsor companies name:\n{body}"}
    ]

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    model_response = chat_completion.choices[0].message['content']
    print(f"{newsletter} sponsor is: {model_response}")
    processed_records += 1

client.close()