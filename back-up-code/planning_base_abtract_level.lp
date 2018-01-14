%========================================================================
% PLANNING PART : Build WorkFlow for ABTRACT LEVEL
%========================================================================
#const n = 3.
step(0..n).

%========================================================================
% 1. PLANNING ENGINE - BASIC PART : Follow Paper_v3.pdf
%========================================================================
% Basic part : individual R exists at the time moment 0. R is a resource class
exists(R, 0) :- initially(R,DF), 
                class(R), 
                subClass(R,phylotastic_resources).

% Basic part : Encode operation A can be executed at time T
%% Cho nay update nghia la class bat buoc phai co INPUT and OUPUT properties moi cho phep tham gia PLANNING
{executable(A,T)} :- operation_class(A), 
                     step(T), 
                     meaning_operation(A).

:- executable(A,T), has_input(A,N,I), not match(A, I, T).
match(A,I,T) :- operation_class(A),
                has_input(A,N,I), 
                T1 <= T, 
                exists(O,T1), 
                subClass(O,I), 
                step(T1), step(T).
-occur(A,I) :- not occur(A,I), 
               step(I), 
               operation_class(A).

% Basic part : generate a possible sequence of operations and records the effects of operations, 
1{ occur(A,T): operation_class(A)}1 :- step(T), not goal(T), T <= n.
:- occur(A,T), not executable(A,T).
exists(O,T+1) :- occur(A,T), has_output(A,N,O), step(T).

% Basic part : AWC for operation
:- operation_class(A1), operation_class(A2), occur(A1,I), occur(A2,I), A1 != A2, step(I).

% Basic part : Move forward for inertial fluent
exists(X,T+1) :- exists(X,T), step(T), not -exists(X,T+1), T <= n.
-exists(X,T+1) :- -exists(X,T), step(T), not exists(X,T+1), T <= n.

% Basic Part : Goal Tracker 1
% goal(O, C) :- exists(O, T), final(O), type_of(O,C), step(T), T<= n.
% :- final(O), type_of(O,C), not goal(O,C).

% Basic Part : Goal Tracker 2
success :- goal(I), I <= n, step(I).
:- not success.

%========================================================================
% 2. PLANNING ENGINE - EXTEND PART - PREFERENCE
%       Define rules for operation class shoud be involved
%       Define rules for concrete operation should be involved
%       Define rules for DO NOT involve FAIL operation/service
%========================================================================
% Extend part : Rules for required class of operation shoud be involved
is_used_class_of_operation(A):- operation_class(A), occur(A, T), T<=n.
:- used_class_of_operation(A), not is_used_class_of_operation(A).

% Extend part : equire involved concrete operation
% is_used_operation(A):- operation(A), occur(A, T), T<=n.
% :- used_operation(A), not is_used_operation(A).

% Extend Part : Require involved class of operation C executed before class of operation D

% Extend Part : Remove un-need or fail service
:- executable(A,T), step(T), fail_operation(A), operation(A), T<=n.

%========================================================================
% 3. USER DEFINED : 
%   1. Initial State and Goal State  (required)
%   2. Which class of operation shoud be involved ? (optional)
%   3. Which concrete operation shoud be involved ? (optional)
%   4. Which rules of sequence of operation (classes) in ordering ? Class C first and then class D
%========================================================================
% Basic part : initial and goal state (SHOULD BE IN DIFFERENT FILES)
%initially(resource_CountryCode).
%initially(resource_Name).


%initially(resource_WebURL).

%goal(I) :- exists(resource_speciesTree,I), step(I).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%% QoS : This Part will be achieved from QoS module
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Extend Part : Require involved class of operation (SHOULD BE IN DIFFERENT FILES)
% used_class_of_operation(country_code_to_name).

% Extend Part : Require involved concrete operation (SHOULD BE IN DIFFERENT FILES)
%used_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_GET).
%used_operation(phylotastic_GetPhylogeneticTree_OT_POST).

% Entend Part : Detect un-need or fail service (SHOULD BE IN DIFFERENT FILES)
%fail_operation(phylotastic_GetPhylogeneticTree_OT_POST).
%fail_operation(phylotastic_GetPhylogeneticTree_OT_GET).

%=====================SUPPORT RULES=====================================
% Get all possible concrete operations per each class
no_concrete(Y) :- {isInstanceOf(X,Y):instance(X)}0, operation_class(Y).
:- no_concrete(X), occur(X,T).
possible_concrete_operation(X,Y,T) :- isInstanceOf(X,Y), occur(Y,T).
%========================================================================
#show occur/2.
#show possible_concrete_operation/3.
#show goal/1.
#show initially/2.
#show finally/2.
