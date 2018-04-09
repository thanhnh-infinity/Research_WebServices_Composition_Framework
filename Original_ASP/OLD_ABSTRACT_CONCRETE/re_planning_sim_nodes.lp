#script (python)
from random import *
def calculate_sim_between_2_nodes(occur_node_1,index_1,occur_node_2,index_2):
  return randint(0,100)
#end.
occur(x,1).
occur(y,1).
occur(z,1).
occur(m,1).
occur(n,1).
occur(p,1).


old_occur(a,0).
old_occur(b,1).
old_occur(c,2).
old_occur(d,3).
old_occur(e,4).
old_occur(f,5).
single_sim_2_nodes(X,Y,Z) :- old_occur(X,I1), occur(Y,I2), Z = @calculate_sim_between_2_nodes(X,I1,Y,I2).
sum_single_sim_2_nodes(T) :- T = #sum {Z : single_sim_2_nodes(X,Y,Z)}.
sim_nodes_workflows(R,T,N_Old_Nodes,N_New_Nodes) :- sum_single_sim_2_nodes(T), N_Old_Nodes = #count {X: old_occur(X,I1)}, N_New_Nodes = #count {Y : occur(Y,I2)}, R = 2*T / (N_Old_Nodes + N_New_Nodes).

#show sim_nodes_workflows/4.