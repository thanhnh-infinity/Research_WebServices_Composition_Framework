#const n = 3.

%------------------------
%:- occur(buyItem(X),I).
%:- occur(checkout(webShopTypeA),I).

%========================================================================
% Generate INPUT
initially(webShopTypeC,open).
initially(credit_card,enough_account_balance).


% Generate OUTPUT
finally(beer,possess(client)).
finally(bread,possess(client)).


%goal(I) :- exists(bread,possess(client),I), I <= n.
%goal(I) :- exists(cart_web_shop_A,paid,I), I <= n.
%goal(I) :- exists(laptop,on_cart_A,I), I <= n.

goal(H) :- exists(beer,possess(client),I1),exists(bread,possess(client),I2), H = #max{I1;I2}, H <= n.