%-------------------------------------------------
% Multiple shoot solving
%-------------------------------------------------
#script (python)
import clingo
import json
import sys
import os

def generate_MatchProblemID(O,DF_IN,T2,I,DF_OUT,T3):
    return clingo.Function(O.name + "_" + DF_IN.name + "_" + str(T2.number) + "_" + I.name + "_" + DF_OUT.name + "_" + str(T3.number))

# Generate 1{not a; not b;...}.
def build_no_op_rule_for_predicate_With_Active(answer_set_symbols,predicate_name,index,level):
    if ("concrete" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_concrete(%d)."
    elif ("abstract" in level):
        contrains_distince_wf_rule = "1{%s} :- active_rule_abstract(%d)."

    component_rule = ""
    for atom in answer_set_symbols:
        str_atom = str(atom)
        #if (predicate_name in str_atom):
        if (atom.name == predicate_name):
            component_rule = component_rule + "not " + str_atom + "; "
    component_rule = component_rule[:len(component_rule)-2]
    return contrains_distince_wf_rule %(component_rule,index)

def main(prg):
    def load_asp():

        prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","planning_TESTING.lp"))
        prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","ontology_TESTING.lp"))
        prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","concrete_TESTING.lp"))
        prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","concrete_DF_convert.lp"))
        prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","configuration.lp"))
        prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","composite_qos.lp"))
        prg.load(os.path.join(os.getcwd(),"ASP_Planning","planning","planning_preference.lp"))

    def enable_active_rule_for_subprogram(prg,multishot_id,level):
        external_name = ""
        if ("concrete" in level):
            external_name = "active_rule_concrete"
        elif ("abstract" in level):
            external_name = "active_rule_abstract"
        prg.assign_external(clingo.Function(external_name, [multishot_id]), True)
    def disable_active_rule_for_subprogram(prg,multishot_id,level):
        external_name = ""
        if ("concrete" in level):
            external_name = "active_rule_concrete"
        elif ("abstract" in level):
            external_name = "active_rule_abstract"
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
    prg.ground(base_program)

    enable_active_rule_for_subprogram(prg,1,"abstract")
    while (True): # outter loop for abstract
        if (multi_shot_id == 1):
            answer_set_abstract = []
            with prg.solve(yield_=True) as handle:
                for m in handle:
                    answer_set_abstract = m.symbols(shown=True)

            answer_set_symbols = []
            for x in answer_set_abstract:
                answer_set_symbols.append(x)

        else:
            multi_shot_sub_prg_name_abstract = "multi_shot_abstract_%d" %(multi_shot_id)
            check_rule_define_abstract = "check_add_abstract_ok(%d) :- active_rule_abstract(%d)." %(multi_shot_id,super_index)

            # Build choice rule with active_rule control
            contrains_distince_wf_rule_abstract = build_no_op_rule_for_predicate_With_Active(answer_set_abstract,"occur",super_index,"abstract")

            # Add choice rule with active control to program
            prg.add(multi_shot_sub_prg_name_abstract, [], contrains_distince_wf_rule_abstract  + check_rule_define_abstract)
            prg.ground([(multi_shot_sub_prg_name_abstract, [])])

            # Solve updated program
            answer_set_abstract = []
            answer_set_abstract = solve_iter(prg)

            if (answer_set_abstract is None or len(answer_set_abstract) <=0):
                break

            answer_set_symbols = []
            for x in answer_set_abstract:
                answer_set_symbols.append(x)


        loop = 1
        enable_active_rule_for_subprogram(prg,multi_shot_id,"concrete")
        while (True): # Inner loop for concrete
            if (answer_set_symbols is None or len(answer_set_symbols) <= 0):
                break
            multi_shot_sub_prg_name = "multi_shot_concrete_%d_%d" %(multi_shot_id,loop)
            check_rule_define = "check_add_concrete_ok(%d,%d) :- active_rule_concrete(%d)." %(multi_shot_id,loop,multi_shot_id)

            # Build choice rule with active_rule control
            contrains_distince_wf_rule = build_no_op_rule_for_predicate_With_Active(answer_set_symbols,"occur_concrete",multi_shot_id,"concrete")

            # Add choice rule with active control to program
            prg.add(multi_shot_sub_prg_name, [], contrains_distince_wf_rule  + check_rule_define)
            prg.ground([(multi_shot_sub_prg_name, [])])

            # Solve updated program
            answer_set_symbols = []
            answer_set_symbols = solve_iter(prg)
            loop = loop + 1
        #disable_active_rule_for_subprogram(prg,multi_shot_id,"concrete")
        multi_shot_id = multi_shot_id + 1
        #break
    disable_active_rule_for_subprogram(prg,super_index,"abstract")
#end.
%-----------------------------------------------
#external active_rule_concrete(1..10000).
#external active_rule_abstract(1).
check_add_abstract_ok(0).
%-----------------------------------------------
%#show run/2.
%#show map/2.
%#show service/1.
%#show occur_concrete/2.
%#show occur/2.
%#show possible_occur_concrete/2.
%#show finally_data_format/3.
%#show initially_data_format/3.
%#show match/5.
%#show consider_abtract_step/1.
%#show occur_convert_op_instance/4.
%#show mpID/2.
%#show map_df/8.
%#show match/5.
%#show check_add_concrete_ok/2.
%#show active_rule_concrete/1.
%#show check_add_abstract_ok/1.
%#show active_rule_abstract/1.
%#show has_input_occur/3.
%#show has_output_occur/3.
%#show match_service_class_occur/5.
