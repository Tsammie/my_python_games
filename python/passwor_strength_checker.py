user_password = input("What is your password: ")
alpl = 'abcdefghijklmnopqrstuvwxyz'
alpu = alpl.upper()
digit = '1234567890'
spc = '!@#$%^&*()_+}{|?><'
a,b,c,d = False,False,False,False

for i in user_password:
    if i in alpl:
        a = True
    elif i in alpu:
        b = True
    elif i in digit:
        c = True
    elif i in spc:
        d = True
if len(user_password) > 8 and a and b and c and d:
    print("Strong Password\nAccepted!!!")
else:
    print('Not strong enough, Please try again!')


# Regular Expression (REGEX)
# These are sequence of characters that define search pattern. They are used for string manipulation and matching.
import re
# Example 1. Find all occurence 
# text = "There are 123 apples and 456 oranges."

# pattern = r'\d+'

# matches = re.findall(pattern,text)

# print(matches)

# Example 2: Simple match
# text = 'A word in a sentence'

# pattern = r'\bword\b'

# matches = re.search(pattern, text)

# print(matches)

# Example 3: Replace text
# text = 'This     is  a text'

# pattern = r'\s+'

# matches = re.sub(pattern, ' ', text)

# print(matches)

# Example 4: Matching specific pattern part 1
# text = "Contact us at supp+ort@example.com for more info. should be @ working hours"

# pattern = r'\w+@\w+.\w{2,3}'

# matches = re.findall(pattern, text)

# print(matches)

# part 2 
# text = "Contact us at supp+ort@example.com for more info. should be @ working hours"

# pattern = r'[a-zA-Z0-9_+-]+@[a-zA-Z0-9.]+\.[a-zA-z]{2,3}'

# matches = re.findall(pattern, text)

# print(matches)

# Example 5: Extracting data
# Example 2: Extract dates in YYYY-MM-DD format
# text = "The event is on 2023-08-15. Deadline is 2023-08-01."

# Validating a phone number 
# phone_number = "(123) 456-7890"

# pattern = r'\(\d{3}\) \d{3}-\d{4}'

# match = re.findall(pattern, phone_number)

# if match:
#     print('Correct phone number')
#     print(match)
# else:
#     print('Incorrect phone number format')


# # Example 6: Splitting strings

# text = "apple  , banana,      cherry  ,   date"

# pattern = r'\s*,\s*'

# match = re.split(pattern, text)

# print(match)

# Using groups and capturing 
# Exmaple 7: Capture groups of text

# text = "Emails: alice@example.com, bob@domain.org"

# pattern = r"(\w+)@(\w+\.\w+)"

# match = re.findall(pattern, text)

# print(match)

# for user, domain in match:
#     print("User:", user, "Domain:", domain)

import re
# Example 7: Using named groups
# pattern = r"(?P<user>[a-zA-Z0-9.]+)@(?P<domain>\w+\.\w+)"
# text = "Contact: john.doe@company.com"
# match = re.search(pattern, text)
# if match:
#     print("User:", match.group("user")) 
#     print("Domain:", match.group("domain"))

# Example 8: Compiling a regex for reuse
pattern = re.compile(r"\b\w{4}\b")
text = "This is a test of regex patterns."
matches = pattern.findall(text)
print("Four-letter words:", matches)
