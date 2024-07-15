# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.

URL = "https://en.wikipedia.org/wiki/Web_scraping"

import requests
from bs4 import BeautifulSoup
import re

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract all the links on the page
links = soup.find_all('a')

# Filter out the navigation links
filtered_links = [link.get('href') for link in links if link.get('href') and not link.get('href').startswith('#') and link.get('href').startswith('/wiki/')]

# pick a random number between 1-20, then use that to select a link to follow
import random

random_link = random.choice(filtered_links)

# Follow the link

response = requests.get(f"https://en.wikipedia.org{random_link}")

soup = BeautifulSoup(response.text, 'html.parser')

# Extract the text content from the article

text = soup.get_text()

# Save the text content to a local text file

with open('wiki_text.txt', 'w', encoding = 'utf-8') as file:
    file.write(text)