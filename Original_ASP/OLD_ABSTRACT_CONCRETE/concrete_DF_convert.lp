%========================================================================
% PLANNING PART : Build WorkFlow for CONCRETE LEVEL LEVEL
%========================================================================

%=================DEFINE INSTANCES of DATA FORMAT CONVERTION SERVICES================================
class(data_format_A).
class(data_format_A_1).
class(data_format_A_2).
class(data_format_A_3).
class(data_format_unknown).
subClass(data_format_A_1,data_format_A).
subClass(data_format_A_2,data_format_A_1).

class(nmsu_tree_format).

class(names_format_1).
class(names_format_2).
class(names_format_3).
class(names_format_4).
class(names_format_5).
class(names_format_6).
class(names_format_resolved_GNR).
class(names_format_resolved_OT).
subClass(names_format_1, names_format).
subClass(names_format_2, names_format).
subClass(names_format_3, names_format).
subClass(names_format_4, names_format).
subClass(names_format_5, names_format).
subClass(names_format_6, names_format).
subClass(names_format_resolved_GNR, names_format).
subClass(names_format_resolved_OT, names_format).

class(data_format_B).
class(data_format_C).
class(data_format_C_1).
class(data_format_C_2).
subClass(data_format_C_1, data_format_C).
subClass(data_format_C_2, data_format_C_1).

class(tree_format_1).
class(tree_format_2).
class(tree_format_3).
class(tree_format_4).
subClass(tree_format_1,treeFormat).
subClass(tree_format_2,treeFormat).
subClass(tree_format_3,treeFormat).
subClass(tree_format_4,treeFormat).

class(data_format_D).
class(data_format_E).
class(data_format_F).
subClass(X,X) :- class(X).

% INSTANCES
instance(example_convertForm_A_to_B_GET).
instance(example_convertForm_A1_to_B_GET).
instance(example_convertForm_B_to_C_GET).
instance(example_convertForm_B_to_C2_GET).
instance(example_convertForm_C_to_D_GET).
instance(example_convertForm_C2_to_E_GET).
instance(example_convertForm_C_to_Plain_Text_GET).
instance(example_convert_names_format_from_1_to_3).
instance(example_convert_names_format_from_3_to_5).
instance(example_convert_names_format_from_3_to_7).
instance(example_convert_names_format_from_5_to_names_format_resolved_GNR).
instance(example_convert_names_format_from_2_to_4).
instance(example_convert_names_format_from_4_to_6).
instance(example_convert_names_format_from_6_to_names_format_resolved_OT).
instance(example_convertTreeFormat_r_to_NewickTree).

instance(example_convertTreeFormat_r_to_NewickTree).
instance(ex_convertTreeFormat_1_to_2).
instance(ex_convertTreeFormat_2_to_3).
instance(ex_convertTreeFormat_3_to_Newick).
instance(ex_convertTreeFormat_3_to_Phylo4Tree).

convertion_operation_instance(example_convertForm_A_to_B_GET).
convertion_operation_instance(example_convertForm_A1_to_B_GET).
convertion_operation_instance(example_convertForm_B_to_C_GET).
convertion_operation_instance(example_convertForm_B_to_C2_GET).
convertion_operation_instance(example_convertForm_C_to_D_GET).
convertion_operation_instance(example_convertForm_C2_to_E_GET).
convertion_operation_instance(example_convertForm_C_to_Plain_Text_GET).
convertion_operation_instance(example_convert_names_format_from_1_to_3).
convertion_operation_instance(example_convert_names_format_from_3_to_5).
convertion_operation_instance(example_convert_names_format_from_3_to_7).
convertion_operation_instance(example_convert_names_format_from_5_to_names_format_resolved_GNR).
convertion_operation_instance(example_convert_names_format_from_2_to_4).
convertion_operation_instance(example_convert_names_format_from_4_to_6).
convertion_operation_instance(example_convert_names_format_from_6_to_names_format_resolved_OT).
convertion_operation_instance(example_convertTreeFormat_r_to_NewickTree).

