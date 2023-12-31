import openai
import config

def identify_sponsor(record):
    openai.api_key = config.gpt
    newsletter = record.get('from', '')
    body = record.get('body', '')

    conversation = [
        {
            "role": "user",
            "content": f"""Please read this email sent from {newsletter} and identify the sponsor.
            \n Make sure that you only return the sponsor company's name, DO NOT INCLUDE ANY OTHER WORDS.
            \n Make sure that you do not return the same name as the newsletter name, the sponsor must be a different company.
            \n If there is no sponsor, simply say - no sponsor found
            \n The email copy to scrape is below:
            \n {body}"""
        }
    ]

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=conversation
    )

    model_response = chat_completion.choices[0].message['content']
    return model_response
