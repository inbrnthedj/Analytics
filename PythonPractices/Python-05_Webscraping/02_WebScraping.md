## Webscraping

- A process used to automatically extract information from a website.

In this notebook, we'll use BeautifulSoup.

```python
# Import BeautifulSoup
from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html>
    <head>
        <title>PageTitle</title>
    </head>
    <body>
        <h3><b id='boldest'>Lebron James</b></h3>
        <p>Salary: $ 92,000,000 </p>
        <h3>Stephen Curry</h3>
        <p>Salary: $ 85,000,000 </p>
        <h3>Kevin Durant</h3>
        <p>Salary: $ 92,000,000 </p>
    </body>
</html>"""

# To parse the document, pass into the BeautifulSoup constructor
soup = BeautifulSoup(html, 'html5lib')
```

### Beautiful Soup

Beautiful Soup represents the HTML document as a set of Tree-like objects with methods to parse the doc.

#### `tag_object = soup.title`

```html
<title>PageTitle</title>
```

#### `tag_object = soup.h3`

```html
<h3><b id='boldest'>Lebron James</b></h3>
```

##### Navigate the child down from parent

```python
tag_child = tag_object.b
```

`tag_child`:
```html
<b id='boldest'>Lebron James</b>
```

##### Navigate the parent up from child

```python
parent_tag = tag_child.parent
```

`parent_tag`:
```html
<h3><b id='boldest'>Lebron James</b></h3>
```

##### Next-sibling attribute

```python
sibling_1 = tag_object.next_sibling
```

`sibling_1`:
```html
<p>Salary: $ 92,000,000 </p>
```

##### Navigable attributes

```python
tag_child.attrs
# Output: {'id': 'boldest'}
```

##### Navigating strings

```python
tag_child.string
# Output: 'Lebron James'
```

#### `find_all`

```python
# Define a BeautifulSoup object
from bs4 import BeautifulSoup

html = """<table>
    <tr>
        <td>PizzaPlace</td>
        <td>Orders</td>
        <td>Slices</td>
    </tr>
    <tr>
        <td>Domino'sPizza</td>
        <td>10</td>
        <td>100</td>
    </tr>
    <tr>
        <td>LittleCaesars</td>
        <td>12</td>
        <td>144</td>
    </tr>
</table>"""

table = BeautifulSoup(html, 'html5lib')

table_rows = table.find_all(name='tr')
```

`table_rows` output:
```html
[
    <tr><td>Pizza Place</td><td>Orders</td><td>Slices</td></tr>,
    <tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr>,
    <tr><td>Little Caesars</td><td>12</td><td>144</td></tr>
]
```

##### Tag object

```python
first_row = table_rows[0]
# This gets the first entry in table_rows, which contains the HTML of the first row
```

`first_row`:
```html
<tr><td>Pizza Place</td><td>Orders</td><td>Slices</td></tr>
```

Extract the first data cell:
```python
first_row.td
# Output: <td>Pizza Place</td>
```

##### Variable Row

```python
# Iterate through each table cell
for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all("td")

    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)
```

### Overview

```python
# First, import modules needed
import requests
from bs4 import BeautifulSoup

# Use the get method to download the webpage
page = requests.get("http://www.EnterpriseWebsiteUrl...").text

# Create BeautifulSoup object - allows parsing through the webpage
soup = BeautifulSoup(page, "html.parser")

# Pulls all instances of <a> tag
artists = soup.find_all('a')

# Print names and links for all tags
for artist in artists:
    names = artist.contents[0]
    fullLink = artist.get('href')
    print(names)
    print(fullLink)
```
