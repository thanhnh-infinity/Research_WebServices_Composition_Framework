from classes.plans import Abtract_Planning,InitialState,GoalState,Concrete_Planning
from classes.services import Service_Class,Service_Instance,DataFormatObject,Match_Object
import os
import subprocess
import sys
import json
import random
#import utility
import pprint
import time
import planning_algorithms
import configuration


clingo_path = 'clingo'
clingo_options = ['--outf=2','-n 0']
clingo_command = [clingo_path] + clingo_options

FULL_PATH_ABTRACT_PLANNING_ENGINE_MODEL = os.path.join(os.getcwd(), "ASP_Planning","planning")
FULL_PATH_PLANNING_STATES_FOLDER = os.path.join(os.getcwd(),"ASP_Planning" ,"states")
FULL_PATH_PLANNING_PREFERENCE_FOLDER = os.path.join(os.getcwd(), "ASP_Planning","preference")


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

out_predicates = "goal_data_format"

GOAL_ABTRACT_IN = 0

ASP_RULE_CONSIDER_ABTRACT_STEP = "consider_abtract_step(%s)."
ASP_RULE_INITIAL_DATA_FORMAT = "initially_data_format(%s,T) :- consider_abtract_step(T). \n"
ASP_RULE_GOAL_DATA_FORMAT = "goal_data_format(T,Time) :- %s consider_abtract_step(T)."
ASP_RULE_EXIST_DATA_FORMAT_FOR_GOAL_STATE = "exists_data_format(%s,T,Time),"

GLOBAL_ABTRACT_PLANNING = Abtract_Planning()

