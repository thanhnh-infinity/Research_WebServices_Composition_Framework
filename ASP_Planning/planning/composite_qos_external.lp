has_qos_response_time_involved_concrete(X,T,RT) :- occur(X,T),has_qos_response_time(X,RT).
has_qos_throughput_involved_concrete(X,T,TP) :- occur(X,T), has_qos_throughput(X,TP).
has_qos_reliability_involved_concrete(X,T,RA) :- occur(X,T), has_qos_reliability(X,RA).
has_qos_availability_involved_concrete(X,T,AA) :- occur(X,T), has_qos_availability(X,AA).                                                       


#show has_qos_response_time_involved_concrete/3.
#show has_qos_throughput_involved_concrete/3.
#show has_qos_reliability_involved_concrete/3.
#show has_qos_availability_involved_concrete/3.
                                                       