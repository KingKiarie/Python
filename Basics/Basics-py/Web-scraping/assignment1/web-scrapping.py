import requests
import re
from bs4 import BeautifulSoup
import csv

url ='https://hojaleaks.com/'
response = requests.get(url)

html_content = response.text

soup =BeautifulSoup(html_content,'html.parser')


print(soup)

data = []

headings = soup.find_all('h1')

for heading in headings:
    header = heading.text
    header = header.split()
    data.append(header)
    print(heading.text)

with open('headings.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)