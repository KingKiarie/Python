import re
import csv
import requests

from bs4 import BeautifulSoup

url = 'https://www.barnesandnoble.com/'
response = requests.get(url)

content = response.text

soup = BeautifulSoup(content,'html.parser')

# print(soup)

header =[]
writer =[]
date =[]


title_pattern=r'^(?P<BookTitle>.+)$'
title =re.findall(content,title_pattern)
authors_pattern=r'^(?P<Author>[A-Za-z\s.+?])$'
authors=re.findall(content,authors_pattern)
times_pattern=r'^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$'
times=re.findall(content,times_pattern)

for text in title:
    heading = text.text
    heading = heading.split()
    header.append(heading)

for author in authors:
    author = author.text
    author = author.split()
    writer.append(author)

for time in times:
    period = time.text
    time = period.split()
    date.append(time)

with open('library.csv','w',newline='') as store:
    writer = csv.writer(store)
    writer.writerows(header + '\n',writer + '\n', date + '\n')