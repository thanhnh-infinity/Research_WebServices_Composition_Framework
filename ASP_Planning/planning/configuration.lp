#const n = 6.
#const m = 3.

%-------------------------------
% Good view for output predicate in answer set
%-------------------------------
has_input_occur_service_class(A,N,I) :- has_input(A,N,I), occur(A,T), step(T).
has_output_occur_service_class(A,N,O) :- has_output(A,N,O), occur(A,T), step(T).
match_occur_service_class(A,I,T,B,O,T1) :- occur(A,T),
                                           has_input(A,N2,I),
                                           occur(B,T1-1),
                                           has_output(B,N1,O),
                                           A != B,
                                           T >= T1,
                                           T1 > 0,
                                           match(A,I,T,O,T1).
match_occur_service_class(A,I,T,initial_state,O,0) :- occur(A,T),
                                                      has_input(A,N1,I),
                                                      match(A,I,T,O,0).
%-------------------------------
% SHOWING
%-------------------------------
%#show run/2.
%#show map/2.
%#show service/1.
#show occur_concrete/2.
#show occur/2.
%#show possible_occur_concrete/2.
%#show finally_data_format/3.
%#show initially_data_format/3.
%#show match/5.
%#show consider_abtract_step/1.
#show occur_convert_op_instance/4.
%#show mpID/2.
%#show map_df/8.
%#show match/5.
%#show check_add_concrete_ok/2.
%#show active_rule_concrete/1.
%#show check_add_abstract_ok/1.
%#show active_rule_abstract/1.
#show has_input_occur_service_class/3.
#show has_output_occur_service_class/3.
#show match_occur_service_class/6.
#show has_qos_response_time_involved_concrete/2.
#show has_qos_throughput_involved_concrete/2.
#show has_qos_reliability_involved_concrete/2.
#show has_qos_availability_involved_concrete/2.
