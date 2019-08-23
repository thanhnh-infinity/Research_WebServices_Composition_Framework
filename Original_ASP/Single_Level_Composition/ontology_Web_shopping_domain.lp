%=======================================================================
%PART 1 : Define classes that are used from Entity
%=======================================================================
class(shopping_thing).
subClass(shopping_thing,phylotastic_resources).

class(payment).
class(card).
class(credit_card).
class(debit_card).
class(prepaid_card).
class(cash).
class(itemPrice).

class(shopping_cart).
subClass(shopping_cart,shopping_thing).
class(cart_web_shop_A).
class(cart_web_shop_B).
subClass(cart_web_shop_A,shopping_cart).
subClass(cart_web_shop_B,shopping_cart).

subClass(payment,shopping_thing).
subClass(card,payment).
subClass(cash,payment).
subClass(check,payment).
subClass(credit_card,card).
subClass(debit_card,card).

class(people).
class(buyer).
class(seller).
class(owner).
class(client).
class(customer).

subClass(people,shopping_thing).
subClass(buyer,people).
subClass(seller,people).
subClass(owner,people).
subClass(client,buyer).
subClass(customer,buyer).

class(item).
class(food).
class(electrical_device).
class(beverage).
class(furniture).

subClass(item,shopping_thing).
subClass(food,item).
subClass(electrical_device,item).
subClass(beverage,item).
subClass(furniture,item).

class(laptop).
class(smart_phone).
class(camera).
class(desk).
class(chair).

class(coke).
class(beer).
class(water).
class(bread).
class(butter).
class(meat).

subClass(coke,beverage).
subClass(beer,beverage).
subClass(water,beverage).
subClass(meat,food).
subClass(bread,food).
subClass(butter,food).

subClass(laptop,electrical_device).
subClass(smart_phone,electrical_device).
subClass(camera,electrical_device).
subClass(desk,furniture).
subClass(chair,furniture).

class(organization).
class(webShop).
class(webShopTypeA).
class(webShopTypeB).

subClass(organization,shopping_thing).
subClass(webShop,organization).
subClass(webShopTypeA,webShop).
subClass(webShopTypeB,webShop).


class(list_of_items).
subClass(list_of_items,resource_SetOfThings).

class(list_electrical_device_items).
class(list_food_items).
class(list_beverage_items).
class(list_furniture_items).

subClass(list_electrical_device_items,list_of_items).
subCLass(list_food_items,list_of_items).
subClass(list_beverage_items,list_of_items).
subClass(list_furniture_items,list_of_items).


class(open).
class(available).
class(not_empty).
class(on_cart).

%=======================================================================
%PART 2 : Define classes + instances are defined Operation
%=======================================================================
% Define class of operation
class(get_list_operation).
class(add_to_cart_operation).
class(remove_from_cart_operation).
class(checkout_operation).

class(buy_item_operation).
class(get_price_operation).
class(get_item_list_operation).

% Define subclass of operation
class(shopping_operation).
subClass(shopping_operation,operationClassification).

subClass(get_list_operation,shopping_operation).
subClass(add_to_cart_operation,shopping_operation).
subClass(remove_from_cart_operation,shopping_operation).
subClass(checkout_operation,shopping_operation).
subClass(buy_item_operation,shopping_operation).
subClass(get_price_operation,shopping_operation).
subClass(get_item_list_operation,shopping_operation).



%========================================================================
% PART 3 :  Instance of operations classes
%========================================================================
instance(getItemsList(webShopTypeA)).
instance(getItemsList(webShopTypeB)).

instance(addToCart(laptop)).
instance(addToCart(camera)).
instance(addToCart(smart_phone)).
instance(addToCart(desk)).
instance(addToCart(chair)).

instance(addToCart(coke)).
instance(addToCart(beer)).
instance(addToCart(water)).
instance(addToCart(bread)).
instance(addToCart(butter)).
instance(addToCart(meat)).

instance(removeFromCart).
instance(checkout).

instance(buyItem).
instance(getPrice).

isInstanceOf_immediate(getItemsList(webShopTypeB),get_item_list_operation).
isInstanceOf_immediate(getItemsList(webShopTypeA),get_item_list_operation).

isInstanceOf_immediate(addToCart(laptop),add_to_cart_operation).
isInstanceOf_immediate(addToCart(camera),add_to_cart_operation).
isInstanceOf_immediate(addToCart(smart_phone),add_to_cart_operation).
isInstanceOf_immediate(addToCart(desk),add_to_cart_operation).
isInstanceOf_immediate(addToCart(chair),add_to_cart_operation).

