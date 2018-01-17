import nltk
import string
import os
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

from classes.plans import Abtract_Planning,InitialState,GoalState,Concrete_Planning
from classes.services import Service_Class,Service_Instance,DataFormatObject,Match_Object
import os
import sys
import json
import utility
import pprint
import planning_algorithms
import configuration
import composite_response


##########TEST DATA#########################
import test

############################################
########NODE SIMILARITY MATCHING############
############################################

#nltk.download('punkt')
stemmer = PorterStemmer()

def preprocessing(text):
    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    return no_punctuation

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

def calSimNodes_btw_2_descriptions(des_1, des_2):
    #data = tokenize(des_2)
    #for item in data:
    #    print item
    #print des_1
    #print des_2
    vect  = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf = vect.fit_transform([preprocessing(des_1),preprocessing(des_2)])
    #print tfidf
    pairwise_similarity = (tfidf * tfidf.T).A
    print pairwise_similarity
    return pairwise_similarity[0][1]

def calSimNodes_btw_2_InputSets(ServiceClassObj_1, ServiceClassObj_2):
    return 1

def calSimNodes_btw_2_OutputSets(ServiceClassObj_1, ServiceClassObj_2):
    return 1

def calSimNodes_Ontology(ServiceClassObj_1, ServiceClassObj_2):
    return 1

def simNodes(ServiceClassObj_1, ServiceClassObj_2):
    return 1

############################################
########EDGE SIMILARITY MATCHING############
############################################
def simEdges(edgesWF1, edgesWG2):
  return 1

def calSim_2Edges(edge_1, edge_2):
  return 1 

############################################
########TOPOLOGY SIMILARITY MATCHING########
############################################

############################################
########MAIN########
############################################
print "Thanh NH : " + str(calSimNodes_btw_2_descriptions("Thanh Nguyen","Thanh Hai nguyen"))
print test.WORKFLOW_2

