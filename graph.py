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
                'names_conversion_operation' : ['names_operation','data_format_conversion','common_name_to_scientific_name'],
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

        'convert_operation' : ['operationClassification','data_format_conversion'],
                'data_format_conversion' : ['convert_operation','names_conversion_operation','tree_format_conversion','list_scientific_names_conversion','text_conversion'],
                          'tree_format_conversion' : ['data_format_conversion'],
                          'list_scientific_names_conversion' : ['data_format_conversion'],
                          'text_conversion' : ['data_format_conversion'],

        'tree_operation': ['operationClassification', 'tree_generation' ,'tree_information', 'tree_comparison','tree_visualization','tree_transformation'],
                'tree_generation' : ['tree_operation','tree_retrieval_operation','tree_reconciliation','tree_extraction_operation'],
                          'tree_retrieval_operation' : ['tree_generation'],
                          'tree_reconciliation' : ['tree_generation'],
                          'tree_extraction_operation' : ['tree_generation','phylogeny_based_extraction','gene_based_extraction','taxonomy_based_extraction'],
                                'phylogeny_based_extraction' : ['tree_extraction_operation'],
                                'gene_based_extraction' : ['tree_extraction_operation'],
                                'taxonomy_based_extraction' : ['tree_extraction_operation'],
                'tree_information' : ['tree_operation','tree_support_studies','tree_metadata'],
                          'tree_support_studies' : ['tree_information','tree_publifications'],
                                'tree_publifications' : ['tree_support_studies'],
                          'tree_metadata' : ['tree_information','tree_medatadata_chronogram'],
                                'tree_medatadata_chronogram' : ['tree_metadata'],      
                'tree_comparison' : ['tree_operation','branch_length_comparison_operation','symmetric_comparison_operation'],
                          'branch_length_comparison_operation' : ['tree_comparison'],
                          'symmetric_comparison_operation' : ['tree_comparison'],
                'tree_visualization' : ['tree_operation'],
                'tree_transformation' : ['tree_operation','tree_scaling_operation'],
                          'tree_scaling_operation' : ['tree_transformation','gene_tree_scaling','species_tree_scaling'],
                                'gene_tree_scaling' : ['tree_scaling_operation'],
                                'species_tree_scaling' : ['tree_scaling_operation']

}


