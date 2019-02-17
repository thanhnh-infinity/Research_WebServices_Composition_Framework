%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%
% Remember OLD Workflow => Including DGA Graph : 
%          Node : occur(X,T) 
%          Normal Edge (from service to service) : map(A,I,DF_I,T,B,O,DF_O,T1)
%          Edge start from v_{0} : map(A,I,DF_I,T,initial_state,O,DF_O,0)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Detect fail service at time T in Graph G
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fail_service(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,1).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate G_{exe}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

old_occ_exe(convert_df_text_format_raw_to_plain,0).

old_map_exe(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text,0,initial_state,resource_FreeText,raw_text,0).


% Simulate an action plays initial state role



