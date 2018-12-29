#!/usr/bin/env python
# coding=utf-8
import keywordExtract
import pageCrawler
import os
import download_snippets
import bestLink
import time
import loadParagraph
import best_answer
import paragraph_to_vector
import shutil

def helloworld(): 
        return "Hello world"
def run(Query,userID):
    workDir = "/var/www/project/finalCode/"
    os.system("cd /var/www/project/finalCode")
    print("current dir: ")
    os.system("pwd")
    returnlist=[]
    URL = Query.replace(" ","+")
    # URL = "https://www.google.com/search?num=20&q=" +URL
    URL = "https://www.google.com/search\?num\=30\&q\=" +URL
    print(URL)
    #userID = 1;
    tempDir = "/var/www/project/temp"
    tempDir = tempDir + str(userID) + "/"
    if not os.path.exists(tempDir):
        os.makedirs(tempDir)
    #method ot store google featuredSnippet
    featuredSnippet = download_snippets.run(Query)
    print(featuredSnippet)

    #download google result // slowing down
    # os.system("bash googleCrawler.sh " +tempDir + " " + URL)
    print("Downloading Google Results....")
    print("lynx -dump "+ URL + " >"+ tempDir + "gone.tmp")
    # pageCrawler.run(URL, tempDir, "gone.html")
    # os.system("lynx -dump "+tempDir+"gone.html > " + tempDir + "gone.tmp")
    os.system("lynx -dump "+ URL + " >"+ tempDir + "gone.tmp")


    #method to store keyword in keywordResult
    keyword_Result = keywordExtract.run(Query)
    print(keyword_Result);

    #generate title No Abstract Links
    os.system("bash generator.sh " + tempDir )


    # generate best page
    bestPageURL= bestLink.run(Query , tempDir )
    # bestPageURL= "https://www.liverpool.ac.uk/files/docs/maps/liverpool-university-campus-map.pdf"
    print("Best Link " + bestPageURL)


    #download Best Page
    print("Downloading Best Page....")
    # os.system("lynx -dump "+ bestPageURL + " >"+ tempDir + "target.html")
    pageCrawler.run(bestPageURL, tempDir, "target.html")

    ##generate paragraph
    print("Generateing paragraph")
    os.system("bash generateParagraph " + tempDir)

    ## generate best paragraph
    paragraphNumber = os.popen("bash getParagraphNo " + tempDir).read().strip();
    print(paragraphNumber)


    paragraphs=loadParagraph.run(tempDir, paragraphNumber)
    paragraph_vector=paragraph_to_vector.run(paragraphs)

    best_para=best_answer.run(paragraph_vector,keyword_Result,Query,paragraphs)

    returnlist.append(best_para)
    returnlist.append(bestPageURL)
    if os.path.exists(tempDir):
        shutil.rmtree(tempDir)


    return returnlist  
    

