import sys
import time
import planning_algorithms
import configuration
from app_web_serivce import Interact_Planning_Engine

try:
    method = sys.argv[1]
    print "Method == " + method
    t0 = time.time()
except:
    print "Command : main.py <method> \n"
    print "Method cound be : back-forward, back-tracking, asp_pure"
    sys.exit(0)

def main():
    if (method == "asp_pure"):
        print Interact_Planning_Engine.generateWorkflow()
    else:
        concretes = planning_algorithms.procedure_concrete_planning(method)
        print("==========================")
        print("----Concrete plan(s)------")
        if (concretes is not None and len(concretes) > 0):
            step = 1
            for concrete in concretes:
                print "%s : %s" %(str(step),concrete)
                step = step + 1
            print("----Size of conrete : %s" %(str(len(concretes))))
        else:
            print("--No conrete plan available---")
        t1 = time.time()
        total = t1-t0
        print("---Time Performance : %s miliseconds" %(str(total)))
#################################################
####MAIN
#################################################
if __name__ == '__main__':
    main()