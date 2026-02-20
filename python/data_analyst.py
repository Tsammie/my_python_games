# Scenario:
# You are working as a data analyst for a marketing company. You have been given a large text document containing customer reviews and feedback. Your task is to extract all email addresses and phone numbers from this document for further analysis.
import re
# Task:
# Write a Python script named `data_analyst.py` that:
# Reads the contents of a text file named reviews.txt.
with open("reviews.txt","r") as file:
    reviews = file.read()
# print(reviews)
# Extracts all email addresses and phone numbers from the text.
# Email addresses follow the standard format: username@domain.tld
pattern = r'[a-zA-Z0-9_+-]+@[a-zA-Z0-9.]+\.[a-zA-z]{2,3}'
matches = re.findall(pattern,reviews)
# print(matches)
# Phone numbers are in the format: +234 803 456 7890
phone_pattern = r'[+]\d{3} \d{3} \d{3} \d{4}'
phone_match = re.findall(phone_pattern,reviews)
# print(phone_match)
# Writes the extracted email addresses to a file named emails.txt and the phone numbers to a file named phone_numbers.txt.
with open('emails.txt','w') as file:
    for match in matches:
        file.write(match + "\n")

with open('phone_numbers.txt','w') as file:
    for phone in phone_match:
        file.write(phone + "\n")
# Requirements:
# Use regular expressions to find the email addresses and phone numbers.
# Ensure that the extracted data is saved in separate files, one for emails and one for phone numbers.
