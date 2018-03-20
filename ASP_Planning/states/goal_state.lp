% Generate OUTPUT
%finally(resource_speciesTree,phylo4Tree).
%goal(I) :- exists(resource_speciesTree,phylo4Tree,I), step(I).

%finally(resource_SetOfTaxon,resolved_names_format_GNR).
%goal(I) :- exists(resource_SetOfTaxon,resolved_names_format_GNR,I), step(I).

finally(resource_reconcileTree,newickTree).
goal(I) :- exists(resource_reconcileTree,newickTree,I), step(I).

%finally(resource_AreSameTree,boolean).
%goal(I) :- exists(resource_AreSameTree,boolean,I), step(I).

%finally(resource_geneTree,phylo4Tree).
%goal(I) :- exists(resource_geneTree,phylo4Tree,I), step(I).


% Componet
%finally(resource_speciesTree,newickTree).
%goal(M) :- exists(resource_speciesTree,newickTree,I), exists(resource_geneTree,newickTree,J), step(I), step(J), M = #max{I;J}.
%finally(resource_geneTree,newickTree).
%goal(I) :- exists(resource_geneTree,newickTree,I), step(I).