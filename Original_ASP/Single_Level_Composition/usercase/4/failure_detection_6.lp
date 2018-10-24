%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%
% Remember OLD Workflow => Including DGA Graph : 
%          Node : occur(X,T) 
%          Normal Edge (from service to service) : map(A,I,DF_I,T,B,O,DF_O,T1)
%          Edge start from v_{0} : map(A,I,DF_I,T,initial_state,O,DF_O,0)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Detect fail service at time T in Graph G
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fail_service(convert_df_taxons_format_GNR_to_PhyloT,6).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate G_{exe}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

old_occ_exe(convert_df_text_format_raw_to_plain,0).
old_occ_exe(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,1).
old_occ_exe(convert_df_sci_names_format_1_to_3,2).
old_occ_exe(convert_df_sci_names_format_3_to_5,3).
old_occ_exe(convert_df_sci_names_format_5_to_GNR,4).
old_occ_exe(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,5).

old_map_exe(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text,0,initial_state,resource_FreeText,raw_text,0).
old_map_exe(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text,1,convert_df_text_format_raw_to_plain,resource_FreeText,plain_text,1).
old_map_exe(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1,2,phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1,2).
old_map_exe(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3,3,convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3,3).
old_map_exe(convert_df_sci_names_format_5_to_GNR,resource_SetOfSciName,raw_names_format_5,4,convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5,4).
old_map_exe(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,resource_SetOfSciName,raw_names_format_GNR,5,convert_df_sci_names_format_5_to_GNR,resource_SetOfSciName,raw_names_format_GNR,5).

% Simulate an action plays initial state role
