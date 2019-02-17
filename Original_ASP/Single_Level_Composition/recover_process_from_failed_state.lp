%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%RECOVERY PROCESS 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%
% Remember OLD Workflow => Including DGA Graph : 
%          Node : occur(X,T) 
%          Normal Edge (from service to service) : map(A,I,DF_I,T,B,O,DF_O,T1)
%          Edge start from v_{0} : map(A,I,DF_I,T,initial_state,O,DF_O,0)
% Detect fail service at time T in Graph G

#include "./usercase/failed_state/1/failure_detection_1.lp".
#include "./usercase/failed_state/1/domain.lp".
#include "./single_level_planning_need_domain.lp".
#include "./ontology_TESTING_Working.lp".

%%%%%%%%%% LOGIC FOR RECOVERY PROCESS - FORMALIZATION %%%%%%%%%%%%%%%%

resource_reuseable(R,DF_R,Data) :- resource_generated(R,DF_R,Data),
                                   occur(Y',T),
                                   map(Y',I,DF_I,T,initial_state,R,DF_R,0).

reused(X) :- X = #count{R,DF_R,Data : resource_reuseable(R,DF_R,Data)}.

#maximize{X : reused(X)}.


%---------------------------------------------------------------------

%--------------------------------------------------------------------- 
#show occur/2.
#show map/8.

%#show predecessor/2.


