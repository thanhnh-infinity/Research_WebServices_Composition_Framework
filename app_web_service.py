import cherrypy
from OWL_Ontology_App import OWLEngine
import composite_response
import composite_parser
import planning_algorithms
import json
import os
import sys
import time
import subprocess
import shutil
import datetime
from pprint import pprint
import requests
import ultility

HOST_PLANNING_ENGINE_URL_COMPOSITE = "http://127.0.0.1:8000/planningEngine/generateWorkflow"
PORT = 8000

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET,POST,OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Headers"] = "X-Auth-Token,Content-Type,Accept,Content-Length"

def return_response_error(code, type, mess, format="JSON"):
    if (format == "JSON"):
        cherrypy.response.headers['Content-Type'] = "application/json"
        cherrypy.response.headers['Retry-After'] = 60
        cherrypy.response.status = code
        message = {type: mess}
        return json.dumps(message)
    else:
        return "Not support yet"
def return_success_get(data):
    cherrypy.response.headers['Content-Type'] = "application/json"
    cherrypy.response.headers['Retry-After'] = 60
    cherrypy.response.status = 200
    return json.dumps(data, indent=4)

def return_success_get_json(data):
    cherrypy.response.headers['Content-Type'] = "application/json"
    cherrypy.response.headers['Retry-After'] = 60
    cherrypy.response.status = 200
    return data

