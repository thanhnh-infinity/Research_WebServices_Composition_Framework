# Command to include clingcon to compute QoS values - no preference
clingcon-3.3.0 single_level_planning_Working.lp ontology_TESTING_Working.lp composite_qos_weight.lp --warn=no-operation-undefined --warn=no-variable-unbounded --warn=no-atom-undefined

# Command to run single program plannging : planning, ontology and planning preference
clingcon-3.3.0 single_level_planning_Working.lp ontology_TESTING_Working.lp composite_qos_weight.lp composite_preference.lp --warn=no-operation-undefined --warn=no-variable-unbounded --warn=no-atom-undefined

or

# Without clingcon - use clingo
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp  composite_preference.lp composite_qos_weight.lp 
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp  composite_preference.lp
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp

# Run program
clingo Program_Composite.lp
clingo Program_Multiple_Workflows.lp
clingo Program_Re_Composite_S1_OnModel.lp

