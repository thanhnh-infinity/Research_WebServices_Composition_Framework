%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%RE-COMPOSITION PREFERENCE : Add more preference for planning engine
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Add more rule because to heavy for planning code
% Extend Part : Require involved operation C executed before operation D
%%%% Super poor performance
%is_ordered_services(C,D) :- operation(C),
%                            operation(D),
%                            occur(C,T1),
%                            occur(D,T2),
%                            goal(G),
%                            T1 < T2,
%                            T2 < G.
%:- ordered_services(C,D), not is_ordered_services(C,D).
%used_operation(C) :- ordered_services(C,D), 
%                     operation(C).
%used_operation(D) :- ordered_services(C,D), 
%                     operation(C).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Constraint for Advanced Modification

% HAVE TO USE
%used_operation(phylotastic_GetPhylogeneticTree_Phylomatic_GET).
%used_operation(phylotastic_GetPhylogeneticTree_OT_GET).
%used_operation(phylotastic_GetPhylogeneticTree_OT_POST).
%used_operation(phylotastic_GetPhylogeneticTree_PhyloT_GET).
%used_operation(phylotastic_GetPhylogeneticTree_PhyloT_POST).
%used_operation(phylotastic_GetPhylogeneticTree_Phylomatic_POST).

used_operation(phylotastic_GeneTree_Scaling).

% DO NOT USE 
%do_not_use_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_GET).

%do_not_use_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_POST).
%do_not_use_operation(phylotastic_ResolvedScientificNames_OT_TNRS_GET).
%do_not_use_operation(phylotastic_ResolvedScientificNames_OT_TNRS_POST).

% USE IN ORDERING
%ordered_services(phylotastic_GeneTree_Scaling,phylotastic_GetPhylogeneticTree_OT_GET).