class Interact_Planning_Engine(object):
    _cp_config = {
        'tools.sessions.on': True,
        'tools.sessions.httponly': True
    }

    FULL_PATH_PLANNING_ENGINE_MODEL = os.path.join(os.getcwd(), "ASP_Planning","planning")
    FULL_PATH_PLANNING_STATES_FOLDER = os.path.join(os.getcwd(),"ASP_Planning" ,"states")
    DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","default.lp")
    #FULL_PATH_CLINGO_EXECUTATBLE = "clingo-python"
    FULL_PATH_CLINGCON_EXECUTATBLE = "clingcon-3.3.0"
    FULL_PATH_CLINGO_EXECUTATBLE = "clingo"
   

    # Function
    def prepareDistinguish_Input_Output_Folder_PerEachProcess(self):
        current = time.time()
        current = "R" + str(current)
        states_file_directory = os.path.join(os.getcwd(),"ASP_Planning","states","%s" % str(current))
        if not os.path.exists(states_file_directory):
            os.makedirs(states_file_directory)
        return str(current)

    def index(self):
        return "Planning Engine Invoking"

    # Use Case 1 : Generate Species Tree from Raw Text    
    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]},"models":{"number":1,"engine":1}}'

    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]},"models":{"number":5,"engine":2}}'

    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]},"models":{"number":1,"engine":3}}'

    # Use Case 2 : Generate Gene Tree and Species tree from set of gene names
    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"models":{"number":1,"engine":1},"request_parameters":{"input":[{"name" : "Set of gene names","resource_ontology_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings","resource_ontology_id":"resource_SetOfGeneStrings","resource_data_format_id":"list_of_strings","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#list_of_strings"}],"output":[{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"},{"name" : "Gene Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree","resource_ontology_id" : "resource_geneTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]}}'

    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"models":{"number":2,"engine":2},"request_parameters":{"input":[{"name" : "Set of gene names","resource_ontology_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings","resource_ontology_id":"resource_SetOfGeneStrings","resource_data_format_id":"list_of_strings","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#list_of_strings"}],"output":[{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"},{"name" : "Gene Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree","resource_ontology_id" : "resource_geneTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]}}'

    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"models":{"number":1,"engine":3},"request_parameters":{"input":[{"name" : "Set of gene names","resource_ontology_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings","resource_ontology_id":"resource_SetOfGeneStrings","resource_data_format_id":"list_of_strings","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#list_of_strings"}],"output":[{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"},{"name" : "Gene Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree","resource_ontology_id" : "resource_geneTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]}}'


    # Use Case 3 : Generate Reconciliation Tree
    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"models":{"number":1,"engine":1},"request_parameters":{"input":[{"name" : "Set of gene names","resource_ontology_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings","resource_ontology_id":"resource_SetOfGeneStrings","resource_data_format_id":"list_of_strings","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#list_of_strings"}],"output":[{"name" : "Reconciliation Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_reconcileTree","resource_ontology_id" : "resource_reconcileTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]}}'

    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"models":{"number":4,"engine":2},"request_parameters":{"input":[{"name" : "Set of gene names","resource_ontology_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings","resource_ontology_id":"resource_SetOfGeneStrings","resource_data_format_id":"list_of_strings","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#list_of_strings"}],"output":[{"name" : "Reconciliation Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_reconcileTree","resource_ontology_id" : "resource_reconcileTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]}}'

    #curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d '{"models":{"number":1,"engine":3},"request_parameters":{"input":[{"name" : "Set of gene names","resource_ontology_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings","resource_ontology_id":"resource_SetOfGeneStrings","resource_data_format_id":"list_of_strings","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#list_of_strings"}],"output":[{"name" : "Reconciliation Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_reconcileTree","resource_ontology_id" : "resource_reconcileTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}]}}'
    
    # Generate workflow
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def generateWorkflow(self,**request_data):
        CORS()
        if cherrypy.request.method == "OPTIONS":
             return ""
        input_json = cherrypy.request.json

        #Format JSON input example:
        '''
        input_json =  {
            "request_parameters" : {
                "input" : [
                    {
                        "name" : "Set of Gene Names",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings",
                        "resource_ontology_id" : "resource_SetOfGeneStrings",
                        "resource_data_format_id":"list_of_strings",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#list_of_strings"
                    }
                ],
                "output" : [
                    {
                        "name" : "Reconciliation Tree",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_reconcileTree",
                        "resource_ontology_id" : "resource_reconcileTree",
                        "resource_data_format_id":"newickTree",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"
                   }
                ],
                "avoidance" : ["phylotastic_GetPhylogeneticTree_Phylomatic_POST","phylotastic_GetPhylogeneticTree_Phylomatic_GET"],
                "inclusion" : ["phylotastic_GetPhylogeneticTree_OT_POST"],
                "insertion" : []
            },
            "models":{
                "number":1,
                "engine":2
            }
        }

        input_json =  {
            "request_parameters" : {
                "input" : [
                    {
                        "name" : "A Raw Text mixes many types of encoding",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText",
                        "resource_ontology_id" : "resource_FreeText",
                        "resource_data_format_id":"raw_text",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"
                    }
                ],
                "output" : [
                    {
                        "name" : "Species Tree",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree",
                        "resource_ontology_id" : "resource_speciesTree",
                        "resource_data_format_id":"newickTree",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"
                   }
                ],
                "avoidance" : ["phylotastic_GetPhylogeneticTree_Phylomatic_POST","phylotastic_GetPhylogeneticTree_Phylomatic_GET"],
                "inclusion" : ["phylotastic_GetPhylogeneticTree_OT_POST"],
                "insertion" : []
            },
            "models":{
                "number":1,
                "engine":1
            }
        }
        '''
        try:
            request_parameters = input_json['request_parameters'];
        except:
            return return_response_error(400,"error","Missing input","JSON")

        if ((request_parameters is None) or (request_parameters == '')):
            return return_response_error(400,"error","Missing params","JSON")
       
        try:
            
            models = input_json['models']
            number_of_models = models["number"]
            engine = models["engine"]
            
        except Exception as err:
            print(err)
            number_of_models = 1
            engine = 1
  
        # Step 2 : parser input/output/avoidance,inclusion,insertion
        json_input_re = request_parameters["input"]
        if ((json_input_re is None) or (json_input_re == '')):
            return return_response_error(400,"error","Missing input","JSON")
        if (len(json_input_re) <= 0):
            return return_response_error(400,"error","Empty Input","JSON")

        json_output_re = request_parameters["output"]
        if ((json_output_re is None) or (json_output_re == '')):
            return return_response_error(400,"error","Missing output","JSON")
        if (len(json_output_re) <= 0):
            return return_response_error(400,"error","Empty Output","JSON")

        isAvoidance = True
        isInclusion = True
        isInsertion = True
        
        json_avoidance_re = request_parameters["avoidance"]
        if ((json_avoidance_re is None) or (json_avoidance_re == '')):
            print("Planning -- No avoidance request")
            isAvoidance = False
        if (len(json_avoidance_re) <= 0):
            print("Planning -- No avoidance request")
            isAvoidance = False

        json_inclusion_re = request_parameters["inclusion"]
        if ((json_inclusion_re is None) or (json_inclusion_re == '')):
            print("Planning -- No inclusion request")
            isInclusion = False
        if (len(json_inclusion_re) <= 0):
            print("Planning --  No inclusion request")
            isInclusion = False

        json_insertion_re = request_parameters["insertion"]
        if ((json_insertion_re is None) or (json_insertion_re == '')):
            print("Planning -- No insertion request")
            isInsertion = False
        if (len(json_insertion_re) <= 0):
            print("Planning -- No insertion request")
            isInsertion = False    

        # Step 2.1 : Write input/output to ASP files
        folder_name = self.prepareDistinguish_Input_Output_Folder_PerEachProcess()
        #print folder_name
        fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),"wb")
        print("---Create Initial State--")
        fo.write("%------------------------------------------------------------------------\n")
        fo.write("% INPUT PART : Initial State\n")
        fo.write("%------------------------------------------------------------------------\n")
        input_resource_string = ""
        for i in range(0,len(json_input_re)):
            input_resource_string = input_resource_string + " | " + str(json_input_re[i]["resource_ontology_id"])
            fo.write("initially(%s,%s).\n" %(str(json_input_re[i]["resource_ontology_id"]),str(json_input_re[i]["resource_data_format_id"])))
        fo.write("%------------------------------------------------------------------------\n")
        fo.close()

        fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"), "wb")
        print("---Create Goal State--")
        fo.write("%------------------------------------------------------------------------\n")
        fo.write("% GOAL State\n")
        fo.write("%------------------------------------------------------------------------\n")
        content = ""
        max_content = ""
        output_resource_string = ""
        for i in range(0,len(json_output_re)):
            output_resource_string = output_resource_string + " | " + str(json_output_re[i]["resource_ontology_id"])
            fo.write("finally(%s, %s).\n" %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"])))
            # Cho nay can lam phuc tap hon nua
            if (len(json_output_re) > 1):
                content += "exists(%s,%s,I%s),step(I%s)," %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"]),str(i),str(i))
                if (i == 0):
                    max_content = "I%s" %(str(i))
                else:
                    max_content += ";I%s" %(str(i))    
            if (len(json_output_re) == 1):
                content += "exists(%s,%s,I), " %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"]))

        if (len(json_output_re) > 1):        
            fo.write("goal(M) :- %s M = #max{%s}.\n" %(content,max_content))
        else:
            fo.write("goal(I) :- %s step(I).\n" %(content)) 

        #fo.write("goal(I) :- %s step(I).\n" %(content))
        fo.write("%------------------------------------------------------------------------\n")
        fo.close()

        # Step 2.2 : Write avoidance/inclusion/insertion to ASP files
        fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"composite_preference.lp"),"wb")
        print("---Create Preferences and Constraint From--")
        if (isAvoidance):
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% AVOIDANCE  SERVICES \n")
            fo.write("%------------------------------------------------------------------------\n")
            for i in range(0,len(json_avoidance_re)):
                fo.write("do_not_use_operation(%s).\n" %(str(json_avoidance_re[i])))
            fo.write("%------------------------------------------------------------------------\n")
        if (isInclusion):
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% INCLUSION  SERVICES \n")
            fo.write("%------------------------------------------------------------------------\n")
            for i in range(0,len(json_inclusion_re)):
                fo.write("used_operation(%s).\n" %(str(json_inclusion_re[i])))
            fo.write("%------------------------------------------------------------------------\n")
        if (isInsertion):
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% INSERTION  SERVICES \n")
            fo.write("%------------------------------------------------------------------------\n")  
            fo.write("%------------------------------------------------------------------------\n")
        fo.close()

        #=========================================================================================================
        '''
        if (("resource_speciesTree" in output_resource_string) and ("resource_speciesTree_with_BranchLengths" not in output_resource_string)):
            if ("resource_FreeText" in input_resource_string):
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_8.lp")
            elif ("resource_WebURL" in input_resource_string):  
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_8.lp")
            elif ("resource_SetOfGeneStrings" in input_resource_string):    
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_11.lp")
            else:
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")    
        elif ("resource_reconcileTree" in output_resource_string):
            DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")
        elif (("resource_speciesTree_with_BranchLengths" in output_resource_string) or ("resource_metadata_tree_scaling" in output_resource_string)):
            if ("resource_FreeText" in input_resource_string):
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_9.lp")
            elif ("resource_WebURL" in input_resource_string):  
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_9.lp")
            elif ("resource_SetOfGeneStrings" in input_resource_string):
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_10.lp")
            else:
              DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_11.lp")
            if (("resource_speciesTree_with_BranchLengths" in output_resource_string) and ("resource_metadata_tree_scaling" in output_resource_string)):
                if ("resource_FreeText" in input_resource_string):
                  DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_10.lp")
                elif ("resource_WebURL" in input_resource_string):  
                  DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_10.lp")
                elif ("resource_SetOfGeneStrings" in input_resource_string):
                  DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_11.lp")
                else:
                  DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")       
        else:
            DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")       
        '''
        DEFAULT_STEP = ultility.expect_number_step(input_resource_string,output_resource_string)         
        # Step 3 : Run planning
        # Solution 1 : Run Multi-shot LP program
        if (engine == 1): # Solution 1 : Run simple Multi-shot LP program pick only 1
            if (number_of_models > 1):
                return return_response_error(303,"error","Engine 1 generated only one Plan with maximum QoS and It has not supported multiple models. Using Engine 2 in order to display more than one model ","JSON")

            planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Composite.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"composite_preference.lp"),DEFAULT_STEP,str(1))
            
            
            print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
            delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
            if (os.path.exists(delete_path)):
                try:
                    shutil.rmtree(delete_path)
                except OSError:
                    pass
        

            json_planning_data = json.loads(planing_data)
            model_result = str(json_planning_data["Result"])
            model_number = json_planning_data["Models"]["Number"]

            if (model_result.strip().upper() == "SATISFIABLE"
                    or model_result.strip().upper() == "UNKNOWN"
                    or (model_number >= 1)):

                    BIG_LIST_ANSWER_SETS = []
                    array_plans_result_json = []
                    for i in range(0,model_number):
                        if (json_planning_data["Call"][i]["Witnesses"] is not None
                            and len(json_planning_data["Call"][i]["Witnesses"]) > 0):
                            array_plans_result_json = json_planning_data["Call"][i]["Witnesses"]
                            BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                    if (len(BIG_LIST_ANSWER_SETS) > 0):
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="planning")
                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                    else:
                        return return_response_error(400,"error","engine error","JSON")                   

        elif (engine == 2): # Solution 2 : Multi-shot LP Program with QoS External Calculation
            print(DEFAULT_STEP)
            planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "program_multiple_workflows.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"composite_preference.lp"),DEFAULT_STEP,str(1))


            
            print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
            delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
            if (os.path.exists(delete_path)):
                try:
                    shutil.rmtree(delete_path)
                except OSError:
                    pass
            

            # Step 4 : Read planning data
            json_planning_data = json.loads(planing_data)
            model_result = str(json_planning_data["Result"])
            model_number = json_planning_data["Models"]["Number"]


            if (model_result.strip().upper() == "SATISFIABLE"
                or model_result.strip().upper() == "UNKNOWN"
                or (model_number >= 1)):

                BIG_LIST_ANSWER_SETS = []
                array_plans_result_json = []
                for i in range(0,model_number):
                    if (json_planning_data["Call"][i]["Witnesses"] is not None
                        and len(json_planning_data["Call"][i]["Witnesses"]) > 0):
                        array_plans_result_json = json_planning_data["Call"][i]["Witnesses"]
                        BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                if (len(BIG_LIST_ANSWER_SETS) > 0):
                    json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,True,True,number_of_models,"planning")
                    if (json_output is not None):
                        return return_success_get_json(json_output)
                    else:
                        return return_response_error(403,"error","Data error","JSON")
                else:
                    return return_response_error(400,"error","engine error","JSON")

           
        elif (engine == 3): # Solutioon 3 : Run Clingcon-3.3.0 with QoS Internal Calculation - Ranking by the best QoS too
            if (number_of_models > 1):
                return return_response_error(303,"error","Engine 3 generated only one Plan with maximum QoS by CLINGCON. Using Engine 2 in order to display more than one model ","JSON")

            planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGCON_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Composite_ForClingcon.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"composite_preference.lp"),DEFAULT_STEP,str(1))
            
            
            print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
            delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
            if (os.path.exists(delete_path)):
                try:
                    shutil.rmtree(delete_path)
                except OSError:
                    pass
            

            json_planning_data = json.loads(planing_data)
            model_result = str(json_planning_data["Result"])
            model_number = json_planning_data["Models"]["Number"]
            # Case 1 : Run without Optimization &maximize or &minimize
            if (model_result.strip().upper() == "SATISFIABLE"
                    or model_result.strip().upper() == "UNKNOWN"
                    or (model_number >= 1)):

                BIG_LIST_ANSWER_SETS = []
                array_plans_result_json = []
                for i in range(0,model_number):
                    if (json_planning_data["Call"][i]["Witnesses"] is not None
                        and len(json_planning_data["Call"][i]["Witnesses"]) > 0):
                        array_plans_result_json = json_planning_data["Call"][i]["Witnesses"]
                        BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                if (len(BIG_LIST_ANSWER_SETS) > 0):
                    json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="planning")
                    if (json_output is not None):
                        return return_success_get_json(json_output)
                    else:
                        return return_response_error(403,"error","Data error","JSON")
                else:
                    return return_response_error(400,"error","engine error","JSON")   
            elif (model_result.strip().upper() == "OPTIMUM FOUND"):  # Case 2 : Run with Optimization &maximize and &minimize
                an_optimum =  json_planning_data["Models"]["Optimum"]
                an_optimal =  int(json_planning_data["Models"]["Optimal"])
                # Check to see optimization
                BIG_LIST_ANSWER_SETS = []
                if (an_optimum == "yes" and an_optimal == 1):
                    # Get optimization value
                    optimal_value = int(json_planning_data["Models"]["Costs"][0])
                    list_witnesses = json_planning_data["Call"][0]["Witnesses"]
                    for witness in list_witnesses:
                        if (int(witness["Costs"][0]) == optimal_value):
                            small_list = []
                            small_list.append(witness)
                            BIG_LIST_ANSWER_SETS.append(small_list)
                    if (len(BIG_LIST_ANSWER_SETS) > 0):
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="planning")
                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                    else:
                        return return_response_error(400,"error","engine error","JSON")  
                else:
                    return return_response_error(400,"error","unsatisfy data","JSON")     
            else:
                return return_response_error(400,"error","engine error","JSON")    

        #--------------END-----------------------------------------
        #==========================================================
    
    # Use Case 1 : Generate Species Tree from Raw Text
    ## No Preference No Original Workflow
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":[],"inclusion":[],"insertion":[],"original_workflow":[]},"models":{"number":1,"engine":1}}'

    ## No Original Workflow _ HAVE Preference 1
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":["phylotastic_GetPhylogeneticTree_Phylomatic_POST","phylotastic_GetPhylogeneticTree_Phylomatic_GET"],"inclusion":["phylotastic_GetPhylogeneticTree_OT_POST"],"insertion":[],"original_workflow":[]},"models":{"number":1,"engine":1}}'

    ## No Original Workflow _ HAVE Preference 2
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":["phylotastic_ResolvedScientificNames_GNR_TNRS_GET"],"inclusion":["phylotastic_GetPhylogeneticTree_PhyloT_POST"],"insertion":[],"original_workflow":[]},"models":{"number":1,"engine":1}}'

    ## No Original Workflow _ HAVE Preference 3
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":["phylotastic_ResolvedScientificNames_GNR_TNRS_GET"],"inclusion":["phylotastic_GetPhylogeneticTree_PhyloT_POST"],"insertion":[],"original_workflow":[]},"models":{"number":2,"engine":2}}'

    ## No Original Workflow _ HAVE Preference 4
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":["phylotastic_ResolvedScientificNames_GNR_TNRS_GET"],"inclusion":["phylotastic_GetPhylogeneticTree_PhyloT_POST"],"insertion":[],"original_workflow":[]},"models":{"number":1,"engine":3}}'

    ## HAVE Original Workflow _ NO Preference
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":[],"inclusion":[],"insertion":[],"original_workflow":["goal(8)", "map(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text,1,convert_df_text_format_raw_to_plain,resource_FreeText,plain_text,1)", "map(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1,2,phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1,2)", "map(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3,3,convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3,3)", "map(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5,4,convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5,4)", "map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,5,convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT,5)", "map(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT,6,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,6)", "map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,7,phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format,7)", "map(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,resource_speciesTree,newickTree,9,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,8)", "map(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text,0,initial_state,resource_FreeText,raw_text,0)", "operation_has_input_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text)", "operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT)", "operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_input_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text)", "operation_has_input_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1)", "operation_has_input_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3)", "operation_has_input_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5)", "operation_has_input_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_ConnectionTime,integer)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfResolvedName,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_Tree,nmsu_tree_format)", "operation_has_output_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,plain_text)", "operation_has_output_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3)", "operation_has_output_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5)", "operation_has_output_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT)", "operation_has_output_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree)", "occur(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,1)", "occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,5)", "occur(phylotastic_GetPhylogeneticTree_OT_POST,6)", "occur(convert_df_text_format_raw_to_plain,0)", "occur(convert_df_sci_names_format_1_to_3,2)", "occur(convert_df_sci_names_format_3_to_5,3)", "occur(convert_df_sci_names_format_5_to_OT,4)", "occur(convert_species_tree_format_NMSU_to_NewickTree,7)"]},"models":{"number":1,"engine":2}}'

    ## HAVE Original Workflow _ HAve Preference
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":["phylotastic_ResolvedScientificNames_GNR_TNRS_GET"],"inclusion":["phylotastic_GetPhylogeneticTree_PhyloT_POST"],"insertion":[],"original_workflow":["goal(8)", "map(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text,1,convert_df_text_format_raw_to_plain,resource_FreeText,plain_text,1)", "map(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1,2,phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1,2)", "map(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3,3,convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3,3)", "map(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5,4,convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5,4)", "map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,5,convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT,5)", "map(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT,6,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,6)", "map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,7,phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format,7)", "map(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,resource_speciesTree,newickTree,9,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,8)", "map(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text,0,initial_state,resource_FreeText,raw_text,0)", "operation_has_input_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text)", "operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT)", "operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_input_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text)", "operation_has_input_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1)", "operation_has_input_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3)", "operation_has_input_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5)", "operation_has_input_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_ConnectionTime,integer)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfResolvedName,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_Tree,nmsu_tree_format)", "operation_has_output_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,plain_text)", "operation_has_output_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3)", "operation_has_output_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5)", "operation_has_output_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT)", "operation_has_output_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree)", "occur(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,1)", "occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,5)", "occur(phylotastic_GetPhylogeneticTree_OT_POST,6)", "occur(convert_df_text_format_raw_to_plain,0)", "occur(convert_df_sci_names_format_1_to_3,2)", "occur(convert_df_sci_names_format_3_to_5,3)", "occur(convert_df_sci_names_format_5_to_OT,4)", "occur(convert_species_tree_format_NMSU_to_NewickTree,7)"]},"models":{"number":1,"engine":2}}'

    ## HAVE Original Workflow _ HAve Preference
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recomposite" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"avoidance":["phylotastic_ResolvedScientificNames_GNR_TNRS_GET"],"inclusion":["phylotastic_GetPhylogeneticTree_PhyloT_POST"],"insertion":[],"original_workflow":["goal(8)", "map(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text,1,convert_df_text_format_raw_to_plain,resource_FreeText,plain_text,1)", "map(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1,2,phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1,2)", "map(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3,3,convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3,3)", "map(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5,4,convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5,4)", "map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,5,convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT,5)", "map(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT,6,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,6)", "map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,7,phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format,7)", "map(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,resource_speciesTree,newickTree,9,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,8)", "map(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text,0,initial_state,resource_FreeText,raw_text,0)", "operation_has_input_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text)", "operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT)", "operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_input_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text)", "operation_has_input_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1)", "operation_has_input_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3)", "operation_has_input_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5)", "operation_has_input_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_ConnectionTime,integer)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfResolvedName,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_Tree,nmsu_tree_format)", "operation_has_output_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,plain_text)", "operation_has_output_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3)", "operation_has_output_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5)", "operation_has_output_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT)", "operation_has_output_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree)", "occur(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,1)", "occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,5)", "occur(phylotastic_GetPhylogeneticTree_OT_POST,6)", "occur(convert_df_text_format_raw_to_plain,0)", "occur(convert_df_sci_names_format_1_to_3,2)", "occur(convert_df_sci_names_format_3_to_5,3)", "occur(convert_df_sci_names_format_5_to_OT,4)", "occur(convert_species_tree_format_NMSU_to_NewickTree,7)"]},"models":{"number":1,"engine":1}}'

    # Re-Generate workflow - Recomposite 
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def recomposite(self,**request_data):
        CORS()
        if cherrypy.request.method == "OPTIONS":
             return ""
        input_json = cherrypy.request.json
        '''
        input_json =  {
            "request_parameters" : {
                "input" : [
                    {
                        "name" : "A Raw Text mixes many types of encoding",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText",
                        "resource_ontology_id" : "resource_FreeText",
                        "resource_data_format_id":"raw_text",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"
                    }
                ],
                "output" : [
                    {
                        "name" : "Species Tree",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree",
                        "resource_ontology_id" : "resource_speciesTree",
                        "resource_data_format_id":"newickTree",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"
                   }
                ],
                "avoidance" : ["phylotastic_GetPhylogeneticTree_Phylomatic_POST","phylotastic_GetPhylogeneticTree_Phylomatic_GET"],
                "inclusion" : ["phylotastic_GetPhylogeneticTree_OT_POST"],
                "insertion" : [],
                "original_workflow" : []
            },
            "models":{
                "number":1,
                "engine":1
            }
        }
        '''
        try:
            request_parameters = input_json['request_parameters'];
        except:
            return return_response_error(400,"error","Missing input","JSON")

        if ((request_parameters is None) or (request_parameters == '')):
            return return_response_error(400,"error","Missing params","JSON")
       
        try:
            models = input_json['models']
            number_of_models = models["number"]
            engine = models["engine"]
        except Exception as err:
            print(err)
            number_of_models = 1
            engine = 1
  
        # Step 2 : parser input/output/avoidance,inclusion,insertion
        isAvoidance = True
        isInclusion = True
        isInsertion = True
        isOriginalWorkflow = True
        kindToRun = "NORMAL"
        
        json_input_re = request_parameters["input"]
        if ((json_input_re is None) or (json_input_re == '')):
            return return_response_error(400,"error","Missing input","JSON")
        if (len(json_input_re) <= 0):
            return return_response_error(400,"error","Empty Input","JSON")

        json_output_re = request_parameters["output"]
        if ((json_output_re is None) or (json_output_re == '')):
            return return_response_error(400,"error","Missing output","JSON")
        if (len(json_output_re) <= 0):
            return return_response_error(400,"error","Empty Output","JSON")

        json_avoidance_re = request_parameters["avoidance"]
        if ((json_avoidance_re is None) or (json_avoidance_re == '')):
            print("No avoidance request")
            isAvoidance = False
        if (len(json_avoidance_re) <= 0):
            print("No avoidance request")
            isAvoidance = False

        json_inclusion_re = request_parameters["inclusion"]
        if ((json_inclusion_re is None) or (json_inclusion_re == '')):
            print("No inclusion request")
            isInclusion = False
        if (len(json_inclusion_re) <= 0):
            print("No inclusion request")
            isInclusion = False

        json_insertion_re = request_parameters["insertion"]
        if ((json_insertion_re is None) or (json_insertion_re == '')):
            print("No insertion request")
            isInsertion = False
        if (len(json_insertion_re) <= 0):
            print("No insertion request")
            isInsertion = False

        json_original_workflows = request_parameters["original_workflow"]
        if ((json_original_workflows is None) or (json_original_workflows == '')):
            print("No Original Workflow - Simialrity Index will be terminated")
            isOriginalWorkflow = False
        if (len(json_original_workflows) <= 0):
            print("No Original Workflow - Simialrity Index will be terminated")
            isOriginalWorkflow = False    
        
        is_Preference = True
        if (not isAvoidance) and (not isInclusion) and (not isInsertion):
            is_Preference = False
            print("Switch to Composition - Planning - Input/Output specified but NO Prefernce and Current Workflow - Comming Soon")
            #return return_response_error(300,"warnning","No request for Avoidance or Inclusion or Insertion - Back to original planning engine - Comming Soon","JSON") 
            
        if (isOriginalWorkflow and is_Preference):
            kindToRun = "NORMAL" # Normal running
        elif (isOriginalWorkflow and not is_Preference):
            kindToRun = "HAVE_ORIGINAL_WF_NO_PREFERENCE" #Ok-Done
        elif (not isOriginalWorkflow and is_Preference):
            kindToRun = "NO_ORIGINAL_WF_HAVE_PREFERENCE" #Ok-Done   
        else :
            kindToRun = "ORIGINAL_PLANNING"

        print(kindToRun)

        # Step 2.1 : Write input/output to ASP files
        folder_name = self.prepareDistinguish_Input_Output_Folder_PerEachProcess()
        #print folder_name
        #folder_name = "R" + str(folder_name)

        fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),"wb")
        print("---Create Initial State--")
        fo.write("%------------------------------------------------------------------------\n")
        fo.write("% INPUT PART : Initial State\n")
        fo.write("%------------------------------------------------------------------------\n")
        input_resource_string = ""
        for i in range(0,len(json_input_re)):
            input_resource_string = input_resource_string + " | " + str(json_input_re[i]["resource_ontology_id"])
            fo.write("initially(%s,%s).\n" %(str(json_input_re[i]["resource_ontology_id"]),str(json_input_re[i]["resource_data_format_id"])))
        fo.write("%------------------------------------------------------------------------\n")
        fo.close()

        fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"), "wb")
        print("---Create Goal State--")
        fo.write("%------------------------------------------------------------------------\n")
        fo.write("% GOAL State\n")
        fo.write("%------------------------------------------------------------------------\n")
        content = ""
        max_content = ""
        output_resource_string = ""

        for i in range(0,len(json_output_re)):
            output_resource_string = output_resource_string + " | " + str(json_output_re[i]["resource_ontology_id"])
            fo.write("finally(%s, %s).\n" %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"])))
            if (len(json_output_re) > 1):
                content += "exists(%s,%s,I%s),step(I%s)," %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"]),str(i),str(i))
                if (i == 0):
                    max_content = "I%s" %(str(i))
                else:
                    max_content += ";I%s" %(str(i))    
            if (len(json_output_re) == 1):
                content += "exists(%s,%s,I), " %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"]))

        if (len(json_output_re) > 1):        
            fo.write("goal(M) :- %s M = #max{%s}.\n" %(content,max_content))
        else:
            fo.write("goal(I) :- %s step(I).\n" %(content)) 

        #fo.write("goal(I) :- %s step(I).\n" %(content))
        fo.write("%------------------------------------------------------------------------\n")
        fo.close()
        #========================================================================================================= 

        # Step 2.2 : Write avoidance/inclusion/insertion to ASP files
        fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"re_composite_preference.lp"),"wb")
        print("---Create Preferences and Constraint From--")
        if (isAvoidance):
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% AVOIDANCE  SERVICES \n")
            fo.write("%------------------------------------------------------------------------\n")
            for i in range(0,len(json_avoidance_re)):
                fo.write("do_not_use_operation(%s).\n" %(str(json_avoidance_re[i])))
            fo.write("%------------------------------------------------------------------------\n")
        if (isInclusion):
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% INCLUSION  SERVICES \n")
            fo.write("%------------------------------------------------------------------------\n")
            for i in range(0,len(json_inclusion_re)):
                fo.write("used_operation(%s).\n" %(str(json_inclusion_re[i])))
            fo.write("%------------------------------------------------------------------------\n")
        if (isInsertion):
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% INSERTION  SERVICES \n")
            fo.write("%------------------------------------------------------------------------\n")  
            fo.write("%------------------------------------------------------------------------\n")
        fo.close()

        # Step 2.3 : Write Original Workflow Objet to python file
        #fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"original_workflow.py"),"wb")
        #==========================================================================================
        '''
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
        '''
        DEFAULT_STEP = ultility.expect_number_step(input_resource_string,output_resource_string)      
        # Step 3 : Run planning
        if ("NORMAL" in kindToRun):    
            if (isOriginalWorkflow):
                original_workflow_removed = [str(i) for i in json_original_workflows]
                fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"original_workflow_data.json"),"wb")
                for item in original_workflow_removed:
                    fo.write(item)
                    fo.write("\n")
                fo.close()

            if (number_of_models > 1):
                 return return_response_error(300,"warnning","Multiple models have not supported yet","JSON")  
                    
            if (engine == 2):
                print(DEFAULT_STEP)
                if ("phylotastic_GetPhylogeneticTree_PhyloT_POST" in json_inclusion_re):
                      DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_9.lp")
                planing_data = OWLEngine.run_re_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Re_Composite_S1_OnModel.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"re_composite_preference.lp"),folder_name,DEFAULT_STEP,str(number_of_models),engine)
            
                print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
                delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
                if (os.path.exists(delete_path)):
                    try:
                        shutil.rmtree(delete_path)
                    except OSError:
                        pass
                  
                json_planning_data = json.loads(planing_data)
                if (len(json_planning_data['workflows_list']) > 0):
                        BIG_LIST_ANSWER_SETS = []
                        for i in range(0,len(json_planning_data['workflows_list'])):
                            array_plans_result_json = []
                            data = {}
                            data['Value'] = json_planning_data['workflows_list'][i]['workflow']
                            data['Sim_Index'] = json_planning_data['workflows_list'][i]['sim_index']
                            
                            json_planning_data['Models'] = "1"
                            json_planning_data['Time'] = "1ms"
                            json_planning_data['Solver'] = "Clingo"

                            array_plans_result_json.append(data)
                            BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=number_of_models,solver="recomposite")
                        
                        json_output['info']['Approach'] = "Multiple-Shot OnModel checking - Exact Sim_index"

                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                else:
                    return return_response_error(400,"error","engine error","JSON") 
            elif (engine == 1):
                print(DEFAULT_STEP)
                
                if ("phylotastic_GetPhylogeneticTree_PhyloT_POST" in json_inclusion_re):
                      DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_9.lp")

                planing_data = OWLEngine.run_re_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Re_Composite_S2_SimNodes.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"re_composite_preference.lp"),folder_name,DEFAULT_STEP,str(number_of_models),engine)


                print("--DELETE Temp Input Folder and Output Folder Rosetta Model --- 123")
                delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
                if (os.path.exists(delete_path)):
                    try:
                        shutil.rmtree(delete_path)
                    except OSError:
                        pass
                

                json_planning_data = json.loads(planing_data)
                model_result = str(json_planning_data["Result"])
                model_number = json_planning_data["Models"]["Number"]
                # Case 1 : Run without Optimization &maximize or &minimize
                if (model_result.strip().upper() == "SATISFIABLE"
                        or model_result.strip().upper() == "UNKNOWN"):

                    BIG_LIST_ANSWER_SETS = []
                    array_plans_result_json = []
                    for i in range(0,model_number):
                        if (json_planning_data["Call"][i]["Witnesses"] is not None
                            and len(json_planning_data["Call"][i]["Witnesses"]) > 0):
                            array_plans_result_json = json_planning_data["Call"][i]["Witnesses"]
                            BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                    if (len(BIG_LIST_ANSWER_SETS) > 0):
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="recomposite")
                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                    else:
                        return return_response_error(400,"error","engine error","JSON")   
                elif (model_result.strip().upper() == "OPTIMUM FOUND"):  # Case 2 : Run with Optimization &maximize and &minimize
                    #print "Vao day"
                    an_optimum =  json_planning_data["Models"]["Optimum"]
                    an_optimal =  int(json_planning_data["Models"]["Optimal"])
                    # Check to see optimization
                    BIG_LIST_ANSWER_SETS = []
                    if (an_optimum == "yes" and an_optimal == 1):
                        # Get optimization value
                        optimal_value = int(json_planning_data["Models"]["Costs"][0])
                        list_witnesses = json_planning_data["Call"][0]["Witnesses"]
                        for witness in list_witnesses:
                            if (int(witness["Costs"][0]) == optimal_value):
                                small_list = []
                                small_list.append(witness)
                                BIG_LIST_ANSWER_SETS.append(small_list)
                        if (len(BIG_LIST_ANSWER_SETS) > 0):
                            json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="recomposite")
                            #print "Tai sao ko add duoc"
                            json_output['info']['Approach'] = "Approximate sim index - Nodes Only"
                            if (json_output is not None):
                                return return_success_get_json(json_output)
                            else:
                                return return_response_error(403,"error","Data error","JSON")
                        else:
                            return return_response_error(400,"error","engine error","JSON")  
                    else:
                        return return_response_error(400,"error","unsatisfy data","JSON")     
                else:
                    return return_response_error(400,"error","engine error","JSON")

        elif ("HAVE_ORIGINAL_WF_NO_PREFERENCE" in kindToRun):
            BIG_LIST_ANSWER_SETS = []
            simulate_data = []
            data = {}
            data['Value'] = json_original_workflows
            simulate_data.append(data)
            BIG_LIST_ANSWER_SETS.append(simulate_data)
            json_planning_data = {}
            json_planning_data['Models'] = "Return data"
            json_planning_data['Time'] = "1ms"
            json_planning_data['Solver'] = "Clingo"
            json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="recomposite")

            print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
            delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
            if (os.path.exists(delete_path)):
                try:
                    shutil.rmtree(delete_path)
                except OSError:
                    pass
            if (json_output is not None):
                return return_success_get_json(json_output)
            else:
                return return_response_error(403,"error","Data error","JSON")
        elif ("NO_ORIGINAL_WF_HAVE_PREFERENCE" in kindToRun):
            # Solution 1 : Run Multi-shot LP program
            if (engine == 1): # Solution 1 : Run simple Multi-shot LP program pick only 1
                if (number_of_models > 1):
                    return return_response_error(303,"error","Engine 1 generated only one Plan with maximum QoS and It has not supported multiple models. Using Engine 2 in order to display more than one model ","JSON")

                if ("phylotastic_GetPhylogeneticTree_PhyloT_POST" in json_inclusion_re):
                      DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_9.lp")
                print(DEFAULT_STEP)      
                planing_data = OWLEngine.run_re_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Composite.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"re_composite_preference.lp"),None,DEFAULT_STEP,str(1),engine)
                
                
                print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
                delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
                if (os.path.exists(delete_path)):
                    try:
                        shutil.rmtree(delete_path)
                    except OSError:
                        pass
                

                json_planning_data = json.loads(planing_data)
                model_result = str(json_planning_data["Result"])
                model_number = json_planning_data["Models"]["Number"]

                if (model_result.strip().upper() == "SATISFIABLE"
                        or model_result.strip().upper() == "UNKNOWN"
                        or (model_number >= 1)):

                        BIG_LIST_ANSWER_SETS = []
                        array_plans_result_json = []
                        for i in range(0,model_number):
                            if (json_planning_data["Call"][i]["Witnesses"] is not None
                                and len(json_planning_data["Call"][i]["Witnesses"]) > 0):
                                array_plans_result_json = json_planning_data["Call"][i]["Witnesses"]
                                BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                        if (len(BIG_LIST_ANSWER_SETS) > 0):
                            json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="recomposite")
                            if (json_output is not None):
                                return return_success_get_json(json_output)
                            else:
                                return return_response_error(403,"error","Data error","JSON")
                        else:
                            return return_response_error(400,"error","engine error","JSON")                   

            elif (engine == 2): # Solution 2 : Multi-shot LP Program with QoS External Calculation
                if ("phylotastic_GetPhylogeneticTree_PhyloT_POST" in json_inclusion_re):
                      DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_9.lp")
                print(DEFAULT_STEP)
                planing_data = OWLEngine.run_re_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "program_multiple_workflows.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"re_composite_preference.lp"),None,DEFAULT_STEP,number_of_models,engine)
                
                print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
                delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
                if (os.path.exists(delete_path)):
                    try:
                        shutil.rmtree(delete_path)
                    except OSError:
                        pass
                

                # Step 4 : Read planning data
                json_planning_data = json.loads(planing_data)
                model_result = str(json_planning_data["Result"])
                model_number = json_planning_data["Models"]["Number"]


                if (model_result.strip().upper() == "SATISFIABLE"
                    or model_result.strip().upper() == "UNKNOWN"
                    or (model_number >= 1)):

                    BIG_LIST_ANSWER_SETS = []
                    array_plans_result_json = []
                    for i in range(0,model_number):
                        if (json_planning_data["Call"][i]["Witnesses"] is not None
                            and len(json_planning_data["Call"][i]["Witnesses"]) > 0):
                            array_plans_result_json = json_planning_data["Call"][i]["Witnesses"]
                            BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                    if (len(BIG_LIST_ANSWER_SETS) > 0):
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,True,True,number_of_models,"recomposite")
                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                    else:
                        return return_response_error(400,"error","engine error","JSON")

               
            elif (engine == 3): # Solutioon 3 : Run Clingcon-3.3.0 with QoS Internal Calculation - Ranking by the best QoS too
                if (number_of_models > 1):
                    return return_response_error(303,"error","Engine 3 generated only one Plan with maximum QoS by CLINGCON. Using Engine 2 in order to display more than one model ","JSON")  
                planing_data = OWLEngine.run_re_planning_engine(self.FULL_PATH_CLINGCON_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Composite_ForClingcon.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"re_composite_preference.lp"),None,DEFAULT_STEP,str(1),engine)
                
                #print planning_data
                print("--DELETE Temp Input Folder and Output Folder Rosetta Model")
                delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
                if (os.path.exists(delete_path)):
                    try:
                        shutil.rmtree(delete_path)
                    except OSError:
                        pass
                

                json_planning_data = json.loads(planing_data)
                model_result = str(json_planning_data["Result"])
                model_number = json_planning_data["Models"]["Number"]
                # Case 1 : Run without Optimization &maximize or &minimize
                if (model_result.strip().upper() == "SATISFIABLE"
                        or model_result.strip().upper() == "UNKNOWN"
                        or (model_number >= 1)):

                    BIG_LIST_ANSWER_SETS = []
                    array_plans_result_json = []
                    for i in range(0,model_number):
                        if (json_planning_data["Call"][i]["Witnesses"] is not None
                            and len(json_planning_data["Call"][i]["Witnesses"]) > 0):
                            array_plans_result_json = json_planning_data["Call"][i]["Witnesses"]
                            BIG_LIST_ANSWER_SETS.append(array_plans_result_json)

                    if (len(BIG_LIST_ANSWER_SETS) > 0):
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="recomposite")
                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                    else:
                        return return_response_error(400,"error","engine error","JSON")   
                elif (model_result.strip().upper() == "OPTIMUM FOUND"):  # Case 2 : Run with Optimization &maximize and &minimize
                    an_optimum =  json_planning_data["Models"]["Optimum"]
                    an_optimal =  int(json_planning_data["Models"]["Optimal"])
                    # Check to see optimization
                    BIG_LIST_ANSWER_SETS = []
                    if (an_optimum == "yes" and an_optimal == 1):
                        # Get optimization value
                        optimal_value = int(json_planning_data["Models"]["Costs"][0])
                        list_witnesses = json_planning_data["Call"][0]["Witnesses"]
                        for witness in list_witnesses:
                            if (int(witness["Costs"][0]) == optimal_value):
                                small_list = []
                                small_list.append(witness)
                                BIG_LIST_ANSWER_SETS.append(small_list)
                        if (len(BIG_LIST_ANSWER_SETS) > 0):
                            json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="recomposite")
                            #json_output['info']["Approach"] = "Approximate Sim Index - Nodes only"
                            if (json_output is not None):
                                return return_success_get_json(json_output)
                            else:
                                return return_response_error(403,"error","Data error","JSON")
                        else:
                            return return_response_error(400,"error","engine error","JSON")  
                    else:
                        return return_response_error(400,"error","unsatisfy data","JSON")     
                else:
                    return return_response_error(400,"error","engine error","JSON") 
        elif ("ORIGINAL_PLANNING" in kindToRun):
            return return_response_error(300,"warnning","Back to Composite - Comming Soon","JSON")
        else:
            return return_response_error(300,"error","Unknown","JSON")


    # Recovery Process
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def recovery(self,**request_data):
        CORS()
        if cherrypy.request.method == "OPTIONS":
             return ""
        input_json = cherrypy.request.json        
        
        '''
        input_json =  {
            "request_parameters" : {
                "input" : [
                    {
                        "name" : "A Raw Text mixes many types of encoding",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText",
                        "resource_ontology_id" : "resource_FreeText",
                        "resource_data_format_id":"raw_text",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"
                    }
                ],
                "output" : [
                    {
                        "name" : "Species Tree",
                        "resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree",
                        "resource_ontology_id" : "resource_speciesTree",
                        "resource_data_format_id":"newickTree",
                        "resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"
                   }
                ],
                "failed_service" : [
                    {
                      "ID" : "phylotastic_GetPhylogeneticTree_Phylomatic_POST",
                      "Index" : 3
                    }
                ],
                "original_workflow" : [],
                "generated_resources" : [
                    {
                        "resource_ontology_id" : "a",
                        "resource_data_format_id" : "b",
                        "resource_name_in_output_of_service" : "c",
                        "resource_data" : "data"
                    }
                ]
            },
            "models":{
                "number":1,
                "engine":1
            }
        }
        '''
        try:
            request_parameters = input_json['request_parameters'];
        except:
            return return_response_error(400,"error","Missing input","JSON")

        if ((request_parameters is None) or (request_parameters == '')):
            return return_response_error(400,"error","Missing params","JSON")
       
        try:
            models = input_json['models']
            number_of_models = models["number"]
            engine = models["engine"]
        except Exception as err:
            print(err)
            number_of_models = 1
            engine = 1

        
        # Step 2 : parser input/output/avoidance,inclusion,insertion
        isOriginalWorkflow = True
        isFailedService = True
        json_input_re = request_parameters["input"]
        if ((json_input_re is None) or (json_input_re == '')):
            return return_response_error(400,"error","Missing input","JSON")
        if (len(json_input_re) <= 0):
            return return_response_error(400,"error","Empty Input","JSON")

        json_output_re = request_parameters["output"]
        if ((json_output_re is None) or (json_output_re == '')):
            return return_response_error(400,"error","Missing output","JSON")
        if (len(json_output_re) <= 0):
            return return_response_error(400,"error","Empty Output","JSON")

        json_original_workflows = request_parameters["original_workflow"]
        if ((json_original_workflows is None) or (json_original_workflows == '')):
            print("No Original Workflow - Simialrity Index will be terminated")
            isOriginalWorkflow = False
        if (len(json_original_workflows) <= 0):
            print("No Original Workflow - Simialrity Index will be terminated")
            isOriginalWorkflow = False

        json_fail_service = request_parameters["failed_service"]
        if ((json_fail_service is None) or (json_fail_service == '')):
            print("No Failed Service Detection")
            isFailedService = False
        if (len(json_fail_service) <= 0):
            print("No Failded Service Detection")
            isFailedService = False

        if ((not isFailedService) and (not isOriginalWorkflow)):
            return return_response_error(301,"error","Not recovery process","JSON")
        elif ((isFailedService) and (not isOriginalWorkflow)):
            return return_response_error(301,"error","Original Workflow is required","JSON")
        elif ((not isFailedService) and (isOriginalWorkflow)): 
            return "Good - Original Workflow"
        else:
            # Step 2.1 : Write input/output to ASP files
            folder_name = self.prepareDistinguish_Input_Output_Folder_PerEachProcess()
            fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),"wb")
            print("---Recovery process : Create Initial State-- Engine : %s" %(str(engine)))
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% Recovery process INPUT PART : Initial State\n")
            fo.write("%------------------------------------------------------------------------\n")
            input_resource_string = ""
            for i in range(0,len(json_input_re)):
                input_resource_string = input_resource_string + " | " + str(json_input_re[i]["resource_ontology_id"])
                fo.write("initially(%s,%s).\n" %(str(json_input_re[i]["resource_ontology_id"]),str(json_input_re[i]["resource_data_format_id"])))
            fo.write("%------------------------------------------------------------------------\n")
            fo.close()

            fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"), "wb")
            print("---Recovery process : Create Goal State---- Engine : %s" %(str(engine)))
            fo.write("%------------------------------------------------------------------------\n")
            fo.write("% Recovery process : GOAL State\n")
            fo.write("%------------------------------------------------------------------------\n")
            content = ""
            max_content = ""
            output_resource_string = ""

            for i in range(0,len(json_output_re)):
                output_resource_string = output_resource_string + " | " + str(json_output_re[i]["resource_ontology_id"])
                fo.write("finally(%s, %s).\n" %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"])))
                if (len(json_output_re) > 1):
                    content += "exists(%s,%s,I%s),step(I%s)," %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"]),str(i),str(i))
                    if (i == 0):
                        max_content = "I%s" %(str(i))
                    else:
                        max_content += ";I%s" %(str(i))    
                if (len(json_output_re) == 1):
                    content += "exists(%s,%s,I), " %(str(json_output_re[i]["resource_ontology_id"]),str(json_output_re[i]["resource_data_format_id"]))

            if (len(json_output_re) > 1):        
                fo.write("goal(M) :- %s M = #max{%s}.\n" %(content,max_content))
            else:
                fo.write("goal(I) :- %s step(I).\n" %(content)) 

            #fo.write("goal(I) :- %s step(I).\n" %(content))
            fo.write("%------------------------------------------------------------------------\n")
            fo.close()
            #========================================================================================================= 
            if (isOriginalWorkflow and isFailedService):
                fail_service_ID = json_fail_service[0]["ID"]
                fail_Index = json_fail_service[0]["Index"]

                if (engine == 1 or engine == 2 or engine == 3):
                    original_workflow_removed = [str(i) for i in json_original_workflows]
                    fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"failure_detection.lp"),"wb")
                    fo.write("%--------------------------------------------------------------------\n")
                    fo.write("fail_service(%s,%s).\n" %(str(fail_service_ID),str(fail_Index)))
                    fo.write("%--------------------------------------------------------------------\n")
                    for item in original_workflow_removed:
                        if ('OCCUR(' in str(item).strip().upper()):
                            service_name,step = composite_parser.parse_a_occur_service(str(item))
                            if (int(step) < int(fail_Index)):
                                str_content = "old_occ_exe(%s,%s).\n" %(str(service_name),str(step))
                                fo.write(str_content)
                        if ('MAP(' in str(item).strip().upper()):
                            map_obj = composite_parser.parse_a_match_predicate(str(item))
                            if (int(map_obj[3]) < int(fail_Index)):
                                str_content = "old_map_exe(%s,%s,%s,%s,%s,%s,%s,%s).\n" %(str(map_obj[0]),str(map_obj[1]),str(map_obj[2]),str(map_obj[3]),str(map_obj[4]),str(map_obj[5]),str(map_obj[6]),str(map_obj[7]),)
                                fo.write(str_content)
                        #fo.write("\n")
                    fo.close()
                elif (engine == 4):
                    print("Doing resource_generated(.)")
                    # Generate added_intial_state_base.lp
                    fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"sup_init_generated_resource_failure_detection.lp"),"wb")
                    print("---Recovery process : Supplimental Initial State & Failure Detection -- Engine : %s" %(str(engine)))
                    fo.write("%------------------------------------------------------------------------\n")
                    fo.write("% Recovery process Added Resource : Supplimental Initial State & Failure Detection \n")
                    fo.write("%------------------------------------------------------------------------\n")
                    
                    fail_service_ID = json_fail_service[0]["ID"]
                    fail_Index = json_fail_service[0]["Index"]

                    fo.write("fail_service(%s,%s).\n" %(str(fail_service_ID),str(fail_Index)))
                    fo.write("%--------------------------------------------------------------------\n")
                    json_generated_resource = request_parameters["generated_resources"]
                    if ((json_generated_resource is None) or (json_generated_resource == '')):
                        json_generated_resource = []
                    if (len(json_fail_service) <= 0):
                        json_generated_resource = []

                    fo.write("%--------------------------------------------------------------------\n")
                    fo.write("%--------------------------------------------------------------------\n")
                    sub_init_list = [] 
                    for gen_resource in json_generated_resource:
                        if (gen_resource['resource_ontology_id'] and gen_resource['resource_data_format_id']):
                            gen_resource_string = gen_resource['resource_ontology_id'] + "," + gen_resource['resource_data_format_id']
                            if (gen_resource_string not in sub_init_list):
                                sub_init_list.append(gen_resource_string)

                    fo.write("%------------------------------------------------------------------------\n")
                    fo.write("% Recovery process Added Resource : Supplimental Initial State \n")
                    fo.write("%------------------------------------------------------------------------\n")          
                    for content in sub_init_list:
                        fo.write("intitally(%s).\n" %(str(content)))            
                    fo.write("%------------------------------------------------------------------------\n")             
                    

                    fo.write("%------------------------------------------------------------------------\n")
                    fo.close()


            NUMBER_STEP = ultility.expect_number_step(input_resource_string,output_resource_string)

            # Step 3 : Run planning
            if (engine == 1): # Solution 1 : Pure LP (Clingo) to get 1 Workflow  => Calculate Score workflow by update from prev(u)
                if (number_of_models > 1):
                    return return_response_error(303,"error","Engine 1 has only one model","JSON")
                print("---Recovery process : RUNNING ENGINE 1 : Pure Approach : Score of worklfow based on maximum score of all nodes in G' => Calulate score of node based on Score of prev(u)")    
                planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "recover_process.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"failure_detection.lp"),NUMBER_STEP,str(1))
            elif (engine == 2): # Solution : Pure LP (Clingo) with high performance => Count number    
                if (number_of_models > 1):
                    return return_response_error(303,"error","Engine 2 has only one model","JSON")
                print("---Recovery process : RUNNING ENGINE 2 :  High performance")    
                planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "recover_process_high_performance.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"failure_detection.lp"),NUMBER_STEP,str(1))
            elif (engine == 3): # Solution : REplanning with successfull services => Count number of mapping ONLY
                if (number_of_models > 1):
                    return return_response_error(303,"error","Engine 3 has only one model","JSON")
                print("---Recovery process : RUNNING ENGINE 3 :  Replanning with Successfull Services") 
                planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "recover_process_successful_services.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"failure_detection.lp"),NUMBER_STEP,str(1))
            elif (engine == 4): # Solution : Planning from Failed States => Count number of resource reused
                if (number_of_models > 1):
                    return return_response_error(303,"error","Engine 4 has only one model","JSON")
                print("---Recovery process : RUNNING ENGINE 4 :  Planning from Failed State")
                planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "recover_process_from_failed_state.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"sup_init_generated_resource_failure_detection.lp"),NUMBER_STEP,str(1))
            else:
                return return_response_error(400,"error","no eligible engine","JSON")  
            
              
            print("--DELETE Temp Input Folder and Output Folder-- Recovery")
            delete_path = os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name)
            if (os.path.exists(delete_path)):
                try:
                    shutil.rmtree(delete_path)
                except OSError:
                    pass
            
            
            json_planning_data = json.loads(planing_data)
            model_result = str(json_planning_data["Result"])
            model_number = json_planning_data["Models"]["Number"]

            if (model_result.strip().upper() == "OPTIMUM FOUND"):  #Run with Optimization &maximize and &minimize
                an_optimum =  json_planning_data["Models"]["Optimum"]
                an_optimal =  int(json_planning_data["Models"]["Optimal"])
                # Check to see optimization
                BIG_LIST_ANSWER_SETS = []
                if (an_optimum == "yes" and an_optimal == 1):
                    # Get optimization value
                    optimal_value = int(json_planning_data["Models"]["Costs"][0])
                    list_witnesses = json_planning_data["Call"][0]["Witnesses"]
                    for witness in list_witnesses:
                        if (int(witness["Costs"][0]) == optimal_value):
                            small_list = []
                            small_list.append(witness)
                            BIG_LIST_ANSWER_SETS.append(small_list)
                    if (len(BIG_LIST_ANSWER_SETS) > 0):
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1,solver="recovery")
                        if (engine == 1):
                            json_output['info']['Approach'] = "Failure Detection - Max Matching by ASP Optimization - Pure Approach : Score of worklfow based on maximum score of all nodes in G' => Calulate score of node based on Score of prev(u)"
                        elif (engine == 2):
                            json_output['info']['Approach'] = "Failure Detection - Max Matching by ASP Optimization - High performance: Count the number of mapping only => Get max by workflow has highest number of mapping"
                        elif (engine == 3):
                            json_output['info']['Approach'] = "Failure Detection - Max Matching by ASP Optimization - Replanning with Successfull Services: = 0 if no mapp, = 1 if mapped => Sum all to get maximum"
                        elif (engine == 4):
                            json_output['info']['Approach'] = "Failure Detection - Max Matching by ASP Optimization - Planning from Failed State : Count number of resued resources"
                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                    else:
                        return return_response_error(400,"error","engine error","JSON")  
                else:
                    return return_response_error(400,"error","unsatisfy data","JSON")
            
    #curl -X POST "http://127.0.0.1:8000/planningEngine/recovery" -H "content-type:application/json" -d '{"request_parameters" : {"input" : [{"name" : "A Raw Text mixes many types of encoding","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_FreeText","resource_ontology_id" : "resource_FreeText","resource_data_format_id":"raw_text","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#raw_text"}],"output" : [{"name" : "Species Tree","resource_ontology_uri" : "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree","resource_ontology_id" : "resource_speciesTree","resource_data_format_id":"newickTree","resource_data_format_uri":"http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#newickTree"}],"failed_service":[{"ID" : "phylotastic_GetPhylogeneticTree_OT_POST","Index":6}],"generated_resources":[{"resource_ontology_id" : "a1","resource_data_format_id" : "b1","resource_name_in_output_of_service" : "c1","resource_data" : "data1"},{"resource_ontology_id" : "a2","resource_data_format_id" : "b2","resource_name_in_output_of_service" : "c2","resource_data" : "data2"},{"resource_ontology_id" : "a1","resource_data_format_id" : "b1","resource_name_in_output_of_service" : "c1","resource_data" : "data1"}],"original_workflow":["goal(8)", "map(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text,1,convert_df_text_format_raw_to_plain,resource_FreeText,plain_text,1)", "map(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1,2,phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1,2)", "map(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3,3,convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3,3)", "map(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5,4,convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5,4)", "map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,5,convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT,5)", "map(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT,6,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,6)", "map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,7,phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format,7)", "map(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,resource_speciesTree,newickTree,9,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,8)", "map(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text,0,initial_state,resource_FreeText,raw_text,0)", "operation_has_input_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text)", "operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT)", "operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_input_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text)", "operation_has_input_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1)", "operation_has_input_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3)", "operation_has_input_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5)", "operation_has_input_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_ConnectionTime,integer)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfResolvedName,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_Tree,nmsu_tree_format)", "operation_has_output_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,plain_text)", "operation_has_output_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3)", "operation_has_output_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5)", "operation_has_output_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT)", "operation_has_output_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree)", "occur(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,1)", "occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,5)", "occur(phylotastic_GetPhylogeneticTree_OT_POST,6)", "occur(convert_df_text_format_raw_to_plain,0)", "occur(convert_df_sci_names_format_1_to_3,2)", "occur(convert_df_sci_names_format_3_to_5,3)", "occur(convert_df_sci_names_format_5_to_OT,4)", "occur(convert_species_tree_format_NMSU_to_NewickTree,7)"]},"models":{"number":1,"engine":1}}'    


    #public generate workflow
    generateWorkflow.exposed = True
    #public recomposite similarity workflow
    recomposite.exposed = True
    #public recovery process
    recovery.exposed = True
    #public index
    index.exposed = True
