#import ontospy
import Global_Parameters
import OWLUltility
import sys
import os
import urllib2
import collections
import subprocess
import commands
import json

#CDAO_PHYLOTASTIC_ONT = ontospy.Ontospy(Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL)
#PHYLO_METHODS_ONT = ontospy.Ontospy(Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL)
PREDICATE_NAME_FOR_OCCUR_SERIVCE_CLASS_IN_ABTRACT = "OCCUR"
PREDICATE_NAME_FOR_POSSIBLE_CONCRETE_SERVICE_OP = "POSSIBLE_CONCRETE_OPERATION"
PREDICATE_NAME_FOR_GOAL_ABTRACT = "GOAL"
PREDICATE_NAME_FOR_HAS_INPUT_SERVICE_CLASS = "HAS_INPUT"
PREDICATE_NAME_FOR_HAS_OUTPUT_SERVICE_CLASS = "HAS_OUTPUT"
PREDICATE_NAME_FOR_INPUT_HAS_DATA_FORMAT = "INSTANCE_OPERATION_HAS_INPUT_HAS_DATA_FORMAT"
PREDICATE_NAME_FOR_OUTPUT_HAS_DATA_FORMAT = "INSTANCE_OPERATION_HAS_OUTPUT_HAS_DATA_FORMAT"
PREDICATE_NAME_FOR_INITIAL_FACTS = "INITIALLY"
PREDICATE_NAME_FOR_GOAL_FACTS = "FINALLY"
PREDICATE_REAL_CONCRETE_OPERATION_INSTANCE = "OCCUR_CONCRETE_OPERATION"
PREDICATE_NAME_FOR_MATCHED_I_O = "MATCH"



class MultipleLevelsOfDictionary(collections.OrderedDict):
    def __getitem__(self,item):
        try:
            return collections.OrderedDict.__getitem__(self,item)
        except:
            value = self[item] = type(self)()
            return value

def return_success_get(data):
    cherrypy.response.headers['Content-Type'] = "application/json"
    cherrypy.response.headers['Retry-After'] = 60
    cherrypy.response.status = 200
    return json.dumps(data, indent=4)

def return_response_error(code, type, mess, format="JSON"):
    if (format == "JSON"):
        cherrypy.response.headers['Content-Type'] = "application/json"
        cherrypy.response.headers['Retry-After'] = 60
        cherrypy.response.status = code
        message = {type: mess}
        return json.dumps(message)
    else:
        return "Not support yet"
#Firt method : Get all instances of a nested class (directed class) - Engine 2
def get_all_instances_of_a_directed_class_engine_2(localClassName,sourceOntology):
    full_uri_class = ""
    if (sourceOntology == "CDAO_PHYLOTASTIC"):
        full_uri_class = Global_Parameters.PREFIX_CDAO_PHYLOTASTIC_ONTOLOGY_URL + localClassName
    elif (sourceOntology == "PHYLO_METHODS"):
        full_uri_class = Global_Parameters.PREFIX_PHYLOGENETIC_METHODS_ONTOLOGY_URL + localClassName
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_ALL_INSTANCES_OF_A_DIRECTED_CLASS','-OWLCLASS_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#Firt method : Get all instances of a nested class (directed class) - Engine 1
def get_all_instances_of_a_directed_class_engine_1(owl_class_uri):
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_ALL_INSTANCES_OF_A_DIRECTED_CLASS','-OWLCLASS_URI',owl_class_uri], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

