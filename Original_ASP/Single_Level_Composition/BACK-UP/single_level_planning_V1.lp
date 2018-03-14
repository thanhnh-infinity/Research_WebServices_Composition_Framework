%========================================================================
% PLANNING PART : Build WorkFlow for SINGLE LEVEL OF PLANNING
%========================================================================
%#const n = 9.
#const n = 9.
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


1{match(A,I,DF_I,T,O,DF_O,T1):possible_match(A,I,DF_I,T,O,DF_O,T1)}1 :- step(T).
%1{match(A,I,DF_I,T,O,DF_O,T1):possible_match(A,I,DF_I,T,O,DF_O,T1)}1.

-occur(A,I) :- not occur(A,I),
               step(I),
               operation(A).

% Basic part : generate a possible sequence of operations and records the effects of operations,
1{ occur(A,T): operation(A)}1 :- step(T), not goal(T), T <= n.
:- occur(A,T), not executable(A,T).
exists(O,DF_O,T+1) :- occur(A,T), 
                      instance_operation_has_output_has_data_format(A,O,DF_O),
                      instance_has_output(A,N,O), 
                      step(T).

% Basic part : AWC for operation
:- operation(A1), operation(A2), occur(A1,I), occur(A2,I), A1 != A2, step(I).

% Real Map for Graph
map(A,I,DF_I,T,B,O,DF_O,T1) :- occur(A,T),
                               instance_has_input(A,N2,I),
                               instance_operation_has_input_has_data_format(A,I,DF_I),
                               occur(B,T1-1),
                               instance_has_output(B,N1,O),
                               instance_operation_has_output_has_data_format(B,O,DF_O),
                               A != B,
                               T >= T1,
                               T1 > 0,
                               match(A,I,DF_I,T,O,DF_O,T1).
map(A,I,DF_I,T,initial_state,O,DF_O,0) :- occur(A,T),
                                          instance_has_input(A,N1,I),
                                          instance_operation_has_input_has_data_format(A,I,DF_I),
                                          match(A,I,DF_I,T,O,DF_O,0).

%========================================================================
% Basic Part : Goal Tracker 2
success :- goal(I), I <= n, step(I).
:- not success.
%========================================================================
% 2. PLANNING ENGINE - EXTEND PART - PREFERENCE
%       Define rules for operation class shoud be involved
%       Define rules for ordering of services
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


% Extend part : Rules for required concrete operation shoud be involved
is_used_operation(A) :- operation(A),
                        occur(A,T),
                        T <= n.
:- used_operation(A), 
   not is_used_operation(A). 

:- used_operation(A), 
   not match(A,_,_,_,_,_,_).                       

:- used_operation(X),
   not map(_,_,_,_,X,_,_,_).
   

% Extend part : avoidance concrete operation
:- do_not_use_operation(X), is_used_operation(X).

%========================================================================
% Basic part : initial and goal state (SHOULD BE IN DIFFERENT FILES - INIITAL and GOAL FILES)

% Free-Text - Species const n = 3
initially(resource_FreeText,raw_text).

%initially(resource_SetOfGeneStrings,list_of_strings).

%initially(resource_speciesTree,newickTree).
%initially(resource_geneTree,newickTree).

% Free-Text - Species const n = 3
finally(resource_speciesTree,phylo4Tree).
goal(I) :- exists(resource_speciesTree,phylo4Tree,I), step(I).

%finally(resource_reconcileTree,newickTree).
%goal(I) :- exists(resource_reconcileTree,newickTree,I), step(I).

% Componet
%finally(resource_speciesTree,newickTree).
%goal(I) :- exists(resource_speciesTree,newickTree,I), step(I).

%finally(resource_geneTree,newickTree).
%goal(I) :- exists(resource_geneTree,newickTree,I), step(I).

% Component
%finally(resource_FreeText,plain_text).
%goal(I) :- exists(resource_FreeText,plain_text,I), step(I).

%finally(resource_SetOfSciName,raw_names_format_1).
%goal(I) :- exists(resource_SetOfSciName,raw_names_format_1,I), step(I).

%finally(resource_SetOfTaxon,resolved_names_format_OT).
%goal(I) :- exists(resource_SetOfTaxon,resolved_names_format_OT,I), step(I).


%used_operation(phylotastic_GetPhylogeneticTree_Phylomatic_GET).
%used_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_GET).

%do_not_use_operation(phylotastic_ResolvedScientificNames_GNR_TNRS_POST).
%do_not_use_operation(phylotastic_ResolvedScientificNames_OT_TNRS_GET).
%do_not_use_operation(phylotastic_ResolvedScientificNames_OT_TNRS_POST).
%#minimize{I:goal(I)}.
%========================================================================
#show occur/2.
%#show map/8.
%#show exists/3.
%#show executable/2.
%#show final_df/2.
%#show match/7.
%#show good_match/4.
%#show possible_match/7.
%#show instance_has_input/3.