def solve_program(program):
    input = program.encode()
    process = subprocess.Popen(clingo_command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, error = process.communicate(input)
    #print error
    result = json.loads(output.decode())
    if result['Result'] == 'SATISFIABLE':
        return [value['Value'] for value in result['Call'][0]['Witnesses']]
    else:
        return None

def solve_abtract_level(number_of_model,path_to_planning_base,path_to_ontology_base,path_to_initial,path_to_goal,path_to_configuration,path_to_preference,path_to_qos):
    clingo_command = [clingo_path, '--outf=2', '-n',str(number_of_model),path_to_planning_base,path_to_ontology_base,path_to_initial,path_to_goal,path_to_configuration,path_to_preference,path_to_qos]
    p = subprocess.Popen(clingo_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate()
    result = json.loads(output.decode())

    if result['Result'] == 'SATISFIABLE':
        return [value['Value'] for value in result['Call'][0]['Witnesses']]
    else:
        return None

def get_base_program_mapping_data_format():
    content = ""
    configuration_data = ""
    with open(os.path.join(FULL_PATH_ABTRACT_PLANNING_ENGINE_MODEL,configuration.CONFIGURATION_DATA['dataformat_mapping_level_planning_asp_file']), 'r') as content_file:
         content = content_file.read()
    with open(os.path.join(FULL_PATH_PLANNING_PREFERENCE_FOLDER,configuration.CONFIGURATION_DATA['planning_configuration_asp_file']), 'r') as content_file:
         configuration_data = content_file.read()

    base_program = content + "\n" + configuration_data
    return base_program

def single_run_planning_mapping_data_format(list_input_data_format, list_output_data_format, abtract_step, index_model):
    base_mapping_program = get_base_program_mapping_data_format()
    base_mapping_program += "\n"
    base_mapping_program += ASP_RULE_CONSIDER_ABTRACT_STEP %(str(abtract_step))
    base_mapping_program += "\n"
    # Create input data format
    for df in list_input_data_format:
        base_mapping_program += ASP_RULE_INITIAL_DATA_FORMAT %(df)
    base_mapping_program += "\n"
    # Crate output data format
    string_for_exits_thing_in_goal = ""
    for df in list_output_data_format:
        string_for_exits_thing_in_goal += ASP_RULE_EXIST_DATA_FORMAT_FOR_GOAL_STATE %(df)
        #base_mapping_program += ASP_RULE_GOAL_DATA_FORMAT %(df)
    base_mapping_program += ASP_RULE_GOAL_DATA_FORMAT %(string_for_exits_thing_in_goal)
    #if ("nmsu_tree_format" in list_output_data_format):
    #    print base_mapping_program

    mapping_data_format_planning_data = solve_program(base_mapping_program)
    if (mapping_data_format_planning_data is not None):
        if (index_model == 0):
            return mapping_data_format_planning_data[index_model]
        elif (index_model == -1):
            return mapping_data_format_planning_data
        else:
            if (mapping_data_format_planning_data[index_model] is not None):
                return mapping_data_format_planning_data[index_model] 
    else:
        return None

def read_data_from_abstract_planning(consider_planning_data_json):
    # Raw list of abtract planning - service class in order
    LIST_OF_OCCUR_PREDICATE = []
    LIST_OF_POSSIBLE_CONCRETE_OP_INSTANCES_PREDICATE = []
    LIST_OF_GOAL_ABTRACT_PREDICATE = []
    LIST_OF_HAS_INPUT_OP_CLASS_PREDICATE = []
    LIST_OF_HAS_OUTPUT_OP_CLASS_PREDICATE = []
    LIST_OF_INPUT_DATA_FORMAT_PREDICATE = []
    LIST_OF_OUTPUT_DATA_FORMAT_PREDICATE = []
    LIST_OF_INITIAL_FACTS = []
    LIST_OF_GOAL_FACTS = []
    LIST_OF_MATCH_I_O = []

    if (consider_planning_data_json is not None) and (len(consider_planning_data_json) > 0):
        for predicate in consider_planning_data_json:
           
            if (PREDICATE_NAME_FOR_OCCUR_SERIVCE_CLASS_IN_ABTRACT in predicate.upper()):
                     LIST_OF_OCCUR_PREDICATE.append(predicate) 
            if (PREDICATE_NAME_FOR_POSSIBLE_CONCRETE_SERVICE_OP in predicate.upper()):
                     LIST_OF_POSSIBLE_CONCRETE_OP_INSTANCES_PREDICATE.append(predicate)
            if (PREDICATE_NAME_FOR_GOAL_ABTRACT in predicate.upper()):
                     LIST_OF_GOAL_ABTRACT_PREDICATE.append(predicate)
            if (PREDICATE_NAME_FOR_HAS_INPUT_SERVICE_CLASS in predicate.upper()):
                     LIST_OF_HAS_INPUT_OP_CLASS_PREDICATE.append(predicate)
            if (PREDICATE_NAME_FOR_HAS_OUTPUT_SERVICE_CLASS in predicate.upper()):
                     LIST_OF_HAS_OUTPUT_OP_CLASS_PREDICATE.append(predicate)
            if (PREDICATE_NAME_FOR_INPUT_HAS_DATA_FORMAT in predicate.upper()):
                     LIST_OF_INPUT_DATA_FORMAT_PREDICATE.append(predicate)
            if (PREDICATE_NAME_FOR_OUTPUT_HAS_DATA_FORMAT in predicate.upper()):
                     LIST_OF_OUTPUT_DATA_FORMAT_PREDICATE.append(predicate)
            if (PREDICATE_NAME_FOR_INITIAL_FACTS in predicate.upper()):
                     LIST_OF_INITIAL_FACTS.append(predicate)
            if (PREDICATE_NAME_FOR_GOAL_FACTS in predicate.upper()):
                     LIST_OF_GOAL_FACTS.append(predicate)
            if (PREDICATE_NAME_FOR_MATCHED_I_O in predicate.upper()):
                     LIST_OF_MATCH_I_O.append(predicate)

    min_goal = 9999999999999
    for goal_predicate in LIST_OF_GOAL_ABTRACT_PREDICATE:
        goal_raw = utility.parse_goal_abtract_predicate(goal_predicate)
        if (goal_raw is not None):
            goal_in = int(goal_raw)
            if (goal_in < min_goal):
                min_goal = goal_in
    GOAL_ABTRACT_IN = min_goal

    #print str(GOAL_ABTRACT_IN)

    for occur_prediate in LIST_OF_OCCUR_PREDICATE:
        if (occur_prediate is not None):
            #print occur_prediate
            occur_service_class = utility.parse_a_occur_service_class(occur_prediate)
            if (occur_service_class is not None):
                
                # Read input,ouput - maybe not neccesary - can be REMOVED for better perform
                for has_input_predicate in LIST_OF_HAS_INPUT_OP_CLASS_PREDICATE:
                    if (has_input_predicate is not None):
                        has_input_service_class = utility.parse_a_has_input_service_class(has_input_predicate)
                        if (has_input_service_class is not None and has_input_service_class[0].upper() == occur_service_class.service_class_name.upper()):
                            occur_service_class.service_class_has_input.append(has_input_service_class[1])
                for has_output_predicate in LIST_OF_HAS_OUTPUT_OP_CLASS_PREDICATE:
                    if (has_output_predicate is not None):
                        has_output_service_class = utility.parse_a_has_output_service_class(has_output_predicate)
                        if (has_output_service_class is not None and has_output_service_class[0].upper() == occur_service_class.service_class_name.upper()):
                            occur_service_class.service_class_has_output.append(has_output_service_class[1])

                # Read possible concrete - input/output - data format to service class object
                for possible_concrete_predicate in LIST_OF_POSSIBLE_CONCRETE_OP_INSTANCES_PREDICATE:
                    if (possible_concrete_predicate is not None):
                        instance_op_object = utility.parse_a_possible_concrete_operation(possible_concrete_predicate)
                        if (instance_op_object is not None and instance_op_object.service_instance_of_class.upper() == occur_service_class.service_class_name.upper()):
                            # Read inputformat and output format for each operation
                            for input_data_format_predicate in LIST_OF_INPUT_DATA_FORMAT_PREDICATE:
                                input_data_format_object = utility.parse_a_input_data_format(input_data_format_predicate)
                                if (input_data_format_object is not None 
                                    and input_data_format_object.op_instance_name.upper() == instance_op_object.service_instance_name.upper()
                                    and input_data_format_object.resource_name in occur_service_class.service_class_has_input):
                                    instance_op_object.service_instance_input_data_format.append(input_data_format_object)

                            for output_data_format_predicate in LIST_OF_OUTPUT_DATA_FORMAT_PREDICATE:
                                output_data_format_object = utility.parse_a_output_data_format(output_data_format_predicate)
                                if (output_data_format_object is not None 
                                    and output_data_format_object.op_instance_name.upper() == instance_op_object.service_instance_name.upper()
                                    and output_data_format_object.resource_name in occur_service_class.service_class_has_output):
                                    instance_op_object.service_instance_output_data_format.append(output_data_format_object)        
                            # combine to object
                            occur_service_class.service_operation_instances.append(instance_op_object)

                # Read inputs comes from step
                for match in LIST_OF_MATCH_I_O:
                    #print match
                    if (match is not None):
                        match_data = utility.parse_a_match_predicate(match)
                        if ((match_data is not None)
                            and (match_data.match_step == occur_service_class.service_class_step)
                            and (match_data.service_class_name.strip().upper() == occur_service_class.service_class_name.upper())):
                            occur_service_class.remember_inputs_from_step.append(match_data)


                GLOBAL_ABTRACT_PLANNING.addServiceClass(occur_service_class)


        #print occur_service_class
    init_object = InitialState()  
    for init_predicate in LIST_OF_INITIAL_FACTS:
        init_asset_obj = utility.parse_a_asset_for_initial_fact(init_predicate.strip())
        init_object.assets.append(init_asset_obj)
    goal_object = GoalState()
    for goal_predicate in LIST_OF_GOAL_FACTS:
        goal_asset_obj = utility.parse_a_asset_for_goal_fact(goal_predicate.strip())
        goal_object.assets.append(goal_asset_obj)

    # Can be removed for better performance    
    GLOBAL_ABTRACT_PLANNING.update_preprocessing_service()
    #print init_object.print_data_detail()
    GLOBAL_ABTRACT_PLANNING.initial_state = init_object
    GLOBAL_ABTRACT_PLANNING.goal_state = goal_object    
    return GLOBAL_ABTRACT_PLANNING,GOAL_ABTRACT_IN


# new method servce backtracking and memorize matched data 
def find_df_mapping_plan_between_matched_thing_and_expected_execute_service(GLOBAL_ABTRACT_PLANNING,
    initial_object,
    goal_object,
    picked_conrete_operation, 
    expected_execute_concrete_operation, 
    remember_concrete_plan, 
    step,goal_in_abstract):
    
    objects_concrete_plan = []
    if (remember_concrete_plan is not None and len(remember_concrete_plan) > 0):
        for small_list in remember_concrete_plan:
            for raw_operation in small_list:
                if ("occur_concrete_operation" in raw_operation):
                    operation_name,class_name,index = utility.parse_a_occur_concrete_op_service(raw_operation)
                    check_existed = False
                    for operation in objects_concrete_plan:
                        if ((operation.service_instance_name.strip().upper() == operation_name.strip().upper())
                             and (operation.service_instance_of_class.strip().upper() == class_name.strip().upper())
                             and (index == operation.service_instance_abtract_step)
                           ):
                            check_existed = True
                            break
                    if (not check_existed):                             
                        operation = GLOBAL_ABTRACT_PLANNING.getConcreteOperationFromWorkflowByNames(class_name,operation_name)
                        objects_concrete_plan.append(operation)

    list_pair_df_in_df_out_be_converted = []
    
    if (step == 0):
        consider_service_class_execution = GLOBAL_ABTRACT_PLANNING.abtract_planning[step]
        for in_data_format_obj in expected_execute_concrete_operation.service_instance_input_data_format:
             pair_df_in_out = []
             for matched_data in consider_service_class_execution.remember_inputs_from_step:
                if ((expected_execute_concrete_operation.service_instance_of_class.strip().upper() == matched_data.service_class_name.strip().upper())
                    and (expected_execute_concrete_operation.service_instance_abtract_step == matched_data.match_step)
                    and (in_data_format_obj.resource_name.strip().upper() == matched_data.match_input.strip().upper())
                    and (matched_data.preprocessing_service_class.strip().upper() == "INITIAL_STATE")
                    ):
                        for asset in initial_object.assets:
                            if (in_data_format_obj.resource_name.strip().upper() == asset.resource_name.strip().upper()):
                                pair_df_in_out = [expected_execute_concrete_operation.service_instance_abtract_step,in_data_format_obj.resource_name,asset.resource_data_format,in_data_format_obj.resource_data_format]
                                list_pair_df_in_df_out_be_converted.append(pair_df_in_out)
    elif (step == goal_in_abstract):
        for asset in goal_object.assets:
            pair_df_in_out = []
            for operation in objects_concrete_plan:
                for output_df in operation.service_instance_output_data_format:
                    if (asset.resource_name.strip().upper() == output_df.resource_name.strip().upper()):
                        pair_df_in_out = [goal_in_abstract,asset.resource_name,output_df.resource_data_format,asset.resource_data_format]
                
                        #print pair_df_in_out
                        list_pair_df_in_df_out_be_converted.append(pair_df_in_out)
            

    else:
        consider_service_class_execution = GLOBAL_ABTRACT_PLANNING.abtract_planning[step]
        for in_data_format_obj in expected_execute_concrete_operation.service_instance_input_data_format:
            pair_df_in_out = []
            for matched_data in consider_service_class_execution.remember_inputs_from_step:
                if ((expected_execute_concrete_operation.service_instance_of_class.strip().upper() == matched_data.service_class_name.strip().upper())
                    and (expected_execute_concrete_operation.service_instance_abtract_step == matched_data.match_step)
                    and (in_data_format_obj.resource_name.strip().upper() == matched_data.match_input.strip().upper())
                    ):
                        for operation in objects_concrete_plan:
                           if ((operation.service_instance_of_class.strip().upper() == matched_data.preprocessing_service_class.strip().upper())
                               and (operation.service_instance_abtract_step == matched_data.existed_o_step - 1)
                              ):
                                 for output_df in operation.service_instance_output_data_format:
                                     if (in_data_format_obj.resource_name.strip().upper() == output_df.resource_name.strip().upper()):
                                         pair_df_in_out = [expected_execute_concrete_operation.service_instance_abtract_step,in_data_format_obj.resource_name,output_df.resource_data_format,in_data_format_obj.resource_data_format]
                                  
                                         #print pair_df_in_out
                                         list_pair_df_in_df_out_be_converted.append(pair_df_in_out)


    abtract_index = step
    
    has_plan = True
    full_plan = []


    if (abtract_index == 0):
        for pair_df_in_out in list_pair_df_in_df_out_be_converted:
            df_in = []
            df_out = []
            df_in.append(pair_df_in_out[2])
            df_out.append(pair_df_in_out[3])

            plan_data = single_run_planning_mapping_data_format(df_in, df_out, abtract_index, 0) 
            if (plan_data is not None):
                if (len(plan_data) > 0):
                    for concrete_step in plan_data:
                        if (out_predicates not in concrete_step):
                            full_plan.append(concrete_step)
                else:
                    has_plan = False
            else:
                has_plan = False
        full_plan.append(expected_execute_concrete_operation.getSignature()) 
    elif (abtract_index == goal_in_abstract):
        full_plan.append(picked_conrete_operation.getSignature())
        for pair_df_in_out in list_pair_df_in_df_out_be_converted:
            df_in = []
            df_out = []
            df_in.append(pair_df_in_out[2])
            df_out.append(pair_df_in_out[3])

            plan_data = single_run_planning_mapping_data_format(df_in, df_out, abtract_index, 0) 
            if (plan_data is not None):
                if (len(plan_data) > 0):
                    for concrete_step in plan_data:
                        if (out_predicates not in concrete_step):
                            full_plan.append(concrete_step)
                else:
                    has_plan = False
            else:
                has_plan = False    
    else:
        full_plan.append(picked_conrete_operation.getSignature())
        for pair_df_in_out in list_pair_df_in_df_out_be_converted:
            df_in = []
            df_out = []
            df_in.append(pair_df_in_out[2])
            df_out.append(pair_df_in_out[3])

            plan_data = single_run_planning_mapping_data_format(df_in, df_out, abtract_index, 0) 
            if (plan_data is not None):
                if (len(plan_data) > 0):
                    for concrete_step in plan_data:
                        if (out_predicates not in concrete_step):
                            full_plan.append(concrete_step)
                else:
                    has_plan = False
            else:
                has_plan = False
        full_plan.append(expected_execute_concrete_operation.getSignature())     
    #print full_plan
    return full_plan,has_plan     

# Serve back-tracking
def find_df_mapping_plan_ONE_service_to_ONE_service(first_considered_concrete_operation,second_considered_concrete_operation,next_step):
    abtract_index = next_step
    has_small_plan = False
    
    list_df_in = []
    for comm_df in first_considered_concrete_operation.service_instance_output_data_format:
        if (comm_df not in list_df_in):
            list_df_in.append(comm_df.resource_data_format)
    
    index_current = first_considered_concrete_operation.service_instance_abtract_step

    if (len(list_df_in) <= 0):
        list_df_in.append("data_format_unknown")

    
    index_next = second_considered_concrete_operation.service_instance_abtract_step
    if (index_next <= index_current):
        return None,False

    list_df_out = []
    for comm_df in second_considered_concrete_operation.service_instance_input_data_format:
        if (comm_df not in list_df_out):
            list_df_out.append(comm_df.resource_data_format)
    #print("--------------------------")
    #print list_df_in
    #print list_df_out
    #print("--------------------------")
    if (len(list_df_out) <= 0):
        list_df_in.append("data_format_unknown")
    
    plan = []
    plan.append(first_considered_concrete_operation.getSignature())

    plan_data = single_run_planning_mapping_data_format(list_df_in, list_df_out, abtract_index, 0) 
    #print "-----"
    #print list_df_in
    #print list_df_out
    if (plan_data is not None):
        has_small_plan = True
        if (len(plan_data) > 0):
            for concrete_step in plan_data:
                if (out_predicates not in concrete_step):
                    plan.append(concrete_step)
    plan.append(second_considered_concrete_operation.getSignature()) 
    return plan,has_small_plan

def find_df_mapping_plan_Initial_to_ONE_service_in_first_service_class(initial_state_obj,consider_concrete_operation_in_first_group):
    abtract_index = 0
    list_of_init_to_first_planning = []
    # Between INITAL State -> The first service; (0,0) (0,1) (0,2) means in order to run service 0
    # Create rules for initial df
    has_small_plan = False
    list_df_in = []
    for comm_df in initial_state_obj.assets:
        if (comm_df not in list_df_in):
           list_df_in.append(comm_df.resource_data_format)
    
    if (len(list_df_in) <= 0):
        list_df_in.append("data_format_unknown")   
    list_df_out = []
    plan = []
    for comm_df in consider_concrete_operation_in_first_group.service_instance_input_data_format:
        if (comm_df not in list_df_out):
            list_df_out.append(comm_df.resource_data_format)
    #print("--------------------------")
    #print list_df_in
    #print list_df_out
    #print("--------------------------")
    if (len(list_df_out) <= 0):
        list_df_out.append("data_format_unknown")

    plan_data = single_run_planning_mapping_data_format(list_df_in, list_df_out, abtract_index, 0)          

    if (plan_data is not None):
        has_small_plan = True
        if (len(plan_data) > 0):
            for concrete_step in plan_data:
                if (out_predicates not in concrete_step):
                    plan.append(concrete_step)
        plan.append(consider_concrete_operation_in_first_group.getSignature()) 

    return plan,has_small_plan

def find_df_mapping_plan_ONE_of_last_service_to_GOAL(goal_state_obj,consider_concrete_operation_in_last_group,last_index):
    abtract_index = last_index
    
    list_df_out = []
    for comm_df in goal_state_obj.assets:
        if (comm_df not in list_df_out):
            list_df_out.append(comm_df.resource_data_format)

    if (len(list_df_out) <= 0):
            list_df_out.append("data_format_unknown")

    is_done = False
    
    list_df_in = []
    plan = []
    plan.append(consider_concrete_operation_in_last_group.getSignature())
    for comm_df in consider_concrete_operation_in_last_group.service_instance_output_data_format:
        if (comm_df not in list_df_in):
            list_df_in.append(comm_df.resource_data_format)

    if (len(list_df_in) <= 0):
        list_df_in.append("data_format_unknown")

    last_part_plan_data = single_run_planning_mapping_data_format(list_df_in, list_df_out, abtract_index, 0)          

    #print("--------------------------")
    #print list_df_in
    #print list_df_out
    #print("--------------------------")
    if (last_part_plan_data is not None):
        
        is_done = True
        if (len(last_part_plan_data) > 0):
            for concrete_step in last_part_plan_data:
                if (out_predicates not in concrete_step):
                    plan.append(concrete_step)
       
    return plan,is_done
# remember_concrete_plan is list of list (easy to remove)
def back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
                            initial_state_obj,    
                            consider_serivce_current_step,
                            goal_state_obj,
                            current_step,
                            remember_concrete_plan,
                            remember_picked_services,
                            goal_in_abstract,
                            trash):
    #print remember_picked_services
    if (current_step == 0): # means from initial state to first service
        # Build list of input data format
        co_the_qua_cau = False
        is_able_to_find_a_potential_service = False
        for service_operation in GLOBAL_ABTRACT_PLANNING.abtract_planning[current_step].service_operation_instances:
            if (service_operation not in trash[current_step]):
                is_able_to_find_a_potential_service = True
                part_1_plan,has_plan = find_df_mapping_plan_between_matched_thing_and_expected_execute_service(GLOBAL_ABTRACT_PLANNING,initial_state_obj,goal_state_obj,None,service_operation,remember_concrete_plan,current_step,goal_in_abstract)
                #part_1_plan,has_plan = find_df_mapping_plan_Initial_to_ONE_service_in_first_service_class(initial_state_obj,service_operation)
                if (has_plan):
                    co_the_qua_cau = True
                    remember_concrete_plan.append(part_1_plan)
                    next_step = current_step + 1
                    flag_initial_service_op = Service_Instance("INITIAL_STATE", "NULL",-1)
                    remember_picked_services.append(flag_initial_service_op)
                    # print remember_concrete_planc
                    return back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
                                                    initial_state_obj,    
                                                    service_operation,
                                                    goal_state_obj,
                                                    next_step,
                                                    remember_concrete_plan,
                                                    remember_picked_services,
                                                    goal_in_abstract,
                                                    trash)
                else:
                    trash[current_step].append(service_operation)

        if (not is_able_to_find_a_potential_service): # Doan nay la de thoat
            print("L Cannot find a picked serve in step %s" %(str(current_step)))
            return None,False
        if (not co_the_qua_cau): # Doan nay KO can back-tracking = Vi la step 0 nen ko the back-tracking

            print("KHONG THE TIM DUOC DUOC DE MOVE forward -> step %s" %(str(current_step)))
            return None,False          
    elif (current_step == goal_in_abstract):
        # Build list of input data format
        co_the_qua_cau = False

        
        last_part_plan,has_plan =  find_df_mapping_plan_between_matched_thing_and_expected_execute_service(GLOBAL_ABTRACT_PLANNING,initial_state_obj,goal_state_obj,consider_serivce_current_step,None,remember_concrete_plan,current_step,goal_in_abstract)
        #last_part_plan,has_plan = find_df_mapping_plan_ONE_of_last_service_to_GOAL(goal_state_obj,consider_serivce_current_step,current_step)
        
        if (has_plan):
            co_the_qua_cau = True
            remember_concrete_plan.append(last_part_plan)
            return remember_concrete_plan,True
        else: 
            #Back-Tracking
            previous_step = current_step - 1 
            trash[previous_step].append(consider_serivce_current_step)
            # Back-Tracking FROm service
            back_tracking_concrete_service = remember_picked_services.pop()
            remember_concrete_plan.pop()
            print("--Back-Track at Step %s" %(str(current_step)))
            return back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
                                            initial_state_obj,    
                                            back_tracking_concrete_service,
                                            goal_state_obj,
                                            previous_step,
                                            remember_concrete_plan,
                                            remember_picked_services,
                                            goal_in_abstract,
                                            trash)
    else:
        # print "Normal step %s" %(str(current_step))
        # Build list of input data format
        co_the_qua_cau = False
        is_able_to_find_a_potential_service = False
        for service_operation in GLOBAL_ABTRACT_PLANNING.abtract_planning[current_step].service_operation_instances:
            if (service_operation not in trash[current_step]):
                
                is_able_to_find_a_potential_service = True
                part_n_plan,has_plan = find_df_mapping_plan_between_matched_thing_and_expected_execute_service(GLOBAL_ABTRACT_PLANNING,initial_state_obj,goal_state_obj,consider_serivce_current_step,service_operation,remember_concrete_plan,current_step,goal_in_abstract)
                #part_n_plan,has_plan = find_df_mapping_plan_ONE_service_to_ONE_service(consider_serivce_current_step,service_operation,current_step)
                if (has_plan):
                    co_the_qua_cau = True
                    remember_concrete_plan.append(part_n_plan)
                    next_step = current_step + 1
                    remember_picked_services.append(consider_serivce_current_step)
                    return back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
                                                    initial_state_obj,    
                                                    service_operation,
                                                    goal_state_obj,
                                                    next_step,
                                                    remember_concrete_plan,
                                                    remember_picked_services,
                                                    goal_in_abstract,
                                                    trash)
                else:
                    trash[current_step].append(service_operation)

        if (not is_able_to_find_a_potential_service):
            #Back-Tracking
            
            previous_step = current_step - 1
            trash[previous_step].append(consider_serivce_current_step)
            #trash[current_step] = [] # Co nen ko 
            # Back-Tracking from service
            back_tracking_concrete_service = remember_picked_services.pop()
            #if (not remember_picked_services or "INITIAL_STATE" not in back_tracking_concrete_service.service_instance_name):
            remember_concrete_plan.pop()
            print("Da Back-Track vi KHONG TIM THAY SERVICE TOT at Step %s" %(str(current_step)))
            return back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
                                            initial_state_obj,    
                                            back_tracking_concrete_service,
                                            goal_state_obj,
                                            previous_step,
                                            remember_concrete_plan,
                                            remember_picked_services,
                                            goal_in_abstract,
                                            trash)
            #else:
            #    remember_concrete_plan.pop()
            #    return back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
            #                                    initial_state_obj,    
            #                                    back_tracking_concrete_service,
            #                                    goal_state_obj,
            #                                    previous_step,
            #                                    remember_concrete_plan,
            #                                    remember_picked_services,
            #                                    goal_in_abstract,
            #                                    trash)

        if (not co_the_qua_cau): 
            #Back-Tracking
            previous_step = current_step - 1 
            trash[previous_step].append(consider_serivce_current_step)
            back_tracking_concrete_service = remember_picked_services.pop()
            remember_concrete_plan.pop()
            print("Da Back-Track vi KO TIM THAY PATH at Step %s" %(str(current_step)))
            return back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
                                            initial_state_obj,    
                                            back_tracking_concrete_service,
                                            goal_state_obj,
                                            previous_step,
                                            remember_concrete_plan,
                                            remember_picked_services,
                                            goal_in_abstract,
                                            trash)



         