#Second service : Get all directed subclasses of a class
#Engine 2
def get_all_directed_subclass_of_class_engine_2(localClassName,sourceOntology):
    full_uri_class = ""
    if (sourceOntology == "CDAO_PHYLOTASTIC"):
        full_uri_class = Global_Parameters.PREFIX_CDAO_PHYLOTASTIC_ONTOLOGY_URL + localClassName
    elif (sourceOntology == "PHYLO_METHODS"):
        full_uri_class = Global_Parameters.PREFIX_PHYLOGENETIC_METHODS_ONTOLOGY_URL + localClassName
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DIRECTED_SUBCLASS_OF_CLASS','-OWLCLASS_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#Engine 1
def get_all_directed_subclass_of_class_engine_1(owl_class_uri):
    full_uri_class = owl_class_uri
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DIRECTED_SUBCLASS_OF_CLASS','-OWLCLASS_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#3rd service : Get hierarchy subclasses of a class
def get_hierarchy_subclasses_of_class(full_class_uri,level):
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_HIERARCHY_CLASSES_FROM_ROOT_CLASS','-OWLCLASS_URI',full_class_uri,'-LEVEL',level], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

#4th service : Get detail information of an opertaion - Engine 2
def get_detail_information_of_operation_engine_2(operation_name,sourceOntology):
    full_uri_class = ""
    if (sourceOntology == "CDAO_PHYLOTASTIC"):
        full_uri_class = Global_Parameters.PREFIX_CDAO_PHYLOTASTIC_ONTOLOGY_URL + operation_name
    elif (sourceOntology == "PHYLO_METHODS"):
        full_uri_class = Global_Parameters.PREFIX_PHYLOGENETIC_METHODS_ONTOLOGY_URL + operation_name
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DETAIL_INFO_OF_AN_OPERATION_INSTANCE','-OWLINSTANCE_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#4th service : Get detail information of an opertaion - Engine 1
def get_detail_information_of_operation_engine_1(operation_uri):
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DETAIL_INFO_OF_AN_OPERATION_INSTANCE','-OWLINSTANCE_URI',operation_uri], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

#5th service : Get detail information of a resource - Engine 2
def get_detail_information_of_resource_engine_2(resource_name,sourceOntology):
    full_uri_class = ""
    if (sourceOntology == "CDAO_PHYLOTASTIC"):
        full_uri_class = Global_Parameters.PREFIX_CDAO_PHYLOTASTIC_ONTOLOGY_URL + resource_name
    elif (sourceOntology == "PHYLO_METHODS"):
        full_uri_class = Global_Parameters.PREFIX_PHYLOGENETIC_METHODS_ONTOLOGY_URL + resource_name
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DETAIL_INFO_OF_A_RESOURCE_INSTANCE','-OWLINSTANCE_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#5th service : Get detail information of an opertaion - Engine 1
def get_detail_information_of_resource_engine_1(resource_uri):
    full_uri_class = resource_uri
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DETAIL_INFO_OF_A_RESOURCE_INSTANCE','-OWLINSTANCE_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out

