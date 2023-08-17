import re
from newsletters import newsletter_patterns

long_string = """View image: (https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/asset/file/4366494e-fade-4a91-b532-252544249306/Momentous_Logo_Newsletter.png)
Follow image link: (https://www.livemomentous.com/products/sleep-pack?selling_plan=803373239)
Caption: 

_^We receive free products to review and may receive commissions on purchases made through our links. See ^__[^our disclosure page^](https://barbend.com/additional-disclaimers-disclosures/)__^ for details.^_

Today’s newsletter is presented by Momentous. If you’re struggling to fall asleep or can’t shake that annoying grogginess after you wake up, [head here](https://www.livemomentous.com/products/sleep-pack?selling_plan=803373239) to see how the Momentous Sleep Pack can help."""


def find_sponsor(newsletter_name, long_string):
    if newsletter_name in newsletter_patterns:
        patterns = newsletter_patterns[newsletter_name]
        for pattern in patterns:
            match = re.search(pattern, long_string)
            if match:
                return match.group(1)

    return None

newsletter_name = "Barbend"

sponsor = find_sponsor(newsletter_name, long_string)
if sponsor:
    print(f"Sponsor: {sponsor}")
else:
    print("Sponsor not found.")
