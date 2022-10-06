# Web Scrapping using python

> 1. Small tutorial for web scrapping using python with 'BeautifulSoup' library  
> 2. Step-by-Step tutorial with code & it's use  
> 3. No project, just tutorial. Actual implementation in coming days  
> 4. May not run as there must be some conflicting codes
> 5. Get full code with proper comments in the file [web-scrapping.py](https://github.com/nitin30kumar/web-scrapping-using-python/blob/main/web-scrapping.py)

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
4. CodeEditor - PyCharm Community Edition (Suggested)   

`

    import requests  
    from bs4 import BeautifulSoup  
    url = "https://nitsanon.epizy.com"


---  
**Step 1: Get the HTML source code**  



    content = requests.get(url)  
    htmlContent = content.content  
    print(htmlContent)   # just print the whole source code of webpage



---
**Step 2: Parse the HTML code**  



    soup = BeautifulSoup(htmlContent, 'html.parser')
    print(soup.prettify())  # it'll print source code in well defined order with indendation



---  
**Step 3: HTML Tree traversal**  

> Commonly used types of objects:  
>  - `print(type(title))  # Tag`  
>  - `print(type(soup))  # BeautifulSoup`  
>  - `print(type(title.string))  # NavigableString`  
>  - `Comment`

*# to get title of the page*  

    title = soup.title

  

*# Get all the paragraphs from page*  


    paras = soup.find_all('p')
    print(paras)




*# Get all the anchors code from page*  


    anchor = soup.find_all('a')
    all_links = set()
    print(anchor)




*# Get all the clickable links directly in console from page*  
<pre>

    for link in anchor:
        if link.get('href') != '#':
            link = "https://nitsanon.epizy.com" + link.get('href')  
            all_links.add(link) 
            print(link)

</pre>  


*# get first element in the HTML page*  

    print(soup.find('p'))

*# get first element after p tag*  

    print(soup.find('p')['class'])

*# find all the elements with class lead*  

    print(soup.find_all("p", class_="lead"))


*# Get the text from the tags/soup*  


    print(soup.find('p').get_text())  # print text inside the tag 'p'
    print(soup.get_text())  # print all the text in web page without any tags



*# Comment as last object*  


    markup = "<p><!-- this is a comment --></p>"
    soup2 = BeautifulSoup(markup, features='html5lib')
    print(type(soup2.p))
    print(type(soup2.p.string))  
    exit()




# navigation bars extraction  



    navbarSupportedContent = soup.find(id='navbarSupportedContent') 
    print(navbarSupportedContent) # navbar codes with parent  
    print(navbarSupportedContent.children) # navbar code iteratble  
    print(navbarSupportedContent.contents) # return codes of navbar
    
      
    for elem in navbarSupportedContent: # print title of navbar  
         print(elem)




*# difference between .children & .contents*  
> 
> -  .contents - A tag's children are available are available as a list  
> -  .children - A tag's children are available are available as a generator. Not stored in memory. But can be get using for loop or next function  

*# Print title of navbars*  



    for item in navbarSupportedContent.stripped_strings:  
		print(item)  
    
    for item in navbarSupportedContent.strings:  
        print(item)




*# Immediate parents of the item selected*  

    print(navbarSupportedContent.parent)

  


*# All parents of selected item*  


    for item in navbarSupportedContent.parents:
		print(item.name)

 


*# Find next sibling*  

    print(navbarSupportedContent.next_sibling)

  


*# previous sibling*  

    print(navbarSupportedContent.previous_sibling)

  


*# Full list of code for the id*  


    elem = soup.select('#loginModal')`  
    print(elem)




**Go through full [documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) of BeautifulSoup.**  

