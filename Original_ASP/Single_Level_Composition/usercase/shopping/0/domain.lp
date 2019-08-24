#const n = 8.

%------------------------
:- occur(buyItem(X),I).
%:- occur(checkout(webShopTypeA),I).

%========================================================================
% Generate INPUT
initially(webShopTypeA,open).
initially(webShopTypeB,open).
initially(credit_card,enough_account_balance).


% Generate OUTPUT
finally(laptop,possess(client)).
finally(smart_phone,possess(client)).
finally(beer,possess(client)).
finally(butter,possess(client)).

%goal(I) :- exists(laptop,possess(client),I), I <= n.
%goal(I) :- exists(cart_web_shop_A,paid,I), I <= n.
%goal(I) :- exists(laptop,on_cart_A,I), I <= n.

goal(H) :- exists(laptop,possess(client),I1),exists(smart_phone,possess(client),I2), exists(beer,possess(client),I3), exists(butter,possess(client),I4), H = #max{I1;I2;I3;I4}, H <= n.