#6th service : Get detail information of a component - Engine 2
def get_detail_information_of_component_engine_2(component_name,sourceOntology):
    full_uri_class = ""
    if (sourceOntology == "CDAO_PHYLOTASTIC"):
        full_uri_class = Global_Parameters.PREFIX_CDAO_PHYLOTASTIC_ONTOLOGY_URL + component_name
    elif (sourceOntology == "PHYLO_METHODS"):
        full_uri_class = Global_Parameters.PREFIX_PHYLOGENETIC_METHODS_ONTOLOGY_URL + component_name
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DETAIL_INFO_OF_A_COMPONENT_INSTANCE','-OWLINSTANCE_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#6th service : Get detail information of an component - Engine 1
def get_detail_information_of_component_engine_1(component_uri):
    full_uri_class = component_uri
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_DETAIL_INFO_OF_A_COMPONENT_INSTANCE','-OWLINSTANCE_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#7th : Get Triple Data predicates and objects from subject (uri ID)
def get_triples_predicates_objects_from_subject(subject_uri):
    full_uri_class = subject_uri
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_TRIPLE_STYLE_PREDICATE_OBJECT_FROM_SUBJECT','-SUBJECT_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#8th : Get Triple Data subjects and predicates from object (uri ID)
def get_triples_subjects_predicates_from_object(object_uri):
    full_uri_class = object_uri
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_TRIPLE_STYLE_SUBJECT_PREDICATE_FROM_OBJECT','-OBJECT_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#9th : Get Triple Data subjects and objects from predicate (uri ID)
def get_triples_subjects_objects_from_predicate(predicate_uri):
    full_uri_class = predicate_uri
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_TRIPLE_STYLE_SUBJECT_OBJECT_FROM_PREDICATE','-PREDICATE_URI',full_uri_class], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#10th : Get Triple Data objects from subject + predicate (uri ID)
def get_triples_objects_from_subject_predicate(subject_uri,predicate_uri):
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_TRIPLE_STYLE_OBJECT_FROM_SUBJECT_PREDICATE','-SUBJECT_URI',subject_uri.strip(),'-PREDICATE_URI',predicate_uri.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#11th : Get Triple Data subjects from object + predicate (uri ID)
def get_triples_subjects_from_object_predicate(object_uri,predicate_uri):
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_TRIPLE_STYLE_SUBJECT_FROM_OBJECT_PREDICATE','-OBJECT_URI',object_uri.strip(),'-PREDICATE_URI',predicate_uri.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#12th : Get Triple Data subjects from object + predicate (uri ID)
def get_triples_predicates_from_subject_object(subject_uri,object_uri):
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_TRIPLE_STYLE_PREDICATE_FROM_SUBJECT_OBJECT','-SUBJECT_URI',subject_uri.strip(),'-OBJECT_URI',object_uri.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#13rd : Get Graph of an ontology entity
def get_build_graph_of_ontology_entity(entity_uri,strType):
    p = subprocess.Popen(['java', '-jar', Global_Parameters.PATH_TO_ONTOLOGY_JAR_ENGINE,'-CDAO_ONTOLOGY',Global_Parameters.GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL,'-PHYLO_METHODS_ONTOLOGY',Global_Parameters.GLOBAL_PHYLO_METHODS_ONTOLOGY_URL,'-QUERY','GET_RELATION_GRAPH_OF_ONTOLOGY_ENTITY','-URI',entity_uri.strip(),'-TYPE',strType.strip()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out
#14rd : Run planning
def run_planning_engine(path_to_clingo,path_to_main_base,path_to_initial,path_to_goal,default_step,number_of_model):
    #p = subprocess.Popen([path_to_clingo, '--outf=2', '-n',number_of_model,path_to_planning_base,path_to_ontology_base,path_to_initial,path_to_goal], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen([path_to_clingo, '--outf=2', path_to_main_base,path_to_initial,path_to_goal,default_step], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    #print err
    return out
    
#14rd : Run planning
def run_re_planning_engine(path_to_clingo,path_to_main_base,path_to_initial,path_to_goal,path_to_preference,path_to_original_workflow,default_step,number_of_model):
    #p = subprocess.Popen([path_to_clingo, '--outf=2', '-n',number_of_model,path_to_planning_base,path_to_ontology_base,path_to_initial,path_to_goal], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen([path_to_clingo, '--outf=2', path_to_main_base,path_to_initial,path_to_goal,path_to_preference,path_to_original_workflow,default_step], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    #print err
    return out

def parser_occur_perdicate(occur_string):
    try:
        occur_info = MultipleLevelsOfDictionary()
        occur_info["step"] = 0
        occur_info["web_service"] = ""
        occur_info["operation"] = ""
        occur_info["input_param"] = ""
        occur_info["output_param"] = ""

        prefix = occur_string[0:23]
        if (prefix == "occurs(run_WS_Operation"):
            subfix = occur_string[24:]
            subfix = subfix.replace(")","")

            elements = subfix.split(",")

            occur_info["step"] = int(elements[4])
            occur_info["web_service"] = elements[0]
            occur_info["operation"] = elements[1]
            occur_info["input_param"] = elements[2]
            occur_info["output_param"] = elements[3]
        else:
            return None

        return occur_info
    except Exception,err:
        print err
        return None

#get_all_instances_of_a_directed_class("phylotastic_resources")
#PEFERCT, CLINGO can return JSON : ./clingo --outf=2 -n 1 planning_base.lp ontology_base.lp initial_state_base.lp goal_state_base.lp
