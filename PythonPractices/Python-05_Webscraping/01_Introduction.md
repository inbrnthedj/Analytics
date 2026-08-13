## Webscraping in Data Science

Web scraping (web harvesting / webdata extraction) is used to extract large amounts of data from websites.

In data science, it is used for:
1. **Data Collection**: It is a primary method of collecting data from the internet.
2. **Real-time Application**: For example: weather updates, price comparison, etc.
3. **Machine Learning**: It provides the data needed to train machine learning models.

## Python Libraries for Web Scraping

1. **BeautifulSoup**: Used to pull data from HTML and XML files. It creates a parse tree from the page source code that can be used to extract data in a hierarchical and readable manner.

```python
from bs4 import BeautifulSoup
import requests

URL = "http://www.example.com"
page = requests.get(URL)    
soup = BeautifulSoup(page.content, "html.parser")
```

2. **Scrapy**: Open-source and collaborative web crawling framework used to extract data from websites.

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'quote': quote.css('span.text::text').get()}
```

3. **Selenium**: Used for controlling web browsers through programs and automating browser tasks.

```python
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.example.com")
```

## Applications

Webscraping can be used in:
1. **Price Comparison**: Tools like ParseHub use webscraping to collect data from online shopping websites.
2. **Email Address Gathering**: Many companies use web scraping to collect email IDs and send bulk emails for marketing purposes.
3. **Social Media Scraping**: Used to collect data from social media websites to find out what's trending.
