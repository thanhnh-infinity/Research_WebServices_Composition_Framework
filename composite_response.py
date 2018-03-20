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
HAS_QOS_RESPONSE_TIME_INVOLVED_CONRETE = "HAS_QOS_RESPONSE_TIME_INVOLVED_CONCRETE"
HAS_QOS_AVAILABILITY_INVOLVED_CONRETE = "HAS_QOS_AVAILABILITY_INVOLVED_CONCRETE"
HAS_QOS_THROUGHPUT_INVOLVED_CONRETE = "HAS_QOS_THROUGHPUT_INVOLVED_CONCRETE"
HAS_QOS_RELIABILITY_INVOLVED_CONRETE = "HAS_QOS_RELIABILITY_INVOLVED_CONCRETE"


class MultipleLevelsOfDictionary(collections.OrderedDict):
    def __getitem__(self,item):
        try:
            return collections.OrderedDict.__getitem__(self,item)
        except:
            value = self[item] = type(self)()
            return value

def calculateNormalization(aVector):
    sum_thing = 0
    for a in aVector:
        sum_thing += a*a

    length_vector = math.sqrt(sum_thing)
    normalizeVector = []
    for a in aVector:
        normalizeVector.append(float(a)/length_vector)

    return normalizeVector
def read_QoS_values_for_workflow(json_a_workflow_object):
    # Read all qos attribute of each concrete service that occur in Concrete Plan Level
    qos_response_time_total = 0.0
    qos_availability_total_1 = 1.0
    qos_availability_total_2 = 1.0
    qos_throughput_total = 0.0
    qos_throughput_avg = 0.0
    qos_reliability_total = 0.0
    qos_reliability_avg = 0.0
    count_n_tp = 0
    count_n_ra = 0

    qos_response_time_vector = []
    qos_throughput_vector = []
    qos_reliability_vector = []
    qos_availability_vector = []



    for predicate in json_a_workflow_object:
        # Calcuate qos response time for whole workflow, simple is sum of all. = sum(1->n)T(operation_i)
        if (HAS_QOS_RESPONSE_TIME_INVOLVED_CONRETE in predicate.strip().upper()):
            op,time,response_time = composite_parser.parse_a_has_qos_response_time(predicate.strip())
            #qos_response_time_total += float(response_time.replace("\"",""))
            qos_response_time_total += float(response_time)/1000
            qos_response_time_vector.append(float(response_time)/1000)
        # Calculate qos availability for whole workflow, = Pi(1->n)e^(av(op_i)*z_i)
        if (HAS_QOS_AVAILABILITY_INVOLVED_CONRETE in predicate.strip().upper()):
            op,time,av = composite_parser.parse_a_has_qos_availability(predicate.strip())
            qos_availability_total_1 *= math.exp(float(av)/1000*1)
            qos_availability_total_2 *= float(av)/1000
            qos_availability_vector.append(float(av)/1000)
            #print "Go go"
        # Calculate qos throughput = [Sum(1->n)(tp(op_i))]/n
        if (HAS_QOS_THROUGHPUT_INVOLVED_CONRETE in predicate.strip().upper()):
            count_n_tp = count_n_tp + 1
            op,time,tp = composite_parser.parse_a_has_qos_throughput(predicate.strip())
            qos_throughput_total += float(tp)/1000
            qos_throughput_vector.append(float(tp)/1000)
        # Calculate qos reliability = % Shoud ask Abu about where is he got it
        if (HAS_QOS_RELIABILITY_INVOLVED_CONRETE in predicate.strip().upper()):
            count_n_ra = count_n_ra + 1
            op,time,ra = composite_parser.parse_a_has_qos_reliability(predicate.strip())
            qos_reliability_total += float(ra)/1000
            qos_reliability_vector.append(float(ra)/1000)

    try:
        qos_throughput_avg = qos_throughput_total/count_n_tp
    except:
        qos_throughput_avg = 0.0

    try:
        qos_reliability_avg = qos_reliability_total/count_n_ra
    except:
        qos_reliability_avg = 0.0

    return qos_response_time_vector,qos_throughput_vector,qos_availability_vector,qos_reliability_vector,qos_response_time_total,qos_throughput_avg,qos_availability_total_1,qos_availability_total_2,qos_reliability_avg