isInstanceOf_immediate(addToCart(coke),add_to_cart_operation).
isInstanceOf_immediate(addToCart(beer),add_to_cart_operation).
isInstanceOf_immediate(addToCart(water),add_to_cart_operation).
isInstanceOf_immediate(addToCart(bread),add_to_cart_operation).
isInstanceOf_immediate(addToCart(butter),add_to_cart_operation).
isInstanceOf_immediate(addToCart(meat),add_to_cart_operation).


isInstanceOf_immediate(removeFromCart,remove_from_cart_operation).

isInstanceOf_immediate(checkout(webShopTypeA),checkout_operation).
isInstanceOf_immediate(checkout(webShopTypeB),checkout_operation).

isInstanceOf_immediate(buyItem,buy_item_operation).
isInstanceOf_immediate(getPrice,get_price_operation).


%========================================================================
% PART 4.1 :  Define hierarchy classes of DATA FORMAT
%           Define which instance operation has DATA FORMAT of INPUT/Output
%========================================================================
% Get list items operation
instance_has_input(getItemsList(webShopTypeA),shop_A,webShopTypeA).
instance_operation_has_input_has_data_format(getItemsList(webShopTypeA),webShopTypeA,open).
instance_has_output(getItemsList(webShopTypeA),list_1,list_electrical_device_items).
instance_has_output(getItemsList(webShopTypeA),list_2,list_furniture_items).
instance_operation_has_output_has_data_format(getItemsList(webShopTypeA),list_electrical_device_items,list_of_items).
instance_operation_has_output_has_data_format(getItemsList(webShopTypeA),list_furniture_items,list_of_items).

instance_has_input(getItemsList(webShopTypeB),shop_B,webShopTypeB).
instance_operation_has_input_has_data_format(getItemsList(webShopTypeB),webShopTypeB,open).
instance_has_output(getItemsList(webShopTypeB),list_1,list_beverage_items).
instance_has_output(getItemsList(webShopTypeB),list_2,list_food_items).
instance_operation_has_output_has_data_format(getItemsList(webShopTypeB),list_beverage_items,list_of_items).
instance_operation_has_output_has_data_format(getItemsList(webShopTypeB),list_food_items,list_of_items).

% Add to Cart Operation
instance_operation_has_input_has_data_format(addToCart(laptop),list_electrical_device_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(laptop),laptop,on_cart).
instance_operation_has_output_has_data_format(addToCart(laptop),cart_web_shop_A,not_empty).

instance_operation_has_input_has_data_format(addToCart(camera),list_electrical_device_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(camera),camera,on_cart).
instance_operation_has_output_has_data_format(addToCart(camera),cart_web_shop_A,not_empty).

instance_operation_has_input_has_data_format(addToCart(smart_phone),list_electrical_device_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(smart_phone),smart_phone,on_cart).
instance_operation_has_output_has_data_format(addToCart(smart_phone),cart_web_shop_A,not_empty).

instance_operation_has_input_has_data_format(addToCart(desk),list_furniture_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(desk),desk,on_cart).
instance_operation_has_output_has_data_format(addToCart(desk),cart_web_shop_A,not_empty).

instance_operation_has_input_has_data_format(addToCart(chair),list_furniture_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(chair),chair,on_cart).
instance_operation_has_output_has_data_format(addToCart(chair),cart_web_shop_A,not_empty).

instance_operation_has_input_has_data_format(addToCart(bread),list_food_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(bread),bread,on_cart).
instance_operation_has_output_has_data_format(addToCart(bread),cart_web_shop_B,not_empty).

instance_operation_has_input_has_data_format(addToCart(butter),list_food_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(butter),butter,on_cart).
instance_operation_has_output_has_data_format(addToCart(butter),cart_web_shop_B,not_empty).

instance_operation_has_input_has_data_format(addToCart(meat),list_food_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(meat),meat,on_cart).
instance_operation_has_output_has_data_format(addToCart(meat),cart_web_shop_B,not_empty).

instance_operation_has_input_has_data_format(addToCart(coke),list_beverage_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(coke),coke,on_cart).
instance_operation_has_output_has_data_format(addToCart(coke),cart_web_shop_B,not_empty).

instance_operation_has_input_has_data_format(addToCart(beer),list_beverage_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(beer),beer,on_cart).
instance_operation_has_output_has_data_format(addToCart(beer),cart_web_shop_B,not_empty).

instance_operation_has_input_has_data_format(addToCart(water),list_beverage_items,list_of_items).
instance_operation_has_output_has_data_format(addToCart(water),water,on_cart).
instance_operation_has_output_has_data_format(addToCart(water),cart_web_shop_B,not_empty).







