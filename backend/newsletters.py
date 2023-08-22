#Current Scraped Newsletters

all_newsletters = {
    "barbendnewsletter@mail2.barbend.com": "Barbend",
    "newsletter@mail.milkroad.com": "Milk Road",
    "investingjournal@mail.beehiiv.com": "Investing Journal",
    "general@mail.payloadspace.com": "Payload",
    "eventheodds@mail.beehiiv.com": "Even The Odds",
    "news@execsum.co": "Exec Sum",
    "press@shortsqueez.co": "Short Squeez",
    "theblueprint@mail.readtheblueprint.com": "The Blueprint",
    "news@newsletter.importantnotimportant.com": "Important Not Important",
    "news@thehustle.co": "The Hustle",
    "swaggystocks@mail.beehiiv.com": "Swaggy Stonks",
}


newsletter_patterns = [
        r"This newsletter is sponsored by (.+?)\.",
        r"Today’s BarBend Newsletter is presented by ([A-Za-z0-9\s]+)\.",
        r"Today’s newsletter is presented by ([A-Za-z0-9\s]+)\.",
        r"Sponsored by: (.+)",
        r"today’s sponsor,\s*\[(.*?)\]\(https:\/\/prf\.hn\/click\/[^\)]+\)",
        r"A Message From ([A-Za-z0-9\s]+)\.",
        r"A Message From Litquidity & ([A-Za-z0-9\s&]+)\."
]