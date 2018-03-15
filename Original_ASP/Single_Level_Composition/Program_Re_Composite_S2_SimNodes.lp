%-------------------------------------------------
% Multiple shoot solving
%-------------------------------------------------
#script (python)
import clingo
import time
import composite_parser
import similarity_matching
from random import *
import sys
#----------------------------------------------------------    
ORIGINAL_WORKFLOW = ["instance_operation_has_input_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET,resource_WebURL,http_url)", "instance_operation_has_input_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_FreeText,plain_text)", "instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,resource_SetOfSciName,raw_names_format_GNR)", "instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,resource_SetOfSciName,raw_names_format_GNR)", "instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT)", "instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST,resource_SetOfSciName,raw_names_format_OT)", "instance_operation_has_input_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET,resource_taxon,string)", "instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT)", "instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_SetOfTaxon,resolved_names_format_OT)", "instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_PhyloT_GET,resource_SetOfTaxon,resolved_names_format_PhyloT)", "instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_PhyloT_POST,resource_SetOfTaxon,resolved_names_format_PhyloT)", "instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_Phylomatic_GET,resource_SetOfResolvedName,resolved_names_format_Phylomatic)", "instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_Phylomatic_POST,resource_SetOfResolvedName,resolved_names_format_Phylomatic)", "instance_operation_has_input_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,resource_taxon,string)", "instance_operation_has_input_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,resource_CountryName,string)", "instance_operation_has_input_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,resource_taxon,string)", "instance_operation_has_input_has_data_format(google_ConvertCountryCodeToName_GET,resource_CountryCode,integer)", "instance_operation_has_input_has_data_format(openTree_GetTaxonomyNameFromSciName_GET,resource_ScientificName,string)", "instance_operation_has_input_has_data_format(phylotastic_GetSpeciesScientificNameFromCommonName_NCBI_GET,resource_CommonName,string)", "instance_operation_has_input_has_data_format(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,resource_speciesTree,newickTree)", "instance_operation_has_input_has_data_format(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,phylomatic_method,string)", "instance_operation_has_input_has_data_format(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,resource_speciesTree,newickTree)", "instance_operation_has_input_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,resource_WebURL,data_format_E)", "instance_operation_has_input_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_geneTree,newickTree)", "instance_operation_has_input_has_data_format(phylotastic_GetReconciliationTree_GET,resource_geneTree,newickTree)", "instance_operation_has_input_has_data_format(phylotastic_GetReconciliationTree_GET,resource_speciesTree,newickTree)", "instance_operation_has_input_has_data_format(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings)", "instance_operation_has_input_has_data_format(phylotastic_GeneTree_Scaling,resource_geneTree,newickTree)", "instance_operation_has_input_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,raw_text)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_1)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_3)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_5_to_GNR,resource_SetOfSciName,raw_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_2)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_4)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_6_to_GNR,resource_SetOfSciName,raw_names_format_6)", "instance_operation_has_input_has_data_format(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_6)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_GNR_to_OT,resource_SetOfResolvedName,resolved_names_format_GNR)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_GNR_to_Phylomatic,resource_SetOfResolvedName,resolved_names_format_GNR)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_GNR_to_PhyloT,resource_SetOfResolvedName,resolved_names_format_GNR)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_1_to_3,resource_SetOfResolvedName,resolved_names_format_1)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_3_to_5,resource_SetOfResolvedName,resolved_names_format_3)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_5_to_OT,resource_SetOfResolvedName,resolved_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_5_to_PhyloT,resource_SetOfResolvedName,resolved_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_5_to_Phylomatic,resource_SetOfResolvedName,resolved_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_2_to_4,resource_SetOfResolvedName,resolved_names_format_2)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_4_to_6,resource_SetOfResolvedName,resolved_names_format_4)", "instance_operation_has_input_has_data_format(convert_df_resolved_names_format_6_to_ALL_COMBO,resource_SetOfResolvedName,resolved_names_format_6)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_GNR_to_OT,resource_SetOfTaxon,resolved_names_format_GNR)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_GNR_to_Phylomatic,resource_SetOfTaxon,resolved_names_format_GNR)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_GNR_to_PhyloT,resource_SetOfTaxon,resolved_names_format_GNR)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_1_to_3,resource_SetOfTaxon,resolved_names_format_1)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_3_to_5,resource_SetOfTaxon,resolved_names_format_3)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_5_to_OT,resource_SetOfTaxon,resolved_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_5_to_PhyloT,resource_SetOfTaxon,resolved_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_5_to_Phylomatic,resource_SetOfTaxon,resolved_names_format_5)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_2_to_4,resource_SetOfTaxon,resolved_names_format_2)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_4_to_6,resource_SetOfTaxon,resolved_names_format_4)", "instance_operation_has_input_has_data_format(convert_df_taxons_format_6_to_ALL_COMBO,resource_SetOfTaxon,resolved_names_format_6)", "instance_operation_has_input_has_data_format(convert_species_tree_format_NewickTree_to_ALL_COMBO,resource_speciesTree,newickTree)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_NewickTree_to_ALL_COMBO,resource_geneTree,newickTree)", "instance_operation_has_input_has_data_format(convert_species_tree_format_PhyloTree_to_NMSU,resource_speciesTree,phyloTree)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,phyloTree)", "instance_operation_has_input_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,nmsu_tree_format)", "instance_operation_has_input_has_data_format(convert_species_tree_format_PhyloTree_to_phylo4Tree,resource_speciesTree,phyloTree)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_PhyloTree_to_phylo4Tree,resource_geneTree,phyloTree)", "instance_operation_has_input_has_data_format(convert_species_tree_format_Phylo4Tree_to_PhyloTree,resource_speciesTree,phylo4Tree)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_Phylo4Tree_to_PhyloTree,resource_geneTree,phylo4Tree)", "instance_operation_has_input_has_data_format(convert_species_tree_format_1_to_2,resource_speciesTree,tree_format_1)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_1_to_2,resource_geneTree,tree_format_1)", "instance_operation_has_input_has_data_format(convert_species_tree_format_2_to_pHYLIPTree,resource_speciesTree,tree_format_2)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_2_to_pHYLIPTree,resource_geneTree,tree_format_2)", "instance_operation_has_input_has_data_format(convert_species_tree_format_pHYLIPTree_to_PhyloTree,resource_speciesTree,pHYLIPTree)", "instance_operation_has_input_has_data_format(convert_gene_tree_format_pHYLIPTree_to_PhyloTree,resource_geneTree,pHYLIPTree)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET,resource_SetOfSciName,raw_names_format_2)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET,resource_ConnectionTime,integer)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_SetOfSciName,raw_names_format_1)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,resource_ConnectionTime,integer)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,resource_SetOfTaxon,resolved_names_format_2)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,resource_SetOfResolvedName,resolved_names_format_2)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,resource_SetOfTaxon,resolved_names_format_GNR)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,resource_SetOfResolvedName,resolved_names_format_GNR)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfResolvedName,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST,resource_SetOfTaxon,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST,resource_SetOfResolvedName,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET,resource_SetOfSciName,list_of_strings)", "instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET,resource_taxon,string)", "instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET,resource_Tree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_speciesTree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST,resource_Tree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_PhyloT_GET,resource_speciesTree,newickTree)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_PhyloT_GET,resource_Tree,newickTree)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_PhyloT_POST,resource_speciesTree,newickTree)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_PhyloT_POST,resource_Tree,newickTree)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_Phylomatic_GET,resource_speciesTree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_Phylomatic_GET,resource_Tree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_Phylomatic_POST,resource_speciesTree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_Phylomatic_POST,resource_Tree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,resource_SetOfSciName,list_of_strings)", "instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,resource_taxon,string)", "instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,resource_SetOfSciName,list_of_strings)", "instance_operation_has_output_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,resource_taxon,string)", "instance_operation_has_output_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(google_ConvertCountryCodeToName_GET,resource_CountryName,string)", "instance_operation_has_output_has_data_format(openTree_GetTaxonomyNameFromSciName_GET,resource_taxon,string)", "instance_operation_has_output_has_data_format(phylotastic_GetSpeciesScientificNameFromCommonName_NCBI_GET,resource_ScientificName,string)", "instance_operation_has_output_has_data_format(phylotastic_GetSpeciesScientificNameFromCommonName_NCBI_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_GetSpeciesScientificNameFromCommonName_NCBI_GET,resource_WebURL,http_url)", "instance_operation_has_output_has_data_format(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,resource_AreSameTree,boolean)", "instance_operation_has_output_has_data_format(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_ComparePhylogeneticTrees_Symmetric_POST,ws_response_message,string)", "instance_operation_has_output_has_data_format(phylotastic_GetChronograms_ScaledSpeciesTree_DateLife_POST,resource_speciesTree_with_BranchLengths,newickTree)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,resource_SetOfSciName,raw_names_format_2)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,resource_ConnectionTime,integer)", "instance_operation_has_output_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_SetOfSciName,raw_names_format_2)", "instance_operation_has_output_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_HTTPCode,integer)", "instance_operation_has_output_has_data_format(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_ConnectionTime,integer)", "instance_operation_has_output_has_data_format(phylotastic_GetReconciliationTree_GET,resource_reconcileTree,newickTree)", "instance_operation_has_output_has_data_format(phylotastic_GenerateGeneTree_From_Genes,resource_geneTree,phyloTree)", "instance_operation_has_output_has_data_format(phylotastic_GeneTree_Scaling,resource_geneTree,newickTree)", "instance_operation_has_output_has_data_format(convert_df_text_format_raw_to_plain,resource_FreeText,plain_text)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_1_to_3,resource_SetOfSciName,raw_names_format_3)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_3_to_5,resource_SetOfSciName,raw_names_format_5)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_5_to_GNR,resource_SetOfSciName,raw_names_format_GNR)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_5_to_OT,resource_SetOfSciName,raw_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_4)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_6)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_6_to_GNR,resource_SetOfSciName,raw_names_format_GNR)", "instance_operation_has_output_has_data_format(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_GNR_to_OT,resource_SetOfResolvedName,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_GNR_to_Phylomatic,resource_SetOfResolvedName,resolved_names_format_Phylomatic)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_GNR_to_PhyloT,resource_SetOfResolvedName,resolved_names_format_PhyloT)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_1_to_3,resource_SetOfResolvedName,resolved_names_format_3)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_3_to_5,resource_SetOfResolvedName,resolved_names_format_5)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_5_to_OT,resource_SetOfResolvedName,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_5_to_PhyloT,resource_SetOfResolvedName,resolved_names_format_PhyloT)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_5_to_Phylomatic,resource_SetOfResolvedName,resolved_names_format_Phylomatic)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_2_to_4,resource_SetOfResolvedName,resolved_names_format_4)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_4_to_6,resource_SetOfResolvedName,resolved_names_format_6)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_6_to_ALL_COMBO,resource_SetOfResolvedName,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_6_to_ALL_COMBO,resource_SetOfResolvedName,resolved_names_format_PhyloT)", "instance_operation_has_output_has_data_format(convert_df_resolved_names_format_6_to_ALL_COMBO,resource_SetOfResolvedName,resolved_names_format_Phylomatic)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_GNR_to_OT,resource_SetOfTaxon,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_GNR_to_Phylomatic,resource_SetOfTaxon,resolved_names_format_Phylomatic)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_GNR_to_PhyloT,resource_SetOfTaxon,resolved_names_format_PhyloT)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_1_to_3,resource_SetOfTaxon,resolved_names_format_3)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_3_to_5,resource_SetOfTaxon,resolved_names_format_5)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_5_to_OT,resource_SetOfTaxon,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_5_to_PhyloT,resource_SetOfTaxon,resolved_names_format_PhyloT)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_5_to_Phylomatic,resource_SetOfTaxon,resolved_names_format_Phylomatic)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_2_to_4,resource_SetOfTaxon,resolved_names_format_4)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_4_to_6,resource_SetOfTaxon,resolved_names_format_6)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_6_to_ALL_COMBO,resource_SetOfTaxon,resolved_names_format_OT)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_6_to_ALL_COMBO,resource_SetOfTaxon,resolved_names_format_PhyloT)", "instance_operation_has_output_has_data_format(convert_df_taxons_format_6_to_ALL_COMBO,resource_SetOfTaxon,resolved_names_format_Phylomatic)", "instance_operation_has_output_has_data_format(convert_species_tree_format_NewickTree_to_ALL_COMBO,resource_speciesTree,phyloTree)", "instance_operation_has_output_has_data_format(convert_species_tree_format_NewickTree_to_ALL_COMBO,resource_speciesTree,phylo4Tree)", "instance_operation_has_output_has_data_format(convert_species_tree_format_NewickTree_to_ALL_COMBO,resource_speciesTree,pHYLIPTree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_NewickTree_to_ALL_COMBO,resource_geneTree,phyloTree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_NewickTree_to_ALL_COMBO,resource_geneTree,phylo4Tree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_NewickTree_to_ALL_COMBO,resource_geneTree,pHYLIPTree)", "instance_operation_has_output_has_data_format(convert_species_tree_format_PhyloTree_to_NMSU,resource_speciesTree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,nmsu_tree_format)", "instance_operation_has_output_has_data_format(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree)", "instance_operation_has_output_has_data_format(convert_species_tree_format_PhyloTree_to_phylo4Tree,resource_speciesTree,phylo4Tree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_PhyloTree_to_phylo4Tree,resource_geneTree,phylo4Tree)", "instance_operation_has_output_has_data_format(convert_species_tree_format_Phylo4Tree_to_PhyloTree,resource_speciesTree,phyloTree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_Phylo4Tree_to_PhyloTree,resource_geneTree,phyloTree)", "instance_operation_has_output_has_data_format(convert_species_tree_format_1_to_2,resource_speciesTree,tree_format_2)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_1_to_2,resource_geneTree,tree_format_2)", "instance_operation_has_output_has_data_format(convert_species_tree_format_2_to_pHYLIPTree,resource_speciesTree,pHYLIPTree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_2_to_pHYLIPTree,resource_geneTree,pHYLIPTree)", "instance_operation_has_output_has_data_format(convert_species_tree_format_pHYLIPTree_to_PhyloTree,resource_speciesTree,phyloTree)", "instance_operation_has_output_has_data_format(convert_gene_tree_format_pHYLIPTree_to_PhyloTree,resource_geneTree,phyloTree)", "goal(11)", "occur(phylotastic_ResolvedScientificNames_OT_TNRS_GET,7)", "occur(phylotastic_GetPhylogeneticTree_OT_GET,8)", "occur(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,3)", "occur(phylotastic_GetReconciliationTree_GET,10)", "occur(phylotastic_GenerateGeneTree_From_Genes,0)", "occur(phylotastic_GenerateGeneTree_From_Genes,12)", "occur(convert_df_sci_names_format_2_to_4,4)", "occur(convert_df_sci_names_format_4_to_6,5)", "occur(convert_df_sci_names_format_6_to_OT,6)", "occur(convert_gene_tree_format_PhyloTree_to_NMSU,1)", "occur(convert_species_tree_format_NMSU_to_NewickTree,9)", "occur(convert_gene_tree_format_NMSU_to_NewickTree,2)", "map(convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,phyloTree,1,phylotastic_GenerateGeneTree_From_Genes,resource_geneTree,phyloTree,1)", "map(convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,nmsu_tree_format,2,convert_gene_tree_format_PhyloTree_to_NMSU,resource_geneTree,nmsu_tree_format,2)", "map(phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_geneTree,newickTree,3,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)", "map(phylotastic_GetReconciliationTree_GET,resource_geneTree,newickTree,10,convert_gene_tree_format_NMSU_to_NewickTree,resource_geneTree,newickTree,3)", "map(convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_2,4,phylotastic_ExtractSpeciesNames_From_Gene_Tree_GET,resource_SetOfSciName,raw_names_format_2,4)", "map(convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_4,5,convert_df_sci_names_format_2_to_4,resource_SetOfSciName,raw_names_format_4,5)", "map(convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_6,6,convert_df_sci_names_format_4_to_6,resource_SetOfSciName,raw_names_format_6,6)", "map(phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfSciName,raw_names_format_OT,7,convert_df_sci_names_format_6_to_OT,resource_SetOfSciName,raw_names_format_OT,7)", "map(phylotastic_GetPhylogeneticTree_OT_GET,resource_SetOfTaxon,resolved_names_format_OT,8,phylotastic_ResolvedScientificNames_OT_TNRS_GET,resource_SetOfTaxon,resolved_names_format_OT,8)", "map(convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,nmsu_tree_format,9,phylotastic_GetPhylogeneticTree_OT_GET,resource_speciesTree,nmsu_tree_format,9)", "map(phylotastic_GetReconciliationTree_GET,resource_speciesTree,newickTree,10,convert_species_tree_format_NMSU_to_NewickTree,resource_speciesTree,newickTree,10)", "map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,0,initial_state,resource_SetOfGeneStrings,list_of_strings,0)", "map(phylotastic_GenerateGeneTree_From_Genes,resource_SetOfGeneStrings,list_of_strings,12,initial_state,resource_SetOfGeneStrings,list_of_strings,0)"
          ]
