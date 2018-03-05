% Simulate result of web service composition
% --- List all occur_concrete that results of service composition
% ---------------------------------------
occur_concrete(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,1).
occur_concrete(phylotastic_ResolvedScientificNames_OT_TNRS_GET,2).
occur_concrete(phylotastic_GetPhylogeneticTree_Phylomatic_POST,4).
occur_concrete(phylotastic_GenerateGeneTree_From_Genes,0).
occur_concrete(phylotastic_GeneTree_Scaling,3).
occur_concrete(phylotastic_GetReconciliationTree_GET,5).

% ---------------------------------------
% Simulate all qos data
% Copy from Ontology_TESTING
% Change ASP QoS value = real value *1000
% Response time will be milliseconds
%-------------For Response Time-----------------------------------------
has_qos_response_time(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,680).
has_qos_response_time(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,710).
has_qos_response_time(phylotastic_ResolvedScientificNames_OT_TNRS_GET,440).
has_qos_response_time(phylotastic_ResolvedScientificNames_OT_TNRS_POST,480).
has_qos_response_time(phylotastic_GetAllSpeciesFromTaxon_OT_GET,330).
has_qos_response_time(phylotastic_GetPhylogeneticTree_OT_GET,4040).
has_qos_response_time(phylotastic_GetPhylogeneticTree_OT_POST,4210).
has_qos_response_time(phylotastic_GetPhylogeneticTree_PhyloT_GET,3990).
has_qos_response_time(phylotastic_GetPhylogeneticTree_PhyloT_POST,4010).
has_qos_response_time(phylotastic_GetPhylogeneticTree_Phylomatic_GET,2030).
has_qos_response_time(phylotastic_GetPhylogeneticTree_Phylomatic_POST,2133).
has_qos_response_time(phylotastic_GetInformationURLsOfSpecies_EOL_POST,310).
has_qos_response_time(phylotastic_GetInformationURLsOfSpecies_EOL_GET,320).
has_qos_response_time(phylotastic_GetImageURLsOfSpecies_EOL_GET,1690).
has_qos_response_time(phylotastic_GetImageURLsOfSpecies_EOL_POST,1710).
has_qos_response_time(phylotastic_FindScientificNamesFromWeb_GNRD_GET,4810).
has_qos_response_time(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,450).
has_qos_response_time(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,2100).
has_qos_response_time(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,320).
has_qos_response_time(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,2000).
has_qos_response_time(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,3560).
has_qos_response_time(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,5100).
has_qos_response_time(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,15670).
has_qos_response_time(phylotastic_GetReconciliationTree_GET,6120).
has_qos_response_time(phylotastic_GenerateGeneTree_From_Genes,5050).
has_qos_response_time(phylotastic_GeneTree_Scaling,4200).
has_qos_response_time(google_ConvertCountryCodeToName_GET,1000).
has_qos_response_time(openTree_GetTaxonomyNameFromSciName_GET,2000).
has_qos_response_time(openTree_GetScientificNameFromAName_GET,300).

%-------------For Throughput--------------------------------------------
has_qos_throughput(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,19410).
has_qos_throughput(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,20000).
has_qos_throughput(phylotastic_ResolvedScientificNames_OT_TNRS_GET,27490).
has_qos_throughput(phylotastic_ResolvedScientificNames_OT_TNRS_POST,28000).
has_qos_throughput(phylotastic_GetAllSpeciesFromTaxon_OT_GET,28920).
has_qos_throughput(phylotastic_GetPhylogeneticTree_OT_GET,4330).
has_qos_throughput(phylotastic_GetPhylogeneticTree_OT_POST,4330).
has_qos_throughput(phylotastic_GetPhylogeneticTree_PhyloT_GET,1250).
has_qos_throughput(phylotastic_GetPhylogeneticTree_PhyloT_POST,1250).
has_qos_throughput(phylotastic_GetPhylogeneticTree_Phylomatic_GET,5620).
has_qos_throughput(phylotastic_GetPhylogeneticTree_Phylomatic_POST,6200).
has_qos_throughput(phylotastic_GetInformationURLsOfSpecies_EOL_POST,2292).
has_qos_throughput(phylotastic_GetInformationURLsOfSpecies_EOL_GET,2292).
has_qos_throughput(phylotastic_GetImageURLsOfSpecies_EOL_GET,5550).
has_qos_throughput(phylotastic_GetImageURLsOfSpecies_EOL_POST,5550).
has_qos_throughput(phylotastic_FindScientificNamesFromWeb_GNRD_GET,5560).
has_qos_throughput(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,27170).
has_qos_throughput(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,6600).
has_qos_throughput(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,28560).
has_qos_throughput(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,12500).
has_qos_throughput(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,910).
has_qos_throughput(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,23800).
has_qos_throughput(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,27780).
has_qos_throughput(phylotastic_GetReconciliationTree_GET,15120).
has_qos_throughput(phylotastic_GenerateGeneTree_From_Genes,1780).
has_qos_throughput(phylotastic_GeneTree_Scaling,6300).
has_qos_throughput(google_ConvertCountryCodeToName_GET,0).
has_qos_throughput(openTree_GetTaxonomyNameFromSciName_GET,0).
has_qos_throughput(openTree_GetScientificNameFromAName_GET,0).

