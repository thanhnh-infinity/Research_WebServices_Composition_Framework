#from OWL_Ontology_App import OWLEngine
import json
import os
import sys
from zss import simple_distance, Node

import test

#graph = {'A': ['B', 'C'],
#         'B': ['C', 'D'],
#         'C': ['D'],
#         'D': ['C'],
#         'E': ['F'],
#         'F': ['C

A = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("h"))
            .addkid(Node("c")
                .addkid(Node("l"))))
        .addkid(Node("e"))
    )
B = (
    Node("1")
        .addkid(Node("2")
            .addkid(Node("3"))
            .addkid(Node("4")
                .addkid(Node("5"))))
        .addkid(Node("6"))
    )
C = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("d"))
            .addkid(Node("c")
                .addkid(Node("b"))))
        .addkid(Node("e"))
    )
D = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("h"))
            .addkid(Node("c")
            .addkid(Node("l"))))
        .addkid(Node("e"))
    )
c = Node('c', [])
b = Node('b', [c])
a = Node('a', [b, c])

a2 = Node('a', [Node('c', [Node('b',[])])])

X = Node('f',[Node("a",[Node("h",[]),Node("c",[Node("l",[])])]), Node("e",[])])
Y = Node('f',[Node("a",[Node("h",[Node("l",[])]),Node("c",[Node("e",[])])]) ])

SERVICE_CLASSES_GRAPH = {
    'operationClassification': ['species_operation', 'look_up_operation', 'names_operation','taxon_operation','list_operation','convert_operation','tree_operation'],

        'species_operation': ['operationClassification', 'species_information_operation'],
                'species_information_operation' : ['species_operation','species_url_operation','species_images_operation'],
                        'species_url_operation' : ['species_information_operation'],
                        'species_images_operation' : ['species_information_operation'],

        'look_up_operation': ['operationClassification', 'look_up_taxonomy', 'look_up_scientific_name', 'look_up_location'],
                'look_up_taxonomy' : ['look_up_operation','scientific_name_to_taxonomy'],
                        'scientific_name_to_taxonomy' : ['look_up_taxonomy'],
                'look_up_scientific_name' : ['look_up_operation'],
                'look_up_location' : ['look_up_operation','country_code_to_name'],
                        'country_code_to_name' : ['look_up_location'],

        'names_operation': ['operationClassification' , 'names_resolution_operation', 'names_extraction_operation','names_conversion_operation'],
                'names_resolution_operation' : ['names_operation'],
                'names_extraction_operation' : ['names_operation','names_extraction_web','names_extraction_document','names_extraction_tree','names_extraction_text'],
                        'names_extraction_web'  : ['names_extraction_operation'],
                        'names_extraction_document'  : ['names_extraction_operation'],
                        'names_extraction_tree'  : ['names_extraction_operation'],
                        'names_extraction_text'  : ['names_extraction_operation'],
                'names_conversion_operation' : ['names_operation','convert_operation','common_name_to_scientific_name'],
                        'common_name_to_scientific_name' : ['names_conversion_operation'],

        'taxon_operation' : ['operationClassification','taxon_to_species_operation'],
                'taxon_to_species_operation' : ['taxon_operation','taxon_to_species_by_genome','taxon_to_species_by_country'],
                         'taxon_to_species_by_genome' : ['taxon_to_species_operation'],
                         'taxon_to_species_by_country': ['taxon_to_species_operation'],

        'list_operation' : ['operationClassification','list_update_operation','list_creation_operation','list_retrieval_operation'],
                'list_update_operation' : ['list_operation','list_update_delete','list_update_edit','list_update_add'],
                         'list_update_delete' : ['list_update_operation'],
                         'list_update_edit' : ['list_update_operation','list_update_edit_list_content','list_update_edit_list_metadata'],
                               'list_update_edit_list_content' : ['list_update_edit'],
                               'list_update_edit_list_metadata' : ['list_update_edit'],
                         'list_update_add' : ['list_update_operation'],
                'list_creation_operation' : ['list_operation'],
                'list_retrieval_operation' : ['list_operation'],

        'convert_operation' : ['operationClassification','data_format_conversion','names_conversion_operation'],
                'data_format_conversion' : ['convert_operation'],

        'tree_operation': ['operationClassification', 'tree_generation' ,'tree_information', 'tree_comparison','tree_visualization','tree_transformation'],
                'tree_generation' : ['tree_operation','tree_retrieval_operation','tree_reconciliation','tree_extraction_operation'],
                          'tree_retrieval_operation' : ['tree_generation'],
                          'tree_reconciliation' : ['tree_generation'],
                          'tree_extraction_operation' : ['tree_generation','phylogeny_based_extraction','gene_based_extraction','taxonomy_based_extraction'],
                                'phylogeny_based_extraction' : ['tree_extraction_operation'],
                                'gene_based_extraction' : ['tree_extraction_operation'],
                                'taxonomy_based_extraction' : ['tree_extraction_operation'],
                'tree_information' : ['tree_operation','tree_support_studies'],
                          'tree_support_studies' : ['tree_information','tree_publifications'],
                                'tree_publifications' : ['tree_support_studies'],
                'tree_comparison' : ['tree_operation','branch_length_comparison_operation','symmetric_comparison_operation'],
                          'branch_length_comparison_operation' : ['tree_comparison'],
                          'symmetric_comparison_operation' : ['tree_comparison'],
                'tree_visualization' : ['tree_operation'],
                'tree_transformation' : ['tree_operation','tree_scaling_operation'],
                          'tree_scaling_operation' : ['tree_transformation','gene_tree_scaling','species_tree_scaling'],
                                'gene_tree_scaling' : ['tree_scaling_operation'],
                                'species_tree_scaling' : ['tree_scaling_operation']

}