#---------------------------------------------------------- 
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

#-------------FOR RE PLANNING-----------------------------
def calculate_sim_matching_WF(WF_1,WF_2):
  return randint(0,200)
def calculate_sim_between_2_nodes(occur_node_1,index_1,occur_node_2,index_2):
  return similarity_matching.sim_between_2_nodes_raw_clingo(occur_node_1,index_1,occur_node_2,index_2)
  #return randint(0,100)

def isConsideredPredicate(str_predicate,limits):
    for item in limits:
        if (item in str_predicate):
            return True
    return False

def get_CurrentModifying_Workflow(limits):
   # limits is list of predicate that want to store for new workflow
   '''
   result_list = []
   if (not limits):
       return WORKFLOW_1_RAW_BEAUTY
   for str_predicate in WORKFLOW_1_RAW_BEAUTY:
       if (isConsideredPredicate(str_predicate,limits)):
            result_list.append(str_predicate)
   return result_list
   '''
   #return ["occur(common_name_to_scientific_name,0)", "occur(taxon_to_species_by_country,1)", "occur(names_extraction_document,2)","occur(names_resolution_operation,3)","occur(phylogeny_based_extraction,4)","occur(tree_comparison,5)"]

   #return ["occur(common_name_to_scientific_name,0)", "occur(taxon_to_species_by_country,1)", "occur(names_extraction_document,2)","occur(tree_comparison,3)"]

   return ORIGINAL_WORKFLOW

   #return ["occur(a,0)", "occur(b,1)", "occur(c,2)"]
   #return ["occur(a,0)", "occur(b,1)", "occur(c,2)","occur(d,3)","occur(e,4)","occur(f,5)"]
