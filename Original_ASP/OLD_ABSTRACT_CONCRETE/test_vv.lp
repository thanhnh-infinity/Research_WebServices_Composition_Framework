#script(python)
def calculate_sim_matching(X,Y):
    return 1001
#end.

old_occur(a,0).
old_occur(b,1).
old_occur(c,2).
old_occur(d,3).
old_match_occur_service_class(b,ib,1,a,oa,0).
old_match_occur_service_class(a,ia,0,initial_state,init_data,0).
old_match_occur_service_class(c,ic,2,b,ob,1).
old_match_occur_service_class(d,id,3,c,oc,2).

occur(check0,0).
match_occur_service_class(check0,ic0,0,initial_state,data,0).

occur(check1,1).
match_occur_service_class(check1,ic1,1,check0,oc0,0).

occur(check2,2).
match_occur_service_class(check2,ic2,2,check1,oc1,1).

occur(check3,3).
match_occur_service_class(check3,ic3,3,check2,oc2,2).



sim_index(Z) :- old_occur(a,0),old_occur(b,1),old_occur(c,2),old_occur(d,3),old_match_occur_service_class(b,ib,1,a,oa,0),old_match_occur_service_class(a,ia,0,initial_state,init_data,0),old_match_occur_service_class(c,ic,2,b,ob,1),old_match_occur_service_class(d,id,3,c,oc,2),occur(A0,0), match_occur_service_class(A0,IA0,0,B0,OB0,TB0),occur(A1,1), match_occur_service_class(A1,IA1,1,B1,OB1,TB1),occur(A2,2), match_occur_service_class(A2,IA2,2,B2,OB2,TB2),occur(A3,3), match_occur_service_class(A3,IA3,3,B3,OB3,TB3),Z = @calculate_sim_matching((old_occur(a,0),old_occur(b,1),old_occur(c,2),old_occur(d,3),old_match_occur_service_class(b,ib,1,a,oa,0),old_match_occur_service_class(a,ia,0,initial_state,init_data,0),old_match_occur_service_class(c,ic,2,b,ob,1),old_match_occur_service_class(d,id,3,c,oc,2)),(occur(A0,0), match_occur_service_class(A0,IA0,0,B0,OB0,TB0),occur(A1,1), match_occur_service_class(A1,IA1,1,B1,OB1,TB1),occur(A2,2), match_occur_service_class(A2,IA2,2,B2,OB2,TB2),occur(A3,3), match_occur_service_class(A3,IA3,3,B3,OB3,TB3))).
#maximize{Z:sim_index(Z)}.