import os;
import keywordExtract
import operator
import nltk
import cosine_similarity
from nltk.corpus import wordnet as wn
def run(paras,keyword,query,paragraphs):
    # need modified
    # keywords # this is a list transfer from mainControl
    #Synonyms=keywordExtract.get_synonyms(keywords)
    para_answer=get_best_paragraph(paras,keyword,get_synonyms(keyword),paragraphs)

    return para_answer


def get_best_paragraph(paras,keywords,syn_list,paragraphs):
    score_list=[]
    result=""
    if £¨len(paras)==0£©:
        result="No suitable paragraphs available.\n You can visit the following link directly"
    else:
        for index in range(len(paras)):
            p_vector=paras[index][1]
            #print(p_vector)
            temp_scores=score(p_vector,keywords,syn_list)
            #print(temp_scores)
            score_list.append([paras[index],temp_scores])
        list4=sorted(score_list, key = operator.itemgetter(1), reverse=True)
        index_P=list4[0][0]
        result=paragraphs[index_P[0]
        print(result)

    return(result)




def score(p_vector,keywords,syn_list):
    whole_word=keywords+syn_list
    score=0
    c_keywords=cosine_similarity.vector_to_counter(keywords)
    c_syn_list=cosine_similarity.vector_to_counter(syn_list)
    for i in range(len(p_vector)):
        for j in range(len(whole_word)):
                if(whole_word[j].lower()==p_vector[i].lower()):
                    score=score+10+(len(p_vector)+1-i)*2
                    c_para=cosine_similarity.vector_to_counter(p_vector)
                    c1=cosine_similarity.get_cosine(c_para,c_keywords)
                    c2=cosine_similarity.get_cosine(c_para,c_syn_list)
                    score=score+int(c1*100+c2*100)
    return score

def get_best_sentence(sens,keywords,syn_list):
     key=test.vector_to_counter(keywords)
     syn=test.vector_to_counter(syn_list)
     length=len(sens)
     score_sen=[]
     for i in range(length):
         vector=test.text_to_vector(sens[i])
         score_1=get_cosine(vector,key)
         score_2=get_cosine(vector,syn)
         score_sum=int(score_1*100+score_2*80+10*(length+2))
         score_sen.append(score_sum)
         length=length-1
     score_dictionary=dict(zip(sens,score_sen))
     best_sen=max(dic.items(), key=operator.itemgetter(1))[0]
     return best_sen

def get_synonyms(words):
     syn_list=[]
     for a in range(len(words)):
         print(words[a])
         syns = wn.synsets(words[a])
         for index in range(len(syns)):
             if(syns[index].lemmas()[0].name()!=words[a]):
                   syn_list.append(syns[index].lemmas()[0].name())
     return syn_list;