INSTANCE_IN_CLASS_MAP = {
    "phylotastic_ResolvedScientificNames_GNR_TNRS_GET":"names_resolution_operation",
    "phylotastic_ResolvedScientificNames_GNR_TNRS_POST":"names_resolution_operation",
    "phylotastic_ResolvedScientificNames_OT_TNRS_GET":"names_resolution_operation",
    "phylotastic_ResolvedScientificNames_OT_TNRS_POST":"names_resolution_operation",
    "phylotastic_ResolvedScientificNames_FC":"names_resolution_operation",

    "phylotastic_GetAllSpeciesFromTaxon_OT_GET":"taxon_to_species_operation",
    "phylotastic_GetInformationURLsOfSpecies_EOL_POST":"species_url_operation",
    "phylotastic_GetInformationURLsOfSpecies_EOL_GET":"species_url_operation",
    "phylotastic_GetImageURLsOfSpecies_EOL_GET":"species_images_operation",
    "phylotastic_GetImageURLsOfSpecies_EOL_POST":"species_images_operation",
    "phylotastic_FindScientificNamesFromWeb_GNRD_GET":"names_extraction_web",
    "phylotastic_FindScientificNamesFromFreeText_GNRD_GET":"names_extraction_text",
    "phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET":"taxon_to_species_by_genome",
    "phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET":"taxon_to_species_by_country",

    "phylotastic_GetPhylogeneticTree_OT_GET":"taxonomy_based_extraction",
    "phylotastic_GetPhylogeneticTree_OT_POST":"taxonomy_based_extraction",
    "phylotastic_GetPhylogeneticTree_Phylomatic_GET":"phylogeny_based_extraction",
    "phylotastic_GetPhylogeneticTree_Phylomatic_POST":"phylogeny_based_extraction",
    "phylotastic_GetPhylogeneticTree_PhyloT_GET":"taxonomy_based_extraction",
    "phylotastic_GetPhylogeneticTree_PhyloT_POST":"taxonomy_based_extraction",
    "phylotastic_GetPhylogeneticTree_FC":"phylogeny_based_extraction",


    "phylotastic_ComparePhylogeneticTrees_Symmetric_POST":"symmetric_comparison_operation",
    "phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST":"species_tree_scaling",
    "phylotastic_GetMetadata_Chronogram_DateLife_POST":"tree_metadata_chronogram",
    "phylotastic_GetSpeciesScientificNameFromCommonName_NCBI_GET":"common_name_to_scientific_name",

    "google_ConvertCountryCodeToName_GET":"country_code_to_name",
    "openTree_GetTaxonomyNameFromSciName_GET":"scientific_name_to_taxonomy",

    "phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET":"names_extraction_web",
    "phylotastic_FindScientificNamesFromWeb_FC":"names_extraction_web",

    "phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET":"names_extraction_tree",

    "phylotastic_GetReconciliationTree_GET":"tree_reconciliation",
    "phylotastic_GenerateGeneTree_From_Genes":"gene_based_extraction",
    "phylotastic_GeneTree_Scaling":"gene_tree_scaling",
    "phylotastic_CompareTrees_Sym_Dendropy_POST" : "symmetric_comparison_operation",
    "phylotastic_CompareTrees_BL_Dendropy_POST":"branch_length_comparison_operation",

    "convert_df_text_format_raw_to_plain":"text_conversion",

    "convert_df_sci_names_format_1_to_3":"list_scientific_names_conversion",
    "convert_df_sci_names_format_3_to_5":"list_scientific_names_conversion",
    "convert_df_sci_names_format_5_to_GNR":"list_scientific_names_conversion",
    "convert_df_sci_names_format_5_to_OT":"list_scientific_names_conversion",
    "convert_df_sci_names_format_2_to_4":"list_scientific_names_conversion",
    "convert_df_sci_names_format_4_to_6":"list_scientific_names_conversion",
    "convert_df_sci_names_format_6_to_GNR":"list_scientific_names_conversion",
    "convert_df_sci_names_format_6_to_OT":"list_scientific_names_conversion",

    "convert_df_resolved_names_format_GNR_to_OT":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_GNR_to_Phylomatic":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_GNR_to_PhyloT":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_1_to_3":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_3_to_5":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_5_to_Phylomatic":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_5_to_PhyloT":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_5_to_OT":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_2_to_4":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_4_to_6":"list_scientific_names_conversion",
    "convert_df_resolved_names_format_6_to_ALL_COMBO":"list_scientific_names_conversion",

    "convert_df_taxons_format_GNR_to_OT":"list_scientific_names_conversion",
    "convert_df_taxons_format_GNR_to_Phylomatic":"list_scientific_names_conversion",
    "convert_df_taxons_format_GNR_to_PhyloT":"list_scientific_names_conversion",
    "convert_df_taxons_format_1_to_3":"list_scientific_names_conversion",
    "convert_df_taxons_format_3_to_5":"list_scientific_names_conversion",
    "convert_df_taxons_format_5_to_Phylomatic":"list_scientific_names_conversion",
    "convert_df_taxons_format_5_to_PhyloT":"list_scientific_names_conversion",
    "convert_df_taxons_format_5_to_OT":"list_scientific_names_conversion",
    "convert_df_taxons_format_2_to_4":"list_scientific_names_conversion",
    "convert_df_taxons_format_4_to_6":"list_scientific_names_conversion",
    "convert_df_taxons_format_6_to_ALL_COMBO":"list_scientific_names_conversion",

    "convert_tree_format_NewickTree_to_ALL_COMBO":"tree_format_conversion",
    "convert_tree_format_PhyloTree_to_NMSU":"tree_format_conversion",
    "convert_tree_format_NMSU_to_NewickTree":"tree_format_conversion",
    "convert_tree_format_PhyloTree_to_phylo4Tree":"tree_format_conversion",
    "convert_tree_format_Phylo4Tree_to_PhyloTree":"tree_format_conversion",
    "convert_tree_format_1_to_2":"tree_format_conversion",
    "convert_tree_format_2_to_pHYLIPTree":"tree_format_conversion",
    "convert_tree_format_pHYLIPTree_to_PhyloTree":"tree_format_conversion",

    "convert_species_tree_format_NewickTree_to_ALL_COMBO":"tree_format_conversion",
    "convert_species_tree_format_PhyloTree_to_NMSU":"tree_format_conversion",
    "convert_species_tree_format_NMSU_to_NewickTree":"tree_format_conversion",
    "convert_species_tree_format_PhyloTree_to_phylo4Tree":"tree_format_conversion",
    "convert_species_tree_format_Phylo4Tree_to_PhyloTree":"tree_format_conversion",
    "convert_species_tree_format_1_to_2":"tree_format_conversion",
    "convert_species_tree_format_2_to_pHYLIPTree":"tree_format_conversion",
    "convert_species_tree_format_pHYLIPTree_to_PhyloTree":"tree_format_conversion",

    "convert_gene_tree_format_NewickTree_to_ALL_COMBO":"tree_format_conversion",
    "convert_gene_tree_format_PhyloTree_to_NMSU":"tree_format_conversion",
    "convert_gene_tree_format_NMSU_to_NewickTree":"tree_format_conversion",
    "convert_gene_tree_format_PhyloTree_to_phylo4Tree":"tree_format_conversion",
    "convert_gene_tree_format_Phylo4Tree_to_PhyloTree":"tree_format_conversion",
    "convert_gene_tree_format_1_to_2":"tree_format_conversion",
    "convert_gene_tree_format_2_to_pHYLIPTree":"tree_format_conversion",
    "convert_gene_tree_format_pHYLIPTree_to_PhyloTree":"tree_format_conversion"
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
    list_ZSS_Node = []
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
            #print_ZSSNode(ZSSNode)
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
        #if not graph.has_key(start):
        if start not in graph:
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
        #if not graph.has_key(start):
        if start not in graph:
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
        # For python <= 2    
        # if not graph.has_key(start):
        # For python >= 3
        if start not in graph:
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


