%========================================================================
% PLANNING PART : Build WorkFlow for ABTRACT LEVEL
%========================================================================
%#const n = 6.
step(0..n).

%========================================================================
% 1. PLANNING ENGINE - BASIC PART : Follow Paper_v3.pdf
%========================================================================
% Basic part : individual R exists at the time moment 0. R is a resource class
exists(R, 0) :- initially(R,DF),
                class(R),
                subClass(R,phylotastic_resources).

% Basic part : Encode operation A can be executed at time T
%% Update Input and Output
{executable(A,T)} :- operation_class(A),
                     step(T),
                     meaning_operation(A).

:- executable(A,T), has_input(A,N,I), not good_match(A,I,T).

good_match(A,I,T) :- match(A,I,T,_,_).

possible_match(A,I,T,O,T1) :- operation_class(A),
                              has_input(A,N,I),
                              T1 <= T,
                              exists(O,T1),
                              subClass(O,I),
                              step(T1), step(T).

1{match(A,I,T,O,T1):possible_match(A,I,T,O,T1)}1 :- step(T1), step(T), T1 <= T.


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
%exists(X,T+1) :- exists(X,T), step(T), not -exists(X,T+1), T <= n.
%-exists(X,T+1) :- -exists(X,T), step(T), not exists(X,T+1), T <= n.

% Basic Part : Goal Tracker 1
% goal(O, C) :- exists(O, T), final(O), type_of(O,C), step(T), T<= n.
% :- final(O), type_of(O,C), not goal(O,C).

% Basic Part : Goal Tracker 2
success :- goal(I), I <= n, step(I).
:- not success.

%========================================================================
% 2. PLANNING ENGINE - EXTEND PART - PREFERENCE
%       Define rules for operation class shoud be involved
%       Define rules for ordering of classes of services
%       Define rules for concrete operation should be involved
%       Define rules for DO NOT involve FAIL operation/service
%========================================================================
% Extend part : Rules for required class of operation shoud be involved
is_used_class_of_operation(A):- operation_class(A), occur(A, T), T<=n.
:- used_class_of_operation(A), not is_used_class_of_operation(A).

:- used_class_of_operation(X),
   occur(X,T1),
   has_output(X,N1,O),
   occur(Y,T2),
   T2 > T1,
   has_input(Y,N2,O),
   X != Y,
   not match(Y,O,T2,O,T1+1).

%:- match(A,I,T,O,T1), match(A,I,T,O,T2), T1 != T2.

:- used_class_of_operation(X), not match(X,_,_,_,_).


% Extend part : equire involved concrete operation
% is_used_operation(A):- operation(A), occur(A, T), T<=n.
% :- used_operation(A), not is_used_operation(A).

% Extend Part : Require involved class of operation C executed before class of operation D
is_ordered_class_of_service(C,D) :- operation_class(C),
                                    operation_class(D),
                                    occur(C,T1),
                                    occur(D,T2),
                                    T1 < T2.
:- ordered_class_of_service(C,D), not is_ordered_class_of_service(C,D).
used_class_of_operation(C) :- ordered_class_of_service(C,D), 
                              operation_class(C).
used_class_of_operation(D) :- ordered_class_of_service(C,D), 
                              operation_class(C).

% Extend Part : Remove un-need or fail service
:- executable(A,T), step(T), fail_operation(A), operation(A), T<=n.

%========================================================================
% 3. USER DEFINED :
%   1. Initial State and Goal State  (required)
%   2. Which class of operation shoud be involved ? (optional)
%   3. Which concrete operation shoud be involved ? (optional)
%   4. Which rules of sequence of operation (classes) in ordering ? Class C first and then class D
%========================================================================
% Basic part : initial and goal state (SHOULD BE IN DIFFERENT FILES - INIITAL and GOAL FILES)
%initially(resource_CountryCode).

% Change configure const n = 6
initially(resource_SetOfGeneStrings,list_of_strings).

% const n = 1
%initially(resource_geneTree,newickTree).
%initially(resource_speciesTree,newickTree).

% Free-Text - Species const n = 3
%initially(resource_FreeText,plain_text).
%initially(resource_WebURL,data_format_A).

% Change configure const n = 6
finally(resource_reconcileTree,newickTree).
goal(I) :- exists(resource_reconcileTree,I), step(I).

% Free-Text - Species const n = 3
%finally(resource_speciesTree,newickTree).
%goal(I) :- exists(resource_speciesTree,I), step(I).


%=====================SUPPORT RULES=====================================
% Get all possible concrete operations per each class
%no_concrete(Y) :- {isInstanceOf(X,Y):instance(X)}0, operation_class(Y).
%:- no_concrete(X), occur(X,T).
possible_concrete_operation(X,Y,T) :- isInstanceOf(X,Y), occur(Y,T).
%========================================================================
#show occur/2.
%#show match/5.
%#show possible_concrete_operation/3.
%#show goal/1.
%#show initially/2.
%#show finally/2.