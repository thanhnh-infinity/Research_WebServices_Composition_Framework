import subprocess
import json
import sys
import os

def run_CURL_planning_engine_service(planning_service_url,data):
    
    #p = subprocess.Popen(['curl -X POST', planning_service_url,'-H "content-type:application/json" -d',data], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(['curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d {}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print(err)
    return out

def expect_number_step(input_resource_string,output_resource_string):
    DEFAULT_STEP = 8
    # Step 2.3 : Write Original Workflow Objet to python file
    #fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"original_workflow.py"),"wb")
    #==========================================================================================
    if (("resource_speciesTree" in output_resource_string) and ("resource_speciesTree_with_BranchLengths" not in output_resource_string)):
        if ("resource_FreeText" in input_resource_string):
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_8.lp")
        elif ("resource_WebURL" in input_resource_string):  
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_8.lp")
        elif ("resource_SetOfGeneStrings" in input_resource_string):
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_10.lp")
        else:
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_11.lp")    
    elif ("resource_reconcileTree" in output_resource_string):
        DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")
    elif ("resource_AreSameTree" in output_resource_string):
        DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_11.lp")
    elif (("resource_speciesTree_with_BranchLengths" in output_resource_string) or ("resource_metadata_tree_scaling" in output_resource_string)):
        if ("resource_FreeText" in input_resource_string):
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_11.lp")
        elif ("resource_WebURL" in input_resource_string):  
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_11.lp")
        elif ("resource_SetOfGeneStrings" in input_resource_string):
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")
        else:
          DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_13.lp")

        if (("resource_speciesTree_with_BranchLengths" in output_resource_string) and ("resource_metadata_tree_scaling" in output_resource_string)):
            if ("resource_FreeText" in input_resource_string):
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_10.lp")
            elif ("resource_WebURL" in input_resource_string):  
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_10.lp")
            elif ("resource_SetOfGeneStrings" in input_resource_string):
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")
            else:
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_13.lp")        
    else:
        DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_20.lp")

    return DEFAULT_STEP    