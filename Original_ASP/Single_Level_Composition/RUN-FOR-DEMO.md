# Init : Set of Gene Strings ; Out : Reconciliation Tree
## 1. Run to find original Workflow
### Command :
```
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp
clingo Program_Composite.lp
```
### Result :
```
occur(phylotastic_GenerateGeneTree_From_Genes,0)
occur(convert_gene_tree_format_PhyloTree_to_NMSU,1)
occur(convert_gene_tree_format_NMSU_to_NewickTree,2)
occur(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,3)
occur(convert_df_sci_names_format_2_to_4,4)
occur(convert_df_sci_names_format_4_to_6,5)
occur(convert_df_sci_names_format_6_to_OT,6)
occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,7) 
occur(phylotastic_GetPhylogeneticTree_OT_GET,8)
occur(convert_species_tree_format_NMSU_to_NewickTree,9)
occur(phylotastic_GetReconciliationTree_GET,10)

map(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,phyloTree,1,phylotastic_GenerateGeneTree_From_Genes,resource_geneTree,phyloTree,1)
map(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,nmsu_tree_format,2,convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,nmsu_tree_format,2)
map(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_geneTree,newickTree,3,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)
map(phylotastic_GetReconciliationTree_GET,resource_geneTree,newickTree,10,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)
map(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_2,4,phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_SetOfSciName,raw_names_format_2,4) map(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_4,5,convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_4,5)
map(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_6,6,convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_6,6)
map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,7,convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_OT,7)
map(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT,8,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,8)
map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,9,phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format,9) map(phylotastic_GetReconciliationTree_GET,resource_speciesTree,newickTree,10,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,10)
map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,0,initial_state,resource_SetOfGeneStrings,list_of_strings,0)
map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,12,initial_state,resource_SetOfGeneStrings,list_of_strings,0)
```

## 2.1 Inclusion : Require to use ```phylotastic_GeneTree_Scaling```

### Modify code in ```composite_preference.lp```

### Changes : Add ```phylotastic_GeneTree_Scaling``` into workflow produces one output for ```phylotastic_GetReconciliationTree_GET```

### Command :
```
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp composite_preference.lp
clingo Program_Composite.lp
```

### Result :
```
occur(phylotastic_GenerateGeneTree_From_Genes,0)
occur(convert_gene_tree_format_PhyloTree_to_NMSU,1)
occur(convert_gene_tree_format_NMSU_to_NewickTree,2)
occur(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,3)
occur(convert_df_sci_names_format_2_to_4,4) 
occur(convert_df_sci_names_format_4_to_6,5) 
occur(convert_df_sci_names_format_6_to_OT,6) 
occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,7) 
occur(phylotastic_GetPhylogeneticTree_OT_GET,8) 
occur(phylotastic_GeneTree_Scaling,9)
occur(convert_species_tree_format_NMSU_to_NewickTree,10) 
occur(phylotastic_GetReconciliationTree_GET,11)

map(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,phyloTree,1,phylotastic_GenerateGeneTree_From_Genes,resource_geneTree,phyloTree,1)
map(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,nmsu_tree_format,2,convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,nmsu_tree_format,2)
map(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_geneTree,newickTree,3,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)
map(phylotastic_GeneTree_Scaling,resource_geneTree,newickTree,9,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)
map(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_2,4,phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_SetOfSciName,raw_names_format_2,4)
map(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_4,5,convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_4,5)
map(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_6,6,convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_6,6)
map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,7,convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_OT,7)
map(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT,8,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,8) 
map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,10,phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format,9) map(phylotastic_GetReconciliationTree_GET,resource_geneTree,newickTree,11,phylotastic_GeneTree_Scaling,resource_geneTree,newickTree,10) 
map(phylotastic_GetReconciliationTree_GET,resource_speciesTree,newickTree,11,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,11) 
map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,0,initial_state,resource_SetOfGeneStrings,list_of_strings,0)
```

## 2.2 Inclusion : Require to use ```phylotastic_GetPhylogeneticTree_OT_POST```

### Modify code in ```composite_preference.lp```

### Changes : Simple replace ```phylotastic_GetPhylogeneticTree_OT_GET``` by ```phylotastic_GetPhylogeneticTree_OT_POST```

### Command :
```
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp composite_preference.lp
clingo Program_Composite.lp
```

