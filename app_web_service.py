import cherrypy
from OWL_Ontology_App import OWLEngine
import composite_response
import planning_algorithms
import json
import os
import sys
import time
import subprocess
import shutil
import datetime
from pprint import pprint

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
    #FULL_PATH_CLINGO_EXECUTATBLE = os.path.join(os.getcwd(),"Clingo","clingo-python")

    # Function
    def prepareDistinguish_Input_Output_Folder_PerEachProcess(self):
        current = time.time()
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
                ]
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
            
        except Exception, err:
            print err
            number_of_models = 1
            engine = 1
  
        # Step 2 : parser input/output
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

        # Step 3 : Write input/output to ASP files
        folder_name = self.prepareDistinguish_Input_Output_Folder_PerEachProcess()
        print folder_name
        fo = open(os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),"wb")
        print("---Create Initial State--")
        fo.write("%------------------------------------------------------------------------\n")
        fo.write("% INPUT PART : Initial State\n")
        fo.write("%------------------------------------------------------------------------\n")
        for i in range(0,len(json_input_re)):
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
        for i in range(0,len(json_output_re)):
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

        
        if (len(json_output_re) == 1):
            if ("resource_speciesTree" in json_output_re[i]["resource_ontology_id"]):
                DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_9.lp")
            elif ("resource_reconcileTree" in json_output_re[i]["resource_ontology_id"]):
                DEFAULT_STEP =  os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")
        else:
            DEFAULT_STEP = os.path.join(os.getcwd(),"ASP_Planning" ,"step","step_12.lp")       
                
        # Step 3 : Run planning
        # Solution 1 : Run Multi-shot LP program
        if (engine == 1): # Solution 1 : Run simple Multi-shot LP program pick only 1
            if (number_of_models > 1):
                return return_response_error(303,"error","Engine 1 generated only one Plan with maximum QoS and It has not supported multiple models. Using Engine 2 in order to display more than one model ","JSON")

            planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Composite.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),DEFAULT_STEP,str(1))
            
            
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
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1)
                        if (json_output is not None):
                            return return_success_get_json(json_output)
                        else:
                            return return_response_error(403,"error","Data error","JSON")
                    else:
                        return return_response_error(400,"error","engine error","JSON")                   

        elif (engine == 2): # Solution 2 : Multi-shot LP Program with QoS External Calculation
            planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGO_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "program_multiple_workflows.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),DEFAULT_STEP,str(1))


        
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
                    json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,True,True,number_of_models)
                    if (json_output is not None):
                        return return_success_get_json(json_output)
                    else:
                        return return_response_error(403,"error","Data error","JSON")
                else:
                    return return_response_error(400,"error","engine error","JSON")

           
        elif (engine == 3): # Solutioon 3 : Run Clingcon-3.3.0 with QoS Internal Calculation - Ranking by the best QoS too
            if (number_of_models > 1):
                return return_response_error(303,"error","Engine 3 generated only one Plan with maximum QoS by CLINGCON. Using Engine 2 in order to display more than one model ","JSON")

            planing_data = OWLEngine.run_planning_engine(self.FULL_PATH_CLINGCON_EXECUTATBLE,os.path.join(self.FULL_PATH_PLANNING_ENGINE_MODEL, "Program_Composite_ForClingcon.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"initial_state_base.lp"),os.path.join(self.FULL_PATH_PLANNING_STATES_FOLDER, folder_name ,"goal_state_base.lp"),DEFAULT_STEP,str(1))
            
            
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
                    json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1)
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
                        json_output = composite_response.process_a_plan_json_from_raw(BIG_LIST_ANSWER_SETS,input_json,json_planning_data,qos=False,multi_plans=False,quantity=1)
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

        # Step 5 : Parser planning data to JSON workflow data


        # Step 6 : Return to requester
        #print "ABC"
    #public generate workflow
    generateWorkflow.exposed = True
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
                            'server.socket_port': 8000
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