from OWL_Ontology_App import OWLEngine
import json
import os
import sys

SERVICE_CLASSES_GRAPH = {                        
    'operationClassification': ['species_operation', 'look_up_operation', 'names_operation','taxon_operation','list_operation','convert_operation','tree_operation'],
        'species_operation': ['operationClassification', 'species_information_operation'],
                'species_information_operation' : ['species_operation','species_url_operation','species_images_operation'],
                        'species_url_operation' : ['species_information_operation'],
                        'species_images_operation' : ['species_information_operation'],
        'look_up_operation': ['operationClassification', 'look_up_taxonomy', 'look_up_scientific_name', 'look_up_location'],
                'look_up_taxonomy' : ['look_up_operation','scientific_name_to_taxonomy'],
                'look_up_scientific_name' : ['look_up_operation'],
                'look_up_location' : ['look_up_operation','country_code_to_name'],
        'names_operation': ['operationClassification' , 'names_resolution_operation', 'names_extraction_operation','names_conversion_operation'],
                'names_resolution_operation' : ['names_operation'],
                'names_extraction_operation' : ['names_operation','names_extraction_web','names_extraction_document','names_extraction_tree','names_extraction_text'], 
                        'names_extraction_web'  : ['names_extraction_operation'],
                        'names_extraction_document'  : ['names_extraction_operation'],
                        'names_extraction_tree'  : ['names_extraction_operation'],
                        'names_extraction_text'  : ['names_extraction_operation'],
                'names_conversion_operation' : ['names_operation','common_name_to_scientific_name'],
                        'common_name_to_scientific_name' : ['names_conversion_operation'],
        'taxon_operation' : ['operationClassification'],
        'list_operation' : ['operationClassification'],
        'convert_operation' : ['operationClassification'],
        'tree_operation': ['operationClassification', 'M2' ,'D'],
          'N': ['N1', 'N2', 'D'],
          'M1' :['M'],
          'M2' :['M'],
          'N1' : ['N'],
          'N2' : ['N']
}

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
#graph = {'A': ['B', 'C'],
#         'B': ['C', 'D'],
#         'C': ['D'],
#         'D': ['C'],
#         'E': ['F'],
#         'F': ['C']}



print ("Shortest path")
print(find_shortest_path(SERVICE_CLASSES_GRAPH,'names_extraction_web','scientific_name_to_taxonomy'))

#print ("All path")
#print(find_all_paths(graph,'G','D'))