def find_df_mapping_plan_service_to_service(list_of_concrete_services_current_step,list_of_concrete_services_next_step,next_step):
    abtract_index = next_step
    list_of_service_to_service_planning = []
    is_moving_forward = False
    LIST_GOOD_CONCRETE_SERVICES = []
    for current_service_concrete in list_of_concrete_services_current_step:
        list_df_in = []
        for comm_df in current_service_concrete.service_instance_output_data_format:
            if (comm_df not in list_df_in):
                list_df_in.append(comm_df.resource_data_format)
        
        index_current = current_service_concrete.service_instance_abtract_step

        if (len(list_df_in) <= 0):
            list_df_in.append("data_format_unknown")

        for next_service_concrete in list_of_concrete_services_next_step:
            index_next = next_service_concrete.service_instance_abtract_step
            if (index_next <= index_current):
                continue
            list_df_out = []
            for comm_df in next_service_concrete.service_instance_input_data_format:
                if (comm_df not in list_df_out):
                    list_df_out.append(comm_df.resource_data_format)

            if (len(list_df_out) <= 0):
                list_df_in.append("data_format_unknown")
            
            plan = []
            plan.append(current_service_concrete.getSignature())

            plan_data = single_run_planning_mapping_data_format(list_df_in, list_df_out, abtract_index, 0) 

            if (plan_data is not None):
                is_moving_forward = True
                if (len(plan_data) > 0):
                    for concrete_step in plan_data:
                        if (out_predicates not in concrete_step):
                            plan.append(concrete_step)
            plan.append(next_service_concrete.getSignature()) 

            if (next_service_concrete not in LIST_GOOD_CONCRETE_SERVICES):
                LIST_GOOD_CONCRETE_SERVICES.append(next_service_concrete)      
            list_of_service_to_service_planning.append(plan)

    return list_of_service_to_service_planning,is_moving_forward,LIST_GOOD_CONCRETE_SERVICES


