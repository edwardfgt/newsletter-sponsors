#Current Scraped Newsletters

all_newsletters = {
    "barbendnewsletter@mail2.barbend.com": "Barbend",
    "jeffs-bullseye@b.bullseyeoptiontrading.com": "Bullseye",
    "Thomas@heydink.com": "The Dink",
    "newsletter@mail.milkroad.com": "Milk Road",
    "investingjournal@mail.beehiiv.com": "Investing Journal",
    "general@mail.payloadspace.com": "Payload",
    "eventheodds@mail.beehiiv.com": "Even The Odds",
    "news@execsum.co": "Exec Sum",
    "press@shortsqueez.co": "Short Squeez",
    "theblueprint@mail.readtheblueprint.com": "The Blueprint",
}


newsletter_patterns = {
    "Barbend": [
        r"This newsletter is sponsored by (.+?)\.",
    ],
    "Bullseye": [
        r"Sponsored by: (.+)",
    ],
    "The Dink": [
        r"Sponsored by: (.+)",
    ],
    "Milk Road": [
        r"Sponsored by: (.+)",
    ],
    "Payload": [
        r"Sponsored by: (.+)",
    ],
    "Bullseye": [
        r"Sponsored by: (.+)",
    ],
    "Even The Odds": [
        r"Sponsored by: (.+)",
    ],
    "Exec Sum": [
        r"Sponsored by: (.+)",
    ],
    "Short Squeez": [
        r"Sponsored by: (.+)",
    ],
    "The Blueprint": [
        r"Sponsored by: (.+)",
    ],
    
}

