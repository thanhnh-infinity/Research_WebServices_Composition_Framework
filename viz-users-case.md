1. Input : resource_FreeText (raw_text)   
   Output : resource_AreSameTree (boolean)
   Output : resource_SpeciesTree (newick)
   Clingcon

   Fail (convert_df_text_format_raw_to_plain, 0) :  No fix -- GOOD
   Fail (phylotastic_FindScientificNamesFromFreeText_GNRD_GET, 1) : No fix -- GOOD
   Fail (convert_df_sci_names_format_1_to_3, 2) : No fix -- GOOD
   Fail (convert_df_sci_names_format_3_to_5, 3) : No fix -- GOOD
   Fail (convert_df_sci_names_format_5_to_OT, 4) :  Recovery -- GOOD  (can be example)
   Fail (phylotastic_ResolvedScientificNames_OT_TNRS_GET, 5) : Recovery -- GOOD (Can be example)
   Fail (phylotastic_GetPhylogeneticTree_OT_POST, 6) : Recovery -- GOOD (can be example)
   Fail (convert_species_tree_format_NMSU_to_NewickTree, 7) :  Timeout Err0r - Failed (Type 1) ???

2. Input : resource_FreeText (plain)    =======> Example
   Output : resource_AreSameTree (boolean)
   Ouput : resource_SpecieTRee (newick)
   Clingo

   Fail (phylotastic_FindScientificNamesFromFreeText_GNRD_GET, 0) :   No fix -- GOOD
   Fail (convert_df_sci_names_format_1_to_3, 1) :  No fix -- GOOD
   Fail (convert_df_sci_names_format_3_to_5, 2) :  No fix -- GOOD
   Fail (convert_df_sci_names_format_5_to_OT, 3) :  Recovery -- GOOD (Example)
   Fail (phylotastic_ResolvedScientificNames_OT_TNRS_GET, 4) : Recovery -- GOOD (W Example)
   Fail (phylotastic_GetPhylogeneticTree_OT_GET, 5) : Recovery --- GOOD (Example)
   Fail (phylotastic_GetPhylogeneticTree_OT_POST, 6) : Recovery -- GOOD (Example)
   Fail (convert_species_tree_format_NMSU_to_NewickTree, 7) : Recovery --- GOOD (Strong Example)

3. Input : resource_WebURL (http_url)           =======> Example
   Output : resource_AreSameTree (boolean)
   Output : resource_SpeciesTree (newick)
   Clingo

   Fail (phylotastic_FindScientificNamesFromWeb_GNRD_GET, 0) :  No fix -- GOOD
   Fail (convert_df_sci_names_format_2_to_4, 1) :  No fix -- GOOD
   Fail (convert_df_sci_names_format_4_to_6, 2) :  No fix -- GOOD
   Fail (convert_df_sci_names_format_6_to_OT, 3) : Recovery -- GOOD (w example)
   Fail (phylotastic_ResolvedScientificNames_OT_TNRS_POST, 4) : Recovory -- GOOD (w example)
   Fail (phylotastic_GetPhylogeneticTree_OT_GET, 5) : Recovery -- GOOD 
   Fail (phylotastic_GetPhylogeneticTree_OT_POST, 6) : Recovery -- GOOD
   Fail (convert_species_tree_format_NMSU_to_NewickTree, 7) : Recovery -- GOOD (Strong Example)

4. Input : resource_FreeText (raw_text), speciesTree (compare_tree_format)
   Output : resource_AreSameTree (boolean)
   Clingo

   Fail (convert_df_text_format_raw_to_plain, 0)  :  No fix -- GOOD
   Fail (phylotastic_FindScientificNamesFromFreeText_GNRD_GET, 1) : No fix -- GOOD
   Fail (convert_df_sci_names_format_1_to_3, 2) : No fix -- GOOD
   Fail (convert_df_sci_names_format_3_to_5, 3) : No fix -- GOOD
   Fail (convert_df_sci_names_format_5_to_GNR, 4) : Recovery -- GOOD (w example)
   Fail (phylotastic_ResolvedScientificNames_GNR_TNRS_POST, 5)  : Recovery -- GOOD (Strong EXAMPLE)
   Fail (convert_df_taxons_format_GNR_to_PhyloT, 6) : Recovery -- GOOD (Strong Example)
   Fail (phylotastic_GetPhylogeneticTree_PhyloT_GET, 7) : Timeout Error - Failed ????
   Fail (phylotastic_CompareTrees_BL_Dendropy_POST, 8) :  Timeout Error - Failed 


5. Input : resource_FreeText (plain_text), speciesTree (compare_tree_format)     =======> Example
   Output : resource_AreSameTree (boolean)

   Fail (phylotastic_FindScientificNamesFromFreeText_GNRD_GET, 0) :  No fix -- GOOD
   Fail (convert_df_sci_names_format_1_to_3, 1) :   No fix -- GOOD
   Fail (convert_df_sci_names_format_3_to_5, 2) :  No fix -- GOOD
   Fail (convert_df_sci_names_format_5_to_OT, 3) :  Recovery - Good (W Example)
   Fail (phylotastic_ResolvedScientificNames_OT_TNRS_GET, 4)  :  Recovery -- Good (Strong Example)
   Fail (phylotastic_GetPhylogeneticTree_OT_GET, 5) :  Recovery -- Good 
   Fail (phylotastic_GetPhylogeneticTree_OT_POST, 6) :  Recovery -- Good
   Fail (convert_species_tree_format_NMSU_to_NewickTree, 7) : Recovery -- Good (Strong Example)
   Fail (phylotastic_CompareTrees_BL_Dendropy_POST, 8) :  Timeout Error --- Failed