convertion_operation_instance(ex_convertTreeFormat_1_to_2).
convertion_operation_instance(ex_convertTreeFormat_2_to_3).
convertion_operation_instance(ex_convertTreeFormat_3_to_Newick).
convertion_operation_instance(ex_convertTreeFormat_3_to_Phylo4Tree).

% HAS INPUT/Output for Data Format Convertion services INSTANCES
convert_op_instance_has_in_df(example_convertForm_A_to_B_GET,data_format_A).
convert_op_instance_has_out_df(example_convertForm_A_to_B_GET,data_format_B).

convert_op_instance_has_in_df(example_convertForm_A1_to_B_GET,data_format_A_1).
convert_op_instance_has_out_df(example_convertForm_A1_to_B_GET,data_format_B).

convert_op_instance_has_in_df(example_convertForm_B_to_C_GET,data_format_B).
convert_op_instance_has_out_df(example_convertForm_B_to_C_GET,data_format_C).

convert_op_instance_has_in_df(example_convertForm_B_to_C2_GET,data_format_B).
convert_op_instance_has_out_df(example_convertForm_B_to_C2_GET,data_format_C_2).

convert_op_instance_has_in_df(example_convertForm_C_to_D_GET,data_format_C).
convert_op_instance_has_out_df(example_convertForm_C_to_D_GET,data_format_D).

convert_op_instance_has_in_df(example_convertForm_C_to_Plain_Text_GET,data_format_C).
convert_op_instance_has_out_df(example_convertForm_C_to_Plain_Text_GET,plain_text).

convert_op_instance_has_in_df(example_convertForm_C2_to_E_GET,data_format_C_2).
convert_op_instance_has_out_df(example_convertForm_C2_to_E_GET,data_format_E).

convert_op_instance_has_in_df(example_convert_names_format_from_1_to_3,names_format_1).
convert_op_instance_has_out_df(example_convert_names_format_from_1_to_3,names_format_3).

convert_op_instance_has_in_df(example_convert_names_format_from_3_to_5,names_format_3).
convert_op_instance_has_out_df(example_convert_names_format_from_3_to_5,names_format_5).

convert_op_instance_has_in_df(example_convert_names_format_from_3_to_7,names_format_3).
convert_op_instance_has_out_df(example_convert_names_format_from_3_to_7,names_format_7).

convert_op_instance_has_in_df(example_convert_names_format_from_5_to_names_format_resolved_GNR,names_format_5).
convert_op_instance_has_out_df(example_convert_names_format_from_5_to_names_format_resolved_GNR,names_format_resolved_GNR).

convert_op_instance_has_in_df(example_convert_names_format_from_2_to_4,names_format_2).
convert_op_instance_has_out_df(example_convert_names_format_from_2_to_4,names_format_4).

convert_op_instance_has_in_df(example_convert_names_format_from_4_to_6,names_format_4).
convert_op_instance_has_out_df(example_convert_names_format_from_4_to_6,names_format_6).

convert_op_instance_has_in_df(example_convert_names_format_from_6_to_names_format_resolved_OT, names_format_6).
convert_op_instance_has_out_df(example_convert_names_format_from_6_to_names_format_resolved_OT, names_format_resolved_OT).

convert_op_instance_has_in_df(example_convertTreeFormat_r_to_NewickTree, nmsu_tree_format).
convert_op_instance_has_out_df(example_convertTreeFormat_r_to_NewickTree, newickTree).


convert_op_instance_has_in_df(ex_convertTreeFormat_1_to_2, tree_format_1).
convert_op_instance_has_out_df(ex_convertTreeFormat_1_to_2, tree_format_2).

convert_op_instance_has_in_df(ex_convertTreeFormat_2_to_3, tree_format_2).
convert_op_instance_has_out_df(ex_convertTreeFormat_2_to_3, tree_format_3).

convert_op_instance_has_in_df(ex_convertTreeFormat_3_to_Newick, tree_format_3).
convert_op_instance_has_out_df(ex_convertTreeFormat_3_to_Newick, newickTree).

