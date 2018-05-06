import subprocess
import json
import sys
import os

def run_CURL_planning_engine_service(planning_service_url,data):
    
    #p = subprocess.Popen(['curl -X POST', planning_service_url,'-H "content-type:application/json" -d',data], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p = subprocess.Popen(['curl -X POST "http://127.0.0.1:8000/planningEngine/generateWorkflow" -H "content-type:application/json" -d {}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print err
    return out

 

