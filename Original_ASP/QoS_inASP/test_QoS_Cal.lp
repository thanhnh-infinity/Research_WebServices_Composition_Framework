#script (python)
def times_realnumbers(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    fl_result = fl_X * fl_Y

    return str(fl_result)
def sum_realnumbers(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    fl_result = fl_X + fl_Y

    return str(fl_result)
def minus_realnumbers(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    fl_result = fl_X - fl_Y

    return str(fl_result)
def divide_realnumbers(X,Y,flag):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        if ("norm_max" in flag):
          return "1.0"
        else:
          return None
    else:
        fl_Y = float(str(Y.string))

    if (fl_Y == 0.0):
        if ("norm_max" in flag):
          return "1.0"
        else:
          return None

    fl_result = fl_X / fl_Y
    return str(fl_result)
def find_max(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    return str(X.string) if fl_X >= fl_Y else str(Y.string)
def find_min(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    return str(X.string) if fl_X < fl_Y else str(Y.string)
#end.


a_random_qos(a,0,"4.12").
a_random_qos(b,1,"2.44").
a_random_qos(c,2,"16.2").
a_random_qos(d,3,"5.005").
a_random_qos(e,4,"19.33").

% Find max
init_max("-999999").
iter_max_value(0,@find_max(CurrentMax,Test)) :- a_random_qos(_,0,Test), init_max(CurrentMax).
iter_max_value(T+1,@find_max(CurrentMax,Test)) :- a_random_qos(_,T+1,Test), iter_max_value(T,CurrentMax).
max_element_value(Max) :- iter_max_value(T,Max), count_element(N), T = N - 1.

% Find max
init_min("999999999999999").
iter_min_value(0,@find_min(CurrentMin,Test)) :- a_random_qos(_,0,Test), init_min(CurrentMin).
iter_min_value(T+1,@find_min(CurrentMin,Test)) :- a_random_qos(_,T+1,Test), iter_min_value(T,CurrentMin).
min_element_value(Min) :- iter_min_value(T,Min), count_element(N), T = N - 1.

% Count number of elements
count_element(N) :- N = #count{X : a_random_qos(X,_,Y)}.

% Normalization by Max : norm = (v - min) / (max - min)
a_random_qos_norm(X,I,Ynorm) :- a_random_qos(X,I,Y), max_element_value(Max) , min_element_value(Min) , Ynorm = @divide_realnumbers(T,M,"norm_max"), T = @minus_realnumbers(Y,Min), M = @minus_realnumbers(Max,Min).


% Calculate Score of List in WF = sum of all*weight
weight("0.5").

init_random_qos("0.0").
iter_sum_random_qos(@sum_realnumbers(Current,Added),0) :- a_random_qos_norm(X,0,Added), init_random_qos(Current).
iter_sum_random_qos(@sum_realnumbers(Current,Added),T+1) :- a_random_qos_norm(X,T+1,Added), iter_sum_random_qos(Current,T).
final_sum_all_random_qos(Last) :- iter_sum_random_qos(Last,T), count_element(N), T = N - 1.

score_random_qos(@times_realnumbers(Last,WeightValue)) :- final_sum_all_random_qos(Last),weight(WeightValue).

#show max_element_value/1.
#show min_element_value/1.
#show a_random_qos_norm/3.
#show final_sum_all_random_qos/1.
#show score_random_qos/1.