6. Input : setof GeneNames (list_of_strings)
   Output : ReconcilationTree (newick)

   Fail (phylotastic_GenerateGeneTree_From_Genes, 0)  :  No Fix -- Good
   Fail (convert_gene_tree_format_PhyloTree_to_NMSU, 1) : No Fix -- Good
   Fail (convert_gene_tree_format_NMSU_to_NewickTree, 2) : No Fix -- Good
   Fail (phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET, 3) : No Fix -- Good
   Fail (convert_df_sci_names_format_2_to_4, 4) : No Fix -- Good
   Fail (convert_df_sci_names_format_4_to_6, 5)  : No fix -- Good
   Fail (convert_df_sci_names_format_6_to_OT, 6) : Recovery -- Good (Example)

   Fail (phylotastic_ResolvedScientificNames_OT_TNRS_GET, 7) :  Timeout Error --- Failed ??
   Fail (phylotastic_GetPhylogeneticTree_OT_GET, 8) :  Timeout Error --- Failed ??
   Fail (convert_species_tree_format_NMSU_to_NewickTree, 9)  :  Timeout Error --- Failed ??
   Fail (phylotastic_GetReconciliationTree_GET, 10) : Timeout Error --- Failed ??

7. Input : FreeText (raw_text) and phylomatic_method (string)
   Ouput : SpeciesTree + Chronogram (Newick) and meta data of tree
   Tool : clingcon

   Fail (convert_df_text_format_raw_to_plain, 0)  : No Fix -- Good
   Fail (phylotastic_FindScientificNamesFromFreeText_GNRD_GET, 1) : No Fix -- Good
   Fail (convert_df_sci_names_format_1_to_3, 2)  : No Fix -- Good
   Fail (convert_df_sci_names_format_3_to_5, 3)  : No Fix -- Good
   Fail (convert_df_sci_names_format_5_to_OT, 4) : Recovery -- Good (Strong Example)
   Fail (phylotastic_ResolvedScientificNames_OT_TNRS_POST, 5) : Recovery -- Good (Strong Example)
   Fail (phylotastic_GetPhylogeneticTree_OT_GET, 6)  :  Recovery -- Good (Strong Example)

   Fail (convert_species_tree_format_NMSU_to_NewickTree, 7)  : (Performance is quite slow) : TimeOut -- Failed 
   Fail (phylotastic_GetMetadata_Chronogram_DateLife_POST, 8) :  TimeOut Error -- Failed
   Fail (phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST, 9)  : TimeOut Error -- Failed

8. Input : FreeText (raw_text) and phylomatic_method (string)
   Ouput : SpeciesTree + Chronogram (Newick) and meta data of tree
   Tool : clingo

   Fail (convert_df_text_format_raw_to_plain, 0)  : No Fix -- Good
   Fail (phylotastic_FindScientificNamesFromFreeText_GNRD_GET, 1)  :  No Fix -- Good
   Fail (convert_df_sci_names_format_1_to_3, 2)   :  No Fix -- Good
   Fail (convert_df_sci_names_format_3_to_5, 3)   :  No Fix -- Good
   Fail (convert_df_sci_names_format_5_to_GNR, 4)  :   Recovery -- Good (Example)
   Fail (phylotastic_ResolvedScientificNames_GNR_TNRS_POST, 5) : Recovery -- Good (Example)
   Fail (convert_df_taxons_format_GNR_to_PhyloT, 6)  : Recovery --- Good (Strong Example)

   Fail (phylotastic_GetPhylogeneticTree_PhyloT_GET, 7) : TimeOut Error --- Failed
   Fail (phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST, 8) : TimeOut Error -- Failed
   Fail (phylotastic_GetMetadata_Chronogram_DateLife_POST, 9) : TimeOut Error -- Failed

9. Input : FreeText (plain_text) and phylomatic_method (string)
   Ouput : SpeciesTree + Chronogram (Newick) and meta data of tree
   Tool : clingcon

   Fail (phylotastic_FindScientificNamesFromFreeText_GNRD_GET, 0)  : No Fix --- Good
   Fail (convert_df_sci_names_format_1_to_3, 1)    : No Fix --- Good
   Fail (convert_df_sci_names_format_3_to_5, 2)    : No Fix --- Good
   Fail (convert_df_sci_names_format_5_to_OT, 3)   :  Recovery --- Goood (Strong Example)
   Fail (phylotastic_ResolvedScientificNames_OT_TNRS_POST, 4)  : Recovery --- Good (Strong Ex)
   Fail (phylotastic_GetPhylogeneticTree_OT_POST, 5)    :  Recovery --- Good (Strong Ex)
   Fail (convert_species_tree_format_NMSU_to_NewickTree, 6)      :   Recovery --- Good (Strong Example)

   Fail (phylotastic_GetMetadata_Chronogram_DateLife_POST, 7)    : TimeOut Error -- Failed
   Fail (phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST, 8)   : TimeOut Error -- Failed
   

Summary : REcheck Max_Score and replace to clingcon

