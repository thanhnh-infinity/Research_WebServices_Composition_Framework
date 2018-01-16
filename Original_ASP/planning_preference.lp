%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%PLANNING PREFERENCE : Add more preference for planning engie
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Extend Part : Require involved class of operation
used_class_of_operation(gene_tree_scaling).

% Extend Part : Require ordering of classes of operations in the workflow
ordered_class_of_service(phylogeny_based_extraction,gene_tree_scaling).

% Extend Part : Require involved concrete operation
%used_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_GET).
%used_operation(phylotastic_GetPhylogeneticTree_OT_POST).

% Entend Part : Detect un-need or fail service (SHOULD BE IN DIFFERENT FILES in PREFERNECE FILE)
%fail_operation(phylotastic_GetPhylogeneticTree_OT_POST).
%fail_operation(phylotastic_GetPhylogeneticTree_OT_GET).