def find_df_mapping_plan_Initial_to_first_service(initial_state_obj,LIST_GOOD_CONCRETE_FIRST_STEP):
    abtract_index = 0
    list_of_init_to_first_planning = []
    # Between INITAL State -> The first service; (0,0) (0,1) (0,2) means in order to run service 0
    # Create rules for initial df
    list_df_in = []
    for comm_df in initial_state_obj.assets:
        if (comm_df not in list_df_in):
           list_df_in.append(comm_df.resource_data_format)
    
    if (len(list_df_in) <= 0):
        list_df_in.append("data_format_unknown")

    list_of_concrete_services = LIST_GOOD_CONCRETE_FIRST_STEP
    is_move_forward = False
    LIST_GOOD_CONCRETE_SERVICES = []
    for service_concrete in list_of_concrete_services:
        list_df_out = []
        plan = []
        for comm_df in service_concrete.service_instance_input_data_format:
            if (comm_df not in list_df_out):
                list_df_out.append(comm_df.resource_data_format)

        if (len(list_df_out) <= 0):
            list_df_out.append("data_format_unknown")

        part_1_plan_data = single_run_planning_mapping_data_format(list_df_in, list_df_out, abtract_index, 0)          

        if (part_1_plan_data is not None):
            is_move_forward = True
            if (len(part_1_plan_data) > 0):
                for concrete_step in part_1_plan_data:
                    if (out_predicates not in concrete_step):
                        plan.append(concrete_step)
            plan.append(service_concrete.getSignature()) 
            if (service_concrete not in LIST_GOOD_CONCRETE_SERVICES):
                LIST_GOOD_CONCRETE_SERVICES.append(service_concrete)      
            list_of_init_to_first_planning.append(plan)
    return list_of_init_to_first_planning,is_move_forward,LIST_GOOD_CONCRETE_SERVICES
