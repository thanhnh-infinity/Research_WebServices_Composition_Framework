import parse
#from classes.services import Service_Class,Service_Instance,DataFormatObject,Match_Object
#from classes.states import InitialState,GoalState,CommonAsset_DataFormat
import collections
import json

# occur serivce class
OCCUR_SERVICE_CLASS_ABTRACT_LEVEL = 'occur({},{:d})'
GOAL_PREDICATE = 'goal({:d})'
SERVICE_HAS_INPUT = 'instance_has_input({},{},{})'
SERVICE_HAS_OUTPUT = 'instance_has_output({},{},{})'
INSTANCE_OP_INPUT_HAS_DATA_FORMAT = 'instance_operation_has_input_has_data_format({},{},{})'
INSTANCE_OP_OUPUT_HAS_DATA_FORMAT = 'instance_operation_has_output_has_data_format({},{},{})'
INITIAL_FACTS = 'initially({},{})'
GOAL_FACTS = 'finally({},{})'
MATCH_I_O = 'map({},{},{},{:d},{},{},{},{:d})'
HAS_QOS_RESPONSE_TIME = 'has_qos_response_time_involved_concrete({},{})'
HAS_QOS_AVAILABILITY = 'has_qos_availability_involved_concrete({},{})'
HAS_QOS_THROUGHPUT = 'has_qos_throughput_involved_concrete({},{})'
HAS_QOS_RELIABILITY = 'has_qos_reliability_involved_concrete({},{})'


def parse_a_has_qos_response_time(has_response_time):
    parsed = parse.parse(HAS_QOS_RESPONSE_TIME, has_response_time.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None ):
            return parsed[0],parsed[1]
    return None,None
def parse_a_has_qos_availability(has_availability):
    parsed = parse.parse(HAS_QOS_AVAILABILITY, has_availability.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None ):
            return parsed[0],parsed[1]
    return None,None
def parse_a_has_qos_throughput(has_throughput):
    parsed = parse.parse(HAS_QOS_THROUGHPUT, has_throughput.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None ):
            return parsed[0],parsed[1]
    return None,None
def parse_a_has_qos_reliability(has_reliability):
    parsed = parse.parse(HAS_QOS_RELIABILITY, has_reliability.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None ):
            return parsed[0],parsed[1]
    return None,None
def parse_a_asset_for_goal_fact(goal_fact):
    parsed = parse.parse(GOAL_FACTS, goal_fact.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None):
            resource_name = parsed[0]
            data_format = parsed[1] # if data_format is unknown or ignore means that can anything (system selected)
            asset_obj = CommonAsset_DataFormat(resource_name,data_format)
            return asset_obj
    return None
def parse_a_asset_for_initial_fact(init_fact):
    parsed = parse.parse(INITIAL_FACTS, init_fact.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None):
            resource_name = parsed[0]
            data_format = parsed[1] # if data_format is unknown or ignore means that can anything (system selected)
            asset_obj = CommonAsset_DataFormat(resource_name,data_format)
            return asset_obj
    return None
def parse_a_input_data_format(input_data_format_predicate):
    parsed = parse.parse(INSTANCE_OP_INPUT_HAS_DATA_FORMAT, input_data_format_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None and parsed[2] is not None):
            operation_name = parsed[0]
            resource_name = parsed[1]
            data_format = parsed[2]
            return operation_name,resource_name,data_format
    return None
def parse_a_output_data_format(output_data_format_predicate):
    parsed = parse.parse(INSTANCE_OP_OUPUT_HAS_DATA_FORMAT, output_data_format_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None and parsed[2] is not None):
            operation_name = parsed[0]
            resource_name = parsed[1]
            data_format = parsed[2]
            return operation_name,resource_name,data_format
    return None
def parse_a_service_has_input(has_input_predicate):
    parsed = parse.parse(SERVICE_HAS_INPUT, has_input_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[2] is not None):
           return parsed[0],parsed[1],parsed[2]
    return None
def parse_a_service_has_output(has_output_predicate):
    #occur_service_class = Service_Class()
    parsed = parse.parse(SERVICE_HAS_OUTPUT, has_output_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[2] is not None):
           return parsed[0],parsed[1],parsed[2]
    return None
def parse_a_occur_service(occur_predicate):
    #occur_service_class = Service_Class()
    parsed = parse.parse(OCCUR_SERVICE_CLASS_ABTRACT_LEVEL, occur_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and (int(parsed[1]) or parsed[1] == 0)):
            service_class_name = parsed[0]
            step = int(parsed[1])
            return service_class_name,step
    return None
def parse_goal_in_predicate(goal_predicate):
    parsed = parse.parse(GOAL_PREDICATE, goal_predicate)

    if (parsed is not None) and (int(parsed[0])) :
        return int(parsed[0])
    else:
        return None
def parse_a_match_predicate(match):
    parsed = parse.parse(MATCH_I_O, match.strip())
    if (parsed is not None) :
        return parsed