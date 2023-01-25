# string = "My email address is john@example.com and my friend's"

# email_addresses = []

# for word in string.split():
#     if "@" in word:
#         email_addresses.append(word)

# print("Email addresses: ", email_addresses)

import re

string = "My email address is john@example.com and my friend's email address is mike@example.com"

# Using regular expression to find email addresses
email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', string)

print("Email addresses: ", email_addresses)