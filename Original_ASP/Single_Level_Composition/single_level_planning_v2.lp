%========================================================================
% PLANNING PART : Build WorkFlow for SINGLE LEVEL OF PLANNING
%========================================================================
#const n = 8.
step(0..n).
%========================================================================
% 1. PLANNING ENGINE - BASIC PART
%========================================================================
% Basic part : individual R exists at the time moment 0. R is a resource class
exists(R, DF_R, 0) :- initially(R,DF_R),
                      class(R),
                      subClass(R,phylotastic_resources).

% Basic part : Encode operation A can be executed at time T
{executable(A,T)} :- operation(A),
                     step(T),
                     mean_op(A).

:- executable(A,T), 
   instance_has_input(A,N,I), 
   instance_operation_has_input_has_data_format(A,I,DF_I), 
   not good_match(A,I,DF_I,T).


good_match(A,I,DF_I,T) :- match(A,I,DF_I,T,_,_,_).

possible_match(A,I,DF_I,T,O,DF_O,T1) :- operation(A),
                                        instance_has_input(A,N,I),
                                        instance_operation_has_input_has_data_format(A,I,DF_I),
                                        T1 <= T,
                                        exists(O,DF_O,T1),
                                        subClass(O,I),
                                        subClass(DF_O,DF_I),
                                        step(T1),step(T).


1{match(A,I,DF_I,T,O,DF_O,T1):possible_match(A,I,DF_I,T,O,DF_O,T1)}1 :- occur(A,T).
%1{match(A,I,DF_I,T,O,DF_O,T1):possible_match(A,I,DF_I,T,O,DF_O,T1)}1.

-occur(A,I) :- not occur(A,I),
               step(I),
               operation(A).

% Basic part : generate a possible sequence of operations and records the effects of operations,
1{ occur(A,T): operation(A)}1 :- step(T), not goal(T), T <= n.
:- occur(A,T), not executable(A,T).
exists(O,DF_O,T+1) :- occur(A,T), 
                      instance_operation_has_output_has_data_format(A,O,DF_O),
                      instance_has_output(A,N,O), step(T).

% Basic part : AWC for operation
:- operation(A1), operation(A2), occur(A1,I), occur(A2,I), A1 != A2, step(I).

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


%========================================================================
% Basic part : initial and goal state (SHOULD BE IN DIFFERENT FILES - INIITAL and GOAL FILES)

% Free-Text - Species const n = 3
initially(resource_FreeText,plain_text).


% Free-Text - Species const n = 3
finally(resource_speciesTree,newickTree).
goal(I) :- exists(resource_speciesTree,newickTree,I), step(I).

%finally(resource_FreeText,plain_text).
%goal(I) :- exists(resource_FreeText,plain_text,I), step(I).

%finally(resource_SetOfSciName,raw_names_format_1).
%goal(I) :- exists(resource_SetOfSciName,raw_names_format_1,I), step(I).

%finally(resource_SetOfSciName,raw_names_format_1).
%goal(I) :- exists(resource_SetOfTaxon,resolved_names_format_GNR,I), step(I).


%used_operation(phylotastic_GetPhylogeneticTree_OT_POST).
%#minimize{I:goal(I)}.
%========================================================================
#show occur/2.
%#show real_map/6.
%#show exists/3.
%#show executable/2.
%#show final_df/2.
#show match/7.
%#show good_match/4.
%#show possible_match/7.
%#show instance_has_input/3.