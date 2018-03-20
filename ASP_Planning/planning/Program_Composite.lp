%-------------------------------------------------
% Multiple shoot solving
%-------------------------------------------------
#script (python)
import clingo
import time
from random import *
import sys

#-----------------------
def main(prg):
    def load_asp():
        prg.load("single_level_planning_Working.lp")
        prg.load("ontology_TESTING_Working.lp")

    load_asp()
    # prg.configuration.solve.models = 0
    base_program = [("base", [])]

    # Start
    t0 = time.time()
    print("---Start grounding---")
    prg.ground(base_program)
    print("---End grounding---")
    t1 = time.time()
    print("---Time : %s ms" %(str(t1 - t0)))

    prg.solve()
#end.



