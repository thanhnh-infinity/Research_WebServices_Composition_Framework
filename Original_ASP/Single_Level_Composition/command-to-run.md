# Command to include clingcon to compute QoS values - no preference - Weight
clingcon-3.3.0 single_level_planning_Working.lp ontology_TESTING_Working.lp composite_qos_weight.lp --warn=no-operation-undefined --warn=no-variable-unbounded --warn=no-atom-undefined

# Command to include clingcon to compute QoS values - no preference - Raking
clingcon-3.3.0 single_level_planning_Working.lp ontology_TESTING_Working.lp composite_qos_ranking.lp --warn=no-operation-undefined --warn=no-variable-unbounded --warn=no-atom-undefined

# Command to run single program plannging : planning, ontology and planning preference
clingcon-3.3.0 single_level_planning_Working.lp ontology_TESTING_Working.lp composite_qos_weight.lp composite_preference.lp --warn=no-operation-undefined --warn=no-variable-unbounded --warn=no-atom-undefined

or

# Without clingcon - use clingo
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp  composite_preference.lp composite_qos_weight.lp 
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp  composite_preference.lp
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp

# Run program
clingo Program_Composite.lp --warn=no-operation-undefined --warn=no-atom-undefined
clingo Program_Multiple_Workflows.lp
clingo Program_Re_Composite_S1_OnModel.lp --warn=no-operation-undefined --warn=no-atom-undefined
clingo Program_Re_Composite_S2_SimNodes.lp --warn=no-operation-undefined --warn=no-atom-undefined
clingo Program_Re_Composite_S3_Exact.lp --warn=no-operation-undefined --warn=no-atom-undefined

