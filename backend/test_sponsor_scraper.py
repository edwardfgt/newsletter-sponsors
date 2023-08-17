import re
from newsletters import all_newsletters, newsletter_patterns
from sponsor_scraper import find_sponsor

long_string = """
View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4366494e-fade-4a91-b532-252544249306/Momentous_Logo_Newsletter.png)
Follow image link: (https://www.livemomentous.com/products/sleep-pack?selling_plan=803373239)
Caption: 

_^We receive free products to review and may receive commissions on purchases made through our links. See ^__[^our disclosure page^](https://barbend.com/additional-disclaimers-disclosures/)__^ for details.^_

Today’s newsletter is presented by Momentous. If you’re struggling to fall asleep or can’t shake that annoying grogginess after you wake up, [head here](https://www.livemomentous.com/products/sleep-pack?selling_plan=803373239) to see how the Momentous Sleep Pack can help.

... (rest of the content)

"""

def test_find_sponsor_with_match():
    newsletter_name = "Barbend"
    expected_sponsor = "Momentous"
    sponsor = find_sponsor(newsletter_name, long_string)
    assert sponsor == expected_sponsor

def test_find_sponsor_no_match():
    newsletter_name = "Bullseye" 
    sponsor = find_sponsor(newsletter_name, long_string)
    assert sponsor is None

def test_find_sponsor_invalid_newsletter():
    newsletter_name = "Invalid"
    sponsor = find_sponsor(newsletter_name, long_string)
    assert sponsor is None

# Check that REGEX patterns are established for all newsletters
def test_newsletter_patterns_exist():
    for newsletter_name in all_newsletters.values():
        assert newsletter_name in newsletter_patterns

def test_no_match():
    invalid_long_string = "NO MATCH"

    newsletter_name = "Barbend"
    sponsor = find_sponsor(newsletter_name, invalid_long_string)
    assert sponsor is None, "Expected no match, but a match was found."

