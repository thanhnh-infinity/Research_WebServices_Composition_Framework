#const n = 1.
%========================================================================
% Generate INPUT
initially(webShopTypeA,open).


% Generate OUTPUT
finally(list_electrical_device_items,list_of_items).
goal(I) :- exists(list_electrical_device_items,list_of_items,I), step(I).
