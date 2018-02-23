#script (python)
import clingo
import json
import sys
import time
import similarity_matching
import test
from random import *

WORKFLOW_1_RAW_BEAUTY = ["occur(names_resolution_operation,3)","occur(tree_reconciliation,5)","occur(phylogeny_based_extraction,4)","occur(gene_based_extraction,0)","occur(gene_tree_scaling,2)","occur(names_extraction_tree,1)","occur_concrete(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,1)","occur_concrete(phylotastic_ResolvedScientificNames_OT_TNRS_GET,3)","occur_concrete(phylotastic_GetPhylogeneticTree_Phylomatic_POST,4)","occur_concrete(phylotastic_GenerateGeneTree_From_Genes,0)","occur_concrete(phylotastic_GeneTree_Scaling,2)","occur_concrete(phylotastic_GetReconciliationTree_GET,5)","occur_convert_op_instance(example_convert_names_format_from_2_to_4,3,resource_SetOfSciName_names_format_2_1_resource_SetOfSciName_names_format_resolved_OT_3,0)","occur_convert_op_instance(example_convert_names_format_from_4_to_6,3,resource_SetOfSciName_names_format_2_1_resource_SetOfSciName_names_format_resolved_OT_3,1)","occur_convert_op_instance(example_convert_names_format_from_6_to_names_format_resolved_OT,3,resource_SetOfSciName_names_format_2_1_resource_SetOfSciName_names_format_resolved_OT_3,2)","occur_convert_op_instance(example_convertTreeFormat_r_to_NewickTree,5,resource_speciesTree_nmsu_tree_format_4_resource_speciesTree_newickTree_5,0)","occur_convert_op_instance(ex_convertTreeFormat_1_to_2,1,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_1,0)","occur_convert_op_instance(ex_convertTreeFormat_1_to_2,2,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_2,0)","occur_convert_op_instance(ex_convertTreeFormat_1_to_2,5,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_5,0)","occur_convert_op_instance(ex_convertTreeFormat_2_to_3,5,resource_geneTree_tree_format_2_2_resource_geneTree_newickTree_5,0)","occur_convert_op_instance(ex_convertTreeFormat_2_to_3,1,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_1,1)","occur_convert_op_instance(ex_convertTreeFormat_2_to_3,2,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_2,1)","occur_convert_op_instance(ex_convertTreeFormat_2_to_3,5,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_5,1)","occur_convert_op_instance(ex_convertTreeFormat_3_to_Newick,1,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_1,2)","occur_convert_op_instance(ex_convertTreeFormat_3_to_Newick,2,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_2,2)","occur_convert_op_instance(ex_convertTreeFormat_3_to_Newick,5,resource_geneTree_tree_format_1_0_resource_geneTree_newickTree_5,2)","occur_convert_op_instance(ex_convertTreeFormat_3_to_Newick,5,resource_geneTree_tree_format_2_2_resource_geneTree_newickTree_5,2)","occur_convert_op_instance(ex_convertTreeFormat_3_to_Phylo4Tree,5,resource_geneTree_tree_format_2_2_resource_geneTree_newickTree_5,1)","has_input_occur_service_class(names_resolution_operation,set_of_names_1,resource_SetOfSciName)","has_input_occur_service_class(names_extraction_tree,tree_1,resource_geneTree)","has_input_occur_service_class(tree_reconciliation,tree_1,resource_speciesTree)","has_input_occur_service_class(tree_reconciliation,tree_2,resource_geneTree)","has_input_occur_service_class(phylogeny_based_extraction,set_of_names_1,resource_SetOfResolvedName)","has_input_occur_service_class(gene_based_extraction,set_of_genes_1,resource_SetOfGeneStrings)","has_input_occur_service_class(gene_tree_scaling,phylo_tree_1,resource_geneTree)","has_output_occur_service_class(names_resolution_operation,set_of_names_1,resource_SetOfTaxon)","has_output_occur_service_class(names_resolution_operation,http_code_1,resource_HTTPCode)","has_output_occur_service_class(names_resolution_operation,set_of_names_1,resource_SetOfResolvedName)","has_output_occur_service_class(tree_reconciliation,tree_3,resource_reconcileTree)","has_output_occur_service_class(phylogeny_based_extraction,phylo_tree_1,resource_speciesTree)","has_output_occur_service_class(phylogeny_based_extraction,http_code_1,resource_HTTPCode)","has_output_occur_service_class(gene_based_extraction,phylo_tree_1,resource_geneTree)","has_output_occur_service_class(gene_based_extraction,phylo_tree_2,resource_geneTree)","has_output_occur_service_class(gene_tree_scaling,phylo_tree_2,resource_geneTree)","has_output_occur_service_class(tree_reconciliation,phylo_tree_1,resource_Tree)","has_output_occur_service_class(names_extraction_tree,set_of_names_1,resource_SetOfSciName)","has_output_occur_service_class(names_extraction_tree,http_code_1,resource_HTTPCode)","has_output_occur_service_class(names_extraction_tree,connection_time_1,resource_ConnectionTime)","match_occur_service_class(names_resolution_operation,resource_SetOfSciName,3,names_extraction_tree,resource_SetOfSciName,2)","match_occur_service_class(names_extraction_tree,resource_geneTree,1,gene_based_extraction,resource_geneTree,1)","match_occur_service_class(tree_reconciliation,resource_speciesTree,5,phylogeny_based_extraction,resource_speciesTree,5)","match_occur_service_class(tree_reconciliation,resource_geneTree,5,gene_based_extraction,resource_geneTree,1)","match_occur_service_class(tree_reconciliation,resource_geneTree,5,gene_tree_scaling,resource_geneTree,3)","match_occur_service_class(phylogeny_based_extraction,resource_SetOfResolvedName,4,names_resolution_operation,resource_SetOfResolvedName,4)","match_occur_service_class(gene_tree_scaling,resource_geneTree,2,gene_based_extraction,resource_geneTree,1)","match_occur_service_class(gene_based_extraction,resource_SetOfGeneStrings,0,initial_state,resource_SetOfGeneStrings,0)"]

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
  return similarity_matching.sim_workflows(WF_1,WF_2,"CLINGO_MODELS")
