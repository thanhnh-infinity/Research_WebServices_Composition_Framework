import nltk
import string
import os
import json

#from sets import Set

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

#from classes.plans import Abtract_Planning,InitialState,GoalState,Concrete_Planning
#from classes.services import Service_Class,Service_Instance,DataFormatObject,Match_Object
#from OWL_Ontology_App import OWLEngine
import os
import sys
import json
#import utility
import pprint
#import planning_algorithms
import configuration
import composite_response
import graph
from random import *


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

def calSimNodes_btw_2_descriptions(Service_Obj_1, Service_Obj_2):
    #data = tokenize(des_2)
    #for item in data:
    #    print item
    #print des_1
    #print des_2
    if (Service_Obj_1['service_description']):
        des_1 = Service_Obj_1['service_description']
    else:
        des_1 = None

    if (Service_Obj_2['service_description']):    
        des_2 = Service_Obj_2['service_description']
    else:
        des_2 = None


    if ((des_1 is None or not des_1) and (des_2 is None or not des_2)):
        return float(0)

    if (des_1 is None or not des_1):
        des_1 = ""

    if (des_2 is None or not des_2):
        des_2 = ""


    vect  = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfidf = vect.fit_transform([preprocessing(des_1),preprocessing(des_2)])
    #print tfidf
    pairwise_similarity = (tfidf * tfidf.T).A
    #print pairwise_similarity
    return pairwise_similarity[0][1]

def calSimNodes_btw_2_InputSets(Service_Obj_1, Service_Obj_2):
    try:
        input_components_1 = Service_Obj_1['service_parameters']['input']['components']
        input_components_2 = Service_Obj_2['service_parameters']['input']['components']

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

def calSimNodes_btw_2_OutputSets(Service_Obj_1, Service_Obj_2):
    try:
        out_components_1 = Service_Obj_1['service_parameters']['output']['components']
        out_components_2 = Service_Obj_2['service_parameters']['output']['components']

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
def distNodes_Ontology_RawClingo(node_1,index_1,node_2,index_2):
    ontServiceName_1 = node_1
    ontServiceName_2 = node_2

    if (ontServiceName_1 and not ontServiceName_2):
        return float(9999)

    if (ontServiceName_2 and not ontServiceName_1):
        return float(9999)

    if (ontServiceName_1.strip().upper() == ontServiceName_2.strip().upper()):
        return float(0)    

    # Find class of service from service name
    ontClassName_1 = findClassOfInstance(ontServiceName_1)
    ontClassName_2 = findClassOfInstance(ontServiceName_2)

    if (ontClassName_1 and not ontClassName_2):
        return float(9999)

    if (ontClassName_2 and not ontClassName_1):
        return float(9999)

    if (ontClassName_1.strip().upper() == ontClassName_2.strip().upper()):
        return float(0)    

    shortestPathOverLCA = graph.find_shortest_path(graph.SERVICE_CLASSES_GRAPH,ontClassName_1,ontClassName_2)
    
    if (not shortestPathOverLCA or shortestPathOverLCA is None or len(shortestPathOverLCA) <= 0):
        return float(9999)

    return len(shortestPathOverLCA)      

def findClassOfInstance(instance):
    return graph.INSTANCE_IN_CLASS_MAP[instance]