convert_op_instance_has_in_df(ex_convertTreeFormat_3_to_Phylo4Tree, tree_format_3).
convert_op_instance_has_out_df(ex_convertTreeFormat_3_to_Phylo4Tree, phylo4Tree).

%=================PLANNING CONCRETE LEVEL================================
%%%% Planning in concrete LEVEL
% define step in each stage of abstract
%#const m = 3.
step_data_format(T, MP_ID , 0..m) :- consider_abtract_step(T), mpID(MP_ID,C), map(T,C).

goal_data_format(T, MP_ID , Time) :- exists_data_format(DF,T,MP_ID,Time),
                                     finally_data_format(DF,T,MP_ID),
                                     map(T,C),
                                     mpID(MP_ID,C),
                                     consider_abtract_step(T).

% Integrated data define initially state for each stage T
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Define exist

exists_data_format(R, T, MP_ID ,0) :- initially_data_format(R,T, MP_ID).
{executable_convert_op_instance(CV_A, T, MP_ID , Time)} :-
             convertion_operation_instance(CV_A),
             step_data_format(T, MP_ID, Time).

:- executable_convert_op_instance(CV_A, T, MP_ID , Time),
   convert_op_instance_has_in_df(CV_A, DF_IN),
   not match_convert_data_format(CV_A, DF_IN, T, MP_ID , Time).

match_convert_data_format(CV_A, DF_IN, T, MP_ID , Time) :-
             convertion_operation_instance(CV_A),
             convert_op_instance_has_in_df(CV_A, DF_IN),
             Time1 <= Time,
             exists_data_format(DF_OU, T, MP_ID , Time1),
             subClass(DF_OU, DF_IN),
             step_data_format(T, MP_ID , Time1),
             step_data_format(T, MP_ID , Time).


-occur_convert_op_instance(CV_A, T, MP_ID , Time) :-
             not occur_convert_op_instance(CV_A, T, MP_ID , Time),
             step_data_format(T, MP_ID , Time),
             convertion_operation_instance(CV_A).

% Basic part : generate a possible sequence of operations INSTANCE
% and records the effects of operations,
1{ occur_convert_op_instance(CV_A, T, MP_ID , Time): convertion_operation_instance(CV_A)}1 :-
           step_data_format(T, MP_ID , Time),
           not goal_data_format(T, MP_ID , Time).

:- occur_convert_op_instance(CV_A, T, MP_ID , Time),
   not executable_convert_op_instance(CV_A, T, MP_ID , Time).

exists_data_format(DF_OUT, T, MP_ID , Time+1) :-
           occur_convert_op_instance(CV_A, T, MP_ID , Time),
           convert_op_instance_has_out_df(CV_A, DF_OUT),
           step_data_format(T, MP_ID , Time).

% Basic part : AWC for operation
:- occur_convert_op_instance(A1,T, MP_ID , Time),
   occur_convert_op_instance(A2,T, MP_ID , Time),
   A1 != A2,
   step_data_format(T, MP_ID , Time).

% Basic part : Move forward for inertial fluent
exists_data_format(DF_X, T, MP_ID , Time+1) :-
            exists_data_format(DF_X,T, MP_ID , Time),
            step_data_format(T, MP_ID , Time),
            not -exists_data_format(DF_X,T, MP_ID , Time+1), Time <= m.
-exists_data_format(DF_X, T,MP_ID,Time+1) :-
            -exists_data_format(DF_X, T, MP_ID, Time),
            step_data_format(T,MP_ID, Time),
            not exists_data_format(DF_X, T,MP_ID,Time+1), Time <= m.

% Basic Part : Goal Tracker 2
success_data_format(T,MP_ID) :- goal_data_format(T, MP_ID, Time),
                                Time <= m,
                                step_data_format(T, MP_ID, Time).
:- not success_data_format(T,MP_ID),
   consider_abtract_step(T),
   map(T,C),
   mpID(MP_ID,C).


%#show occur_convert_op_instance/4.
%#show goal_data_format/4.
%#show initially_data_format/4.
%#show goal_data_format/4.
%#show step_data_format/3.
