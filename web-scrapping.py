# ----------------------------------------------------------
# Step-by-step tutorial on scrapping a website using Python
# Code by Nitin Kumar : 27/08/2021
# ----------------------------------------------------------

# Step 0: Install all requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML source code

content = requests.get(url)
htmlContent = content.content
print(htmlContent)

# Step 2: Parse the HTML code

soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify())

# Step 3: HTML Tree traversal

# Commonly used types of objects:
# print(type(title)) # Tag
# print(type(soup)) # BeautifulSoup
# print(type(title.string)) # NavigableString
# Comment

# get the title of html page
title = soup.title

# # Get all the paragraphs from page
paras = soup.find_all('p')
print(paras)
#
# # Get all the anchors from page
anchor = soup.find_all('a')
all_links = set()
print(anchor)
for link in anchor:
    if link.get('href') != '#':
        link = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(link)

# get first element in the HTML page
print(soup.find('p'))
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
print(soup.find('p').get_text())  # print text inside the tag 'p'
print(soup.get_text())  # print all the text in web page without any tags

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup, features='html5lib')
print(type(soup2.p))
print(type(soup2.p.string))
exit()

navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent)
print(navbarSupportedContent.children)
print(navbarSupportedContent.contents)
for elem in navbarSupportedContent:
    print(elem)

# .contents - A tag's children are available are available as a list
# .children - A tag's children are available are available as a generator. Not stored in memory. But can be get using for loop or next function
# almost same

for item in navbarSupportedContent.stripped_strings:
    print(item)

for item in navbarSupportedContent.strings:
    print(item)

# immediate parent of selected item
print(navbarSupportedContent.parent)

# All parents of selected item
for item in navbarSupportedContent.parents:
    print(item.name)

# next sibling
print(navbarSupportedContent.next_sibling)

# previous sibling
print(navbarSupportedContent.previous_sibling)

# list of this id in website
elem = soup.select('#loginModal')
print(elem)

