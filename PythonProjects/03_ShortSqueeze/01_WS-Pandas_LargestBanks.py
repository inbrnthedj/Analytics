''' In this python program, we're going to webscrape wikipedia page of largest banks
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

to install in VS code terminal:
python -m pip install pandas lxml

Process through guided project by instructor Abhishek Gagneja
'''


import urllib.request   # This is needed to gain access to the wikipedia page
import pandas as pd     # We are importing pandas. See notes above

URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'

# Request object with 'User-Agent' header to mimic a web browser
req = urllib.request.Request(
    URL, 
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
)

# open URL using request
html_content = urllib.request.urlopen(req).read()

# pass raw HTML to pandas
tables = pd.read_html(html_content)

# We are extracting the table as a dataframe df
df=tables[0]
print(df)