def find_df_mapping_plan_last_service_to_Goal(goal_state_obj,LIST_GOOD_CONCRETE_LAST_STEP,GOAL_ABTRACT_IN):
    abtract_index = GOAL_ABTRACT_IN
    list_of_last_to_goal_planning = []
    # Between INITAL State -> The first service; (0,0) (0,1) (0,2) means in order to run service 0
    # Create rules for initial df

    list_df_out = []
    for comm_df in goal_state_obj.assets:
        if (comm_df not in list_df_out):
            list_df_out.append(comm_df.resource_data_format)

    if (len(list_df_out) <= 0):
            list_df_out.append("data_format_unknown")

    list_of_concrete_services = LIST_GOOD_CONCRETE_LAST_STEP
    is_done = False
    for service_concrete in list_of_concrete_services:
        list_df_in = []
        plan = []
        plan.append(service_concrete.getSignature())
        for comm_df in service_concrete.service_instance_output_data_format:
            if (comm_df not in list_df_in):
                list_df_in.append(comm_df.resource_data_format)

        if (len(list_df_in) <= 0):
            list_df_in.append("data_format_unknown")
        
        #print list_df_out

        last_part_plan_data = single_run_planning_mapping_data_format(list_df_in, list_df_out, abtract_index, 0)          

        if (last_part_plan_data is not None):
            is_done = True
            if (len(last_part_plan_data) > 0):
                for concrete_step in last_part_plan_data:
                    if (out_predicates not in concrete_step):
                        plan.append(concrete_step)
            list_of_last_to_goal_planning.append(plan)
    return list_of_last_to_goal_planning,is_done



