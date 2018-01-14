#script (python)
def calculate_QoS_response_time_workflow(currentValue,addValue):
    if (currentValue is None or currentValue.string is None):
        currentValue.string = "0.0"

    fl_currentValue = float(str(currentValue.string))
    #print ("Current : %f", (fl_currentValue))
    fl_addValue = float(str(addValue.string))
    #print ("Add : %f" , (fl_addValue))
    fl_currentValue = fl_currentValue + fl_addValue
    #print ("New : %f" , (fl_currentValue))
    return str(fl_currentValue)
#end.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%QoS for Composition
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Define these QoS of services operation involved in Workflow
has_qos_response_time_involved_concrete(X,RT) :- occur_concrete(X,T), has_qos_response_time(X,RT).
has_qos_throughput_involved_concrete(X,TP) :- occur_concrete(X,T), has_qos_throughput(X,TP).
has_qos_reliability_involved_concrete(X,RA) :- occur_concrete(X,T), has_qos_reliability(X,RA).
has_qos_availability_involved_concrete(X,AA) :- occur_concrete(X,T), has_qos_availability(X,AA).

% Calculate each QoS attribute for whole workflow
% --- Firstly, It worked but It will maker low performance
% --- I changed my mind for this step, I moved these logic to Python generate detail workflow client
%init_qos_response_time_wf("0.0").

%has_total_qos_responste_time_workflow(@calculate_QoS_response_time_workflow(Current,Added),0) :- has_qos_response_time_concrete_occur(X,0,Added), init_qos_response_time_wf(Current).

%has_total_qos_responste_time_workflow(@calculate_QoS_response_time_workflow(Current,Added),T+1) :- has_qos_response_time_concrete_occur(X,T+1,Added), has_total_qos_responste_time_workflow(Current,T).

