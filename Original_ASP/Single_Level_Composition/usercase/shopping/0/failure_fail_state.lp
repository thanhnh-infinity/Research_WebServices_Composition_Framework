%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Detect fail service at time T in Graph G
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fail_service(checkout(webShopTypeA),6).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate V_0(st)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
resource_generated(list_electrical_device_items,list_of_items,"abc").
resource_generated(list_furniture_items,list_of_items,"abc").
resource_generated(list_beverage_items,list_of_items,"abc").
resource_generated(list_food_items,list_of_items,"abc").
resource_generated(cart_web_shop_A,not_empty,"abc").
resource_generated(laptop,on_cart(webShop_A),"abc").
resource_generated(smart_phone,on_cart(webShop_A),"abc").
resource_generated(cart_web_shop_B,not_empty,"abc").
resource_generated(beer,on_cart(webShop_B),"abc").
resource_generated(butter,on_cart(webShop_B),"abc").

% Re-generate initial state to planning
initially(list_electrical_device_items,list_of_items).
initially(list_furniture_items,list_of_items).
initially(list_beverage_items,list_of_items).
initially(list_food_items,list_of_items).
initially(cart_web_shop_A,not_empty).
initially(laptop,on_cart(webShop_A)).
initially(smart_phone,on_cart(webShop_A)).
initially(beer,on_cart(webShop_B)).
initially(cart_web_shop_B,not_empty).
initially(butter,on_cart(webShop_B)).

% Simulate an action plays initial state role