def distNodes_Ontology(Service_Obj_1, Service_Obj_2):

    ontServiceName_1 = Service_Obj_1['service_name']
    ontServiceName_2 = Service_Obj_2['service_name']

    if (ontServiceName_1 and not ontServiceName_2):
        return float(9999)

    if (ontServiceName_2 and not ontServiceName_1):
        return float(9999)

    if (ontServiceName_1.strip().upper() == ontServiceName_2.strip().upper()):
        return float(0)    

    # Find class of service from service name
    ontClassName_1 = findClassOfInstance(ontServiceName_1)
    ontClassName_2 = findClassOfInstance(ontServiceName_2)

    #print "------------------"
    #print ontServiceName_1 + " : " + ontClassName_1
    #print ontServiceName_2 + " : " + ontClassName_2

    if (ontClassName_1 and not ontClassName_2):
        return float(9999)

    if (ontClassName_2 and not ontClassName_1):
        return float(9999)

    if (ontClassName_1.strip().upper() == ontClassName_2.strip().upper()):
        return float(0)    

    shortestPathOverLCA = graph.find_shortest_path(graph.SERVICE_CLASSES_GRAPH,ontClassName_1,ontClassName_2)
    
    if (not shortestPathOverLCA or shortestPathOverLCA is None or len(shortestPathOverLCA) <= 0):
        return float(9999)

    return len(shortestPathOverLCA)       

def calSimNodes_Ontology(Service_Obj_1, Service_Obj_2):
    distNodes_Ontology_Value = distNodes_Ontology(Service_Obj_1, Service_Obj_2)
    return 1 / (1 + float(distNodes_Ontology_Value))

def calSimNodes_Ontology_RawClingo(node_1,index_1,node_2,index_2):
    distNodes_Ontology_Value = distNodes_Ontology_RawClingo(node_1,index_1,node_2,index_2)
    return 1 / (1 + float(distNodes_Ontology_Value)) 

def sim_between_2_nodes_raw_clingo(node_1,index_1,node_2,index_2):
    sim_nodes_ontology = calSimNodes_Ontology_RawClingo(str(node_1),index_1,str(node_2),index_2)
    final_value = sim_nodes_ontology
    #print str(node_1) + ":" + str(node_2) + ":" + str(final_value)
    return int(round(final_value*10000))

def simNodes(Service_1, Service_2):
    return configuration.WEIGHT_SIMILARITY_NODES['semantic_ontology']*calSimNodes_Ontology(Service_1, Service_2) + configuration.WEIGHT_SIMILARITY_NODES['input_output']*(calSimNodes_btw_2_InputSets(Service_1, Service_2) + calSimNodes_btw_2_OutputSets(Service_1, Service_2)) + configuration.WEIGHT_SIMILARITY_NODES['service_description']*calSimNodes_btw_2_descriptions(Service_1, Service_2)

def simNodes_workflow(WF_JSON_1, WF_JSON_2):
    number_of_nodes_1 = len(WF_JSON_1)
    number_of_nodes_2 = len(WF_JSON_2)
    
    total_sim_nodes = 0
    for node_1 in WF_JSON_1:
        for node_2 in WF_JSON_2:
            single_sim_nodes = simNodes(node_1,node_2)
            total_sim_nodes = total_sim_nodes + single_sim_nodes

    return 2*float(total_sim_nodes) / (number_of_nodes_1 + number_of_nodes_2)

############################################
########EDGE SIMILARITY MATCHING############
############################################
def simEdges_workflow(WF_JSON_1, WF_JSON_2):
    list_edges_1 = generate_EdgesCollection_FromWF(WF_JSON_1)
    list_edges_2 = generate_EdgesCollection_FromWF(WF_JSON_2)
    
    number_edges_1 = len(list_edges_1) if (list_edges_1 is not None) else 0
    number_edges_2 = len(list_edges_2) if (list_edges_2 is not None) else 0

    # Calculate sim_edges_workflows
    total_sim_edges = 0
    for edge_obj_1 in list_edges_1:
        for edge_obj_2 in list_edges_2:
            total_sim_edges = total_sim_edges + simEdges(edge_obj_1,edge_obj_2)

    return 2*total_sim_edges / (number_edges_1 + number_edges_2) 
def get_information_service(WF_JSON,service_name,service_index):
    for item in WF_JSON:
        if (service_name.strip().upper() == item['service_name'].strip().upper()) and (service_index == item['service_index']):
            return item
