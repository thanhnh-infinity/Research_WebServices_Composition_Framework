%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Detect fail service at time T in Graph G
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fail_service(convert_species_tree_format_NMSU_to_NewickTree,6).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate V_0(st)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
resource_generated(resource_SetOfSciName,raw_names_format_1,"abc").
resource_generated(resource_SetOfSciName,raw_names_format_3,"abc").
resource_generated(resource_SetOfSciName,raw_names_format_5,"abc").
resource_generated(resource_SetOfSciName,raw_names_format_OT,"abc").
resource_generated(resource_SetOfTaxon,resolved_names_format_OT,"abc").
resource_generated(resource_speciesTree,nmsu_tree_format,"abc").

% Re-generate initial state to planning
initially(resource_SetOfSciName,raw_names_format_1).
initially(resource_SetOfSciName,raw_names_format_3).
initially(resource_SetOfSciName,raw_names_format_5).
initially(resource_SetOfSciName,raw_names_format_OT).
initially(resource_SetOfTaxon,resolved_names_format_OT).
initially(resource_speciesTree,nmsu_tree_format).

% Simulate an action plays initial state role



