from OWL_Ontology_App import OWLEngine
import json
import os
import sys
from zss import simple_distance, Node

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
#c = Node('c', [])
#b = Node('b', [])
#a = Node('a', [b, c])

#a2 = Node('a', [Node('c', [])])

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
def buildUp_ZSSGraph(WorkflowGraph):
    Root = Node("initial",[])
    return Root

def distance_topology(Graph_1, Graph_2):
    return simple_distance(Graph_1,Graph_2)

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

print Y
print distance_topology(X,Y)
#print ("Shortest path")
#print(find_shortest_path(SERVICE_CLASSES_GRAPH,'common_name_to_scientific_name','names_extraction_web'))

#print ("All path")
#print(find_all_paths(SERVICE_CLASSES_GRAPH,'common_name_to_scientific_name','names_extraction_web'))



