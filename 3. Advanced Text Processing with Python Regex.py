# Objective:
# The goal of this assignment is to harness the full potential of Python's 
# Regular Expressions for advanced text processing. You'll tackle complex 
#     tasks involving data extraction, validation, and transformation, 
# sharpening your skills in applying regex in various challenging scenarios.

# Task 1: Advanced Data Extraction

# Problem Statement:
# Develop a script to extract specific information from a formatted text. 
# The text contains data entries delimited by semicolons and formatted 
# as 'Key: Value'. Extract the value corresponding to a specific key.

# Code Example:

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
occupation = re.search(r"(?<=Occupation: )\w+",text)
print (occupation.group())

# # Extract the Occupation from the text
# # Your code here

# Expected Outcome:

#     Successfully extract the 'Occupation' value from the text.
#     Implement a regex pattern that accurately targets and captures the desired data.

# Task 2: URL Validator

# Problem Statement:
# Write a Python program to validate a list of URLs. A valid URL should start 
# with 'http://' or 'https://', followed by a domain name.

# Code Example:

urls = ["https://example.com", "www.example.com", "http://test.com"]
# # Validate each URL in the list
# # Your code here
for url in urls:
    correctUrl = re.findall(r"^(http://|https://)\w]+.[\w{3}]",url)
    print(correctUrl)
# Expected Outcome:

#     Correctly identify and categorize valid and invalid URLs from the list.
#     Use regex to validate the format of each URL.
