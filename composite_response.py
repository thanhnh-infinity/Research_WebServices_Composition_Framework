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

def process_a_plan_json_from_raw(big_list_answer_sets,json_in,json_planning_data,qos,multi_plans,quantity):
    try:
        data = MultipleLevelsOfDictionary()
        json_input = json_in['request_parameters']['input']
        array_input = []
        for i in range(0,len(json_input)):
            input_object = json_input[i]
            d = MultipleLevelsOfDictionary()
            d['name'] = input_object['name']
            d['resource_ontology_id'] = input_object['resource_ontology_id']
            d['resource_ontology_uri'] = input_object['resource_ontology_uri']
            d['resource_data_format_id'] = input_object['resource_data_format_id']
            d['resource_data_format_uri'] = input_object['resource_data_format_uri']
            array_input.append(d)
        json_output= json_in['request_parameters']['output']
        array_output = []
        for i in range(0,len(json_output)):
            output_object = json_output[i]
            d = MultipleLevelsOfDictionary()
            d['name'] = output_object['name']
            d['resource_ontology_id'] = output_object['resource_ontology_id']
            d['resource_ontology_uri'] = output_object['resource_ontology_uri']
            d['resource_data_format_id'] = output_object['resource_data_format_id']
            d['resource_data_format_uri'] = output_object['resource_data_format_uri']
            array_output.append(d)

        # For only one plan
        data['workflow_plan'] = []
        all_workflow_plans = []
        final_worklfow_plans = []
        #test_index = 0
        #test_list = [0,9,27,11,36,41]
        #test_list = [0,9,25]
        index = 0
        for workflow in big_list_answer_sets:
            #if (test_index in test_list):    
                detail_workflow = workflow[0]["Value"]
                # Read abstract workflow
                array_plan,raw_plan = read_a_full_workflow_detail(detail_workflow)
                # Read concrete workflow

                # Calculate score of QoS for whole workflow
                if (qos):
                    score_qos_workflow,consider_QoS_Vector = calculate_QoS_For_Workflow(detail_workflow)

                d = MultipleLevelsOfDictionary()
                d['info']['name'] = "Build Reconciliation Tree"
                d['info']['project'] = "Phylotastic"
                d['info']['step_quantity'] = len(array_plan)
    
                if (qos):
                    d['info']['quality_attributes']['qos']['score_qos'] = score_qos_workflow
                    d['info']['quality_attributes']['qos']['response_time'] = consider_QoS_Vector[0]
                    d['info']['quality_attributes']['qos']['throughput'] = consider_QoS_Vector[1]
                    d['info']['quality_attributes']['qos']['reliability'] = consider_QoS_Vector[4]
                    d['info']['quality_attributes']['qos']['availability_1'] = consider_QoS_Vector[2]
                    d['info']['quality_attributes']['qos']['availability_2'] = consider_QoS_Vector[3]
                d['full_plan'] = array_plan
                d['raw_plan'] = raw_plan
                d['ID'] = index
                all_workflow_plans.append(d)
                index = index + 1
            #test_index = test_index+1

        # Sorting workflow based on QoS attribute
        if (qos and multi_plans):
            sorted_plans = sorted(all_workflow_plans, key=lambda workflow : workflow['info']['quality_attributes']['qos']['score_qos'],reverse=True)
            # Select best criterial worlflows to displayed
            final_worklfow_plans = sorted_plans
        else:
            final_worklfow_plans = all_workflow_plans[0]
        #Full JSON data
        data['request_parameters']['input'] = array_input
        data['request_parameters']['output'] = array_output
        data['workflow_plan'] = final_worklfow_plans
        data['info']['moldes'] = json_planning_data['Models']
        data['info']['Time'] = json_planning_data['Time']
        if (qos and multi_plans):
            data['info']['ordered_multiple_workflows'] = True
        return data
    except Exception,err:
        print err
        return None
def read_a_full_workflow_detail(json_a_workflow_object):
    full_plan = []
    raw_plan = []
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
            raw_plan.append(predicate)
            goal_in = composite_parser.parse_goal_in_predicate(predicate)


    for predicate in json_a_workflow_object:
        if (OCCUR_SERIVCE_IN_PLAN in predicate.strip().upper()):
           LIST_OF_OCCUR_CLASS_PREDICATE.append(predicate)
        if (SERVICE_HAS_INPUT_HAS_DATA_FORMAT in predicate.strip().upper()):
           LIST_OF_HAS_INPUT_OP_CLASS_PREDICATE.append(predicate)
           raw_plan.append(predicate)
        if (SERVICE_HAS_OUTPUT_HAS_DATA_FORMAT in predicate.strip().upper()):
           LIST_OF_HAS_OUTPUT_OP_CLASS_PREDICATE.append(predicate)
           raw_plan.append(predicate)
        if (MAP_I_O in predicate.strip().upper()):
           LIST_OF_MATCH_I_O.append(predicate)
           raw_plan.append(predicate)

    for x in LIST_OF_OCCUR_CLASS_PREDICATE:
        service_obj = MultipleLevelsOfDictionary()
        service_name,step = composite_parser.parse_a_occur_service(x)
        if (step < goal_in):
            raw_plan.append(x)
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

    return full_plan,raw_plan
#print json.dumps(read_a_full_workflow_detail(test.ORIGINAL_WORKFLOW))