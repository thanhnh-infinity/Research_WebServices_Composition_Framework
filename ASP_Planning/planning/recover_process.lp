%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%RECOVERY PROCESS 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%
% Remember OLD Workflow => Including DGA Graph : 
%          Node : occur(X,T) 
%          Normal Edge (from service to service) : map(A,I,DF_I,T,B,O,DF_O,T1)
%          Edge start from v_{0} : map(A,I,DF_I,T,initial_state,O,DF_O,0)
% Detect fail service at time T in Graph G

%#include "./failure_detection.lp".
#include "./single_level_planning_Working.lp".
#include "./ontology_TESTING_Working.lp".

%%%%%%%%%% LOGIC FOR RECOVERY PROCESS - FORMALIZATION %%%%%%%%%%%%%%%%

same_operation_id(X,Y) :- operation(X),
                          operation(Y),
                          X = Y.

e_com(initial_state,0,initial_state,0).

%e_com(Y,T1,Y',T3) :- e_com(initial_state,0,initial_state,0), 
%                     old_occ_exe(Y,T1),
%                     old_map_exe(Y,_,_,T1,initial_state,_,_,0),  
%                     occur(Y',T3),
%                     map(Y',_,_,T3,initial_state,_,_,0),
%                     T1 >= 0,
%                     T3 >= 0,
%                     same_operation_id(Y,Y').

e_com(Y,T1,Y',T3) :- e_com(initial_state,0,initial_state,0), 
                     old_occ_exe(Y,T1),
                     old_map_exe(Y,I,DF_I,T1,initial_state,O,DF_O,0),  
                     occur(Y',T3),
                     map(Y',I',DF_I',T3,initial_state,O',DF_O',0),
                     T1 >= 0,
                     T3 >= 0,
                     I = I', DF_I = DF_I',
                     O = O', DF_O = DF_O',
                     same_operation_id(Y,Y').                     

%e_com(Y,T1,Y',T3) :- e_com(X,T2,X',T4), 
%                     old_occ_exe(Y,T1),
%                     old_map_exe(Y,_,_,T1,X,_,_,T2+1),  
%                     occur(Y',T3),
%                     map(Y',_,_,T3,X',_,_,T4+1),
%                     T1 >= T2+1,
%                     T3 >= T4+1,
%                     X != initial_state, X' != initial_state,
%                     same_operation_id(Y,Y').

e_com(Y,T1,Y',T3) :- e_com(X,T2,X',T4), 
                     old_occ_exe(Y,T1),
                     old_map_exe(Y,I,DF_I,T1,X,O,DF_O,T2+1),  
                     occur(Y',T3),
                     map(Y',I',DF_I',T3,X',O',DF_O',T4+1),
                     T1 >= T2+1,
                     T3 >= T4+1,
                     I = I', DF_I = DF_I',
                     O = O', DF_O = DF_O',
                     X != initial_state, X' != initial_state,
                     same_operation_id(Y,Y').                     

score_g(initial_state,0).

score_g(Y',0) :- occur(Y',T3),
                 not e_com(_,_,Y',T3).
                 
predecessor(X',Y') :- occur(Y',T3),
                      map(Y',_,_,T3,X',_,_,T4),
                      old_occ_exe(Y,T1),
                      old_map_exe(Y,_,_,T1,X,_,_,T2),
                      e_com(Y,_,Y',_),
                      e_com(X,_,X',_).

score_g(Y',V_Y') :-  S = #sum{V_X',X' : predecessor(X',Y'),score_g(X',V_X')},
                     V_Y' = S + 1,
                     occur(Y',T3),
                     e_com(_,_,Y',T3).

recovery_score(F_V) :- F_V = #max{V_Y': score_g(Y',V_Y')}.

#maximize{F_V : recovery_score(F_V)}.

%--- Detect time to start avoiding fail service in new workflow ------

max_score_at(Y',T) :- recovery_score(F_V),
                      score_g(Y',F_V),
                      occur(Y',T).

:- fail_service(Fail,Time_Fail), 
   occur(Fail,T), 
   T > Tmax, 
   max_score_at(_,Tmax).

%---------------------------------------------------------------------
%#show occur/2.
%#show map/8.
%#show goal/1.
#show e_com/4.
%#show score_g/2.
%#show count/2.
%#show predecessor/2.
#show recovery_score/1.
%#show old_map_exe/8.
#show max_score_at/2.
