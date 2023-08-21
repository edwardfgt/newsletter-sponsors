import openai

openai.api_key = config.gpt

def identify_sponsor(record):
    newsletter = record.get('from', '')
    body = record.get('body', '')

    conversation = [
        {
            "role": "user",
            "content": f"""Please read this email sent from {newsletter} and identify the sponsor.
            \n Make sure that you only return a single string with the sponsor company's name and no additional filler.
            \n Make sure that you do not return the same name as the newsletter name, the sponsor must be a different company.
            \n If there is no sponsor, simply say - no sponsor found
            \n The email copy to scrape is below:
            \n {body}"""
        }
    ]

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    model_response = chat_completion.choices[0].message['content']
    return f"{newsletter} sponsor is: {model_response}"
