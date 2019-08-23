%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

old_goal(8).
old_occ_exe(getItemsList(webShopTypeB),0).
old_occ_exe(getItemsList(webShopTypeA),1). 
old_occ_exe(addToCart(beer),2).
old_occ_exe(addToCart(smart_phone),3).
old_occ_exe(addToCart(laptop),4). 
old_occ_exe(addToCart(butter),5). 

old_map_exe(getItemsList(webShopTypeB),webShopTypeB,open,0,initial_state,webShopTypeB,open,0).
old_map_exe(getItemsList(webShopTypeA),webShopTypeA,open,1,initial_state,webShopTypeA,open,0).
old_map_exe(addToCart(beer),list_beverage_items,list_of_items,2,getItemsList(webShopTypeB),list_beverage_items,list_of_items,1). 
old_map_exe(addToCart(butter),list_food_items,list_of_items,5,getItemsList(webShop_exeTypeB),list_food_items,list_of_items,1).
old_map_exe(addToCart(smart_phone),list_electrical_device_items,list_of_items,3,getItemsList(webShopTypeA),list_electrical_device_items,list_of_items,2).
old_map_exe(addToCart(laptop),list_electrical_device_items,list_of_items,4,getItemsList(webShopTypeA),list_electrical_device_items,list_of_items,2).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Detect fail service at time T in Graph G
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
fail_service(checkout(webShopTypeA),6).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate G_{exe}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% Simulate an action plays initial state role



