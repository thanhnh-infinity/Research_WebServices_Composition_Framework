%========================================================================
% PLANNING PART : Build WorkFlow for SINGLE LEVEL OF PLANNING
%========================================================================
#const n = 3.
step(0..n).
#const m = 3.


%========================================================================
% 1. PLANNING ENGINE - BASIC PART
%========================================================================
% Basic part : individual R exists at the time moment 0. R is a resource class
exists(R, 0) :- initially(R,DF),
                class(R),
                subClass(R,phylotastic_resources).

% Basic part : Encode operation A can be executed at time T
{executable(A,T)} :- operation(A),
                     step(T),
                     mean_op(A).

:- executable(A,T), instance_has_input(A,N,I), not good_match(A,I,T).

good_match(A,I,T) :- match(A,I,T,_,_).

possible_match(A,I,T,O,T1) :- operation(A),
                              instance_has_input(A,N,I),
                              T1 <= T,
                              exists(O,T1),
                              subClass(O,I),
                              step(T1), step(T).

1{match(A,I,T,O,T1):possible_match(A,I,T,O,T1)}1 :- step(T1), step(T), T1 <= T.


-occur(A,I) :- not occur(A,I),
               step(I),
               operation(A).

% Basic part : generate a possible sequence of operations and records the effects of operations,
1{ occur(A,T): operation(A)}1 :- step(T), not goal(T), T <= n.
:- occur(A,T), not executable(A,T).
exists(O,T+1) :- occur(A,T), instance_has_output(A,N,O), step(T).

% Basic part : AWC for operation
:- operation(A1), operation(A2), occur(A1,I), occur(A2,I), A1 != A2, step(I).


%========================================================================
%Attached data format conversion

real_map(A,I,T,B,O,T1) :- occur(A,T),
                          instance_has_input(A,N2,I),
                          occur(B,T1-1),
                          instance_has_output(B,N1,O),
                          A != B,
                          T >= T1,
                          T1 > 0,
                          match(A,I,T,O,T1).
real_map(A,I,T,initial_state,O,0) :- occur(A,T),
                                     instance_has_input(A,N1,I),
                                     match(A,I,T,O,0).

% Decide need convert for all resource provided in initial state
map_df(-1,InitR,InitDF,I,DF_I,0):- initially(InitR,InitDF),
                                                occur(A,0), operation(A),
                                                instance_has_input(A,N,I),
                                                instance_operation_has_input_has_data_format(A,I,DF_I),
                                                real_map(A,I,0,initial_state,InitR,0),
                                                InitDF != DF_I, not subClass(InitDF,DF_I).

% Decide need convert for resource to resource of operation - operation
map_df(T1,O,DF_O,I,DF_I,T) :-  occur(A1,T1), operation(A1),
                                            instance_has_output(A1,N1,O),instance_operation_has_output_has_data_format(A1,O,DF_O),
                                            occur(A,T), operation(A),
                                            instance_has_input(A,N,I), instance_operation_has_input_has_data_format(A,I,DF_I),
                                            T1 < T,
                                            real_map(A,I,T,A1,O,T1+1),
                                            DF_O != DF_I, not subClass(DF_O,DF_I).

% Decide need convert for resource to goal
map_df(T,O,DF_O,FinalR,FinalDF,999):- finally(FinalR,FinalDF),
                                                   occur(A,T), operation(A),
                                                   instance_has_output(A,N,O),
                                                   instance_operation_has_output_has_data_format(A,O,DF_O),
                                                   subClass(O,FinalR),
                                                   FinalDF != DF_O, not subClass(DF_O,FinalDF).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%  MY OLD APPROACH %%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
init_df(T,DF_O) :- map_df(T,O,DF_O,I,DF_I,T1).
final_df(T,DF_I) :- map_df(T,O,DF_O,I,DF_I,T1).
time(T,0..m) :- step(T).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%  NEW ONE APPROACH  ??? %%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%========================================================================
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
is_used_class_of_operation(C):- operation_class(C), 
                                occur(A, T), 
                                isInstanceOf(A,C),
                                T<=n.
:- used_class_of_operation(A), 
   not is_used_class_of_operation(A).

:- used_class_of_operation(C),
   occur(X,T1),
   isInstanceOf(X,C),
   instance_has_output(X,N1,O),
   occur(Y,T2),
   T2 > T1,
   instance_has_input(Y,N2,O),
   X != Y,
   not match(Y,O,T2,O,T1+1).



% Extend part : Rules for required concrete operation shoud be involved
is_used_operation(A) :- operation(A),
                        occur(A,T),
                        T <= n.
:- used_operation(A), 
   not is_used_operation(A). 

:- used_operation(A), 
   not match(A,_,_,_,_).                       

:- used_operation(X),
   occur(X,T1),
   instance_has_output(X,N1,O),
   occur(Y,T2),
   T2 > T1,
   instance_has_input(Y,N2,O),
   X != Y,
   not match(Y,O,T2,O,T1+1).

% Extend part : equire involved concrete operation


%========================================================================
% Basic part : initial and goal state (SHOULD BE IN DIFFERENT FILES - INIITAL and GOAL FILES)

% Free-Text - Species const n = 3
initially(resource_FreeText,plain_text).

% Free-Text - Species const n = 3
%finally(resource_speciesTree,newickTree).
%goal(I) :- exists(resource_speciesTree,I), step(I).

finally(resource_SetOfTaxon,list_of_strings).
goal(I) :- exists(resource_SetOfTaxon,I), step(I).

%used_operation(phylotastic_GetPhylogeneticTree_OT_POST).
%========================================================================
#show occur/2.
%#show real_map/6.
%#show exists/2.
%#show init_df/2.
%#show final_df/2.
#show match/5.