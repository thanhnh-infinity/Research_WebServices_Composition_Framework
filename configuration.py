import json

CONFIGURATION_DATA = {
    "ontology_web_serivce_asp" : "ontology_TESTING.lp",
    "abtract_level_planning_asp_file" : "planning_TESTING.lp",
    "dataformat_mapping_level_planning_asp_file" : "planning_concrete_level_mapping_data_format.lp",
    "goal_state_asp_file" : "goal_state.lp",
    "initial_state_asp_file" : "initial_state.lp",
    "planning_configuration_asp_file":"planning_configuration.lp",
    "planning_preference_asp_file":"planning_preference.lp",
    "planning_qos_asp_file":"planning_qos.lp"
}


WEIGHT_QoS_DATA = {
  "response_time" : 0.4,
  "throughput" : 0.3,
  "availability" : 0.2,
  "reliability" : 0.1
}