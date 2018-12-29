import requests
from sys import argv
from bs4 import BeautifulSoup


USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def run(link, location, filename):
    #basic
    # print (link)
    page_link=link

    #page_link=page_link[0:len(page_link)-1]
    if ord(page_link[len(page_link)-1:len(page_link)]) == 10:
        page_link=page_link[0:len(page_link)-1]
    page_response = requests.get(page_link, headers=USER_AGENT)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    filepath = location + filename#"target.html"
    f= open(filepath,"w+")
    f.write(str(page_content))
    f.close();