def calculate_QoS_For_Workflow(detail_workflow):
    # Read QoS
    qos_response_time_vector,qos_throughput_vector,qos_availability_vector, qos_reliability_vector,resp_time,throughput,availability_1,availability_2,reliability =read_QoS_values_for_workflow(detail_workflow)

    # Logic to calculate Total QoS for a workflow
    # Cach 1 : Using function vector of composition service
    consider_QoS_Vector = [resp_time,throughput,availability_1,availability_2,reliability]
    # Normalization vector data by max min

    # Cach 2 : Seperate vectors Using Local Optimization
    # Scaling Phase : Normalization data vector by max (Scalling Phase)
    qos_response_time_vector_norm = normalize([qos_response_time_vector],norm='max')
    qos_throughput_vector_norm = normalize([qos_throughput_vector],norm='max')
    qos_availability_vector_norm = normalize([qos_availability_vector],norm='max')
    qos_reliability_vector_norm = normalize([qos_reliability_vector],norm='max')
    '''
    print "--------------------------------"
    print qos_response_time_vector
    print qos_response_time_vector_norm[0]
    print qos_throughput_vector
    print qos_throughput_vector_norm[0]
    print qos_availability_vector
    print qos_availability_vector_norm[0]
    print qos_reliability_vector
    print qos_reliability_vector_norm[0]
    print "--------------------------------"
    '''
    # Weighting Phase Score(WF) = sum(all criterie)(Vi,j*Wj)
    # Calculate score_response_time
    score_qos_response_time = 0.0
    for value in qos_response_time_vector_norm[0]:
        score_qos_response_time += value
    score_qos_response_time = score_qos_response_time*configuration.WEIGHT_QoS_DATA['response_time']
    #print "Response Time : " + str(score_qos_response_time)

    score_qos_throughput = 0.0
    for value in qos_throughput_vector_norm[0]:
        score_qos_throughput += value
    try:
        score_qos_throughput = (score_qos_throughput / len(qos_throughput_vector_norm[0]))*configuration.WEIGHT_QoS_DATA['throughput']
    except:
        score_qos_throughput = 0.0
    #print "Throughput : " + str(score_qos_throughput)

    score_qos_availability = 1.0
    for value in qos_availability_vector_norm[0]:
        score_qos_availability *= value
    score_qos_availability = score_qos_availability*configuration.WEIGHT_QoS_DATA['availability']
    #print "Availability : " + str(score_qos_availability)

    score_qos_reliability= 0.0
    for value in qos_reliability_vector_norm[0]:
        score_qos_reliability += value
    try:
        score_qos_reliability = (score_qos_reliability / len(qos_reliability_vector_norm[0]))*configuration.WEIGHT_QoS_DATA['reliability']
    except:
        score_qos_reliability= 0.0
    #print "Reliability :" + str(score_qos_reliability)

    score_qos_workflow = 0.0
    score_qos_workflow = score_qos_response_time + score_qos_throughput + score_qos_reliability + score_qos_availability
    return score_qos_workflow,consider_QoS_Vector

def process_a_plan_json_from_raw(big_list_answer_sets,json_in,json_planning_data,qos,multi_plans,quantity):
    try:
        remember_qos_total = []

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
            slot = quantity

            for i in range(0,len(sorted_plans)):
                #considered_qos = sorted_plans[i]['info']['quality_attributes']['qos']['score_qos']
                #if (considered_qos not in remember_qos_total):
                final_worklfow_plans.append(sorted_plans[i])
                slot = slot - 1
                if slot == 0:
                    break    
            #Select best criterial worlflows to displayed
            #final_worklfow_plans = sorted_plans
        else:
            final_worklfow_plans.append(all_workflow_plans[0])
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