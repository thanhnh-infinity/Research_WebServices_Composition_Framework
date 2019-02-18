%========================================================================

% Generate INPUT
initially(resource_FreeText,plain_text).


% Generate OUTPUT
finally(resource_speciesTree,newickTree).
goal(I) :- exists(resource_speciesTree,newickTree,I), step(I).

%=======================================================================