def generate_EdgesCollection_FromWF(WF_JSON):
    list_edges = []
    #set_edges = Set([])
    if (WF_JSON and len(WF_JSON) > 0):
        for service_class_obj in WF_JSON:
            #print "Chay day ko"
            child_node_name = service_class_obj['service_name']
            child_node_input_components = service_class_obj['service_parameters']['input']['components']
            if (child_node_input_components and len(child_node_input_components) > 0):  
                for service_com_obj in child_node_input_components:
                    edge = {}
                    child_node_resource = service_com_obj['resource_ontology_id']
                    parent_node_name = service_com_obj['map']['from_service']
                    parent_node_resource = service_com_obj['map']['resource_ontology_id']

                    parent_node = get_information_service(WF_JSON,parent_node_name,int(service_com_obj['map']['at_step']) - 1)
                    edge['source_name'] = parent_node_name
                    edge['source_node'] = parent_node
                    edge['resource_source_ex'] = parent_node_resource
                    edge['resource_des_ex'] = child_node_resource
                    edge['destination_name'] = child_node_name
                    edge['destination_node'] = service_class_obj
                    list_edges.append(edge) 

                    #edge_label = generateEdgeLabel(edge)
                    #set_edges.add(edge_label)
        return list_edges           
    else:
        return None


def simEdges(edge_1, edge_2):
    if (edge_1 is None or edge_2 is None):
        return 0
    sim_edges_nodes_value = sim_edges_nodes(edge_1,edge_2)
    sim_edges_re_value = 0
    #print str(sim_edges_nodes_value) + ":" + str(sim_edges_re_value)
    return 0.5*sim_edges_nodes_value + 0.5*sim_edges_re_value

def sim_edges_nodes(edge_1,edge_2):

    source_node_1 =edge_1['source_node']    
    source_node_2 =edge_2['source_node']
    des_node_1 =edge_1['destination_node']
    des_node_2 =edge_2['destination_node']

    if ("initial_state" not in edge_1['source_name']) and ("initial_state" not in edge_2['source_name']):
        return 0.5*(simNodes(source_node_1,source_node_2) + simNodes(des_node_1,des_node_2))
    else:
        if ("initial_state" in edge_1['source_name']) and ("initial_state" in edge_2['source_name']):
             return 0.5*(1 + simNodes(des_node_1,des_node_2))
        elif ("initial_state" in edge_1['source_name']) and ("initial_state" not in edge_2['source_name']):
             return 0.5*(simNodes(des_node_1,des_node_2))
        elif ("initial_state" not in edge_1['source_name']) and ("initial_state" in edge_2['source_name']):     
             return 0.5*(simNodes(des_node_1,des_node_2))

def generateEdgeLabel(edgeJSON):
    if (edgeJSON):
       return edgeJSON['source'] + "_" + edgeJSON['resource_source_ex'] + "_" +  edgeJSON['resource_des_ex'] +"_"+ edgeJSON['destination'] 
    else:
       return None

############################################
########TOPOLOGY SIMILARITY MATCHING########
############################################
def sim_topologies(WF_JSON_1, WF_JSON_2):
    dist_topology = graph.distance_topology(WF_JSON_1,WF_JSON_2)
    #print dist_topology
    return 1 / (1 + float(dist_topology))
############################################
####### MAIN ###############################
############################################
def sim_workflows_graphStructure(WF_JSON_1,WF_JSON_2):
    
    JSON_WF_1 = json.loads(WF_JSON_1)
    JSON_WF_2 = json.loads(WF_JSON_2)

  
    #print "Node sim : " + str(simNodes_workflow(JSON_WF_1,JSON_WF_2))
    #print "Topo : " + str(sim_topologies(JSON_WF_1,JSON_WF_2))

    return 0.45*simNodes_workflow(JSON_WF_1,JSON_WF_2) + 0.35*simEdges_workflow(JSON_WF_1,JSON_WF_2) + 0.2*sim_topologies(JSON_WF_1,JSON_WF_2)
