import os;
import re
WORD = re.compile(r'\w+')

import keywordExtract

def run(paras):
    # need modified
    # keywords # this is a list transfer from mainControl
    # Synonyms=keywordExtract.get_synonyms(keywords)
    para_vector=[]
    
    for index in range(len(paras)):
        vectors = WORD.findall(paras[index])
        if (len(vectors)>10):
           para_vector.append([index,vectors])
           
    print(len(para_vector))
    return para_vector
