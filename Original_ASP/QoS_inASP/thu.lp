1{highest(wf1);highest(wf2);highest(wf3)}1.

qos_rt_wf(wf1,100). qos_rt_wf(wf2,500). qos_rt_wf(wf3,600).
qos_tp_wf(wf1,800). qos_tp_wf(wf2,7100). qos_tp_wf(wf3,2300).
qos_re_wf(wf1,1000). qos_re_wf(wf2,900). qos_re_wf(wf3,800).
qos_av_wf(wf1,1). qos_av_wf(wf2,2). qos_av_wf(wf3,1).

#maximize {RT@4,X : qos_rt_wf(X,RT)}.
#maximize {RE@3,X : qos_re_wf(X,RE)}.
#maximize {TP@2,X : qos_tp_wf(X,TP)}.
#maximize {AV@1,X : qos_tp_wf(X,AV)}.


%------- Optimize 1 ---------------------------
%1 {highest(wf1;wf2;wf3)} 1.

%qos_rt_wf(wf1,100). qos_rt_wf(wf2,500).qos_rt_wf(wf3,600).
%qos_tp_wf(wf1,800). qos_tp_wf(wf2,7100).qos_tp_wf(wf3,2300).
%qos_re_wf(wf1,1000). qos_re_wf(wf2,900).qos_re_wf(wf3,800).
%qos_av_wf(wf1,1). qos_av_wf(wf2,2).qos_av_wf(wf3,1).

%#maximize[highest(A) : qos_rt_wf(A,X) = X @ 4].
%#maximize[highest(A) : qos_re_wf(A,X) = X @ 3].
%#maximize[highest(A) : qos_tp_wf(A,X) = X @ 2].
%#maximize[highest(A) : qos_av_wf(A,X) = X @ 1].

%------- Test thu nghiem CLINGO 3---------------------------
%1 { hotel(1..5) } 1.
%star(1,5). star(2,4). star(3,3). star(4,3). star(5,2).
%cost(1,170). cost(2,140). cost(3,90). cost(4,75). cost(5,60).
%main_street(4).
%noisy :- hotel(X), main_street(X).
%#maximize [ hotel(X) : star(X,Y) = Y @ 1 ].
%#minimize [ hotel(X) : cost(X,Y) : star(X,Z) = Y/Z @ 2 ].
%#minimize { noisy @ 3 }.

% ------- Test thu nghiem CLINO 5------------------------
%1{ hotel(1..5) }1.
%star(1,5). cost(1,170).
%star(2,4). cost(2,140).
%star(3,3). cost(3,90).
%star(4,3). cost(4,75). 
%main_street(4).
%star(5,2). cost(5,60).
%noisy :- hotel(X), main_street(X).

%#maximize { Y@1,X : hotel(X), star(X,Y) }.
%#minimize { Y/Z@2,X : hotel(X), cost(X,Y), star(X,Z) }.
%:~ noisy. [ 1@3 ] 