%-------------For Reliability-------------------------------------------
has_qos_reliability(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,576440).
has_qos_reliability(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,576440).
has_qos_reliability(phylotastic_ResolvedScientificNames_OT_TNRS_GET,576480).
has_qos_reliability(phylotastic_ResolvedScientificNames_OT_TNRS_POST,576480).
has_qos_reliability(phylotastic_GetAllSpeciesFromTaxon_OT_GET,577760).
has_qos_reliability(phylotastic_GetPhylogeneticTree_OT_GET,577450).
has_qos_reliability(phylotastic_GetPhylogeneticTree_OT_POST,577450).
has_qos_reliability(phylotastic_GetPhylogeneticTree_PhyloT_GET,586090).
has_qos_reliability(phylotastic_GetPhylogeneticTree_PhyloT_POST,586090).
has_qos_reliability(phylotastic_GetPhylogeneticTree_Phylomatic_GET,586080).
has_qos_reliability(phylotastic_GetPhylogeneticTree_Phylomatic_POST,586080).
has_qos_reliability(phylotastic_GetInformationURLsOfSpecies_EOL_POST,577930).
has_qos_reliability(phylotastic_GetInformationURLsOfSpecies_EOL_GET,577930).
has_qos_reliability(phylotastic_GetImageURLsOfSpecies_EOL_GET,577840).
has_qos_reliability(phylotastic_GetImageURLsOfSpecies_EOL_POST,577840).
has_qos_reliability(phylotastic_FindScientificNamesFromWeb_GNRD_GET,576300).
has_qos_reliability(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,576340).
has_qos_reliability(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,577810).
has_qos_reliability(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,577780).
has_qos_reliability(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,520120).
has_qos_reliability(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,1173060).
has_qos_reliability(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,600000).
has_qos_reliability(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,576410).
has_qos_reliability(phylotastic_GetReconciliationTree_GET,580870).
has_qos_reliability(phylotastic_GenerateGeneTree_From_Genes,300980).
has_qos_reliability(phylotastic_GeneTree_Scaling,577230).
has_qos_reliability(google_ConvertCountryCodeToName_GET,0).
has_qos_reliability(openTree_GetTaxonomyNameFromSciName_GET,0).
has_qos_reliability(openTree_GetScientificNameFromAName_GET,0).

