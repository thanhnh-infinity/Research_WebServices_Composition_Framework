%-------------------------------------------------
% Multiple shoot solving
%-------------------------------------------------
#script (python)
import clingo
import time
from random import *
import similarity_matching
import sys
#----------------------------------------------------------    
GLOBAL_BEST_MATCH_WORKFLOW = []
GLOBAL_HIGHEST_SIM_INDEX = -9999999
#----------------------------------------------------------  
ORIGINAL_WORKFLOW = ["goal(11)", "occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,7)", "occur(phylotastic_GetPhylogeneticTree_OT_GET,8)", "occur(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,3)", "occur(phylotastic_GetReconciliationTree_GET,10)", "occur(phylotastic_GenerateGeneTree_From_Genes,0)", "occur(phylotastic_GenerateGeneTree_From_Genes,12)", "occur(convert_df_sci_names_format_2_to_4,4)", "occur(convert_df_sci_names_format_4_to_6,5)", "occur(convert_df_sci_names_format_6_to_OT,6)", "occur(convert_gene_tree_format_PhyloTree_to_NMSU,1)", "occur(convert_species_tree_format_NMSU_to_NewickTree,9)", "occur(convert_gene_tree_format_NMSU_to_NewickTree,2)", "map(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,phyloTree,1,phylotastic_GenerateGeneTree_From_Genes,resource_geneTree,phyloTree,1)", "map(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,nmsu_tree_format,2,convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,nmsu_tree_format,2)", "map(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_geneTree,newickTree,3,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)", "map(phylotastic_GetReconciliationTree_GET,resource_geneTree,newickTree,10,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)", "map(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_2,4,phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_SetOfSciName,raw_names_format_2,4)", "map(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_4,5,convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_4,5)", "map(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_6,6,convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_6,6)", "map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,7,convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_OT,7)", "map(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT,8,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,8)", "map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,9,phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format,9)", "map(phylotastic_GetReconciliationTree_GET,resource_speciesTree,newickTree,10,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,10)", "map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,0,initial_state,resource_SetOfGeneStrings,list_of_strings,0)", "map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,12,initial_state,resource_SetOfGeneStrings,list_of_strings,0)", "operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT)", "operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_input_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_geneTree,newickTree)", "operation_has_input_has_data_format(phylotastic_GetReconciliationTree_GET,resource_geneTree,newickTree)", "operation_has_input_has_data_format(phylotastic_GetReconciliationTree_GET,resource_speciesTree,newickTree)", "operation_has_input_has_data_format(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings)", "operation_has_input_has_data_format(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_2)", "operation_has_input_has_data_format(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_4)", "operation_has_input_has_data_format(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_6)", "operation_has_input_has_data_format(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,phyloTree)", "operation_has_input_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format)", "operation_has_input_has_data_format(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfResolvedName,resolved_names_format_OT)", "operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET,resource_Tree,nmsu_tree_format)", "operation_has_output_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_SetOfSciName,raw_names_format_2)", "operation_has_output_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_HTTPCode,integer)", "operation_has_output_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_ConnectionTime,integer)", "operation_has_output_has_data_format(phylotastic_GetReconciliationTree_GET,resource_reconcileTree,newickTree)", "operation_has_output_has_data_format(phylotastic_GenerateGeneTree_From_Genes,resource_geneTree,phyloTree)", "operation_has_output_has_data_format(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_4)", "operation_has_output_has_data_format(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_6)", "operation_has_output_has_data_format(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_OT)", "operation_has_output_has_data_format(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,nmsu_tree_format)", "operation_has_output_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree)", "operation_has_output_has_data_format(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree)"
]
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
def get_CurrentModifying_Workflow():
  #return ["occur(a,1)", "occur(b,2)", "occur(c,3)"]
  return ORIGINAL_WORKFLOW
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
            old_workflow = get_CurrentModifying_Workflow()
            #print "OLD :"
            #print old_workflow

            new_workflow = []
            for atom in clingo_model.symbols(shown=True):
                new_workflow.append(atom)
            sim_index = sim_matching(old_workflow,new_workflow)
            current_highest_sim = GLOBAL_HIGHEST_SIM_INDEX
            if (sim_index > current_highest_sim):
               GLOBAL_HIGHEST_SIM_INDEX = sim_index
               GLOBAL_BEST_MATCH_WORKFLOW = new_workflow
  
            #print "NEW :"    
            #print new_workflow 
            print "current sim index : " + str(sim_index)
         
            print "\n=================================================="    
        def load_asp(prg):
            prg.load("single_level_planning_Working.lp")
            prg.load("ontology_TESTING_Working.lp")
            prg.load("composite_preference.lp")
            prg.load("re_composite_preference.lp")
        
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

      print("===========================Result======================================\n")
      print("-----> Result \n")
      print("-----> Best Matched Workflow : ")
      print GLOBAL_BEST_MATCH_WORKFLOW
      print("\n-----> Highest Sim Index : " + str(GLOBAL_HIGHEST_SIM_INDEX)) 
      print("=======================================================================\n")

      # Read the final results : RE-composision collection to work on Similarity
      return GLOBAL_BEST_MATCH_WORKFLOW,GLOBAL_HIGHEST_SIM_INDEX
    #----------------------------------------
    re_composition_with_preference(prg)
#end.
%-----------------------------------------------
#external active_rule_single_level(1).
%-----------------------------------------------