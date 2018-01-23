#script (python)

import clingo
from random import *

def sim_matching(WF_1,WF_2):
  return randint(100,999)

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


def main(prg):
  def check_answer_set(clingo_model):
      print("Oh, new model : ")
      print clingo_model
      # try to modify program
      program = "hello"
      prg.add(program, [], "check_modification_program(1).")
      prg.ground([(program,[])])

  def re_composition_with_preference(prg):
      print("Try to recomposition here")
      # Load required file - Difference with planning is PREFERENCE file contains which things to change
      prg.load("test_vv.lp")

      # Re planning again based on planning - 2 loops abtract and concrete
      base_program = [("base", [])]
      prg.ground(base_program)
      prg.solve()
      print("Done")

      # Read the final results : RE-composision collection to work on Similarity

  def build_sim_selection_choice_rule():
      content_rule = ""
      # Similate data
      old_workflow = get_CurrentModifying_Workflow()
      
      # re_composition_with_preference(prg)

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
  # prg.solve(on_model=check_answer_set)
  prg.solve()
  
#end.

selected_sim_workflow(Y) :- sim_index(X,Y,Z).
hightest_sim_index(Z) :- sim_index(X,Y,Z).

#show selected_sim_workflow/1.
#show hightest_sim_index/1.

