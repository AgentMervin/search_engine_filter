#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
from sys import argv

query="Who is trump"
print (query)
query = query.replace(" ","%20")
query = "https://www.google.com/search?q=" + "%22" +query + "%22"
print (query)


r = requests.get(query)
print(r)
html_doc = r.text
# print(html_doc)




soup = BeautifulSoup(html_doc, 'html.parser')
# print("Downloading Snippets....")
# for s in soup.find_all(id="rhs_block"):
# for s in soup.find("span"):
       # print( s.text)
