


import pandas as pd

from bs4 import BeautifulSoup   # this module helps in web scrapping.
import requests                 # this module helps us to download a web page

# Store the html document as a string
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# Parsing document by passing to BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Use prettify() to display HTML in a nested structure - remove '#' on the line bellow to print nested html file
print(soup.prettify()) 

# get the title of page by using Tag
tag_object=soup.title
print("soup.title: ",tag_object)

# If there are more than one tag with the same name, the first element with that tag will be returned
tag_object=soup.h3
print("soup.h3: ",tag_object)       # this shall return the first h3 tag

# The Tag object is a tree of objects and we can access the child, parents and siblings of the tag

# child of h3 [<h3><b id="boldest">Lebron James</b></h3>]
tag_child =tag_object.b
print("tag_child=tag_object.b: ",tag_child)   # this shall return the child of the first h3 tag - b

# Parent of tag_child [<b id="boldest">Lebron James</b>]
parent_tag=tag_child.parent
print("parent_tag=tag_child.parent : ",parent_tag)   # this shall return the parent of b tag - h3

# Sibling of tag_object: on the same heirarchy, if tag_object is the h3, then the first sibling shall be tag p
sibling_1=tag_object.next_sibling
print("sibling_1=tag_object.next_sibling:",sibling_1)

# Next sibling: access by using/adding .next_sibling to sibling_1 
sibling_2=sibling_1.next_sibling
print("sibling_2=sibling_1.next_sibling: ",sibling_2)   # this shall return the next h3 (see nested html)

# Next Sibling: another way
print(sibling_2.next_sibling)

# HTML ATTRIBUTES
# We can access tag attributes
print(tag_child['id'])  # this will return the value of the attribute

# We can also use the get() method
print("using get(): ",tag_child.get('id'))

# We can access directly as attrs:
print(tag_child.attrs)  # this will return the attribute and its value

