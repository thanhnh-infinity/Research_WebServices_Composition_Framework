#script (python)
import clingo

def get_Function(X,Y,Z):
    return clingo.Function(X.name + "-" + Y.name + "-" + Z.name)
def get_Tuple(X,Y,Z):
    return clingo.Tuple([X.name,Y.name,Z.name])
  
#end.

p_function(@get_Function(a,b,c)).
p_tuple(@get_Tuple(a,b,c),12).


sim_index(a,b,1).
sim_index(a,c,2).
sim_index(a,d,3).

find_max_sim_index(Max_Sim) :- Max_Sim = #max{Z : sim_index(X,Y,Z)}.

select(X,Max_Sim) :- find_max_sim_index(Max_Sim), sim_index(M,X,Max_Sim).

