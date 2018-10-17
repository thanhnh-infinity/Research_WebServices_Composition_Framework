%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%RECOVERY PROCESS 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%
% Remember OLD Workflow => Including DGA Graph : 
%          Node : occur(X,T) 
%          Normal Edge (from service to service) : map(A,I,DF_I,T,B,O,DF_O,T1)
%          Edge start from v_{0} : map(A,I,DF_I,T,initial_state,O,DF_O,0)
% Detect fail service at time T in Graph G

#include "./failure_detection.lp".
#include "./single_level_planning_Working.lp".
#include "./ontology_TESTING_Working.lp".

%%%%%%%%%% LOGIC FOR RECOVERY PROCESS %%%%%%%%%%%%%%%%

same_operation_id(X,Y) :- operation(X),
                          operation(Y),
                          X = Y.

e_map(initial_state,0,initial_state,0).

e_map(Y,T1,Y',T3) :- e_map(initial_state,0,initial_state,0), 
               old_occ_exe(Y,T1),
               old_map_exe(Y,_,_,T1,initial_state,_,_,0),  
               occur(Y',T3),
               map(Y',_,_,T3,initial_state,_,_,0),
               T1 >= 0,
               T3 >= 0,
               same_operation_id(Y,Y').
               
e_map(Y,T1,Y',T3) :- e_map(X,T2,X',T4), 
                     old_occ_exe(Y,T1),
                     old_map_exe(Y,_,_,T1,X,_,_,T2+1),  
                     occur(Y',T3),
                     map(Y',_,_,T3,X',_,_,T4+1),
                     T1 >= T2+1,
                     T3 >= T4+1,
                     X != initial_state, X' != initial_state,
                     same_operation_id(Y,Y').

%-----------------------------------------------------
#show occur/2.
%#show map/8.
%#show goal/1.

#show e_map/4.
%#show old_map_exe/8.