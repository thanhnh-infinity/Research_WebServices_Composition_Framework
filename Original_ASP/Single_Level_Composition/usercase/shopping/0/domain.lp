#const n = 4.
%========================================================================
% Generate INPUT
initially(webShopTypeA,open).
initially(webShopTypeB,open).


% Generate OUTPUT
finally(beer,on_cart).
finally(laptop,on_cart).
goal(H) :- exists(beer,on_cart,I), exists(laptop,on_cart,J), H = #max{I;J}.