%-------------For Availability------------------------------------------
has_qos_availability(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,1000).
has_qos_availability(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,1000).
has_qos_availability(phylotastic_ResolvedScientificNames_OT_TNRS_GET,1000).
has_qos_availability(phylotastic_ResolvedScientificNames_OT_TNRS_POST,1000).
has_qos_availability(phylotastic_GetAllSpeciesFromTaxon_OT_GET,1000).
has_qos_availability(phylotastic_GetPhylogeneticTree_OT_GET,1000).
has_qos_availability(phylotastic_GetPhylogeneticTree_OT_POST,1000).
has_qos_availability(phylotastic_GetPhylogeneticTree_PhyloT_GET,1000).
has_qos_availability(phylotastic_GetPhylogeneticTree_PhyloT_POST,1000).
has_qos_availability(phylotastic_GetPhylogeneticTree_Phylomatic_GET,1000).
has_qos_availability(phylotastic_GetPhylogeneticTree_Phylomatic_POST,1000).
has_qos_availability(phylotastic_GetInformationURLsOfSpecies_EOL_POST,1000).
has_qos_availability(phylotastic_GetInformationURLsOfSpecies_EOL_GET,1000).
has_qos_availability(phylotastic_GetImageURLsOfSpecies_EOL_GET,1000).
has_qos_availability(phylotastic_GetImageURLsOfSpecies_EOL_POST,1000).
has_qos_availability(phylotastic_FindScientificNamesFromWeb_GNRD_GET,1000).
has_qos_availability(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,1000).
has_qos_availability(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,1000).
has_qos_availability(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,1000).
has_qos_availability(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,1000).
has_qos_availability(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,1000).
has_qos_availability(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,1000).
has_qos_availability(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,1000).
has_qos_availability(phylotastic_GetReconciliationTree_GET,1000).
has_qos_availability(phylotastic_GenerateGeneTree_From_Genes,1000).
has_qos_availability(phylotastic_GeneTree_Scaling,1000).
has_qos_availability(google_ConvertCountryCodeToName_GET,1000).
has_qos_availability(openTree_GetTaxonomyNameFromSciName_GET,1000).
has_qos_availability(openTree_GetScientificNameFromAName_GET,1000).

% ---------------------------------------
% Logic for QoS based on WEIGHT
% ---------------------------------------
weight_response_time(4).
weight_throughput(3).
weight_availability(1).
weight_reliability(2).
% ---------------------------------------
% Working for Response Time (smaller is better)
% ---------------------------------------
has_qos_response_time_involved_concrete(X,T,R_RT_V) :- occur_concrete(X,T), has_qos_response_time(X,RT_V), R_RT_V = 1000000/RT_V.
qos_response_time_workflow(RT_S) :- RT_S = #sum{RT_V,T : has_qos_response_time_involved_concrete(X,T,RT_V)}.
% ---------------------------------------
% Working for Throughput (bigger is better)
% ---------------------------------------
has_qos_throughput_involved_concrete(X,T,TP_V) :- occur_concrete(X,T), 
                                                  has_qos_throughput(X,TP_V).
qos_throughput_workflow(TP_S) :- S = #sum{TP_V,T : has_qos_throughput_involved_concrete(X,T,TP_V)}, 
                                 N_TP = #count{T : has_qos_throughput_involved_concrete(X,T,Y)},
                                 TP_S = S / N_TP.
% ---------------------------------------
% Working for Availability (probability) (bigger is better) - Using MIN
% ---------------------------------------
has_qos_availability_involved_concrete(X,T,AV_V) :- occur_concrete(X,T), 
                                                    has_qos_availability(X,AV_V).
qos_availability_workflow(AV_W) :- AV_W = #min {AV_V : has_qos_availability_involved_concrete(X,T,AV_V)}.
% ---------------------------------------
% Working for Reliability (bigger is better)
% ---------------------------------------
has_qos_reliability_involved_concrete(X,T,RE_V) :- occur_concrete(X,T), has_qos_reliability(X,RE_V).
qos_reliability_workflow(RE_S) :- S = #sum{RE_V,T : has_qos_reliability_involved_concrete(X,T,RE_V)}, 
                                  N_RE = #count{T : has_qos_reliability_involved_concrete(X,T,Y)},
                                  RE_S = S / N_RE.
%-----------------------------------------------
score_qos_workflow(Final_Score) :- qos_response_time_workflow(RT), weight_response_time(W_RT),
                                   qos_throughput_workflow(TP), weight_throughput(W_TP),
                                   qos_reliability_workflow(RE), weight_reliability(W_RE),
                                   qos_availability_workflow(AV), weight_availability(W_AV),
                                   Final_Score = RT*W_RT/10 + TP*W_TP/10 + RE*W_RE/10 + AV*W_AV/10.

#maximize{Final_Score:score_qos_workflow(Final_Score)}.
%-----------------------------------------------
#show qos_response_time_workflow/1.
#show qos_throughput_workflow/1.
#show qos_reliability_workflow/1.
#show qos_availability_workflow/1.
#show score_qos_workflow/1.
%#show has_qos_response_time_involved_concrete/3.