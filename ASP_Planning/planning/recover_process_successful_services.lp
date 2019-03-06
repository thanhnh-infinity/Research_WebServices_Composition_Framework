%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%RECOVERY PROCESS 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%
% Remember OLD Workflow => Including DGA Graph : 
%          Node : occur(X,T) 
%          Normal Edge (from service to service) : map(A,I,DF_I,T,B,O,DF_O,T1)
%          Edge start from v_{0} : map(A,I,DF_I,T,initial_state,O,DF_O,0)
% Detect fail service at time T in Graph G


#include "./single_level_planning_Working.lp".
#include "./ontology_TESTING_Working.lp".

%%%%%%%%%% LOGIC FOR RECOVERY PROCESS - FORMALIZATION %%%%%%%%%%%%%%%%

same_operation_id(X,Y) :- operation(X),
                          operation(Y),
                          X = Y.

e_com(initial_state,0,initial_state,0).

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


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Working for PI function
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pi(initial_state,0).
pi(Y',0) :- occur(Y',T3), not e_com(_,_,Y',T3).
pi(Y',1) :- occur(Y',T3), e_com(_,_,Y',T3).

score_g(X) :- X = #sum{V_Y',Y' : pi(Y',V_Y')}.
#maximize{X : score_g(X)}.

%--- Detect time to start avoiding fail service in new workflow -
fail_executed_done(Fail,T) :- fail_service(Fail,Time_Fail),
                              occur(Y,T),
                              Y = Fail,
                              e_com(Fail,R,Y,T). 

:- fail_service(Fail,Time_Fail),
   not fail_executed_done(Fail,T),
   occur(Fail,T).
%---------------------------------------------------------------------

%--------------------------------------------------------------------- 
#show occur/2.
#show map/8.
#show e_com/4.

%#show predecessor/2.