#------------------------------------------------------------
def main(prg):
    def run_original_planning_with_sim_index(str_group_sim_nodes_rules):
        final_answer_set_result = []
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
            with prg.solve(yield_=True,on_model=real_time_check_model) as handle:
              for m in handle:
                 symbols = m.symbols(shown=True)
            return symbols
        def real_time_check_model(clingo_model):
            print "--> Get new model"
        def load_asp(prg):
            prg.load("single_level_planning_Working.lp")
            prg.load("ontology_TESTING_Working.lp")
            prg.load("composite_preference.lp")
            prg.load("re_composite_preference.lp")

        # Load another components
        load_asp(prg)
        # Configuration for the ASP solver
      
        base_program = [("base", [])]

        loop = 1
        multi_shot_id = 1
        super_index = 1

        # Star to find 1st answer set
        t0 = time.time()
        print("---Start grounding --> Base Program ---")
        prg.ground(base_program)
        print("---End grounding --> Base Program ---")
        t1 = time.time()
        print("---Time : %s ms" %(str(t1 - t0)))
        
        # Add SIMILARITY INDEX RULE to active Internal Optimization
        prg.add("similarity_index_calculation", [], str_group_sim_nodes_rules)
        
        print("---Start grounding --> SimCal Program ---")    
        prg.ground([("similarity_index_calculation", [])])
        print("---End grounding --> SimCal Program ---")    

        prg.solve()
            

    #-----------FOR RE-COMPOSITION-----------
    def generate_old_occur_string(old_workflow):
        #Step 1 : Find goald
        int_goal = -1
        for predicate in old_workflow:
            if "goal(" in str(predicate):
                int_goal = composite_parser.parse_goal_in_predicate(predicate)

        #Step 2 : Loop and generate
        generate_old_occur = ""
        for predicate in old_workflow:
            if "occur(" in str(predicate):
                service,index_occur = composite_parser.parse_a_occur_service(predicate)
                if (index_occur < int_goal):
                    generate_old_occur = generate_old_occur + "\nold_occur(%s,%d)." %(str(service),index_occur)
        return generate_old_occur

    def build_up_group_similarity_nodes_rules_C1():  #Simple occur and description only
        # Get old worklfow for occur only
        old_workflow = get_CurrentModifying_Workflow(limits=["occur("]) 
        generate_old_occur = generate_old_occur_string(old_workflow)

        single_sim_nodes_rule = "\nsingle_sim_2_nodes(X,Y,Z) :- old_occur(X,I1), occur(Y,I2), goal(G), I2 < G, Z = @calculate_sim_between_2_nodes(X,I1,Y,I2)."       

        sum_sim_nodes_rule = "\nsum_single_sim_2_nodes(T) :- T = #sum {Z : single_sim_2_nodes(X,Y,Z)}."
        #sum_sim_nodes_rule = "\nsum_single_sim_2_nodes(T) :- T = #sum {Z,X,Y : single_sim_2_nodes(X,Y,Z)}."  

        sim_nodes_workflow_rule = "\nsim_nodes_workflows(R) :- sum_single_sim_2_nodes(T), N_Old_Nodes = #count {X,I1: old_occur(X,I1)}, N_New_Nodes = #count {Y,I2 : occur(Y,I2)}, R = 2*T / (N_Old_Nodes + N_New_Nodes)."

        #sim_nodes_workflow_rule = "\nsim_nodes_workflows(R) :- T = #sum {P,M,N : single_sim_2_nodes(M,N,P)}, N_Old_Nodes = #count {X,I1: old_occur(X,I1)}, N_New_Nodes = #count {,I2 : occur(Y,I2)}, R = 2*T / (N_Old_Nodes + N_New_Nodes)."  

        maximize_rule = "\n#maximize{R : sim_nodes_workflows(R)}."
        #maximize_rule = ""

        full_sim_nodes_cal = generate_old_occur + single_sim_nodes_rule + sum_sim_nodes_rule  + sim_nodes_workflow_rule + maximize_rule

        #full_sim_nodes_cal = generate_old_occur + single_sim_nodes_rule  + sim_nodes_workflow_rule
          
        return full_sim_nodes_cal
    #################################################
    def re_composition_with_preference(prg):
        print("--> Start Re-Composition : \n")
        str_group_sim_nodes_rules = build_up_group_similarity_nodes_rules_C1()
      
        print "\n"
        print str_group_sim_nodes_rules
        print "\n"

        print("---->Original Planning + New Preference : START------")
        run_original_planning_with_sim_index(str_group_sim_nodes_rules)
        print("---->Original Planning + New Preference : DONE------\n")
        
    #----------------------------------------
    re_composition_with_preference(prg)
#end.
%-----------------------------------------------
#external active_rule_single_level(1).
%-----------------------------------------------
%#show single_sim_2_nodes/3.
#show sum_single_sim_2_nodes/1.
#show sim_nodes_workflows/1.