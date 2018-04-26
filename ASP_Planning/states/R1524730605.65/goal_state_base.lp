%------------------------------------------------------------------------
% GOAL State
%------------------------------------------------------------------------
finally(resource_speciesTree_with_BranchLengths, newickTree).
finally(resource_metadata_tree_scaling, list_of_strings).
goal(M) :- exists(resource_speciesTree_with_BranchLengths,newickTree,I0),step(I0),exists(resource_metadata_tree_scaling,list_of_strings,I1),step(I1), M = #max{I0;I1}.
%------------------------------------------------------------------------
