time(0..n-1).
%-----------------------------------------------
1{map(I,J):time(J)}1 :- occur(A,I).

:- map(I1,J1),
   map(I2,J2),
   I1 < I2,
   J1 >= J2.

1{occur_concrete(S,I):isInstanceOf(S,A)}1 :- map(J,I),
                                             occur(A,J).
%-----------------------------------------------
% Data format convert
consider_abtract_step(T) :- time(T).
%consider_abtract_step(6).

% for DF out to service
%finally_data_format(DF_OUT,T2) :-  match(A,I,T,O,T1),
%                                   occur(A,T),
%                                   map(T,T2),
%                                   occur_concrete(S,T2),
%                                   instance_operation_has_input_has_data_format(S,I,DF_OUT).

% for DF out to goal
%finally_data_format(goal_state,X,DF_OUT,T) :-  goal(T),finally(X, DF_OUT).
%finally_data_format(DF_OUT,T) :-  goal(T), finally(X, DF_OUT).

% for DF in init
%initially_data_format(initial_state,X,DF_IN,0) :- initially(X,DF_IN).
%initially_data_format(DF_IN,0) :- initially(X,DF_IN).

% for DF in service
%initially_data_format(DF_IN,T) :-  match(A,I,T,O,T1),
%                                   operation_class(C),
%                                   occur(C,T1 - 1),
%                                   occur_concrete(S,T2),
%                                   map(T1-1,T2),
%                                   isInstanceOf(S,C),
%                                   occur(A,T),
%                                   instance_operation_has_output_has_data_format(S,O,DF_IN).

% For both:
map_df(S1,O,T2,DF_IN,S,I,T3,DF_OUT) :- match(A,I,T,O,T1),
                                       operation_class(C),
                                       occur(C,T1 - 1),
                                       occur_concrete(S1,T2),
                                       map(T1-1,T2),
                                       isInstanceOf(S1,C),
                                       occur(A,T),
                                       instance_operation_has_output_has_data_format(S1,O,DF_IN),
                                       occur_concrete(S,T3),
                                       isInstanceOf(S,A),
                                       map(T,T3),
                                       instance_operation_has_input_has_data_format(S,I,DF_OUT).

map_df(initial_state,O,-1,DF_IN,S,I,T3,DF_OUT) :- match(A,I,T,O,0),
                                                  initially(O,DF_IN),
                                                  occur(A,T),
                                                  occur_concrete(S,T3),
                                                  isInstanceOf(S,A),
                                                  map(T,T3),
                                                  instance_operation_has_input_has_data_format(S,I,DF_OUT).



%mpID(S1,O,T2,S,I,T3) :- map_df(S1,O,T2,DF_IN,S,I,T3,DF_OUT).

mapping_df_with_ID(@generate_MatchProblemID(O,DF_IN,T2,I,DF_OUT,T3),S1,O,T2,DF_IN,S,I,T3,DF_OUT) :- map_df(S1,O,T2,DF_IN,S,I,T3,DF_OUT).

initially_data_format(DF_IN,T3, MP_ID) :- mapping_df_with_ID(MP_ID,_,_,_,DF_IN,_,_,T3,_).
finally_data_format(DF_OUT,T3, MP_ID) :- mapping_df_with_ID(MP_ID,_,_,_,_,_,_,T3,DF_OUT).

mpID(P_ID,T3) :- mapping_df_with_ID(P_ID,_,_,_,_,_,_,T3,_).

%initially_data_format(DF_IN,T3) :- map_df(_,_,_,DF_IN,_,_,T3,_).
%finally_data_format(DF_OUT,T3) :- map_df(_,_,_,_,_,_,T3,DF_OUT).

%initially_data_format(tree_format_2,6).
%-------------------------------------------------