def sim_workflows(WF_1,WF_2,type):
    if (type is None or not type):
        return None
    else:
        if ("CLINGO_MODELS" in type):
            WF_JSON_1 =  convert_From_ClingoModels_toBasicGraphStructure(WF_1)
            WF_JSON_2 =  convert_From_ClingoModels_toBasicGraphStructure(WF_2)

            #print "Thanh NH 1"
            #print WF_JSON_1
            #print "ThanhNH 2"
            #print WF_JSON_2

            return sim_workflows_graphStructure(WF_JSON_1,WF_JSON_2) 
        elif ("WF_JSON_GRAPH_STRUCTURE" in type):
            WF_JSON_1 = WF_1
            WF_JSON_2 = WF_2
            return sim_workflows_graphStructure(WF_JSON_1,WF_JSON_2)    

    return None

def convert_From_ClingoModels_toBasicGraphStructure(Clingo_Models_WF):
    new_list = []
    for item in Clingo_Models_WF:
        new_list.append(str(item))
    return json.dumps(composite_response.read_a_full_workflow_detail(new_list)[0])

'''
for i in range(0,3):
   for j in range(i+1,4):
      print "======================================"
      print test.SERVICE_CLASSES[i]['service_class_name']
      print test.SERVICE_CLASSES[j]['service_class_name']
      print "------------------"
      print "Input same : " + str(calSimNodes_btw_2_InputSets(test.SERVICE_CLASSES[i],test.SERVICE_CLASSES[j]))
      print "Output same : " + str(calSimNodes_btw_2_OutputSets(test.SERVICE_CLASSES[i],test.SERVICE_CLASSES[j]))
      print "Des same :" + str(calSimNodes_btw_2_descriptions(test.SERVICE_CLASSES[i],test.SERVICE_CLASSES[j]))
      print "Onto Nodes same : " + str(calSimNodes_Ontology(test.SERVICE_CLASSES[i],test.SERVICE_CLASSES[j]))
      print "------------------"
      print "TOtal Sim : " + str(simNodes(test.SERVICE_CLASSES[i],test.SERVICE_CLASSES[j]))
'''
'''
print "============1-4====================="
print "Nodes matching : " + str(simNodes_workflow(test.WORKFLOW_1, test.WORKFLOW_4))
print "Topo matching : " + str(sim_topologies(test.WORKFLOW_1, test.WORKFLOW_4))
print "Edge matching : " + str(simEdges_workflow(test.WORKFLOW_1, test.WORKFLOW_4))
print "============1-2====================="
print "Nodes matching : " + str(simNodes_workflow(test.WORKFLOW_1, test.WORKFLOW_2))
print "Topo matching : " + str(sim_topologies(test.WORKFLOW_1, test.WORKFLOW_2))
print "Edge matching : " + str(simEdges_workflow(test.WORKFLOW_1, test.WORKFLOW_2))
print "============1-3====================="
print "Nodes matching : " + str(simNodes_workflow(test.WORKFLOW_1, test.WORKFLOW_3))
print "Topo matching : " + str(sim_topologies(test.WORKFLOW_1, test.WORKFLOW_3))
print "Edge matching : " + str(simEdges_workflow(test.WORKFLOW_1, test.WORKFLOW_3))
print "===================================="
'''
#print "Graph of Workflow 1"
#print convert_From_ClingoModels_toBasicGraphStructure(test.WORKFLOW_3_RAW_BEAUTY)
#print sim_workflows(test.WORKFLOW_1_RAW_BEAUTY,test.WORKFLOW_2_RAW_BEAUTY,"CLINGO_MODELS")

#print (OWLEngine.get_hierarchy_subclasses_of_class("http://www.cs.nmsu.edu/~epontell/Ontologies/phylogenetic_methods.owl#operationClassification","0"))      