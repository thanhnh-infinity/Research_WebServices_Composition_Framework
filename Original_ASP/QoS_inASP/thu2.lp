#include <csp>.

&sum {a; b; c} = 113.
vars(a;b;c).
&dom {1..100} = X :- vars(X).
&show {X : vars(X)}.