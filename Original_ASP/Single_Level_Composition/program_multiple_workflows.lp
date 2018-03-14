%-------------------------------------------------
% Multiple shoot solving
%-------------------------------------------------
#script (python)
import clingo
import json
import sys
import time
from random import *

#-----------------------
def measure_QoS():
    return randint(1000,2000) 

# Generate 1{not a; not b;...}.
def build_no_op_rule_for_predicate_With_Active(answer_set_symbols,predicate_name,index,level):
    if ("concrete" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_concrete(%d)."
    elif ("abstract" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_abstract(%d)."
    elif ("single_level" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_single_level(%d)."

    component_rule = ""
    for atom in answer_set_symbols:
        str_atom = str(atom)
        #if (predicate_name in str_atom):
        if (atom.name == predicate_name):
            component_rule = component_rule + "not " + str_atom + "; "
    component_rule = component_rule[:len(component_rule)-2]
    return contrains_distince_wf_rule %(component_rule,index)
#-----------------------
def main(prg):
    def load_asp():
        prg.load("single_level_planning_Working.lp")
        prg.load("ontology_TESTING_Working.lp")
    def enable_active_rule_for_subprogram(prg,multishot_id,level):
        external_name = ""
        if ("concrete" in level):
            external_name = "active_rule_concrete"
        elif ("abstract" in level):
            external_name = "active_rule_abstract"
        elif ("single_level" in level):
            external_name = "active_rule_single_level"
        prg.assign_external(clingo.Function(external_name, [multishot_id]), True)
    def disable_active_rule_for_subprogram(prg,multishot_id,level):
        external_name = ""
        if ("concrete" in level):
            external_name = "active_rule_concrete"
        elif ("abstract" in level):
            external_name = "active_rule_abstract"
        elif ("single_level" in level):
            external_name = "active_rule_single_level"
        prg.release_external(clingo.Function(external_name, [multishot_id]))
    def solve_iter(prg):
        symbols = []
        with prg.solve(yield_=True) as handle:
          for m in handle:
             symbols = m.symbols(shown=True)
        return symbols

    # Load another components
    load_asp()
    # Configuration for the ASP solver
    # prg.configuration.solve.models = 0
    base_program = [("base", [])]

    loop = 1
    multi_shot_id = 1
    super_index = 1

    # Star to find 1st answer set
    t0 = time.time()
    print("---Start grounding---")
    prg.ground(base_program)
    print("---End grounding---")
    t1 = time.time()
    print("---Time : %s ms" %(str(t1 - t0)))

    enable_active_rule_for_subprogram(prg,1,"single_level")
    while (True):     
        if (multi_shot_id == 1):
            answer_sets = []
            with prg.solve(yield_=True) as handle:
                for m in handle:
                    answer_sets = m.symbols(shown=True)

            answer_set_symbols = []
            for x in answer_sets:
                answer_set_symbols.append(x)

        else:
            multi_shot_sub_prg_name_single_level = "multi_shot_single_level_%d" %(multi_shot_id)
            check_rule_define_single_level = "check_add_single_level_ok(%d) :- active_rule_single_level(%d)." %(multi_shot_id,super_index)

            # Build choice rule with active_rule control
            contrains_distince_wf_rule_single_level = build_no_op_rule_for_predicate_With_Active(answer_sets,"occur",super_index,"single_level")

            # Add choice rule with active control to program
            prg.add(multi_shot_sub_prg_name_single_level, [], contrains_distince_wf_rule_single_level  + check_rule_define_single_level)
            prg.ground([(multi_shot_sub_prg_name_single_level, [])])

            # Solve updated program

            answer_sets = []
            answer_sets = solve_iter(prg)

            if (answer_sets is None or len(answer_sets) <=0):
                break

            answer_set_symbols = []
            for x in answer_sets:
                answer_set_symbols.append(x)
        multi_shot_id = multi_shot_id + 1
    disable_active_rule_for_subprogram(prg,super_index,"single_level")
#end.
%-----------------------------------------------
#external active_rule_single_level(1).
check_add_single_level_ok(0).
%-----------------------------------------------


