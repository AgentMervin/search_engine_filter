#!/usr/bin/env python
# coding=utf-8
import os
paragraphList = []
def run(DIR, line):
    line_max = int(line) + 1
    # print(line_max)
    for x in range(1,line_max):
        paragraph=os.popen("bash getParagraph "+ DIR +" "+ str(x)).read().strip();
        paragraphList.append(paragraph)
    return paragraphList