def calculate_sim_matching(WF_1,WF_2):
  return randint(100,500)
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

def convertListOccursToPredicate_2(list_of_atoms):
  # Limit atoms appear in list to easy to view
  '''
  final_list = []
  for atom in list_of_atoms:
      if ("occur(" in atom or "occur_concrete" in atom):
          final_list.append(clingo.Function(atom))
  '''        
  return clingo.Function("workflow",list_of_atoms)


def get_CurrentModifying_Workflow():
   #return ["occur(a,0)", "occur(b,1)", "occur(c,2)"]
   return ["occur(a,0)", "occur(b,1)", "occur(c,2)","occur(d,3)"]
   #return ["occur(a,0)", "occur(b,1)", "occur(c,2)","occur(d,3)","occur(e,4)","occur(f,5)"]
   #return WORKFLOW_1_RAW_BEAUTY

#---------------------------------------------------------- 

def main(prg):
  def run_original_planning(str_group_sim_rules):
      final_answer_set_result = []
      def load_asp(prg):
            prg.load("main_program.lp")
            prg.load("planning_TESTING.lp")
            prg.load("ontology_TESTING.lp")
            prg.load("concrete_TESTING.lp")
            prg.load("concrete_DF_convert.lp")
            prg.load("configuration.lp")
            prg.load("planning_preference.lp")
            prg.load("re_planning_preference.lp")

      def enable_active_rule_for_subprogram(prg,multishot_id,level):
          external_name = ""
          if ("concrete" in level):
              external_name = "active_rule_concrete"
          elif ("abstract" in level):
              external_name = "active_rule_abstract"
          prg.assign_external(clingo.Function(external_name, [multishot_id]), True)
      def disable_active_rule_for_subprogram(prg,multishot_id,level):
          external_name = ""
          if ("concrete" in level):
              external_name = "active_rule_concrete"
          elif ("abstract" in level):
              external_name = "active_rule_abstract"
          prg.release_external(clingo.Function(external_name, [multishot_id]))
      def solve_iter(prg):
          symbols = []
          with prg.solve(yield_=True,on_model=real_time_check_model) as handle:
            for m in handle:
               symbols = m.symbols(shown=True)
          return symbols

      def real_time_check_model(clingo_model):
          print ("----------> new model")
          #print clingo_model
          print ("---------------------")

      # Load another components
      load_asp(prg)
      # Configuration for the ASP solver
      
      base_program = [("base", [])]

      loop = 1
      multi_shot_id = 1
      super_index = 1

      # Star to find 1st answer set
      t0 = time.time()
      print("---Start grounding---")
      prg.ground(base_program)
      print("---End grounding---")
      t1 = time.time()
      print("---Time : %s ms" %(str(t1 - t0)))
      answer_set_abstract = []

      # Add SIMILARITY INDEX RULE to active Internal Optimization
      prg.add("similarity_index_calculation", [], str_group_sim_rules)
      prg.ground([("similarity_index_calculation", [])])

      enable_active_rule_for_subprogram(prg,1,"abstract")
      while (True): # outter loop for abstract
          if (multi_shot_id == 1):
              answer_set_abstract = []
              with prg.solve(yield_=True,on_model=real_time_check_model) as handle:
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
              prg.add(multi_shot_sub_prg_name_abstract, [], contrains_distince_wf_rule_abstract  + check_rule_define_abstract)
              prg.ground([(multi_shot_sub_prg_name_abstract, [])])

              # Solve updated program

              answer_set_abstract = []
              answer_set_abstract = solve_iter(prg)

              if (answer_set_abstract is None or len(answer_set_abstract) <=0):
                  break

              answer_set_symbols = []
              for x in answer_set_abstract:
                  answer_set_symbols.append(x)
              if (len(answer_set_symbols) > 0):
                  final_answer_set_result.append(answer_set_symbols)

          loop = 1
          enable_active_rule_for_subprogram(prg,multi_shot_id,"concrete")
          while (True): # Inner loop for concrete
              
              if (answer_set_symbols is None or len(answer_set_symbols) <= 0):
                  break
              multi_shot_sub_prg_name = "multi_shot_concrete_%d_%d" %(multi_shot_id,loop)
              check_rule_define = "check_add_concrete_ok(%d,%d) :- active_rule_concrete(%d)." %(multi_shot_id,loop,multi_shot_id)

              # Build choice rule with active_rule control
              contrains_distince_wf_rule = build_no_op_rule_for_predicate_With_Active(answer_set_symbols,"occur_concrete",multi_shot_id,"concrete")

              # Add choice rule with active control to program
              prg.add(multi_shot_sub_prg_name, [], contrains_distince_wf_rule  + check_rule_define)
              prg.ground([(multi_shot_sub_prg_name, [])])

              # Solve updated program
              answer_set_symbols = []
              answer_set_symbols = solve_iter(prg)
              #print answer_set_symbols
              if (len(answer_set_symbols) > 0):
                  final_answer_set_result.append(answer_set_symbols)

              loop = loop + 1
          #disable_active_rule_for_subprogram(prg,multi_shot_id,"concrete")
          multi_shot_id = multi_shot_id + 1
          #break
      disable_active_rule_for_subprogram(prg,super_index,"abstract")    
      return final_answer_set_result

  #-----------FOR RE-COMPOSITION-----------
  ## Build Up the cach 1
  #----------------------------------------
  def build_up_old_workflow_represent(old_workflow):
      fomulation_string = "old_workflow(wf_data(%s))"
      wf_data = ""
      index = 0
      for atom in old_workflow:
          if (index == 0):
              wf_data = str(atom)
          else:
              wf_data = wf_data + "," + str(atom)
          index = index + 1
      return fomulation_string %(str(wf_data))

  def get_number_steps_old_workflow_pre(old_workflow):
      number = 0
      for atom in old_workflow:
          if atom.name() == "occur":
             number = number + 1
      return number    
      
  def get_number_steps_old_workflow_str(old_workflow):
      number = 0
      for atom in old_workflow:
          if ("occur(" in str(atom)):
             number = number + 1
      return number

  def generate_Predicates_for_New_Workflow(number_of_steps_in_old,max_steps,type):
      if (type == "FIT_OLD_STEPS_INDEXES"):
        predicates_content = ""
        for step in range(0,number_of_steps_in_old):
            if (step == 0):
                predicates_content = "occur(A%s,%s)" %(str(step),str(step))
                #predicates_content = "occur_concrete(A%s,%s)" %(str(step),str(step))
                #predicates_content = "occur(A%s,%s),occur_concrete(O%s,%s)" %(str(step),str(step),str(step),str(step))
            else:
                predicates_content = predicates_content + ",occur(A%s,%s)" %(str(step),str(step))
                #predicates_content = predicates_content + ",occur_concrete(A%s,%s)" %(str(step),str(step))
                #predicates_content = predicates_content + ",occur(A%s,%s),occur_concrete(O%s,%s)" %(str(step),str(step),str(step),str(step))
        formula_generatedPredicates_data = "new_workflow(wf_data(%s),%s) :- %s." %(str(predicates_content),str(number_of_steps_in_old),str(predicates_content))        
        return formula_generatedPredicates_data
      elif (type == "PERMUTE_0_TO_MAX_STEPS"):
        full_formula_predicates_content = ""
        for step_index in range(1,max_steps + 1):
            for step in range(0,step_index):
              if (step == 0):
                  predicates_content = "occur(A%s,%s)" %(str(step),str(step))
              else:
                  predicates_content = predicates_content + ",occur(A%s,%s)" %(str(step),str(step))
            formula_generatedPredicates_data = "\nnew_workflow(wf_data(%s),%s) :- %s." %(str(predicates_content),str(step_index),str(predicates_content))
            full_formula_predicates_content += formula_generatedPredicates_data
        return full_formula_predicates_content        
      else:
        return ""   

  def build_up_group_similarity_rules():
       # For old workflow
       old_workflow = get_CurrentModifying_Workflow()
       old_workflow_predicate = build_up_old_workflow_represent(old_workflow)
       old_workflow_fact = old_workflow_predicate + "."

       # For new workflow
       generatedPredicates_data = generate_Predicates_for_New_Workflow(get_number_steps_old_workflow_str(old_workflow),0,"FIT_OLD_STEPS_INDEXES")
       #generatedPredicates_data = generate_Predicates_for_New_Workflow(get_number_steps_old_workflow_str(old_workflow),6,"PERMUTE_0_TO_MAX_STEPS")

       # Rule for similarity calculation
       formula_sim_cal_rule = "sim_index(Y,Z) :- old_workflow(X), new_workflow(Y,Number_Steps), Z = @calculate_sim_matching(X,Y)."

       return "%s\n%s\n%s" % (str(old_workflow_fact),str(generatedPredicates_data),str(formula_sim_cal_rule))

  #------------------------------     
  ## Build up theo cach 2
  #------------------------------
  def build_up_old_workflow_represent_2(old_workflow):
      fomulation_string = "%s"
      wf_data = ""
      index = 0
      for atom in old_workflow:
          if (index == 0):
              wf_data = "old_" + str(atom)
          else:
              wf_data = wf_data + "," + "old_" + str(atom)
          index = index + 1
      return fomulation_string %(str(wf_data))     

  def generate_Predicates_for_New_Workflow_2(number_of_steps_in_old,max_steps,type):
      if (type == "FIT_OLD_STEPS_INDEXES"):
        predicates_content = ""
        for step in range(0,number_of_steps_in_old):
            if (step == 0):
                predicates_content = "occur(A%s,%s)" %(str(step),str(step))
            else:
                predicates_content = predicates_content + ",occur(A%s,%s)" %(str(step),str(step))
        formula_generatedPredicates_data = predicates_content      
        return formula_generatedPredicates_data
      elif (type == "PERMUTE_0_TO_MAX_STEPS"):
        return ""       
      else:
        return ""   
            
  def build_up_group_similarity_rules_2():
       # For old workflow
       old_workflow = get_CurrentModifying_Workflow()
       old_workflow_predicate = build_up_old_workflow_represent_2(old_workflow)
       old_workflow_fact = ""
       for atom in old_workflow:
           old_workflow_fact = old_workflow_fact + "\n" +  "old_" + str(atom) + "."

       # For new workflow
       generatedPredicates_data = generate_Predicates_for_New_Workflow_2(get_number_steps_old_workflow_str(old_workflow),0,"FIT_OLD_STEPS_INDEXES")
       #generatedPredicates_data = generate_Predicates_for_New_Workflow(get_number_steps_old_workflow_str(old_workflow),6,"PERMUTE_0_TO_MAX_STEPS")

       # Rule for similarity calculation
       #formula_sim_cal_rule = "sim_index((%s),Z) :- %s,%s,Z = @calculate_sim_matching((%s),(%s))." %(str(generatedPredicates_data),str(old_workflow_predicate),str(generatedPredicates_data),str(old_workflow_predicate),str(generatedPredicates_data))

       formula_sim_cal_rule = "sim_index((%s),Z) :- %s,%s,Z = @calculate_sim_matching((%s),(%s))." %(str(generatedPredicates_data),str(old_workflow_predicate),str(generatedPredicates_data),str(old_workflow_predicate),str(generatedPredicates_data))

       return "%s\n%s" % (str(old_workflow_fact),str(formula_sim_cal_rule))    
  #################################################
  def re_composition_with_preference(prg):
      print("--> Start Re-Composition : \n")
      answer_sets = []
      
      str_group_sim_rules = build_up_group_similarity_rules_2()
      #str_group_sim_rules = build_up_group_similarity_rules()
      
      print "\n"
      print str_group_sim_rules
      print "\n"

      print("---->Original Planning + New Preference : START------")
      answer_sets = run_original_planning(str_group_sim_rules)
      print("---->Original Planning + New Preference : DONE------\n")
      # Read the final results : RE-composision collection to work on Similarity
      return answer_sets
  #----------------------------------------
  re_composition_with_preference(prg)
#end.

%selected_sim_workflow(Y) :- sim_index(X,Y,Z).
%hightest_sim_index(Z) :- sim_index(X,Y,Z).

%#show selected_sim_workflow/1.
%#show hightest_sim_index/1.

%#maximize{Z:sim_index(Y,Z)}.

#show sim_index/2.
%#show new_workflow/2.