def get_head_map_concrete_op(services_sequence,index):
    lst_real = []
    #print services_sequence
    #print index
    for service_text in services_sequence:
        if (PREDICATE_REAL_CONCRETE_OPERATION_INSTANCE in service_text.strip().upper()
            and str(index) in service_text.strip().upper()):
            return service_text
    return None
def get_tail_map_concrete_op(services_sequence,index):
    lst_real = []
    print(services_sequence)
    for service_text in services_sequence:
        if (PREDICATE_REAL_CONCRETE_OPERATION_INSTANCE in service_text.strip().upper()
            and str(index+1) in service_text.strip().upper()):
            return service_text
    return None
def procecure_abtract_planning():
    planning_data = solve_abtract_level(1,
    os.path.join(FULL_PATH_ABTRACT_PLANNING_ENGINE_MODEL,configuration.CONFIGURATION_DATA['abtract_level_planning_asp_file']),
    os.path.join(FULL_PATH_ABTRACT_PLANNING_ENGINE_MODEL,configuration.CONFIGURATION_DATA['ontology_web_serivce_asp']),
    os.path.join(FULL_PATH_PLANNING_STATES_FOLDER,configuration.CONFIGURATION_DATA['initial_state_asp_file']),
    os.path.join(FULL_PATH_PLANNING_STATES_FOLDER,configuration.CONFIGURATION_DATA['goal_state_asp_file']),
    os.path.join(FULL_PATH_PLANNING_PREFERENCE_FOLDER,configuration.CONFIGURATION_DATA['planning_configuration_asp_file']),
    os.path.join(FULL_PATH_PLANNING_PREFERENCE_FOLDER,configuration.CONFIGURATION_DATA['planning_preference_asp_file']),
    os.path.join(FULL_PATH_PLANNING_PREFERENCE_FOLDER,configuration.CONFIGURATION_DATA['planning_qos_asp_file']))

    if (planning_data is None or len(planning_data) <= 0):
        print(utility.return_response_error(404,"error","NO_PLAN"))
        sys.exit()

    # Select only one workflow to follow === Cai nay can xem xet lai
    consider_planning_data_json = planning_data[0]
    return consider_planning_data_json

