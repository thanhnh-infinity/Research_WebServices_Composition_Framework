#script (python)
import clingo
import json
import sys
import time

import similarity_matching

from random import *

#-------------FOR ORIGINAL PLANNING-------------------------
def generate_MatchProblemID(O,DF_IN,T2,I,DF_OUT,T3):
    return clingo.Function(O.name + "_" + DF_IN.name + "_" + str(T2.number) + "_" + I.name + "_" + DF_OUT.name + "_" + str(T3.number))

# Generate 1{not a; not b;...}.
def build_no_op_rule_for_predicate_With_Active(answer_set_symbols,predicate_name,index,level):
    if ("concrete" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_concrete(%d)."
    elif ("abstract" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_abstract(%d)."

    component_rule = ""
    for atom in answer_set_symbols:
        str_atom = str(atom)
        #if (predicate_name in str_atom):
        if (atom.name == predicate_name):
            component_rule = component_rule + "not " + str_atom + "; "
    component_rule = component_rule[:len(component_rule)-2]
    return contrains_distince_wf_rule %(component_rule,index)
#----------------------------------------------------------    

#-------------FOR RE PLANNING-------------------------
def sim_matching(WF_1,WF_2):
  return similarity_matching.sim_workflows(WF_1,WF_2)

def generateBeautyString(symbol):
    name = symbol.name + "("
    arguments = symbol.arguments
    index = 0
    for arg in arguments:
        if (index == 0):
          name = name + arg.name
        else:
          name = name + "," + arg.name 
        index = index + 1  
    name = name + ")"
    return name

def convertListOccursToPredicate(list):
  result = ""
  new_list = []
  for item in list:
      item = clingo.Function(str(item))
      new_list.append(item)
  return clingo.Function("workflow",new_list)

def generateListOfAction(string):
  raw_items = string.name.split("__s__")
  list = []
  for raw_item in raw_items:
      if raw_item:
        beauty_item = raw_item.replace("__t__","(")
        beauty_item = beauty_item.replace("__f__",")")
        beauty_item = beauty_item.replace("__c__",",")
        list.append(beauty_item)
  return clingo.String(list)

def generateFunctionListOfAction(string):
  raw_items = string.name.split("__s__")
  list = []
  for raw_item in raw_items:
      if raw_item:
        beauty_item = raw_item.replace("__t__","(")
        beauty_item = beauty_item.replace("__f__",")")
        beauty_item = beauty_item.replace("__c__",",")
        list.append(clingo.Function(beauty_item))
  return clingo.Function("workflow",list)

def get_CurrentModifying_Workflow():
   return ["occur(a,1)", "occur(b,2)", "occur(c,3)"]

#---------------------------------------------------------- 

def main(prg):
  def run_original_planning():
      final_answer_set_result = []
      def load_asp(clingo_control):
            clingo_control.load("main_program.lp")
            clingo_control.load("planning_TESTING.lp")
            clingo_control.load("ontology_TESTING.lp")
            clingo_control.load("concrete_TESTING.lp")
            clingo_control.load("concrete_DF_convert.lp")
            clingo_control.load("configuration.lp")
            clingo_control.load("planning_preference.lp")
            clingo_control.load("re_planning_preference.lp")

      def enable_active_rule_for_subprogram(clingo_control,multishot_id,level):
          external_name = ""
          if ("concrete" in level):
              external_name = "active_rule_concrete"
          elif ("abstract" in level):
              external_name = "active_rule_abstract"
          clingo_control.assign_external(clingo.Function(external_name, [multishot_id]), True)
      def disable_active_rule_for_subprogram(clingo_control,multishot_id,level):
          external_name = ""
          if ("concrete" in level):
              external_name = "active_rule_concrete"
          elif ("abstract" in level):
              external_name = "active_rule_abstract"
          clingo_control.release_external(clingo.Function(external_name, [multishot_id]))
      def solve_iter(clingo_control):
          symbols = []
          with clingo_control.solve(yield_=True,on_model=real_time_check_model) as handle:
            for m in handle:
               symbols = m.symbols(shown=True)
          return symbols

      def real_time_check_model(clingo_model):
          print ("--------oh, new model")
          #print clingo_model

      clingo_control = clingo.Control()
      # Load another components
      load_asp(clingo_control)
      # Configuration for the ASP solver
      
      base_program = [("base", [])]

      loop = 1
      multi_shot_id = 1
      super_index = 1

      # Star to find 1st answer set
      t0 = time.time()
      print("---Start grounding---")
      clingo_control.ground(base_program)
      print("---End grounding---")
      t1 = time.time()
      print("---Time : %s ms" %(str(t1 - t0)))
      answer_set_abstract = []

      enable_active_rule_for_subprogram(clingo_control,1,"abstract")
      while (True): # outter loop for abstract
          print ("Chay vong lon")
          if (multi_shot_id == 1):
              answer_set_abstract = []
              with clingo_control.solve(yield_=True,on_model=real_time_check_model) as handle:
                  for m in handle:
                      answer_set_abstract = m.symbols(shown=True)

              answer_set_symbols = []
              for x in answer_set_abstract:
                  answer_set_symbols.append(x)

              #print answer_set_symbols
              if (len(answer_set_symbols) > 0):
                  final_answer_set_result.append(answer_set_symbols)
          else:
              multi_shot_sub_prg_name_abstract = "multi_shot_abstract_%d" %(multi_shot_id)
              check_rule_define_abstract = "check_add_abstract_ok(%d) :- active_rule_abstract(%d)." %(multi_shot_id,super_index)

              # Build choice rule with active_rule control
              contrains_distince_wf_rule_abstract = build_no_op_rule_for_predicate_With_Active(answer_set_abstract,"occur",super_index,"abstract")

              # Add choice rule with active control to program
              clingo_control.add(multi_shot_sub_prg_name_abstract, [], contrains_distince_wf_rule_abstract  + check_rule_define_abstract)
              clingo_control.ground([(multi_shot_sub_prg_name_abstract, [])])

              # Solve updated program

              answer_set_abstract = []
              answer_set_abstract = solve_iter(clingo_control)

              if (answer_set_abstract is None or len(answer_set_abstract) <=0):
                  break

              answer_set_symbols = []
              for x in answer_set_abstract:
                  answer_set_symbols.append(x)
              if (len(answer_set_symbols) > 0):
                  final_answer_set_result.append(answer_set_symbols)

          loop = 1
          enable_active_rule_for_subprogram(clingo_control,multi_shot_id,"concrete")
          while (True): # Inner loop for concrete
              print "-----Chay nho hon-----"
              if (answer_set_symbols is None or len(answer_set_symbols) <= 0):
                  break
              multi_shot_sub_prg_name = "multi_shot_concrete_%d_%d" %(multi_shot_id,loop)
              check_rule_define = "check_add_concrete_ok(%d,%d) :- active_rule_concrete(%d)." %(multi_shot_id,loop,multi_shot_id)

              # Build choice rule with active_rule control
              contrains_distince_wf_rule = build_no_op_rule_for_predicate_With_Active(answer_set_symbols,"occur_concrete",multi_shot_id,"concrete")

              # Add choice rule with active control to program
              clingo_control.add(multi_shot_sub_prg_name, [], contrains_distince_wf_rule  + check_rule_define)
              clingo_control.ground([(multi_shot_sub_prg_name, [])])

              # Solve updated program
              answer_set_symbols = []
              answer_set_symbols = solve_iter(clingo_control)
              #print answer_set_symbols
              if (len(answer_set_symbols) > 0):
                  final_answer_set_result.append(answer_set_symbols)

              loop = loop + 1
          #disable_active_rule_for_subprogram(clingo_control,multi_shot_id,"concrete")
          multi_shot_id = multi_shot_id + 1
          #break
      disable_active_rule_for_subprogram(clingo_control,super_index,"abstract")    
      return final_answer_set_result

  #-----------FOR RE-PLANNING----------- 
  def re_composition_with_preference(prg):
      print("Try to recomposition here")
      # Load required files - Difference with planning is PREFERENCE file contains which things to change
      print("ORIGINAL_PLANNING + PREFERENCE : START------")
      answer_sets = run_original_planning()
      print (len(answer_sets))
      for set in answer_sets:
          print set
          print "\n"
      print "\n"
      print("ORIGINAL_PLANNING + PREFERENCE : DONE------\n")

      # Read the final results : RE-composision collection to work on Similarity

  def build_sim_selection_choice_rule():
      content_rule = ""
      # Similate data
      old_workflow = get_CurrentModifying_Workflow()
      
      re_composition_with_preference(prg)

      new_set_workflows = [["occur(x,1)", "occur(y,2)", "occur(z,3)"],
                           ["occur(m,1)", "occur(n,2)", "occur(p,3)"],
                           ["occur(h,1)", "occur(i,2)", "occur(k,3)"],
                          ]
      index = 0
      for new_workflow in new_set_workflows:
          sim_index = sim_matching(old_workflow,new_workflow)
          str_predicate_old_workflow = generateBeautyString(convertListOccursToPredicate(old_workflow))
          str_predicate_new_workflow = generateBeautyString(convertListOccursToPredicate(new_workflow))
          rule_sim_index = "sim_index(%s,%s,%d)" %(str(str_predicate_old_workflow),str(str_predicate_new_workflow),int(sim_index)) 
          if (index == 0):
               content_rule = rule_sim_index  
          else:
               content_rule = content_rule + ";" + rule_sim_index  
          index = index + 1
              

      constrain_rule = "1{%s}1."
      constrain_rule = constrain_rule %(content_rule)
      return constrain_rule
  #Register base program    
  base_program = [("base", [])]
  prg.ground(base_program)

  #Register program working with sim index
  program = "test"
  constraint_rule = build_sim_selection_choice_rule()
  print "ThanhNH : " + constraint_rule
  prg.add(program, [], constraint_rule + "\n#maximize{Z:sim_index(X,Y,Z)}.") 
  
  # Ground all programs to find Answer Set
  prg.ground([("base", []),(program, [])])
  prg.solve()
  #----------------------------------------
#end.

selected_sim_workflow(Y) :- sim_index(X,Y,Z).
hightest_sim_index(Z) :- sim_index(X,Y,Z).

#show selected_sim_workflow/1.
#show hightest_sim_index/1.

