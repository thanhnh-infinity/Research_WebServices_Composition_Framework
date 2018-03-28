%------------------------------------------------------------------------
% GOAL State
%------------------------------------------------------------------------
finally(resource_speciesTree, newickTree).
finally(resource_geneTree, newickTree).
goal(M) :- exists(resource_speciesTree,newickTree,I0), step(I0),exists(resource_geneTree,newickTree,I1), step(I1), M = #max{I0;I1}.
%------------------------------------------------------------------------
