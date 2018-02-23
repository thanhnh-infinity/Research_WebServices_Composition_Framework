#script (python)
def times_realnumbers(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    fl_result = fl_X * fl_Y

    return str(fl_result)
def sum_realnumbers(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    fl_result = fl_X + fl_Y

    return str(fl_result)
def minus_realnumbers(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    fl_result = fl_X - fl_Y

    return str(fl_result)
def divide_realnumbers(X,Y,flag):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        if ("norm_min" in str(flag.string)):
          return "1.0"
        else:
          if (Y.number is None):
             return None
          else:
             fl_Y = float(Y.number)
    else:
        fl_Y = float(str(Y.string))

    if (fl_Y == 0.0):
        if ("norm_min" in str(flag.string)):
          return "1.0"
        else:
          return None

    fl_result = fl_X / fl_Y
    return str(fl_result)
def find_max(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    return str(X.string) if fl_X >= fl_Y else str(Y.string)
def find_min(X,Y):
    fl_X = 0.0
    fl_Y = 0.0
    if (X is None or X.string is None):
        fl_X = float("0.0")
    else:
        fl_X = float(str(X.string))
    if (Y is None or Y.string is None):
        fl_Y = float("0.0")
    else:
        fl_Y = float(str(Y.string))
    return str(X.string) if fl_X < fl_Y else str(Y.string)
def inverse_value(X):
    fl_X = 0.0
    if (X is None or X.string is None):
       fl_X = 0.0
    else:
       fl_X = float(str(X.string))

    if (fl_X == 0.0):
        return "1.0"
    else:
        return str(1/fl_X)
#end.

% Simulate result of web service composition
% --- List all occur_concrete that results of service composition
% ---------------------------------------
occur_concrete(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,1).
occur_concrete(phylotastic_ResolvedScientificNames_OT_TNRS_GET,2).
occur_concrete(phylotastic_GetPhylogeneticTree_Phylomatic_POST,4).
occur_concrete(phylotastic_GenerateGeneTree_From_Genes,0).
occur_concrete(phylotastic_GeneTree_Scaling,3).
occur_concrete(phylotastic_GetReconciliationTree_GET,5).


weight_response_time("0.4").
weight_throughput("0.3").
weight_availability("0.2").
weight_reliability("0.1").

% ---------------------------------------
% Simulate all qos data
% Copy from Ontology_TESTING

%-------------For Response Time-----------------------------------------
has_qos_response_time(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,"0.68").
has_qos_response_time(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,"0.68").
has_qos_response_time(phylotastic_ResolvedScientificNames_OT_TNRS_GET,"0.44").
has_qos_response_time(phylotastic_ResolvedScientificNames_OT_TNRS_POST,"0.44").
has_qos_response_time(phylotastic_GetAllSpeciesFromTaxon_OT_GET,"0.33").
has_qos_response_time(phylotastic_GetPhylogeneticTree_OT_GET,"4.04").
has_qos_response_time(phylotastic_GetPhylogeneticTree_OT_POST,"4.04").
has_qos_response_time(phylotastic_GetPhylogeneticTree_PhyloT_GET,"3.99").
has_qos_response_time(phylotastic_GetPhylogeneticTree_PhyloT_POST,"3.99").
has_qos_response_time(phylotastic_GetPhylogeneticTree_Phylomatic_GET,"2.03").
has_qos_response_time(phylotastic_GetPhylogeneticTree_Phylomatic_POST,"2.03").
has_qos_response_time(phylotastic_GetInformationURLsOfSpecies_EOL_POST,"0.31").
has_qos_response_time(phylotastic_GetInformationURLsOfSpecies_EOL_GET,"0.31").
has_qos_response_time(phylotastic_GetImageURLsOfSpecies_EOL_GET,"1.69").
has_qos_response_time(phylotastic_GetImageURLsOfSpecies_EOL_POST,"1.69").
has_qos_response_time(phylotastic_FindScientificNamesFromWeb_GNRD_GET,"4.81").
has_qos_response_time(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,"0.45").
has_qos_response_time(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,"2.1").
has_qos_response_time(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,"0.32").
has_qos_response_time(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,"2.0").
has_qos_response_time(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,"3.56").
has_qos_response_time(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,"5.1").
has_qos_response_time(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,"15.67").
has_qos_response_time(phylotastic_GetReconciliationTree_GET,"6.12").
has_qos_response_time(phylotastic_GenerateGeneTree_From_Genes,"5.05").
has_qos_response_time(phylotastic_GeneTree_Scaling,"4.2").
has_qos_response_time(google_ConvertCountryCodeToName_GET,"0").
has_qos_response_time(openTree_GetTaxonomyNameFromSciName_GET,"0").
has_qos_response_time(openTree_GetScientificNameFromAName_GET,"0").

%-------------For Throughput--------------------------------------------
has_qos_throughput(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,"19.41").
has_qos_throughput(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,"19.41").
has_qos_throughput(phylotastic_ResolvedScientificNames_OT_TNRS_GET,"27.49").
has_qos_throughput(phylotastic_ResolvedScientificNames_OT_TNRS_POST,"27.49").
has_qos_throughput(phylotastic_GetAllSpeciesFromTaxon_OT_GET,"28.92").
has_qos_throughput(phylotastic_GetPhylogeneticTree_OT_GET,"4.33").
has_qos_throughput(phylotastic_GetPhylogeneticTree_OT_POST,"4.33").
has_qos_throughput(phylotastic_GetPhylogeneticTree_PhyloT_GET,"1.25").
has_qos_throughput(phylotastic_GetPhylogeneticTree_PhyloT_POST,"1.25").
has_qos_throughput(phylotastic_GetPhylogeneticTree_Phylomatic_GET,"5.62").
has_qos_throughput(phylotastic_GetPhylogeneticTree_Phylomatic_POST,"5.62").
has_qos_throughput(phylotastic_GetInformationURLsOfSpecies_EOL_POST,"22.92").
has_qos_throughput(phylotastic_GetInformationURLsOfSpecies_EOL_GET,"22.92").
has_qos_throughput(phylotastic_GetImageURLsOfSpecies_EOL_GET,"5.55").
has_qos_throughput(phylotastic_GetImageURLsOfSpecies_EOL_POST,"5.55").
has_qos_throughput(phylotastic_FindScientificNamesFromWeb_GNRD_GET,"5.56").
has_qos_throughput(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,"27.17").
has_qos_throughput(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,"6.6").
has_qos_throughput(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,"28.56").
has_qos_throughput(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,"12.5").
has_qos_throughput(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,"0.91").
has_qos_throughput(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,"23.8").
has_qos_throughput(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,"27.78").
has_qos_throughput(phylotastic_GetReconciliationTree_GET,"15.12").
has_qos_throughput(phylotastic_GenerateGeneTree_From_Genes,"1.78").
has_qos_throughput(phylotastic_GeneTree_Scaling,"6.3").
has_qos_throughput(google_ConvertCountryCodeToName_GET,"0").
has_qos_throughput(openTree_GetTaxonomyNameFromSciName_GET,"0").
has_qos_throughput(openTree_GetScientificNameFromAName_GET,"0").

%-------------For Reliability-------------------------------------------
has_qos_reliability(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,"576.44").
has_qos_reliability(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,"576.44").
has_qos_reliability(phylotastic_ResolvedScientificNames_OT_TNRS_GET,"576.48").
has_qos_reliability(phylotastic_ResolvedScientificNames_OT_TNRS_POST,"576.48").
has_qos_reliability(phylotastic_GetAllSpeciesFromTaxon_OT_GET,"577.76").
has_qos_reliability(phylotastic_GetPhylogeneticTree_OT_GET,"577.45").
has_qos_reliability(phylotastic_GetPhylogeneticTree_OT_POST,"577.45").
has_qos_reliability(phylotastic_GetPhylogeneticTree_PhyloT_GET,"586.09").
has_qos_reliability(phylotastic_GetPhylogeneticTree_PhyloT_POST,"586.09").
has_qos_reliability(phylotastic_GetPhylogeneticTree_Phylomatic_GET,"586.08").
has_qos_reliability(phylotastic_GetPhylogeneticTree_Phylomatic_POST,"586.08").
has_qos_reliability(phylotastic_GetInformationURLsOfSpecies_EOL_POST,"577.93").
has_qos_reliability(phylotastic_GetInformationURLsOfSpecies_EOL_GET,"577.93").
has_qos_reliability(phylotastic_GetImageURLsOfSpecies_EOL_GET,"577.84").
has_qos_reliability(phylotastic_GetImageURLsOfSpecies_EOL_POST,"577.84").
has_qos_reliability(phylotastic_FindScientificNamesFromWeb_GNRD_GET,"576.3").
has_qos_reliability(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,"576.34").
has_qos_reliability(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,"577.81").
has_qos_reliability(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,"577.78").
has_qos_reliability(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,"520.12").
has_qos_reliability(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,"1173.06").
has_qos_reliability(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,"600.0").
has_qos_reliability(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,"576.41").
has_qos_reliability(phylotastic_GetReconciliationTree_GET,"580.87").
has_qos_reliability(phylotastic_GenerateGeneTree_From_Genes,"300.98").
has_qos_reliability(phylotastic_GeneTree_Scaling,"577.23").
has_qos_reliability(google_ConvertCountryCodeToName_GET,"0.0").
has_qos_reliability(openTree_GetTaxonomyNameFromSciName_GET,"0.0").
has_qos_reliability(openTree_GetScientificNameFromAName_GET,"0.0").

%-------------For Availability------------------------------------------
has_qos_availability(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,"1.0").
has_qos_availability(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,"1.0").
has_qos_availability(phylotastic_ResolvedScientificNames_OT_TNRS_GET,"1.0").
has_qos_availability(phylotastic_ResolvedScientificNames_OT_TNRS_POST,"1.0").
has_qos_availability(phylotastic_GetAllSpeciesFromTaxon_OT_GET,"1.0").
has_qos_availability(phylotastic_GetPhylogeneticTree_OT_GET,"1.0").
has_qos_availability(phylotastic_GetPhylogeneticTree_OT_POST,"1.0").
has_qos_availability(phylotastic_GetPhylogeneticTree_PhyloT_GET,"1.0").
has_qos_availability(phylotastic_GetPhylogeneticTree_PhyloT_POST,"1.0").
has_qos_availability(phylotastic_GetPhylogeneticTree_Phylomatic_GET,"1.0").
has_qos_availability(phylotastic_GetPhylogeneticTree_Phylomatic_POST,"1.0").
has_qos_availability(phylotastic_GetInformationURLsOfSpecies_EOL_POST,"1.0").
has_qos_availability(phylotastic_GetInformationURLsOfSpecies_EOL_GET,"1.0").
has_qos_availability(phylotastic_GetImageURLsOfSpecies_EOL_GET,"1.0").
has_qos_availability(phylotastic_GetImageURLsOfSpecies_EOL_POST,"1.0").
has_qos_availability(phylotastic_FindScientificNamesFromWeb_GNRD_GET,"1.0").
has_qos_availability(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,"1.0").
has_qos_availability(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,"1.0").
has_qos_availability(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,"1.0").
has_qos_availability(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,"1.0").
has_qos_availability(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,"1.0").
has_qos_availability(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,"0.75").
has_qos_availability(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,"1.0").
has_qos_availability(phylotastic_GetReconciliationTree_GET,"1.0").
has_qos_availability(phylotastic_GenerateGeneTree_From_Genes,"1.0").
has_qos_availability(phylotastic_GeneTree_Scaling,"1.0").
has_qos_availability(google_ConvertCountryCodeToName_GET,"0").
has_qos_availability(openTree_GetTaxonomyNameFromSciName_GET,"0").
has_qos_availability(openTree_GetScientificNameFromAName_GET,"0").

% ---------------------------------------
% Logic for QoS
% ---------------------------------------

% Define these QoS of services operation involved in Workflow
has_qos_response_time_involved_concrete(X,T,RT) :- occur_concrete(X,T), has_qos_response_time(X,RT).
has_qos_throughput_involved_concrete(X,T,TP) :- occur_concrete(X,T), has_qos_throughput(X,TP).
has_qos_reliability_involved_concrete(X,T,RA) :- occur_concrete(X,T), has_qos_reliability(X,RA).
has_qos_availability_involved_concrete(X,T,AA) :- occur_concrete(X,T), has_qos_availability(X,AA).

% ---------------------------------------
% Working for Response Time (smaller is better)
% ---------------------------------------
% because Response Time smaller is better 1/value
vector_response_time_involved(X,T,@inverse_value(RT)) :- has_qos_response_time_involved_concrete(X,T,RT).

% Find max QoS Response Time
init_max_res_time("-9999999999").
iter_max_res_time(0,@find_max(CurrentMax,Test)) :- vector_response_time_involved(_,0,Test), init_max_res_time(CurrentMax).
iter_max_res_time(T+1,@find_max(CurrentMax,Test)) :- vector_response_time_involved(_,T+1,Test), iter_max_res_time(T,CurrentMax).
max_response_time(Max) :- iter_max_res_time(T,Max), count_element_response_time_vector(N), T = N - 1.

% Find min
init_min_res_time("9999999999").
iter_min_res_time(0,@find_min(CurrentMin,Test)) :- vector_response_time_involved(_,0,Test), init_min_res_time(CurrentMin).
iter_min_res_time(T+1,@find_min(CurrentMin,Test)) :- vector_response_time_involved(_,T+1,Test), iter_min_res_time(T,CurrentMin).
min_response_time(Min) :- iter_min_res_time(T,Min), count_element_response_time_vector(N), T = N - 1.

% Count number of elements in QoS vector
count_element_response_time_vector(N) :- N = #count{X : has_qos_response_time_involved_concrete(X,_,_)}.

% Normalization Response by Max : norm = (v - min) / (max - min)
vector_response_time_involved_norm(X,I,RTnorm) :- vector_response_time_involved(X,I,RT), max_response_time(Max) , min_response_time(Min) , RTnorm = @divide_realnumbers(T,M,"norm_min"), T = @minus_realnumbers(RT,Min), M = @minus_realnumbers(Max,Min).

% Calculate Value of QoS Response = sum of all Responstime component
init_response_time_wf("0.0").
iter_response_time_wf(@sum_realnumbers(Current,Added),0) :- vector_response_time_involved_norm(X,0,Added), init_response_time_wf(Current).
iter_response_time_wf(@sum_realnumbers(Current,Added),T+1) :- vector_response_time_involved_norm(X,T+1,Added), iter_response_time_wf(Current,T).
final_response_time_wf(Last) :- iter_response_time_wf(Last,T), count_element_response_time_vector(N), T = N - 1.

score_response_time_wf(@times_realnumbers(Last,WeightValue)) :- final_response_time_wf(Last),weight_response_time(WeightValue).

% ---------------------------------------
% Working for Throughput (bigger is better)
% ---------------------------------------
% bigger is better so vector throughput keep data in ontology
vector_throughput_involved(X,T,TP) :- has_qos_throughput_involved_concrete(X,T,TP).

% Find max QoS Throughput
init_max_throughput("-9999999999").
iter_max_throughput(0,@find_max(CurrentMax,Test)) :- vector_throughput_involved(_,0,Test), init_max_throughput(CurrentMax).
iter_max_throughput(T+1,@find_max(CurrentMax,Test)) :- vector_throughput_involved(_,T+1,Test), iter_max_throughput(T,CurrentMax).
max_throughput(Max) :- iter_max_throughput(T,Max), count_element_throughput_vector(N), T = N - 1.

% Find min
init_min_throughput("9999999999").
iter_min_throughput(0,@find_min(CurrentMin,Test)) :- vector_throughput_involved(_,0,Test), init_min_throughput(CurrentMin).
iter_min_throughput(T+1,@find_min(CurrentMin,Test)) :- vector_throughput_involved(_,T+1,Test), iter_min_throughput(T,CurrentMin).
min_throughput(Min) :- iter_min_throughput(T,Min), count_element_throughput_vector(N), T = N - 1.

% Count number of elements in QoS vector Throughput
count_element_throughput_vector(N) :- N = #count{X : has_qos_throughput_involved_concrete(X,_,_)}.

% Normalization throughput by Min : norm = (v - min) / (max - min)
vector_throughput_involved_norm(X,I,TPnorm) :- vector_throughput_involved(X,I,TP), max_throughput(Max) , min_throughput(Min) , TPnorm = @divide_realnumbers(T,M,"norm_min"), T = @minus_realnumbers(TP,Min), M = @minus_realnumbers(Max,Min).

% Calculate Value of QoS throughput = sum of all Throughput component / n = average
init_throughput_wf("0.0").
iter_throughput_wf(@sum_realnumbers(Current,Added),0) :- vector_throughput_involved_norm(X,0,Added), init_throughput_wf(Current).
iter_throughput_wf(@sum_realnumbers(Current,Added),T+1) :- vector_throughput_involved_norm(X,T+1,Added), iter_throughput_wf(Current,T).
final_throughput_wf(@divide_realnumbers(Last,N,"normally")) :- iter_throughput_wf(Last,T), count_element_throughput_vector(N), T = N - 1.

score_throughput_wf(@times_realnumbers(Last,WeightValue)) :- final_throughput_wf(Last),weight_throughput(WeightValue).

% ---------------------------------------
% Working for Availability (probability) (bigger is better)
% ---------------------------------------
% bigger is better so vector throughput keep data in ontology
vector_availability_involved(X,T,AV) :- has_qos_availability_involved_concrete(X,T,AV).

% Find max QoS availability
init_max_availability("-9999999999").
iter_max_availability(0,@find_max(CurrentMax,Test)) :- vector_availability_involved(_,0,Test), init_max_availability(CurrentMax).
iter_max_availability(T+1,@find_max(CurrentMax,Test)) :- vector_availability_involved(_,T+1,Test), iter_max_availability(T,CurrentMax).
max_availability(Max) :- iter_max_availability(T,Max), count_element_availability_vector(N), T = N - 1.

% Find min
init_min_availability("9999999999").
iter_min_availability(0,@find_min(CurrentMin,Test)) :- vector_availability_involved(_,0,Test), init_min_availability(CurrentMin).
iter_min_availability(T+1,@find_min(CurrentMin,Test)) :- vector_availability_involved(_,T+1,Test), iter_min_availability(T,CurrentMin).
min_availability(Min) :- iter_min_availability(T,Min), count_element_availability_vector(N), T = N - 1.

% Count number of elements in QoS vector
count_element_availability_vector(N) :- N = #count{X : has_qos_availability_involved_concrete(X,_,_)}.

% Normalization availability by Min : norm = (v - min) / (max - min)
vector_availability_involved_norm(X,I,AVnorm) :- vector_availability_involved(X,I,AV), max_availability(Max) , min_availability(Min) , AVnorm = @divide_realnumbers(T,M,"norm_min"), T = @minus_realnumbers(AV,Min), M = @minus_realnumbers(Max,Min).

% Calculate Value of QoS availability = Pi of availability component (multiple)
init_availability_wf("1.0").
iter_availability_wf(@times_realnumbers(Current,Added),0) :- vector_availability_involved_norm(X,0,Added), init_availability_wf(Current).
iter_availability_wf(@times_realnumbers(Current,Added),T+1) :- vector_availability_involved_norm(X,T+1,Added), iter_availability_wf(Current,T).
final_availability_wf(Last) :- iter_availability_wf(Last,T), count_element_availability_vector(N), T = N - 1.

score_availability_wf(@times_realnumbers(Last,WeightValue)) :- final_availability_wf(Last),weight_availability(WeightValue).

% ---------------------------------------
% Working for Reliability (bigger is better)
% ---------------------------------------
% bigger is better so vector throughput keep data in ontology
vector_reliability_involved(X,T,RA) :- has_qos_reliability_involved_concrete(X,T,RA).

% Find max QoS availability
init_max_reliability("-9999999999").
iter_max_reliability(0,@find_max(CurrentMax,Test)) :- vector_reliability_involved(_,0,Test), init_max_reliability(CurrentMax).
iter_max_reliability(T+1,@find_max(CurrentMax,Test)) :- vector_reliability_involved(_,T+1,Test), iter_max_reliability(T,CurrentMax).
max_reliability(Max) :- iter_max_reliability(T,Max), count_element_reliability_vector(N), T = N - 1.

% Find min
init_min_reliability("9999999999").
iter_min_reliability(0,@find_min(CurrentMin,Test)) :- vector_reliability_involved(_,0,Test), init_min_reliability(CurrentMin).
iter_min_reliability(T+1,@find_min(CurrentMin,Test)) :- vector_reliability_involved(_,T+1,Test), iter_min_reliability(T,CurrentMin).
min_reliability(Min) :- iter_min_reliability(T,Min), count_element_reliability_vector(N), T = N - 1.

% Count number of elements in QoS vector
count_element_reliability_vector(N) :- N = #count{X : has_qos_reliability_involved_concrete(X,_,_)}.

% Normalization reliability by Min : norm = (v - min) / (max - min)
vector_reliability_involved_norm(X,I,RAnorm) :- vector_reliability_involved(X,I,RA), max_reliability(Max) , min_reliability(Min) , RAnorm = @divide_realnumbers(T,M,"norm_min"), T = @minus_realnumbers(RA,Min), M = @minus_realnumbers(Max,Min).

% Calculate Value of QoS reliability = sum of all reliability component / n = average
init_reliability_wf("0.0").
iter_reliability_wf(@sum_realnumbers(Current,Added),0) :- vector_reliability_involved_norm(X,0,Added), init_reliability_wf(Current).
iter_reliability_wf(@sum_realnumbers(Current,Added),T+1) :- vector_reliability_involved_norm(X,T+1,Added), iter_reliability_wf(Current,T).
final_reliability_wf(@divide_realnumbers(Last,N,"normally")) :- iter_reliability_wf(Last,T), count_element_reliability_vector(N), T = N - 1.

score_reliability_wf(@times_realnumbers(Last,WeightValue)) :- final_reliability_wf(Last),weight_reliability(WeightValue).

%-----------------------------------------------

sum_group_1(@sum_realnumbers(X,Y)) :- score_reliability_wf(X), score_throughput_wf(Y).
sum_group_2(@sum_realnumbers(X,Y)) :- score_response_time_wf(X), score_availability_wf(Y).
score_qos_wf(@sum_realnumbers(X,Y)) :- sum_group_1(X),sum_group_2(Y).

%-----------------------------------------------
%#show vector_reliability_involved_norm/3.
%#show max_reliability/1.
%#show min_reliability/1.
%#show count_element_reliability_vector/1.
#show score_reliability_wf/1.
#show score_throughput_wf/1.
#show score_response_time_wf/1.
#show score_availability_wf/1.
#show score_qos_wf/1.