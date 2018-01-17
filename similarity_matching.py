import nltk
import string
import os
import json
from sets import Set

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

def calSimNodes_btw_2_descriptions(ServiceClassObj_1, ServiceClassObj_2):
    #data = tokenize(des_2)
    #for item in data:
    #    print item
    #print des_1
    #print des_2
    des_1 = ServiceClassObj_1['service_class_description']
    des_2 = ServiceClassObj_2['service_class_description']

    vect  = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf = vect.fit_transform([preprocessing(des_1),preprocessing(des_2)])
    #print tfidf
    pairwise_similarity = (tfidf * tfidf.T).A
    print pairwise_similarity
    return pairwise_similarity[0][1]

def calSimNodes_btw_2_InputSets(ServiceClassObj_1, ServiceClassObj_2):
    try:
        input_components_1 = ServiceClassObj_1['service_class_parameters']['input']['components']
        input_components_2 = ServiceClassObj_2['service_class_parameters']['input']['components']

        if (len(input_components_1) <= 0):
            if (len(input_components_2) <= 0):
                return float(1)
            else:
                return float(0)
        elif (len(input_components_2) <= 0):
            if (len(input_components_1) <= 0):
                return float(1)
            else:
                return float(0)
        elif (len(input_components_1) > 0 and len(input_components_2) > 0):
            input_components_set_1 = Set([])
            for com in input_components_1:
                input_components_set_1.add(com['resource_ontology_id'])

            input_components_set_2 = Set([])
            for com in input_components_2:
                input_components_set_2.add(com['resource_ontology_id'])

            #print input_components_set_1
            #print input_components_set_2
            components_intersect = input_components_set_1.intersection(input_components_set_2) 
            #print components_intersect
            #print len(components_intersect)
            #print len(input_components_set_1)
            #print len(input_components_set_2)
            return (2* float(len(components_intersect)) / (float(len(input_components_set_1)) + float(len(input_components_set_2))))
        else:
            return float(0)
    except:
        return float(0)

def calSimNodes_btw_2_OutputSets(ServiceClassObj_1, ServiceClassObj_2):
    try:
        out_components_1 = ServiceClassObj_1['service_class_parameters']['output']['components']
        out_components_2 = ServiceClassObj_2['service_class_parameters']['output']['components']

        if (len(out_components_1) <= 0):
            if (len(out_components_2) <= 0):
                return float(1)
            else:
                return float(0)
        elif (len(out_components_2) <= 0):
            if (len(out_components_1) <= 0):
                return float(1)
            else:
                return float(0)
        elif (len(out_components_1) > 0 and len(out_components_2) > 0):
            out_components_set_1 = Set([])
            for com in out_components_1:
                out_components_set_1.add(com['resource_ontology_id'])

            out_components_set_2 = Set([])
            for com in out_components_2:
                out_components_set_2.add(com['resource_ontology_id'])

            #print input_components_set_1
            #print input_components_set_2
            components_intersect = out_components_set_1.intersection(out_components_set_2) 
            #print components_intersect
            #print len(components_intersect)
            #print len(input_components_set_1)
            #print len(input_components_set_2)
            return (2* float(len(components_intersect)) / (float(len(out_components_set_1)) + float(len(out_components_set_2))))
        else:
            return float(0)
    except:
        return float(0)

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
print "Similarity Matching works"

def sim_workflows(WF_1,WF_2):
    return 1

print calSimNodes_btw_2_OutputSets(test.SERVICE_CLASS_1, test.SERVICE_CLASS_2)