### Result :
```
occur(phylotastic_GenerateGeneTree_From_Genes,0)
occur(convert_gene_tree_format_PhyloTree_to_NMSU,1)
occur(convert_gene_tree_format_NMSU_to_NewickTree,2)
occur(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,3)
occur(convert_df_sci_names_format_2_to_4,4)
occur(convert_df_sci_names_format_4_to_6,5)
occur(convert_df_sci_names_format_6_to_OT,6)
occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,7) 
occur(phylotastic_GetPhylogeneticTree_OT_POST,8)
occur(convert_species_tree_format_NMSU_to_NewickTree,9)
occur(phylotastic_GetReconciliationTree_GET,10)

map(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,phyloTree,1,phylotastic_GenerateGeneTree_From_Genes,resource_geneTree,phyloTree,1)
map(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,nmsu_tree_format,2,convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,nmsu_tree_format,2)
map(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_geneTree,newickTree,3,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)
map(phylotastic_GetReconciliationTree_GET,resource_geneTree,newickTree,10,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)
map(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_2,4,phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_SetOfSciName,raw_names_format_2,4) map(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_4,5,convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_4,5)
map(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_6,6,convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_6,6)
map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,7,convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_OT,7)
map(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT,8,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,8)
map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,9,phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format,9) map(phylotastic_GetReconciliationTree_GET,resource_speciesTree,newickTree,10,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,10)
map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,0,initial_state,resource_SetOfGeneStrings,list_of_strings,0)
map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,12,initial_state,resource_SetOfGeneStrings,list_of_strings,0)
```

## 3.3 Inclusion : ```phylotastic_GetPhylogeneticTree_PhyloT_GET```

### Modify code in ```composite_preference.lp```

### Changes : Add ```phylotastic_GetPhylogeneticTree_PhyloT_GET``` into workflow AND add one more service ```convert_df_taxons_format_GNR_to_PhyloT``` before ```phylotastic_GetPhylogeneticTree_PhyloT_GET```

### Command :
```
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp composite_preference.lp
clingo Program_Composite.lp
```

### Result :
```
occur(phylotastic_GenerateGeneTree_From_Genes,0)
occur(convert_gene_tree_format_PhyloTree_to_NMSU,1)
occur(convert_gene_tree_format_NMSU_to_NewickTree,2)
occur(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,3)
occur(convert_df_sci_names_format_2_to_4,4)
occur(convert_df_sci_names_format_4_to_6,5)
occur(convert_df_sci_names_format_6_to_GNR,6)
occur(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,7)
occur(convert_df_taxons_format_GNR_to_PhyloT,8)
occur(phylotastic_GetPhylogeneticTree_PhyloT_GET,9)
occur(phylotastic_GetReconciliationTree_GET,10) 
occur(phylotastic_GenerateGeneTree_From_Genes,12)     
```

## 4.1  Avoidance : ```phylotastic_ResolvedScientificNames_GNR_TNRS_POST``` ; ```phylotastic_ResolvedScientificNames_OT_TNRS_GET```, ```phylotastic_ResolvedScientificNames_OT_TNRS_POST```

### Modify code in ```composite_preference.lp```

### Changes : add 3 data convertion operation ```convert_df_taxons_format_2_to_4``` ; ```convert_df_taxons_format_4_to_6``` ; ```convert_df_taxons_format_6_to_ALL_COMBO```
in order to use ```phylotastic_ResolvedScientificNames_GNR_TNRS_GET```

### Command :
```
clingo single_level_planning_Working.lp ontology_TESTING_Working.lp composite_preference.lp
clingo Program_Composite.lp
```

### Result :
```
occur(phylotastic_GenerateGeneTree_From_Genes,0)
occur(convert_gene_tree_format_PhyloTree_to_NMSU,1)
occur(convert_gene_tree_format_NMSU_to_NewickTree,2) 
occur(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,3)
occur(convert_df_sci_names_format_2_to_4,4)
occur(convert_df_sci_names_format_4_to_6,5)
occur(convert_df_sci_names_format_6_to_GNR,6)
occur(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,7)
occur(convert_df_taxons_format_2_to_4,8)
occur(convert_df_taxons_format_4_to_6,9)
occur(convert_df_taxons_format_6_to_ALL_COMBO,10)
occur(phylotastic_GetPhylogeneticTree_PhyloT_GET,11)
occur(phylotastic_GetReconciliationTree_GET,12)      
```