def procedure_concrete_planning(mt):
    method = mt
    #####Phase 1 : Reading Abtract data level
    consider_planning_data_json = procecure_abtract_planning()
    GLOBAL_ABTRACT_PLANNING,GOAL_ABTRACT_IN = read_data_from_abstract_planning(consider_planning_data_json)
    GLOBAL_ABTRACT_PLANNING.reorderSevices()
    GLOBAL_ABTRACT_PLANNING.print_workflow("with_match_data")
    INITIAL_STATE_OBJ = GLOBAL_ABTRACT_PLANNING.initial_state
    GOAL_STATE_OBJ = GLOBAL_ABTRACT_PLANNING.goal_state
    # Do loop planning + backtracking algorithm + replanning concrete level
   
    # Cach 1 : Straigh-Forward 
    if ("BACK-FORWARD" in method.strip().upper()):
        abtract_index = 0
        DOMAIN_CONCRETE_PLANS = []

        FIRST_PART_CONCRETE_PLANS, is_init_to_first_service_worked,LIST_GOOD_SERVICES_FIST_STEP = find_df_mapping_plan_Initial_to_first_service(INITIAL_STATE_OBJ,GLOBAL_ABTRACT_PLANNING.abtract_planning[0].service_operation_instances)
        if (is_init_to_first_service_worked):
            DOMAIN_CONCRETE_PLANS.append(FIRST_PART_CONCRETE_PLANS)
            is_continue_services_worked = False

            lst_good = LIST_GOOD_SERVICES_FIST_STEP
            for index in range(1,GOAL_ABTRACT_IN):
                list_concrete_service_1 = lst_good
                list_concrete_service_2 = GLOBAL_ABTRACT_PLANNING.abtract_planning[index].service_operation_instances
                NEXT_CONCRETE_PLANS, is_s_to_s_worked, lst_good = find_df_mapping_plan_service_to_service(list_concrete_service_1,list_concrete_service_2,index)

                if (is_s_to_s_worked):
                    DOMAIN_CONCRETE_PLANS.append(NEXT_CONCRETE_PLANS)
                else:
                    is_continue_services_worked = False
                    print("CANNOT MOVE FORWARD - BREAK AT %s" %(str(index)))
                    return None

            is_continue_services_worked = True

            #print lst_good
            if (is_continue_services_worked):
                LAST_PART_CONCRETE_PLANS, is_completed = find_df_mapping_plan_last_service_to_Goal(GOAL_STATE_OBJ,
                                                                                        lst_good, # Se lai doi
                                                                                        GOAL_ABTRACT_IN)
                if (is_completed):
                    DOMAIN_CONCRETE_PLANS.append(LAST_PART_CONCRETE_PLANS)
                else:
                    print("CANNOT COMPLETE")
                    return None
        else:
            print("CANNOT MOVE FROM INITIAL to FIRST SERVICE")
            return None

        #print DOMAIN_CONCRETE_PLANS
        
        #- BACK-FORWARD using DFS
        FINAL_CONCRETE_PLAN_S = []
        FINAL_CONCRETE_PLAN = [] # Stack

        abtract_index = GOAL_ABTRACT_IN
        while abtract_index >= 0:
            if (abtract_index == GOAL_ABTRACT_IN):
                services_sequence_cols = DOMAIN_CONCRETE_PLANS[abtract_index]
                # Picked random sequence of mini plan
                randomIndex = random.randint(0,len(services_sequence_cols)-1)
                picked_services_sequence = services_sequence_cols[randomIndex]
                for i in range(len(picked_services_sequence)-1,-1,-1):
                    service_op = picked_services_sequence[i]
                    if (service_op not in FINAL_CONCRETE_PLAN):
                        FINAL_CONCRETE_PLAN.append(service_op)
                righ_concrete_op_need_map_text = get_head_map_concrete_op(picked_services_sequence,abtract_index-1)
                
                if (righ_concrete_op_need_map_text is None):
                    print("Unexpected error")
                    return None
                
            else:
                services_sequence_cols = DOMAIN_CONCRETE_PLANS[abtract_index]
                candidate_services_sequenc_cols = []
                for service_sequence in services_sequence_cols:
                    if (righ_concrete_op_need_map_text in service_sequence):
                        candidate_services_sequenc_cols.append(service_sequence)
                # Picked random sequence of mini plan
                randomIndex = random.randint(0,len(candidate_services_sequenc_cols)-1)
                picked_services_sequence = candidate_services_sequenc_cols[randomIndex]
                for i in range(len(picked_services_sequence)-1,-1,-1):
                    service_op = picked_services_sequence[i]
                    if (service_op not in FINAL_CONCRETE_PLAN):
                        FINAL_CONCRETE_PLAN.append(service_op)
                if (index > 0):
                    righ_concrete_op_need_map_text = get_head_map_concrete_op(picked_services_sequence,abtract_index-1)

                   
            abtract_index = abtract_index - 1            
        FINAL_CONCRETE_PLAN.reverse()
        return FINAL_CONCRETE_PLAN
            
    elif ("BACK-TRACKING" in method.strip().upper()):
        # Cach 2 : Back-Tracking (better)
        FINAL_CONCRETE_PLAN = []
        consider_serivce_current_step = None
        remember_concrete_plan = []
        remember_picked_services = []
        trash = []
        for i in range (0,GOAL_ABTRACT_IN+1):
            trash.append([])
        plan,is_ok = back_tracking_algorithm(GLOBAL_ABTRACT_PLANNING,
                                             INITIAL_STATE_OBJ,    
                                             consider_serivce_current_step,
                                             GOAL_STATE_OBJ,
                                             0,
                                             remember_concrete_plan,
                                             remember_picked_services,
                                             GOAL_ABTRACT_IN,
                                             trash)

        if (is_ok and plan is not None):
            for service_cols in plan:
                for service_op in service_cols:
                    if (service_op not in FINAL_CONCRETE_PLAN):
                        FINAL_CONCRETE_PLAN.append(service_op)
            
            return FINAL_CONCRETE_PLAN
    else:
        print("unspport")