%-------------------------------------------------
% Multiple shoot solving
%-------------------------------------------------
#script (python)
import clingo
import time
from random import *
import similarity_matching
import sys
import os
import json
import collections
from pprint import pprint
#----------------------------------------------------------    
GLOBAL_BEST_MATCH_WORKFLOW = []
GLOBAL_HIGHEST_SIM_INDEX = -9999999
OLD_WORKFLOW = []

#----------------------------------------------------------    
class MultipleLevelsOfDictionary(collections.OrderedDict):
    def __getitem__(self,item):
        try:
            return collections.OrderedDict.__getitem__(self,item)
        except:
            value = self[item] = type(self)()
            return value
#---------------------------------------------------------- 
# Generate 1{not a; not b;...}.
def build_no_op_rule_for_predicate_With_Active(answer_set_symbols,predicate_name,index,level):
    if ("concrete" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_concrete(%d)."
    elif ("abstract" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_abstract(%d)."
    elif ("single_level" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_single_level(%d)."

    component_rule = ""
    for atom in answer_set_symbols:
        str_atom = str(atom)
        #if (predicate_name in str_atom):
        if (atom.name == predicate_name):
            component_rule = component_rule + "not " + str_atom + "; "
    component_rule = component_rule[:len(component_rule)-2]
    return contrains_distince_wf_rule %(component_rule,index)
#-------------FOR RE PLANNING-------------------------
def sim_matching(WF_1,WF_2):
  return similarity_matching.sim_workflows(WF_1,WF_2,"CLINGO_MODELS")
  #return randint(1000,2000) 
def get_CurrentModifying_Workflow(prg,old_wf):
  try:
      if (len(old_wf) <= 0):
          print("READ ONLY ONE")
          folder = str(prg.get_const("folder").string)
          original_workflowfile_name = os.path.join(os.getcwd(),"ASP_Planning","states",folder,"original_workflow_data.json")
          with open(original_workflowfile_name) as f:
               content = f.readlines()
          old_wf = [x.strip() for x in content]
          print(old_wf)
      return old_wf
  except  Exception as inst:
      print(inst)
      return []
#---------------------------------------------------------- 
def main(prg):
    def run_original_planning_with_sim_index(prg):
        final_answer_set_result = []
        def enable_active_rule_for_subprogram(prg,multishot_id,level):
            external_name = ""
            if ("concrete" in level):
                external_name = "active_rule_concrete"
            elif ("abstract" in level):
                external_name = "active_rule_abstract"
            elif ("single_level" in level):
                external_name = "active_rule_single_level"
            prg.assign_external(clingo.Function(external_name, [multishot_id]), True)
        def disable_active_rule_for_subprogram(prg,multishot_id,level):
            external_name = ""
            if ("concrete" in level):
                external_name = "active_rule_concrete"
            elif ("abstract" in level):
                external_name = "active_rule_abstract"
            elif ("single_level" in level):
                external_name = "active_rule_single_level"
            prg.release_external(clingo.Function(external_name, [multishot_id]))
        def solve_iter(prg):
            symbols = []
            with prg.solve(yield_=True,on_model=real_time_check_model) as handle:
              for m in handle:
                 symbols = m.symbols(shown=True)
                 #symbols = m.symbols()
            return symbols
        def real_time_check_model(clingo_model):
            global GLOBAL_BEST_MATCH_WORKFLOW
            global GLOBAL_HIGHEST_SIM_INDEX
            global OLD_WORKFLOW
        
            OLD_WORKFLOW = get_CurrentModifying_Workflow(prg,OLD_WORKFLOW) 
        

            new_workflow = []
            for atom in clingo_model.symbols(shown=True):
                new_workflow.append(atom)
            sim_index = sim_matching(OLD_WORKFLOW,new_workflow)
            current_highest_sim = GLOBAL_HIGHEST_SIM_INDEX
            if (sim_index > current_highest_sim):
               GLOBAL_HIGHEST_SIM_INDEX = sim_index
               GLOBAL_BEST_MATCH_WORKFLOW = new_workflow
            
            #print "New : "
            #print new_workflow 
            #print "current sim index : " + str(sim_index)
         
            #print "\n=================================================="    
        def load_asp(prg):
            prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","single_level_planning_Working.lp"))
            prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","ontology_TESTING_Working.lp"))
      
        # Load another components
        load_asp(prg)
        # Configuration for the ASP solver

        base_program = [("base", [])]

        loop = 1
        multi_shot_id = 1
        super_index = 1

        # Star to find 1st answer set
        t0 = time.time()
        #print("---Start grounding---")
        prg.ground(base_program)
        #print("---End grounding---")
        t1 = time.time()
        #print("---Time : %s ms" %(str(t1 - t0)))
        enable_active_rule_for_subprogram(prg,1,"single_level")
        while (True):     
            if (multi_shot_id == 1):
                answer_sets = []
                with prg.solve(yield_=True,on_model=real_time_check_model) as handle:
                    for m in handle:
                        answer_sets = m.symbols(shown=True)

                answer_set_symbols = []
                for x in answer_sets:
                    answer_set_symbols.append(x)

            else:
                multi_shot_sub_prg_name_single_level = "multi_shot_single_level_%d" %(multi_shot_id)
                check_rule_define_single_level = "check_add_single_level_ok(%d) :- active_rule_single_level(%d)." %(multi_shot_id,super_index)

                # Build choice rule with active_rule control
                contrains_distince_wf_rule_single_level = build_no_op_rule_for_predicate_With_Active(answer_sets,"occur",super_index,"single_level")

                # Add choice rule with active control to program
                prg.add(multi_shot_sub_prg_name_single_level, [], contrains_distince_wf_rule_single_level  + check_rule_define_single_level)
                prg.ground([(multi_shot_sub_prg_name_single_level, [])])

                # Solve updated program

                answer_sets = []
                answer_sets = solve_iter(prg)

                if (answer_sets is None or len(answer_sets) <=0):
                    break

                answer_set_symbols = []
                for x in answer_sets:
                    answer_set_symbols.append(x)

                if (len(answer_set_symbols) > 0):
                  final_answer_set_result.append(answer_set_symbols)    
            multi_shot_id = multi_shot_id + 1
        disable_active_rule_for_subprogram(prg,super_index,"single_level")
        return final_answer_set_result
    #-----------FOR RE-PLANNING----------- 
    def re_composition_with_preference(prg):
      print("--> Start Re-Composition : \n")
      answer_sets = []
      print("---->Original Planning + New Preference : START------")
      answer_sets = run_original_planning_with_sim_index(prg)
      print("---->Original Planning + New Preference : DONE------\n")


      d = MultipleLevelsOfDictionary()
      data = MultipleLevelsOfDictionary()
      workflows_list = []
      print("====START-RESULT-THE-BEST-MATCH=====")
      TEMP_WORKFLOW = []
      for item in GLOBAL_BEST_MATCH_WORKFLOW:
          TEMP_WORKFLOW.append(str(item))
      d['workflow'] = TEMP_WORKFLOW
      d['sim_index'] = GLOBAL_HIGHEST_SIM_INDEX
      workflows_list.append(d)
      data['workflows_list'] = workflows_list
      print(json.dumps(data))
      print("====END-RESULT-THE-BEST-MATCH======\n")
     
      # Read the final results : RE-composision collection to work on Similarity
      return GLOBAL_BEST_MATCH_WORKFLOW,GLOBAL_HIGHEST_SIM_INDEX
    #----------------------------------------
    re_composition_with_preference(prg)
#end.
#const folder = "ACS".
%-----------------------------------------------
#external active_rule_single_level(1).
%-----------------------------------------------