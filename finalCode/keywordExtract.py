# coding=utf-8
import nltk
import re
import numpy
import time
#file=open("sample.txt")
class TextRank(object):
	
	def __init__(self, sentence, window, damp, iternum):
		self.sentence=sentence
		self.window=window
		self.damp=damp
		self.wordList=[]
		self.edgeDict={}
		self.iternum=iternum
		self.clasification="NOTFOUND"

	def sepSentence(self):
		tokens=nltk.word_tokenize(self.sentence)
		tagged = nltk.pos_tag(tokens)
		
		for index,x in enumerate(tagged[:]):
			syntax=r'(CD|FW|JJ|NN|P|R|SYM|VB|W|IN).*'
			symme=r'(is|are|very|of|in|at|on)'
			if not re.match(syntax,x[1]):
				tagged.remove(x)
			elif re.match(symme,x[0]):
				tagged.remove(x)
			elif re.match(r'W.*',x[1]):
				#The classification of question
				self.clasification=x[0]
				tagged.remove(x)
			if (index!=0):
				if(x[0]=='n\'t'):
					tempEle=tagged[index-1][0]+'n\'t'
					tempSyn=tagged[index-1][1]
					tagged.remove(x)
					tagged.insert(index,(tempEle,tempSyn))
					tagged.remove(tagged[index-1])
		for value in tagged:
			self.wordList.append(value[0]);
	
	#Construct the graph to represent relations of each word
	def edgeNodes(self):
		tempList=[]
		wordLen=len(self.wordList)
		for index, word in enumerate(self.wordList):
			if word not in self.edgeDict.keys():
				tempList.append(word)
				tempSet=set()
				#Set the window edge
				leftEdge=index-self.window+1
				if leftEdge < 0: leftEdge = 0
				rightEdge=index+self.window 
				if rightEdge>=wordLen: rightEdge= wordLen
				for i in range(leftEdge,rightEdge):
					if index==i:
						continue
					tempSet.add(self.wordList[i])
				#The word shows in the same window出边�?
				self.edgeDict[word]=tempSet
	
	#Construct the matrix of the edge links relation
	def relatedMatrix(self):
		wordSetLen=len(set(self.wordList))
		self.matrix=numpy.zeros([wordSetLen, wordSetLen])
		self.wordIndex = {} 
		self.indexDict = {}
		
		for i, v in enumerate(set(self.wordList)):
			#The index of the word
			self.wordIndex[v] = i
			#The word index
			self.indexDict[i] = v
		#The center of the window
		for key in self.edgeDict.keys():
			
			for value in self.edgeDict[key]:
				self.matrix[self.wordIndex[key]][self.wordIndex[value]] =1
				self.matrix[self.wordIndex[value]][self.wordIndex[key]] =1

			
		#Normalisation
		#to each column
		for j in range(self.matrix.shape[1]):
			sum = 0
			for i in range(self.matrix.shape[0]):
				sum += self.matrix[i][j];
			for i in range(self.matrix.shape[0]): 
				self.matrix[i][j] /= sum;
		

	#Calculate textrank of each word for 500 times
	def calculateTR(self):
		self.TR=numpy.ones([len(set(self.wordList)), 1])
		for i in range(self.iternum):  
			self.TR = (1 - self.damp) + self.damp * numpy.dot(self.matrix, self.TR)
	
	#Outout the result
	def doResult(self):
		wordTR={}
		for i in range(len(self.TR)):
			wordTR[self.indexDict[i]]=self.TR[i][0]
		result=sorted(wordTR.items(),key = lambda x:x[1],reverse=True)
		self.resultList=[]
		wordNum=len(self.wordList);
		if wordNum>=5: wordNum=5
		for mark in range(wordNum):
			self.resultList.append(result[mark][0])
		return self.resultList # keywords extracted
		
   

# if __name__ == '__main__':
def run(query):

	start =time.clock()
	s="what is the most important thing in the world" # string to extract
	s=query # string to extract
	tr=TextRank(s,3,0.85,500)
	tr.sepSentence()
	tr.edgeNodes();
	tr.relatedMatrix();
	tr.calculateTR();
	return tr.doResult();
	# print(tr.doResult());
	end = time.clock()
	# print('Running time: %s Seconds'%(end-start))
