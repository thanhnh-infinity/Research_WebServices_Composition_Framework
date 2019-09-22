%-------------------------------------------------
% Multiple shoot solving
%-------------------------------------------------
#script (python)
import clingo
import time
import composite_parser
import similarity_matching
from random import *
import sys
import os
#----------------------------------------------------------    

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

#-------------FOR RE PLANNING-----------------------------
def calculate_sim_matching_WF(WF_1,WF_2):
  return randint(0,200)
def calculate_sim_between_2_nodes(occur_node_1,index_1,occur_node_2,index_2):
  #print("ABC")
  return similarity_matching.sim_between_2_nodes_raw_clingo(occur_node_1,index_1,occur_node_2,index_2)
  #return randint(0,100)

def isConsideredPredicate(str_predicate,limits):
    for item in limits:
        if (item in str_predicate):
            return True
    return False

def get_CurrentModifying_Workflow(prg):
  old_wf = []
  try:
      if (len(old_wf) <= 0):
          #print "READ ONLY ONE"
          #folder = str(prg.get_const("folder").string)
          folder = str(prg.get_const("folder"))
          #print(folder)
          original_workflowfile_name = os.path.join(os.getcwd(),"ASP_Planning","states",folder,"original_workflow_data.json")
          with open(original_workflowfile_name) as f:
               content = f.readlines()
          old_wf = [x.strip() for x in content]
          #print old_wf
      return old_wf
  except:
      #print err
      return []
#------------------------------------------------------------
def main(prg):
    def run_original_planning_with_sim_index(prg,str_group_sim_nodes_rules):
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
            with prg.solve(yield_=True) as handle:
              for m in handle:
                 symbols = m.symbols(shown=True)
            return symbols
        
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
        #print("---Start grounding --> Base Program ---")
        prg.ground(base_program)
        #print("---End grounding --> Base Program ---")
        t1 = time.time()
        #print("---Time : %s ms" %(str(t1 - t0)))
        
        # Add SIMILARITY INDEX RULE to active Internal Optimization
        # print("ADD");
        prg.add("similarity_index_calculation", [], str_group_sim_nodes_rules)
        
        #print("---Start grounding --> SimCal Program ---") 
        # print("Ground")
        prg.ground([("similarity_index_calculation", [])])
        #print("---End grounding --> SimCal Program ---")    

        prg.solve()
            

    #-----------FOR RE-COMPOSITION-----------
    def generate_old_occur_string(old_workflow):
        #Step 1 : Find goald
        int_goal = -1
        for predicate in old_workflow:
            if "goal(" in str(predicate):
                int_goal = composite_parser.parse_goal_in_predicate(predicate)

        #Step 2 : Loop and generate
        generate_old_occur = ""
        for predicate in old_workflow:
            if "occur(" in str(predicate):
                service,index_occur = composite_parser.parse_a_occur_service(predicate)
                if (index_occur < int_goal):
                    generate_old_occur = generate_old_occur + "\nold_occur(%s,%d)." %(str(service),index_occur)
        return generate_old_occur

    def build_up_group_similarity_nodes_rules_C1(prg):  #Simple occur and description only
        # Get old worklfow for occur only

        old_workflow = get_CurrentModifying_Workflow(prg) 
        generate_old_occur = generate_old_occur_string(old_workflow)

        single_sim_nodes_rule = "\nsingle_sim_2_nodes(X,Y,Z) :- old_occur(X,I1), occur(Y,I2), goal(G), I2 < G, Z = @calculate_sim_between_2_nodes(X,I1,Y,I2)."       

        sum_sim_nodes_rule = "\nsum_single_sim_2_nodes(T) :- T = #sum {Z : single_sim_2_nodes(X,Y,Z)}."
        #sum_sim_nodes_rule = "\nsum_single_sim_2_nodes(T) :- T = #sum {Z,X,Y : single_sim_2_nodes(X,Y,Z)}."  

        sim_nodes_workflow_rule = "\nsim_nodes_workflows(R) :- sum_single_sim_2_nodes(T), N_Old_Nodes = #count {X,I1: old_occur(X,I1)}, N_New_Nodes = #count {Y,I2 : occur(Y,I2)}, R = 2*T / (N_Old_Nodes + N_New_Nodes)."

        #sim_nodes_workflow_rule = "\nsim_nodes_workflows(R) :- T = #sum {P,M,N : single_sim_2_nodes(M,N,P)}, N_Old_Nodes = #count {X,I1: old_occur(X,I1)}, N_New_Nodes = #count {,I2 : occur(Y,I2)}, R = 2*T / (N_Old_Nodes + N_New_Nodes)."  

        maximize_rule = "\n#maximize{R : sim_nodes_workflows(R)}."
        #maximize_rule = ""

        full_sim_nodes_cal = generate_old_occur + single_sim_nodes_rule + sum_sim_nodes_rule  + sim_nodes_workflow_rule + maximize_rule

        #full_sim_nodes_cal = generate_old_occur + single_sim_nodes_rule  + sim_nodes_workflow_rule
          
        return full_sim_nodes_cal
    #################################################
    def re_composition_with_preference(prg):
        #print("--> Start Re-Composition : \n")
        str_group_sim_nodes_rules = build_up_group_similarity_nodes_rules_C1(prg)
        
        #print("\n")
        #print(str_group_sim_nodes_rules)
        #print("\n")

        #print("---->Original Planning + New Preference : START------")
        run_original_planning_with_sim_index(prg,str_group_sim_nodes_rules)
        #print("---->Original Planning + New Preference : DONE------\n")
        
    #----------------------------------------
    re_composition_with_preference(prg)
#end.
%-----------------------------------------------
#external active_rule_single_level(1).
#const folder = "ACS".
%-----------------------------------------------
%#show single_sim_2_nodes/3.
#show sum_single_sim_2_nodes/1.
#show sim_nodes_workflows/1.