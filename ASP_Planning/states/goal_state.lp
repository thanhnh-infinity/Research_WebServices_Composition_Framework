% Basic part : initial and goal state (SHOULD BE IN DIFFERENT FILES)
finally(resource_reconcileTree, newickTree).
%finally(resource_speciesTree, newickTree).
goal(I) :- exists(resource_reconcileTree,I), step(I).
%goal(I) :- exists(resource_speciesTree,I), step(I).
%finally(resource_geneTree, nmsu_tree_format).
%goal(I) :- exists(resource_geneTree,I), step(I).