# Should be take time to implement this one overnight
def getZSSNode_from_ListNode(listZSS,current_node_name):
    for ZSSNode in listZSS:
        if (current_node_name == ZSSNode.label):
            return ZSSNode
    return None
def updateZSSNode_to_ListNode(listZSS,current_node):
    numberNodes = len(listZSS)
    for i in range(0, numberNodes):
        if (listZSS[i].label == current_node.label):
            listZSS[i] = current_node

    return listZSS

def buildUp_ZSSGraph(WorkflowGraph):
    #Root = Node("initial",[])

    list_ZSS_Node = []

   
    #Root = Node("initial_state",[])

    list_ZSS_Node.append(Node("initial_state",[]))
    for service_class_obj in WorkflowGraph:
        consider_node_name = service_class_obj['service_name']
        list_ZSS_Node.append(Node(consider_node_name))

    for service_class_obj in WorkflowGraph:
        child_node_name = service_class_obj['service_name']
        child_node = getZSSNode_from_ListNode(list_ZSS_Node,child_node_name)
        if (child_node):
            child_node_input_components = service_class_obj['service_parameters']['input']['components']
            if (child_node_input_components and len(child_node_input_components) > 0):
                for service_com_obj in child_node_input_components:
                    parent_node_name = service_com_obj['map']['from_service']
                    parent_ZSS_Node = getZSSNode_from_ListNode(list_ZSS_Node,parent_node_name)
                    if (parent_ZSS_Node):
                        parent_ZSS_Node.addkid(child_node)
                        list_ZSS_Node = updateZSSNode_to_ListNode(list_ZSS_Node,parent_ZSS_Node)



    for ZSSNode in list_ZSS_Node:
        if (ZSSNode.label == "initial_state"):
            return ZSSNode    

    #return list_ZSS_Node

def print_ZSSNode(ZSSNode):
    childs = ZSSNode.children
    str_child = ""
    for child in childs:
        str_mini_child  = ""
        for mini_child in child.children:
            str_mini_mini_child = ""
            for mini_mini_child in mini_child.children:
                #print "\n" + mini_mini_child.label
                str_mono_child  = ""
                for mono_child in mini_mini_child.children:
                    if (str_mono_child):
                        if (len(mono_child.children) > 0):
                            str_mono_child = str_mono_child + "," + "Node(" + mono_child.label + ",[" + str(mono_child.children) + "])"
                        else:
                            str_mono_child = str_mono_child + "," + "Node(" + mono_child.label + ",[])"
                    else:
                        if (len(mono_child.children) > 0):
                            str_mono_child = "Node(" + mono_child.label + ",[" + str(mono_child.children) + "])"
                        else:
                            str_mono_child = "Node(" + mono_child.label + ",[])"        
                if (str_mini_mini_child):
                    if (len(mini_mini_child.children) > 0):
                       str_mini_mini_child = str_mini_mini_child + "," + "Node(" + mini_mini_child.label + ",[" + str_mono_child + "])"
                    else:
                       str_mini_mini_child = str_mini_mini_child + "," + "Node(" + mini_mini_child.label + ",[])"   
                else:
                    if (len(mini_mini_child.children) > 0):
                        str_mini_mini_child = "Node(" + mini_mini_child.label + ",[" + str_mono_child + "])"
                    else:
                        str_mini_mini_child = "Node(" + mini_mini_child.label + ",[])"

            if (str_mini_child):
                str_mini_child = str_mini_child + "," + "Node(" + mini_child.label + ",[" + str_mini_mini_child + "])"
            else:
                str_mini_child = "Node(" + mini_child.label + ",[" + str_mini_mini_child + "])"

        if (str_child):    
            str_child = str_child + "," + "Node(" + child.label + ",[" + str_mini_child + "])"
        else:
            str_child = "Node(" + child.label + ",[" + str_mini_child + "])"


    print (" Node(" + ZSSNode.label + ",[" + str_child + "])")
    

def distance_topology(Graph_1, Graph_2):
    ZSSGraph_1 = buildUp_ZSSGraph(Graph_1)
    ZSSGraph_2 = buildUp_ZSSGraph(Graph_2)

    return simple_distance(ZSSGraph_1,ZSSGraph_2)

# Have to be done so far
def convert_OntologyJSONGraph_to_BasicGraph(ontServiceClassesGraphJSON):
    return None

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

#print Y
#print simple_distance(a,a2)
#print distance_topology(test.WORKFLOW_2,test.WORKFLOW_4)
#print ("Shortest path")
#print(find_shortest_path(SERVICE_CLASSES_GRAPH,'common_name_to_scientific_name','names_extraction_web'))

#print ("All path")
#print(find_all_paths(SERVICE_CLASSES_GRAPH,'common_name_to_scientific_name','names_extraction_web'))

'''
print "=========="
print "Workflow 1"
print_ZSSNode(buildUp_ZSSGraph(test.WORKFLOW_1))
print "=========="
print "Workflow 4"
print_ZSSNode(buildUp_ZSSGraph(test.WORKFLOW_4))
'''

#items = A.iter()

#for item in items:
#    print item.label + ";"


