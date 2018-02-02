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
def calculate_sim_matching_WF(WF_1,WF_2):
  return randint(0,200)
def calculate_sim_between_2_nodes(occur_node_1,index_1,occur_node_2,index_2):
  return similarity_matching.sim_between_2_nodes_raw_clingo(occur_node_1,index_1,occur_node_2,index_2)

def isConsideredPredicate(str_predicate,limits):
    for item in limits:
        if (item in str_predicate):
            return True
    return False

def get_CurrentModifying_Workflow(limits):
   # limits is list of predicate that want to store for new workflow
   '''
   result_list = []
   if (not limits):
       return WORKFLOW_1_RAW_BEAUTY
   for str_predicate in WORKFLOW_1_RAW_BEAUTY:
       if (isConsideredPredicate(str_predicate,limits)):
            result_list.append(str_predicate)
   return result_list
   '''
   #return ["occur(common_name_to_scientific_name,0)", "occur(taxon_to_species_by_country,1)", "occur(names_extraction_document,2)","occur(names_resolution_operation,3)","occur(phylogeny_based_extraction,4)","occur(tree_comparison,5)"]

   return ["occur(common_name_to_scientific_name,0)", "occur(taxon_to_species_by_country,1)", "occur(names_extraction_document,2)","occur(tree_comparison,3)"]


   #return ["occur(a,0)", "occur(b,1)", "occur(c,2)"]
   #return ["occur(a,0)", "occur(b,1)", "occur(c,2)","occur(d,3)","occur(e,4)","occur(f,5)"]
#---------------------------------------------------------- 

def main(prg):
  def run_original_planning(str_group_sim_nodes_rules):
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
      prg.add("similarity_index_calculation", [], str_group_sim_nodes_rules)
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
  def build_up_group_similarity_nodes_rules_C1():  #Simple occur and description only
      # Get old worklfow for occur only
      old_workflow = get_CurrentModifying_Workflow(limits=["occur("]) 
      generate_old_occur = ""
      for old_item in old_workflow:
          if "occur(" in old_item:
              generate_item = old_item.replace("occur(","old_occur(")
              generate_old_occur = generate_old_occur + "\n%s." %(str(generate_item))          

      single_sim_nodes_rule = "\nsingle_sim_2_nodes(X,Y,Z) :- old_occur(X,I1), occur(Y,I2), Z = @calculate_sim_between_2_nodes(X,I1,Y,I2)."       

      sum_sim_nodes_rule = "\nsum_single_sim_2_nodes(T) :- T = #sum {Z : single_sim_2_nodes(X,Y,Z)}."
      #sum_sim_nodes_rule = "\nsum_single_sim_2_nodes(T) :- T = #sum {Z,X,Y : single_sim_2_nodes(X,Y,Z)}."  

      sim_nodes_workflow_rule = "\nsim_nodes_workflows(R) :- sum_single_sim_2_nodes(T), N_Old_Nodes = #count {X,I1: old_occur(X,I1)}, N_New_Nodes = #count {Y,I2 : occur(Y,I2)}, R = 2*T / (N_Old_Nodes + N_New_Nodes)."

      #sim_nodes_workflow_rule = "\nsim_nodes_workflows(R) :- T = #sum {P,M,N : single_sim_2_nodes(M,N,P)}, N_Old_Nodes = #count {X,I1: old_occur(X,I1)}, N_New_Nodes = #count {,I2 : occur(Y,I2)}, R = 2*T / (N_Old_Nodes + N_New_Nodes)."  

      full_sim_nodes_cal = generate_old_occur + single_sim_nodes_rule + sum_sim_nodes_rule  + sim_nodes_workflow_rule

      #full_sim_nodes_cal = generate_old_occur + single_sim_nodes_rule  + sim_nodes_workflow_rule
      
      return full_sim_nodes_cal
  
  #################################################
  def re_composition_with_preference(prg):
      print("--> Start Re-Composition : \n")
      answer_sets = []
      str_group_sim_nodes_rules = build_up_group_similarity_nodes_rules_C1()
      
      print "\n"
      print str_group_sim_nodes_rules
      print "\n"

      print("---->Original Planning + New Preference : START------")
      answer_sets = run_original_planning(str_group_sim_nodes_rules)
      print("---->Original Planning + New Preference : DONE------\n")
      # Read the final results : RE-composision collection to work on Similarity
      return answer_sets
  #----------------------------------------
  re_composition_with_preference(prg)
#end.

#show single_sim_2_nodes/3.
#show sum_single_sim_2_nodes/1.
#show sim_nodes_workflows/1.