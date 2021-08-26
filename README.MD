# Web Scrapping using python

> 1. Small tutorial for web scrapping using python with 'BeautifulSoup' library  
> 2. Step-by-Step tutorial with code & it's use  
> 3. No project, just tutorial. Actual implementation in coming days  
> 4. May not run as there must be some conflicting codes
> 5. Get full code with proper comments in the file [web-scrapping.py]()

# Modules used

- requests
- bs4 
- html5lib

# Steps to perform

> In order to perform web scrapping, we need to perform it in 4 steps:
> - Step 0: Install all requirements
> - Step 1: Get the HTML source code
> - Step 2: Parse the HTML code
> - Step 3: HTML Tree traversal

# Actual implementation

**Step 0: Install all requirements**

1. pip install requests  
2. pip install bs4  
3. pip install html5lib
<br />
4. Suggested CodeEditor - PyCharm Community Edition

<code>import requests  
from bs4 import BeautifulSoup  
url = "https://nitsanon.epizy.com"  
</code>  
---
**Step 1: Get the HTML source code**

<code>content = requests.get(url)  
htmlContent = content.content    
print(htmlContent)   # just print the whole source code of webpage    
</code>
---
**Step 2: Parse the HTML code**

<code>soup = BeautifulSoup(htmlContent, 'html.parser')    
print(soup.prettify())  # it'll print source code in well defined order with indendation    
</code>
---
**Step 3: HTML Tree traversal**

> Commonly used types of objects:  
>  - `print(type(title))  # Tag`  
>  - `print(type(soup))  # BeautifulSoup`  
>  - `print(type(title.string))  # NavigableString`  
>  - `Comment`

*# to get title of the page*  
`title = soup.title`  

*# Get all the paragraphs from page*  
<code>paras = soup.find_all('p')    
print(paras)  
</code>

*# Get all the anchors code from page*  
<code>anchor = soup.find_all('a')    
all_links = set()    
print(anchor)  
</code>

*# Get all the clickable links directly in console from page*  
<code>for link in anchor:  
     &nbsp;&nbsp;&nbsp;if link.get('href') != '#':  
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link = "https://nitsanon.epizy.com" + link.get('href')  
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all_links.add(link)  
         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(link)  
</code>

*# get first element in the HTML page*
<code>print(soup.find('p'))</code>  

*# get first element after p tag  
<code>print(soup.find('p')['class'])</code>


*# find all the elements with class lead*
<code>print(soup.find_all("p", class_="lead"))</code>


*# Get the text from the tags/soup*
<code>print(soup.find('p').get_text())  # print text inside the tag 'p'  
print(soup.get_text())  # print all the text in web page without any tags</code>

*# Comment as last object*  
`markup = "<p><!-- this is a comment --></p>"`  
<code>soup2 = BeautifulSoup(markup, features='html5lib')  
print(type(soup2.p))  
print(type(soup2.p.string))  
exit()  
</code>

*# navigation bars extraction*  

<code>navbarSupportedContent = soup.find(id='navbarSupportedContent')  
print(navbarSupportedContent) # navbar codes with parent  
print(navbarSupportedContent.children) # navbar code iteratble  
print(navbarSupportedContent.contents) # return codes of navbar  
<br>
for elem in navbarSupportedContent: # print title of navbar  
     &nbsp;&nbsp;&nbsp;&nbsp;print(elem)  
</code>

> *# difference between .children & .contents*  
> 
> -  .contents - A tag's children are available are available as a list  
> -  .children - A tag's children are available are available as a generator. Not stored in memory. But can be get using for loop or next function  

*# Print title of navbars*

<code>for item in navbarSupportedContent.stripped_strings:
&nbsp;&nbsp;&nbsp;&nbsp;print(item)  

for item in navbarSupportedContent.strings:
     print(item)  
</code>

*# Immediate parents of the item selected*
<code>print(navbarSupportedContent.parent)</code>


*# All parents of selected item*  
<code>for item in navbarSupportedContent.parents:  
&nbsp;&nbsp;&nbsp;&nbsp;print(item.name)
</code>

*# Find next sibling*
`print(navbarSupportedContent.next_sibling)`  


*# previous sibling*
`print(navbarSupportedContent.previous_sibling)`  


*# Full list of code for the id*  
<code>elem = soup.select('#loginModal')  
print(elem)
</code>

**Go through full [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) of BeautifulSoup.**














