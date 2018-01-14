import parse
from classes.services import Service_Class,Service_Instance,DataFormatObject,Match_Object
from classes.states import InitialState,GoalState,CommonAsset_DataFormat
import collections
import json

# occur serivce class
OCCUR_SERVICE_CLASS_ABTRACT_LEVEL = 'occur({},{:d})'
GOAL_PREDICATE = 'goal({:d})'
POSSIBLE_CONCRETE_OPERATION_IN_CLASS = 'possible_concrete_operation({},{},{:d})'
HAS_INPUT_SERIVCE_CLASS_ABTRACT_LEVEL = 'has_input({},{},{})'
HAS_OUTPUT_SERIVCE_CLASS_ABTRACT_LEVEL = 'has_output({},{},{})'
INSTANCE_OP_INPUT_HAS_DATA_FORMAT = 'instance_operation_has_input_has_data_format({},{},{})'
INSTANCE_OP_OUPUT_HAS_DATA_FORMAT = 'instance_operation_has_output_has_data_format({},{},{})'
INITIAL_FACTS = 'initially({},{})'
GOAL_FACTS = 'finally({},{})'
OCCUR_CONVERTION_CONCRETE_SERVIVE = 'occur_convert_op_instance({},{:d},{:d})'
OCCUR_CONCRETE_SERVIVE = 'occur_concrete_operation({},{},{:d})'
MATCH_I_O = 'match({},{},{:d},{},{:d})'


class MultipleLevelsOfDictionary(collections.OrderedDict):
    def __getitem__(self,item):
        try:
            return collections.OrderedDict.__getitem__(self,item)
        except:
            value = self[item] = type(self)()
            return value

def return_success_get(data):
    return json.dumps(data, indent=4)

def return_response_error(code, type, mess, format="JSON"):
    if (format == "JSON"):
        message = {type: mess}
        return json.dumps(message)
    else:
        return "Not support yet"
def parse_a_occur_concrete_op_service(concrete_op):
    parsed = parse.parse(OCCUR_CONCRETE_SERVIVE, concrete_op.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None and parsed[2] is not None):
            return parsed[0],parsed[1],parsed[2]
    return None
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
            data_format_object = DataFormatObject(operation_name,resource_name,data_format)
            return data_format_object
    return None

def parse_a_output_data_format(output_data_format_predicate):
    parsed = parse.parse(INSTANCE_OP_OUPUT_HAS_DATA_FORMAT, output_data_format_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[1] is not None and parsed[2] is not None):
            operation_name = parsed[0]
            resource_name = parsed[1]
            data_format = parsed[2]
            data_format_object = DataFormatObject(operation_name,resource_name,data_format)
            return data_format_object
    return None

def parse_a_has_input_service_class(has_input_predicate):
    #occur_service_class = Service_Class()
    parsed = parse.parse(HAS_INPUT_SERIVCE_CLASS_ABTRACT_LEVEL, has_input_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[2] is not None):
           return [parsed[0],parsed[2]]
    return None
def parse_a_has_output_service_class(has_output_predicate):
    #occur_service_class = Service_Class()
    parsed = parse.parse(HAS_OUTPUT_SERIVCE_CLASS_ABTRACT_LEVEL, has_output_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and parsed[2] is not None):
           return [parsed[0],parsed[2]]
    return None
def parse_a_occur_service_class(occur_predicate):
    #occur_service_class = Service_Class()
    parsed = parse.parse(OCCUR_SERVICE_CLASS_ABTRACT_LEVEL, occur_predicate.strip())
    if (parsed is not None):
        if (parsed[0] is not None and (int(parsed[1]) or parsed[1] == 0)):
            service_class_name = parsed[0]
            step = int(parsed[1])
            occur_service_class = Service_Class(service_class_name,step)
            return occur_service_class
    return None
def parse_goal_abtract_predicate(goal_predicate):
    parsed = parse.parse(GOAL_PREDICATE, goal_predicate)

    if (parsed is not None) and (int(parsed[0])) :
        return int(parsed[0])
    else:
        return None

def parse_a_possible_concrete_operation(possible_concrete):
    parsed = parse.parse(POSSIBLE_CONCRETE_OPERATION_IN_CLASS, possible_concrete.strip())
    if (parsed is not None):
        if (parsed[0] is not None and (int(parsed[2]) or parsed[2] == 0) and parsed[1] is not None):
            operation_name = parsed[0]
            class_name = parsed[1]
            abtract_step = int(parsed[2])
            instance_op_object = Service_Instance(operation_name,class_name,abtract_step)
            return instance_op_object
    return None
def parse_a_concrete_plan_to_execute(concrete_plan):
    print "Executable plan"
def parse_a_match_predicate(match):
    parsed = parse.parse(MATCH_I_O, match.strip())
    if (parsed is not None):
        if (parsed[0] is not None and (int(parsed[2]) or parsed[2] == 0) and parsed[1] is not None and parsed[3] is not None and (int(parsed[4]) or parsed[4] == 0)):
            name = parsed[0]
            match_input = parsed[1]
            match_step = int(parsed[2])
            existed_o = parsed[3]
            existed_o_step = int(parsed[4])
            match_object = Match_Object(name,match_input,match_step,existed_o,existed_o_step)
            return match_object