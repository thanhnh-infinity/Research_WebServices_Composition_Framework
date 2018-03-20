import os
import sys
import json
#import utility
import pprint
import composite_parser
import urllib2
import collections
import commands
import math
from sklearn.preprocessing import normalize
import configuration
import test

CDAO_URL_ONTOLOGY = "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#"


OCCUR_SERIVCE_IN_PLAN = "OCCUR("
GOAL_IN = "GOAL("
SERVICE_HAS_INPUT = "INSTANCE_HAS_INPUT("
SERVICE_HAS_OUTPUT = "INSTANCE_HAS_OUTPUT("
#SERVICE_HAS_INPUT_HAS_DATA_FORMAT = "INSTANCE_OPERATION_HAS_INPUT_HAS_DATA_FORMAT"
#SERVICE_HAS_OUTPUT_HAS_DATA_FORMAT = "INSTANCE_OPERATION_HAS_OUTPUT_HAS_DATA_FORMAT"
SERVICE_HAS_INPUT_HAS_DATA_FORMAT = "OPERATION_HAS_INPUT_HAS_DATA_FORMAT"
SERVICE_HAS_OUTPUT_HAS_DATA_FORMAT = "OPERATION_HAS_OUTPUT_HAS_DATA_FORMAT"
INITIAL_FACTS = "INITIALLY"
FINALLY_FACTS = "FINALLY"
MAP_I_O = "MAP("


class MultipleLevelsOfDictionary(collections.OrderedDict):
    def __getitem__(self,item):
        try:
            return collections.OrderedDict.__getitem__(self,item)
        except:
            value = self[item] = type(self)()
            return value

def read_a_full_workflow_detail(json_a_workflow_object):
    full_plan = []
    # Raw list of abtract planning - service class in order
    LIST_OF_OCCUR_CLASS_PREDICATE = []
    LIST_OF_GOAL_ABTRACT_PREDICATE = []
    LIST_OF_HAS_INPUT_OP_CLASS_PREDICATE = []
    LIST_OF_HAS_OUTPUT_OP_CLASS_PREDICATE = []
    LIST_OF_INITIAL_FACTS = []
    LIST_OF_GOAL_FACTS = []
    LIST_OF_MATCH_I_O = []

    #print json_a_workflow_object
    goal_in = -1

    for predicate in json_a_workflow_object:
        if (GOAL_IN in predicate.strip().upper()):
            goal_in = composite_parser.parse_goal_in_predicate(predicate)


    for predicate in json_a_workflow_object:
        if (OCCUR_SERIVCE_IN_PLAN in predicate.strip().upper()):
           LIST_OF_OCCUR_CLASS_PREDICATE.append(predicate)
        if (SERVICE_HAS_INPUT_HAS_DATA_FORMAT in predicate.strip().upper()):
           LIST_OF_HAS_INPUT_OP_CLASS_PREDICATE.append(predicate)
        if (SERVICE_HAS_OUTPUT_HAS_DATA_FORMAT in predicate.strip().upper()):
           LIST_OF_HAS_OUTPUT_OP_CLASS_PREDICATE.append(predicate)
        if (MAP_I_O in predicate.strip().upper()):
           LIST_OF_MATCH_I_O.append(predicate)

    for x in LIST_OF_OCCUR_CLASS_PREDICATE:
        service_obj = MultipleLevelsOfDictionary()
        service_name,step = composite_parser.parse_a_occur_service(x)
        if (step < goal_in): 
            service_obj['service_index'] = step
            service_obj['service_name'] = service_name
            service_obj['service_description'] = ""
            service_obj['service_uri'] = "%s%s" %(str(CDAO_URL_ONTOLOGY),str(service_name))
            service_obj['service_parameters'] = {}
            input_obj = MultipleLevelsOfDictionary()
            input_obj['info']['data_format'] = "x-www-urlencoded(Fixed)"
            input_components = []
            for ip in LIST_OF_HAS_INPUT_OP_CLASS_PREDICATE:
                
                hasIn_service_name,hasIn_resource,hasIn_data_format = composite_parser.parse_a_input_data_format(ip)
                if (service_name.strip() == hasIn_service_name.strip()):
                    input_com = MultipleLevelsOfDictionary()
                    input_com['resource_ontology_id'] = hasIn_resource
                    input_com['resource_ontology_uri'] = "%s%s" %(str(CDAO_URL_ONTOLOGY),str(hasIn_resource))
                    input_com['resource_data_format'] = hasIn_data_format
                    input_com['map'] = {}

                    for mapp in LIST_OF_MATCH_I_O:
                        match_obj = composite_parser.parse_a_match_predicate(mapp)

                        if (match_obj[0].strip() == service_name.strip()
                            and match_obj[1].strip() == hasIn_resource
                            and match_obj[3] == step):
                            input_com['map']['resource_ontology_id'] = match_obj[5]
                            input_com['map']['resource_data_format'] = match_obj[6]
                            input_com['map']['at_step'] = match_obj[7]
                            input_com['map']['from_service'] = match_obj[4]
                    input_components.append(input_com)
            input_obj['components'] = input_components
            service_obj['service_parameters']['input'] = input_obj

            output_obj = MultipleLevelsOfDictionary()
            output_obj['info']['data_format'] = "application/json"
            output_components = []
            for ou in LIST_OF_HAS_OUTPUT_OP_CLASS_PREDICATE:
                hasOut_service_name,hasOut_resource,hasOut_data_format = composite_parser.parse_a_output_data_format(ou)
                if (service_name.strip() == hasOut_service_name.strip()):
                    output_com = MultipleLevelsOfDictionary()
                    output_com['resource_ontology_id'] = hasOut_resource
                    output_com['resource_ontology_uri'] = "%s%s" %(str(CDAO_URL_ONTOLOGY),str(hasOut_resource))
                    output_com['resource_data_format'] = hasOut_data_format
                    output_components.append(output_com)

            output_obj['components'] = output_components
            service_obj['service_parameters']['output'] = output_obj
            full_plan.append(service_obj)

    return full_plan
#print json.dumps(read_a_full_workflow_detail(test.ORIGINAL_WORKFLOW))