class OntologyAPI_Service(object):
    _cp_config = {
        'tools.sessions.on': True,
        'tools.sessions.httponly': True
    }
    def index(self):
        return "OntologyAPI_Service"
    def query(self, **request_data):
        CORS()
        if cherrypy.request.method == "OPTIONS":
             print("Thay OPTIONS - IGNORES")
             return ""
        try:
            request = str(request_data['request']).strip()
        except:
            return return_response_error(300, "error", "need provide request param", "JSON")

        if ((request is None) or (request == "")):
            return return_response_error(300, "error", "need provide request param", "JSON")

        #http://localhost:8000/query?request=get_all_instances_of_a_class&parser_engine=2&owlclass=phylotastic_resources&ontology=cdao_phylotastic
        #http://localhost:8000/query?request=get_all_instances_of_a_class&parser_engine=1&owlclass_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23tree_generation
        if (request.strip().upper() == "GET_ALL_INSTANCES_OF_A_CLASS"):
            try:
                parser_engine = str(request_data['parser_engine']).strip()
            except:
                parser_engine = "2"

            if ((parser_engine == 2) or (parser_engine == "2")):
                try:
                    owlclass = str(request_data['owlclass']).strip()
                except:
                    return return_response_error(300, "error", "need provide owlclass param", "JSON")

                try:
                    ontology = str(request_data['ontology']).strip()
                except:
                    return return_response_error(300, "error", "need provide ontology param", "JSON")

                message = OWLEngine.get_all_instances_of_a_directed_class_engine_2(owlclass,ontology.strip().upper())
                return return_success_get_json(message)
            elif ((parser_engine == 1) or (parser_engine == "1")):
                try:
                    owl_class_uri = str(request_data['owl_class_uri']).strip()
                except:
                    return return_response_error(300, "error", "need provide owl_class_uri param - Replace hash symbol (#) by %23 ", "JSON")

                message = OWLEngine.get_all_instances_of_a_directed_class_engine_1(owl_class_uri.strip())
                return return_success_get_json(message)



        #http://localhost:8000/query?request=get_all_directed_subclass_of_a_class&parser_engine=2&owlclass=list_operation&ontology=phylo_methods
        #http://localhost:8000/query?request=get_all_directed_subclass_of_a_class&parser_engine=1&owl_class_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23names_operation
        if (request.strip().upper() == "GET_ALL_DIRECTED_SUBCLASS_OF_A_CLASS"):

            try:
                parser_engine = str(request_data['parser_engine']).strip()
            except:
                parser_engine = "2"

            if ((parser_engine == 2) or (parser_engine == "2")):
                try:
                    owlclass = str(request_data['owlclass']).strip()
                except:
                    return return_response_error(300, "error", "need provide owlclass param", "JSON")

                try:
                    ontology = str(request_data['ontology']).strip()
                except:
                    return return_response_error(300, "error", "need provide ontology param", "JSON")

                message = OWLEngine.get_all_directed_subclass_of_class_engine_2(owlclass,ontology.strip().upper())
                return return_success_get_json(message)
            elif ((parser_engine == 1) or (parser_engine == "1")):
                try:
                    owl_class_uri = str(request_data['owl_class_uri']).strip()
                except:
                    return return_response_error(300, "error", "need provide owl_class_uri param - Replace hash symbol (#) by %23 ", "JSON")

                message = OWLEngine.get_all_directed_subclass_of_class_engine_1(owl_class_uri.strip())
                return return_success_get_json(message)

        #http://localhost:8000/query?request=get_hierarchy_subclasses_of_a_class&owl_class_uri=http://www.cs.nmsu.edu/~epontell/Ontologies/phylogenetic_methods.owl#operationClassification&level=0
        if (request.strip().upper() == "GET_HIERARCHY_SUBCLASSES_OF_A_CLASS"):
            try:
                owl_class_uri = str(request_data['owl_class_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_class_uri param", "JSON")

            try:
                level = str(request_data['level']).strip()
            except:
                level = "0"
            message = OWLEngine.get_hierarchy_subclasses_of_class(owl_class_uri.strip(),level.strip())
            return return_success_get_json(message)

        #http://localhost:8000/query?request=get_detail_information_of_a_operation&parser_engine=2&owl_operation_name=phylotastic_FindScientificNamesFromFreeText_GNRD_GET&ontology=cdao_phylotastic
        #http://localhost:8000/query?request=get_detail_information_of_a_operation&parser_engine=1&owl_operation_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23phylotastic_GetPhylogeneticTree_OT_POST
        if (request.strip().upper() == "GET_DETAIL_INFORMATION_OF_A_OPERATION"):
            try:
                parser_engine = str(request_data['parser_engine']).strip()
            except:
                parser_engine = "1"

            if ((parser_engine == 2) or (parser_engine == "2")):
                    try:
                        owl_operaion_name = str(request_data['owl_operation_name']).strip()
                    except:
                        return return_response_error(300, "error", "need provide owl_operation_name param", "JSON")

                    try:
                        ontology = str(request_data['ontology']).strip()
                    except:
                        return return_response_error(300, "error", "need provide ontology param", "JSON")

                    message = OWLEngine.get_detail_information_of_operation_engine_2(owl_operaion_name,ontology.strip().upper())
                    return return_success_get_json(message)
            elif ((parser_engine == 1) or (parser_engine == "1")):
                    try:
                        owl_operaion_uri = str(request_data['owl_operation_uri']).strip()
                    except:
                        return return_response_error(300, "error", "need provide owl_operation_uri param - Replace hash symbol (#) by %23", "JSON")

                    message = OWLEngine.get_detail_information_of_operation_engine_1(owl_operaion_uri)
                    return return_success_get_json(message)


        #http://localhost:8000/query?request=get_detail_information_of_a_resource&parser_engine=2&owl_resource_name=free_text&ontology=cdao_phylotastic
        #http://localhost:8000/query?request=get_detail_information_of_a_resource&parser_engine=1&owl_resource_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa
        if (request.strip().upper() == "GET_DETAIL_INFORMATION_OF_A_RESOURCE"):
            try:
                parser_engine = str(request_data['parser_engine']).strip()
            except:
                parser_engine = "1"

            if ((parser_engine == 2) or (parser_engine == "2")):
                    try:
                        owl_resource_name = str(request_data['owl_resource_name']).strip()
                    except:
                        return return_response_error(300, "error", "need provide owl_resource_name param", "JSON")

                    try:
                        ontology = str(request_data['ontology']).strip()
                    except:
                        return return_response_error(300, "error", "need provide ontology param", "JSON")

                    message = OWLEngine.get_detail_information_of_resource_engine_2(owl_resource_name,ontology.strip().upper())
                    return return_success_get_json(message)
            elif ((parser_engine == 1) or (parser_engine == "1")):
                    try:
                        owl_resource_uri = str(request_data['owl_resource_uri']).strip()
                    except:
                        return return_response_error(300, "error", "need provide owl_resource_uri param - Replace hash symbol (#) by %23", "JSON")

                    message = OWLEngine.get_detail_information_of_resource_engine_1(owl_resource_uri)
                    return return_success_get_json(message)

        #http://localhost:8000/query?request=get_detail_information_of_a_component&parser_engine=2&owl_component_name=param_species&ontology=cdao_phylotastic
        #http://localhost:8000/query?request=get_detail_information_of_a_component&parser_engine=1&owl_component_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23param_resolved_names
        if (request.strip().upper() == "GET_DETAIL_INFORMATION_OF_A_COMPONENT"):
            try:
                parser_engine = str(request_data['parser_engine']).strip()
            except:
                parser_engine = "1"
            if ((parser_engine == 2) or (parser_engine == "2")):
                    try:
                        owl_component_name = str(request_data['owl_component_name']).strip()
                    except:
                        return return_response_error(300, "error", "need provide owl_component_name param", "JSON")

                    try:
                        ontology = str(request_data['ontology']).strip()
                    except:
                        return return_response_error(300, "error", "need provide ontology param", "JSON")

                    message = OWLEngine.get_detail_information_of_component_engine_2(owl_component_name,ontology.strip().upper())
                    return return_success_get_json(message)
            elif ((parser_engine == 1) or (parser_engine == "1")):
                    try:
                        owl_component_uri = str(request_data['owl_component_uri']).strip()
                    except:
                        return return_response_error(300, "error", "need provide owl_component_uri param - Replace hash symbol (#) by %23", "JSON")

                    message = OWLEngine.get_detail_information_of_component_engine_1(owl_component_uri)
                    return return_success_get_json(message)
    # Build Graph
    def buildGraph(self, **request_data):
        CORS()
        if cherrypy.request.method == "OPTIONS":
             return ""
        try:
            graph_type = str(request_data['graph_type']).strip()
        except:
            graph_type = "1"

        if ((graph_type != "1") and (graph_type != 1) and (graph_type != "2") and (graph_type != 2) and (graph_type != "3") and (graph_type != 3)):
            return return_response_error(300, "error", "graph type is not correct", "JSON")

        try:
            entity_uri = str(request_data['owl_entity_uri']).strip()
        except:
            return return_response_error(300, "error", "need provide owl_entity_uri param - Replace hash symbol (#) by %23 ", "JSON")


        message = OWLEngine.get_build_graph_of_ontology_entity(entity_uri.strip(),graph_type)
        return return_success_get_json(message)


    # Get Triple Data
    def getTriples(self, **request_data):
        CORS()
        if cherrypy.request.method == "OPTIONS":
             return ""
        try:
            triple_type = str(request_data['triple_type']).strip()
        except:
            return return_response_error(300, "error", "need provide triple_type param", "JSON")

        if ((triple_type == 1) or (triple_type == "1")):
            # Type 1 : Get predicates objects from input subject
            #   http://localhost:8000/getTriples?triple_type=1&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa
            try:
                owl_subject_uri = str(request_data['owl_subject_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_subject_uri param - Replace hash symbol (#) by %23 ", "JSON")

            message = OWLEngine.get_triples_predicates_objects_from_subject(owl_subject_uri.strip())
            return return_success_get_json(message)
        elif ((triple_type == 2) or (triple_type == "2")):
            # Type 2 : Get predicates objects from input subject
            #   http://localhost:8000/getTriples?triple_type=2&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa

            try:
                owl_object_uri = str(request_data['owl_object_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_object_uri param - Replace hash symbol (#) by %23 ", "JSON")

            message = OWLEngine.get_triples_subjects_predicates_from_object(owl_object_uri.strip())
            return return_success_get_json(message)
        elif ((triple_type == 3) or (triple_type == "3")):
            # Type 3 : Get predicates objects from input subject
            #   http://localhost:8000/getTriples?triple_type=3&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23has_Element
            try:
                owl_predicate_uri = str(request_data['owl_predicate_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_predicate_uri param - Replace hash symbol (#) by %23 ", "JSON")

            message = OWLEngine.get_triples_subjects_objects_from_predicate(owl_predicate_uri.strip())
            return return_success_get_json(message)
        elif ((triple_type == 4) or (triple_type == "4")):
            # Type 4 : Get objects from input subject + predicate
            #   http://localhost:8000/getTriples?triple_type=4&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23has_Element
            #   http://localhost:8000/getTriples?triple_type=4&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23param_resolved_names&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/Ontologies/phylogenetic_methods.owl%23is_a
            try:
                owl_subject_uri = str(request_data['owl_subject_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_subject_uri param - Replace hash symbol (#) by %23 ", "JSON")

            try:
                owl_predicate_uri = str(request_data['owl_predicate_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_predicate_uri param - Replace hash symbol (#) by %23 ", "JSON")

            message = OWLEngine.get_triples_objects_from_subject_predicate(owl_subject_uri.strip(),owl_predicate_uri.strip())
            return return_success_get_json(message)
        elif ((triple_type==5) or (triple_type=="5")):
            # Type 5 : Get subjects from input object + predicate
            #   http://localhost:8000/getTriples?triple_type=5&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxon&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23has_Element
            #   http://localhost:8000/getTriples?triple_type=5&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/Ontologies/phylogenetic_methods.owl%23is_a
            try:
                owl_object_uri = str(request_data['owl_object_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_object_uri param - Replace hash symbol (#) by %23 ", "JSON")

            try:
                owl_predicate_uri = str(request_data['owl_predicate_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_predicate_uri param - Replace hash symbol (#) by %23 ", "JSON")

            message = OWLEngine.get_triples_subjects_from_object_predicate(owl_object_uri.strip(),owl_predicate_uri.strip())
            return return_success_get_json(message)
        elif ((triple_type==6) or (triple_type=="6")):
            # Type 6 : Get predicates from input subject + object
            #   http://localhost:8000/getTriples?triple_type=6&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxon
            try:
                owl_subject_uri = str(request_data['owl_subject_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_subject_uri param - Replace hash symbol (#) by %23 ", "JSON")

            try:
                owl_object_uri = str(request_data['owl_object_uri']).strip()
            except:
                return return_response_error(300, "error", "need provide owl_object_uri param - Replace hash symbol (#) by %23 ", "JSON")

            message = OWLEngine.get_triples_predicates_from_subject_object(owl_subject_uri.strip(),owl_object_uri.strip())
            return return_success_get_json(message)
    # Public /index
    index.exposed = True
    # public /query
    query.exposed = True
    # public /getTriples
    getTriples.exposed = True
    # public /buildGraph
    buildGraph.exposed = True

if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool("before_finalize", CORS)
    # Configure Server
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port': PORT
                            })
    conf = {
        '/': {
            'tools.CORS.on': True
        }
    }
    # Starting Server
    #cherrypy.quickstart(OntologyAPI_Service(), "/", conf)
    cherrypy.tree.mount(OntologyAPI_Service(), '/', conf)
    cherrypy.tree.mount(Interact_Planning_Engine(), '/planningEngine', conf )
    # cherrypy.engine.start()
    cherrypy.engine.start()
    cherrypy.engine.block()

'''
Ending Source code for App Engine - Web Service Composition
'''    