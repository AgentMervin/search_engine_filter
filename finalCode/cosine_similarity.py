import re, math
import operator
from collections import Counter

WORD = re.compile(r'\w+')
Querytext='the three best cities in Italy'#load data
titles=['The Top 10 Cities You Should Visit in Italy - TripSavvy','The best places and cities to visit in Italy | Telegraph Travel']
vectors=[]
cvectors=[]
cvalue=[]
value=[]
cdict={}

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     #print("words:   ", words)
     return Counter(words)

def vector_to_counter(vector):
     return Counter(vector)

#text1 = 'The Top 10 Cities You Should Visit in Italy - TripSavvy'
#text2 = 'The best places and cities to visit in Italy | Telegraph Travel'
def best_title_0(titles, Querytext):
    for index in range(len(titles)):
        temp = text_to_vector(titles[index])
        vectors.append(temp)

    vectorQuery=text_to_vector(Querytext)

    for index in range(len(vectors)):
        value.append(get_cosine(vectors[index], vectorQuery))

    dic=dict(zip(titles, value))
    result=max(dic.items(), key=operator.itemgetter(1))[0]
    

    return result

def best_title_1(titles, Querytext, contents):
    cvectors=[]
    cdict=[]
    content_list=[]
    
    for index in range(len(contents)):
        temp = text_to_vector(contents[index])
        cvectors.append(temp)

    vectorQuery=text_to_vector(Querytext)

    for index in range(len(cvectors)):
        temp2=get_cosine(cvectors[index], vectorQuery)
        if temp2 > 0.1:
            content_list.append([contents[index],temp2])
    list1=[]
    list3=[]
    for index1 in range(len(content_list)):
        for index2 in range(len(content_list)):
            if index1>=index2:
                continue
            else:
                vec1=text_to_vector(content_list[index1][0])
                vec2=text_to_vector(content_list[index2][0])
                cosine =get_cosine(vec1,vec2)
                if cosine not in list3:
                    list1.append([content_list[index1][0],content_list[index2],cosine])
                    list3.append(cosine)
            #print(list1[0])
    list4=sorted(list1, key = operator.itemgetter(2), reverse=True)
    return(list4[0])
