#const n = 8.



%========================================================================


% Generate INPUT
initially(resource_FreeText,raw_text).


finally(resource_speciesTree,newickTree).
goal(I) :- exists(resource_speciesTree,newickTree,I), step(I).

