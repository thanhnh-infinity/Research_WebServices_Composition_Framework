#const n = 5.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

old_goal(8).
old_occur(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,0).
old_occur(convert_df_sci_names_format_1_to_3,1).
old_occur(convert_df_sci_names_format_3_to_5,2).
old_occur(convert_df_sci_names_format_5_to_OT,3).
old_occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,4).
old_occur(phylotastic_GetPhylogeneticTree_OT_GET,5).
old_occur(convert_species_tree_format_NMSU_to_NewickTree,6).
old_occur(phylotastic_CompareTrees_Sym_Dendropy_POST,7).




old_map(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1,1,phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1,1). 
old_map(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3,2,convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3,2).
old_map(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5,3,convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5,3). 
old_map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,4,convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT,4).
old_map(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT,5,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,5).
old_map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,6,phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format,6).
old_map(phylotastic_CompareTrees_Sym_Dendropy_POST,resource_speciesTree,newickTree,7,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,7).

old_map(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text,0,initial_state,resource_FreeText,plain_text,0).
old_map(phylotastic_CompareTrees_Sym_Dendropy_POST,resource_speciesTree,compare_tree_format,7,initial_state,resource_speciesTree,compare_tree_format,0). 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Detect fail service at time T in Graph G
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fail_service(convert_df_sci_names_format_5_to_OT,3).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate V_0(st)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

resource_generated(resource_SetOfSciName,set_of_names_1,raw_names_format_1,"abc").
resource_generated(resource_SetOfSciName,cv_names_1,raw_names_format_3,"abc").
resource_generated(resource_SetOfSciName,cv_names_1,raw_names_format_5,"abc").

initially(resource_SetOfSciName,raw_names_format_1).
initially(resource_SetOfSciName,raw_names_format_3).
initially(resource_SetOfSciName,raw_names_format_5).

% Simulate an action plays initial state role



