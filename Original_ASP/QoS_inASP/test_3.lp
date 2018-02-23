has_qos_rt(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,1500).
has_qos_rt(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,356).
has_qos_rt(phylotastic_ResolvedScientificNames_OT_TNRS_GET,721).
has_qos_rt(phylotastic_ResolvedScientificNames_OT_TNRS_POST,100).
has_qos_rt(phylotastic_GetAllSpeciesFromTaxon_OT_GET,32).
has_qos_rt(phylotastic_GetPhylogeneticTree_OT_GET,98).
has_qos_rt(phylotastic_GetPhylogeneticTree_OT_POST,1200).
has_qos_rt(phylotastic_GetPhylogeneticTree_PhyloT_GET,1111).
has_qos_rt(phylotastic_GetPhylogeneticTree_PhyloT_POST,399).
has_qos_rt(phylotastic_GetPhylogeneticTree_Phylomatic_GET,203).
has_qos_rt(phylotastic_GetPhylogeneticTree_Phylomatic_POST,203).
has_qos_rt(phylotastic_GetInformationURLsOfSpecies_EOL_POST,331).
has_qos_rt(phylotastic_GetInformationURLsOfSpecies_EOL_GET,331).
has_qos_rt(phylotastic_GetImageURLsOfSpecies_EOL_GET,169).
has_qos_rt(phylotastic_GetImageURLsOfSpecies_EOL_POST,169).
has_qos_rt(phylotastic_FindScientificNamesFromWeb_GNRD_GET,481).
has_qos_rt(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,450).
has_qos_rt(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,210).
has_qos_rt(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,32).
has_qos_rt(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,200).
has_qos_rt(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,356).
has_qos_rt(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,510).
has_qos_rt(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,1567).
has_qos_rt(phylotastic_GetReconciliationTree_GET,612).
has_qos_rt(phylotastic_GenerateGeneTree_From_Genes,505).
has_qos_rt(phylotastic_GeneTree_Scaling,420).

max_rt(Max):- Max = #max{VRT : has_qos_rt(OP,VRT )}.
min_rt(Min):- Min = #min{VRT : has_qos_rt(OP,VRT )}.
count_rt_el(N):- N = #count{VRT : has_qos_rt(OP,VRT)}.
vector_rt_norm(OP,VRTnorm):- has_qos_rt(OP,VRT ), max_rt(MaxRT), min_rt(MinRT), VRTnorm = 10000clear
*(MaxRT - VRT ) / (MaxRT - MinRT ).

#show vector_rt_norm/2.