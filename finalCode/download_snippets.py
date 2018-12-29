#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
from sys import argv
def run(query):

    print (query)
    query = query.replace(" ","%20")
    query = "https://www.google.com/search?q=" + "%22" +query + "%22"
    print (query)


    r = requests.get(query)
    html_doc = r.text


    

    soup = BeautifulSoup(html_doc, 'html.parser')
    print("Downloading Snippets....")
    for s in soup.find_all(id="rhs_block"):
           print( s.text)
