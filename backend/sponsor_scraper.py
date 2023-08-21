import re
from newsletters import newsletter_patterns

long_string = """**Together with**


———————————————————————————

## **A Message From Litquidity & BOND**

What’s up everyone! If anyone here is an accredited investor or qualified purchaser and has interest in seeing private opportunities in the Padel space, please fill out a brief investor survey so we can keep you in mind on upcoming deal flow. 


*
"""


def find_sponsor(long_string):
    for pattern in newsletter_patterns:
        match = re.search(pattern, long_string)
        if match:
            return match.group(1)

    return None

newsletter_name = "Exec Sum"

sponsor = find_sponsor(long_string)
if sponsor:
    print(f"Sponsor: {sponsor}")
else:
    print("Sponsor not found.")


