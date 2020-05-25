%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%RECOVERY PROCESS 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%% FAILURE DETECTION %%%%%%%%%%%%%%%%%%%%%%%%%%%
% Remember OLD Workflow => Including DGA Graph : 
%          Node : occur(X,T) 
%          Normal Edge (from service to service) : map(A,I,DF_I,T,B,O,DF_O,T1)
%          Edge start from v_{0} : map(A,I,DF_I,T,initial_state,O,DF_O,0)
% Detect fail service at time T in Graph G

% For all domains
#include "./single_level_planning_need_domain.lp".
#include "./ontology_TESTING_Working.lp".

% For Phylotastic Domain
#include "./usercase/failed_state_N/0/failure_detection_6.lp".
#include "./usercase/failed_state_N/0/domain.lp".

% For Shopping Domain
%#include "./usercase/shopping/0/failure_fail_state.lp".
%#include "./usercase/shopping/0/domain.lp".


%%%%%%%%%% LOGIC FOR RECOVERY PROCESS - FORMALIZATION %%%%%%%%%%%%%%%%

%%% Define reused resources and count them

produced_resource(R,DF_R) :-  resource_generated(R,DF_R,DataR),
                              occur(X,T),
                              operation_has_output_has_data_format(X,R,DF_R).

resource_reuseable(R,DF_R,DataR) :- resource_generated(R,DF_R,DataR),
                                    occur(Y',T), goal(G), T < G,
                                    map(Y',I,DF_I,T,initial_state,R,DF_R,0),
                                    not produced_resource(R,DF_R).

reused(X) :- X = #count{R,DF_R,Data : resource_reuseable(R,DF_R,Data)}.

#maximize{X : reused(X)}.


%%% Avoid failed services
:- fail_service(A,T), is_used_operation(A).

%---------------------------------------------------------------------

%--------------------------------------------------------------------- 
#show occur/2.
%#show map/8.
#show goal/1.
#show resource_reuseable/3.
%#show produced_resource/2.


