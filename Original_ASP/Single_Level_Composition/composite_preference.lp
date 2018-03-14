%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%PLANNING PREFERENCE : Add more preference for planning engie
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Constraint for Advanced Modification

% HAVE TO USE
%used_operation(phylotastic_GetPhylogeneticTree_Phylomatic_GET).
%used_operation(phylotastic_GetPhylogeneticTree_OT_GET).
%used_operation(phylotastic_GetPhylogeneticTree_OT_POST).
%used_operation(phylotastic_GetPhylogeneticTree_PhyloT_GET).
%used_operation(phylotastic_GetPhylogeneticTree_PhyloT_POST).
%used_operation(phylotastic_GetPhylogeneticTree_Phylomatic_POST).

%used_operation(phylotastic_GeneTree_Scaling).

% DO NOT USE 
%do_not_use_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_GET).

%do_not_use_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_POST).
%do_not_use_operation(phylotastic_ResolvedScientificNames_OT_TNRS_GET).
%do_not_use_operation(phylotastic_ResolvedScientificNames_OT_TNRS_POST).

% USE IN ORDERING
%ordered_services(phylotastic_GeneTree_Scaling,phylotastic_GetPhylogeneticTree_OT_GET).