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
has_qos_response_time_involved_concrete(X,T,R_RT_V) :- occur_concrete(X,T), has_qos_response_time(X,RT_V), R_RT_V = 1000000/RT_V.
qos_response_time_workflow(RT_S) :- RT_S = #sum{RT_V,T : has_qos_response_time_involved_concrete(X,T,RT_V)}.

%qos_response_time_workflow(RT_S) :- RT_S = #sum{RT_V : has_qos_response_time_involved_concrete(X,T,RT_V)}.

% ---------------------------------------
% Working for Throughput (bigger is better)
% ---------------------------------------
has_qos_throughput_involved_concrete(X,T,TP_V) :- occur_concrete(X,T), 
                                                  has_qos_throughput(X,TP_V).
qos_throughput_workflow(TP_S) :- S = #sum{TP_V,T : has_qos_throughput_involved_concrete(X,T,TP_V)}, 
                                 N_TP = #count{T : has_qos_throughput_involved_concrete(X,T,Y)},
                                 TP_S = S / N_TP.

%qos_throughput_workflow(TP_S) :- S = #sum{TP_V : has_qos_throughput_involved_concrete(X,T,TP_V)}, 
%                                 N_TP = #count{T : has_qos_throughput_involved_concrete(X,T,Y)},
%                                 TP_S = S / N_TP.

%qos_throughput_workflow(TP_S) :- TP_S = #sum{TP_V : has_qos_throughput_involved_concrete(X,T,TP_V)}.

% ---------------------------------------
% Working for Availability (probability) (bigger is better) - Using MIN
% ---------------------------------------
has_qos_availability_involved_concrete(X,T,AV_V) :- occur_concrete(X,T), 
                                                    has_qos_availability(X,AV_V).
qos_availability_workflow(AV_W) :- AV_W = #min {AV_V : has_qos_availability_involved_concrete(X,T,AV_V)}.

% ---------------------------------------
% Working for Reliability (bigger is better)
% ---------------------------------------
has_qos_reliability_involved_concrete(X,T,RE_V) :- occur_concrete(X,T), has_qos_reliability(X,RE_V).

qos_reliability_workflow(RE_S) :- S = #sum{RE_V,T : has_qos_reliability_involved_concrete(X,T,RE_V)}, 
                                  N_RE = #count{T : has_qos_reliability_involved_concrete(X,T,Y)},
                                  RE_S = S / N_RE.

%qos_reliability_workflow(RE_S) :- S = #sum{RE_V : has_qos_reliability_involved_concrete(X,T,RE_V)}, 
%                                  N_RE = #count{T : has_qos_reliability_involved_concrete(X,T,Y)},
%                                  RE_S = S / N_RE.                                  

%qos_reliability_workflow(4556).

%-----------------------------------------------
score_qos_workflow(Final_Score) :- qos_response_time_workflow(RT), weight_response_time(W_RT),
                                   qos_throughput_workflow(TP), weight_throughput(W_TP),
                                   qos_reliability_workflow(RE), weight_reliability(W_RE),
                                   qos_availability_workflow(AV), weight_availability(W_AV),
                                   Final_Score = RT*W_RT/10 + TP*W_TP/10 + RE*W_RE/10 + AV*W_AV/10.
%#maximize{Final_Score:score_qos_workflow(Final_Score)}.

