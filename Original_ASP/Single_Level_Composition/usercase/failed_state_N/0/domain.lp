%========================================================================
% Generate INPUT
initially(resource_FreeText,plain_text).
initially(resource_speciesTree,compare_tree_format).

% Generate OUTPUT
finally(resource_AreSameTree,boolean).
goal(I) :- exists(resource_AreSameTree,boolean,I), step(I).

