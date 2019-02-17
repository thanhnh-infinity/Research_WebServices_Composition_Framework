#const n = 9.

%% Performance problem

%========================================================================


% Generate INPUT
initially(resource_FreeText,raw_text).
initially(resource_speciesTree,compare_tree_format).


finally(resource_AreSameTree,boolean).
goal(I) :- exists(resource_AreSameTree,boolean,I), step(I).

