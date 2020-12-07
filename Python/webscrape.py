from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

lawyers = "https://www.martindale.com/search/law-firms/?term=Insurance%20defense"

response = get(lawyers, headers=headers)
print(response)
#print(response.text[:1000])

html_soup = BeautifulSoup(response.text, 'html.parser')
print(html_soup.prettify())

for phone in html_soup.find_all('button-text'):
    print(link.get('href'))

lawyer_phone = html_soup.find_all('div', class_="button-text")
print(lawyer_phone)

#first = lawyer_name[0]
#first.find_all('span')