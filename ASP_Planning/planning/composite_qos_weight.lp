#include <csp>.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%QoS for Composition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ---------------------------------------
% Logic for QoS
% ---------------------------------------
weight_response_time(4).
weight_throughput(3).
weight_availability(1).
weight_reliability(2).
% ---------------------------------------
% Working for Response Time (smaller is better)
% ---------------------------------------
has_qos_response_time_involved_concrete(X,T,R_RT_V) :- occur(X,T), 
                                                       has_qos_response_time(X,RT_V), 
                                                       R_RT_V = 1000000/RT_V.

&sum{qos_response_time(0)} = RT_V :- has_qos_response_time_involved_concrete(X,0,RT_V).
&sum{qos_response_time(V); RT_V} = qos_response_time(T) :- has_qos_response_time_involved_concrete(X,T,RT_V), 
                                                           V = T - 1, 
                                                           T >= 1, goal(G), T <= G - 1.

%&sum{qos_response_time(Y)} = sum_response_time :- Y = X - 1, goal(X).
%&show{sum_response_time/0}.
%&show{qos_response_time/1}.

%#show has_qos_response_time_involved_concrete/3.
% Solution 2
%&sum{V,T,X : has_qos_response_time_involved_concrete(X,T,V)} = sum_response_time.
%&show{sum_response_time/0}.


% ---------------------------------------
% Working for Throughput (bigger is better)
% ---------------------------------------

has_qos_throughput_involved_concrete(X,T,TP_AVG_V) :- occur(X,T), 
                                                      has_qos_throughput(X,TP_V),
                                                      goal(G),
                                                      TP_AVG_V = TP_V/G.

&sum{qos_throughput(0)} = RT_V :- has_qos_throughput_involved_concrete(X,0,RT_V).
&sum{qos_throughput(V); RT_V} = qos_throughput(T) :- has_qos_throughput_involved_concrete(X,T,RT_V), 
                                                     V = T - 1, 
                                                     T >= 1, goal(G), T <= G - 1.
%#show has_qos_throughput_involved_concrete/3.
%&show{qos_throughput/1}.
%#show has_qos_throughput_involved_concrete/3.
% ---------------------------------------
% Working for Availability (probability) (bigger is better) - Using MIN
% ---------------------------------------
has_qos_availability_involved_concrete(X,T,AV_V) :- occur(X,T), 
                                                    has_qos_availability(X,AV_V).
qos_availability(AV_W) :- AV_W = #min {AV_V : has_qos_availability_involved_concrete(X,T,AV_V)}.

% ---------------------------------------
% Working for Reliability (bigger is better)
% ---------------------------------------
has_qos_reliability_involved_concrete(X,T,RE_AVG_V) :- occur(X,T), 
                                                       has_qos_reliability(X,RE_V),
                                                       goal(G),
                                                       RE_AVG_V = RE_V/G.
&sum{qos_reliability(0)} = RE_V :- has_qos_reliability_involved_concrete(X,0,RE_V).
&sum{qos_reliability(V); RE_V} = qos_reliability(T) :- has_qos_reliability_involved_concrete(X,T,RE_V), 
                                                       V = T - 1, 
                                                       T >= 1, goal(G), T <= G - 1.
                              
%#show has_qos_reliability_involved_concrete/3.
%&show{qos_reliability/1}.
%-----------------------------------------------
&sum{qos_response_time(V);qos_throughput(V);qos_reliability(V);AV_W} = score_qos_workflow :- goal(T), 
                                                                                             V = T - 1,
                                                                                             qos_availability(AV_W).
&show{score_qos_workflow}.
%&minimize{qos_response_time(10)}.