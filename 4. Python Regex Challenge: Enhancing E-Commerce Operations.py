# Objective:

# This assignment aims to refine your skills in using Python Regular Expressions 
# to address common challenges in e-commerce operations. You will focus on tasks 
# such as product categorization, customer review analysis, and data formatting, 
# crucial for efficient e-commerce management.

# Task 1: Product Description Keyword Tagging

# Problem Statement:
# You have a list of product descriptions. Your task is to tag each product based 
# on keywords in the description. For instance, tag products as 'Electronics', 'Apparel', 
# or 'Home & Kitchen' based on relevant keywords found in their descriptions.

# Code Example:

import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

keywords = {
    "Electronics": ["smartphone", "screen", "memory"],
    "Apparel": ["cotton", "t-shirt", "size"],
    "Home & Kitchen": ["stainless steel", "kitchen", "knife"]
}

def tag_products(descriptions, keywords):
    tagged_products = []
    for description in descriptions:
        tag = ""

        for category, words in keywords.items():
            for word in words:
                if re.search(word, description):
                    tag = category
                    break
            if bool(tag) == True:
                break

        tagged_products.append((tag, description))
    return tagged_products

tagged_products = tag_products(descriptions, keywords)
print(tagged_products)


# # Tag each product based on keywords in the description
# # Your code here

# Expected Outcome:

#     Efficiently tag each product with the appropriate category 
# ('Electronics', 'Apparel', 'Home & Kitchen') using regex to identify relevant keywords.
#     Use regex to match specific product-related keywords in each description.

# Task 2: Pricing Format Standardization

# Problem Statement:
# You have a string containing various price formats from an international e-commerce 
# site. Standardize all prices to the format 'USD XX.XX', converting from formats 
# like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.

# Code Example:

price_data = "Items cost $15.99, 20.00 USD, and 7.50$."

def repl(match):
        price = match.group(1) if match.group(1) else match.group(2)
        return f"USD {price}"

def standardize_prices(price_data):
    newPrice = re.sub(r"\$?(\d+\.\d+)\$? USD|\$?(\d+\.\d+)\$?", repl, price_data)
    return newPrice

new_prices = standardize_prices(price_data)
print(new_prices)

# # Standardize all prices to 'USD XX.XX' format
# # Your code here

# Expected Outcome:

#     Convert all price formats in the string to a standardized 'USD XX.XX' format.
#     Use re.sub() to perform the necessary replacements and format transformations.
