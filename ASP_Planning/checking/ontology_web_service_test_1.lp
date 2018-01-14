%=======================================================================
%PART 1 : Define classes that are used from CDAO ontology
%=======================================================================
class(network).
class(cDAOAnnotation).
class(setOfThings).
class(galledTree).
class(reticulateEvolution).
class(tree).
class(polyphyleticGroup).
class(monophyleticGroup).
class(characterStateDataMatrixAnnotation).
class(edgeAnnotation).
class(treeAnnotation).
class(tUAnnotation).
class(modelDescription).
class(setOfNodes).
class(setOfCharacters).
class(setOfObjects).
class(unrootedTree).
class(clade).
class(fullyResolvedTree).
class(rootedTree).
class(subtree).
class(reconcileTree).
class(bifurcatingTree).
class(speciesTree).
class(resource_Tree).
class(unresolvedTree).
class(paraphyleticGroup).
class(holophyleticGroup).
class(alignmentProcedure).
class(dataMatrixFormat).
class(edgeLength).
class(treeFormat).
class(treeProcedure).
class(taxonomicLink).
class(gapCost).
class(substitutionModel).
class(fullyResolvedUnrootedTree).
class(unresolvedUnrootedTree).
class(rootedSubtree).
class(starTree).
class(fullyResolvedRootedTree).
class(unresolvedRootedTree).
class(lineage).
class(unrootedSubtree).
class(resource_reconcileTree).
class(phylotasticETESpeciesTree).
class(resource_speciesTree).
class(phylotasticSpeciesTree).
class(resource_imagesSpeciesTree).
class(resource_geneTree).
class(pHYLIPDataMatrix).
class(fASTADataMatrix).
class(genBankDataMatrix).
class(nexusDataBlock).
class(newickTree).
class(phyloTree).
class(sIMMAPTree).
class(nEXUSTreeBlock).
class(phylo4Tree).
class(pHYLIPTree).
class(jukesKantor).
class(kimura2Parameters).
class(gammaDistribution).


subClass(galledTree,network).
subClass(reticulateEvolution,network).
subClass(tree,network).
subClass(polyphyleticGroup,network).
subClass(monophyleticGroup,network).
subClass(characterStateDataMatrixAnnotation,cDAOAnnotation).
subClass(edgeAnnotation,cDAOAnnotation).
subClass(treeAnnotation,cDAOAnnotation).
subClass(tUAnnotation,cDAOAnnotation).
subClass(modelDescription,cDAOAnnotation).
subClass(setOfNodes,setOfThings).
subClass(setOfCharacters,setOfThings).
subClass(setOfObjects,setOfThings).
subClass(unrootedTree,tree).
subClass(clade,tree).
subClass(fullyResolvedTree,tree).
subClass(rootedTree,tree).
subClass(subtree,tree).
subClass(reconcileTree,tree).
subClass(bifurcatingTree,tree).
subClass(speciesTree,tree).
subClass(resource_Tree,tree).
subClass(unresolvedTree,tree).
subClass(paraphyleticGroup,monophyleticGroup).
subClass(holophyleticGroup,monophyleticGroup).
subClass(alignmentProcedure,characterStateDataMatrixAnnotation).
subClass(dataMatrixFormat,characterStateDataMatrixAnnotation).
subClass(edgeLength,edgeAnnotation).
subClass(treeFormat,treeAnnotation).
subClass(treeProcedure,treeAnnotation).
subClass(taxonomicLink,tUAnnotation).
subClass(gapCost,modelDescription).
subClass(substitutionModel,modelDescription).
subClass(fullyResolvedUnrootedTree,unrootedTree).
subClass(unresolvedUnrootedTree,unrootedTree).
subClass(rootedSubtree,rootedTree).
subClass(starTree,rootedTree).
subClass(fullyResolvedRootedTree,rootedTree).
subClass(unresolvedRootedTree,rootedTree).
subClass(lineage,rootedTree).
subClass(rootedSubtree,subtree).
subClass(unrootedSubtree,subtree).
subClass(resource_reconcileTree,reconcileTree).
subClass(fullyResolvedRootedTree,bifurcatingTree).
subClass(fullyResolvedUnrootedTree,bifurcatingTree).
subClass(phylotasticETESpeciesTree,speciesTree).
subClass(resource_speciesTree,speciesTree).
subClass(phylotasticSpeciesTree,speciesTree).
subClass(resource_speciesTree,resource_Tree).
subClass(resource_imagesSpeciesTree,resource_Tree).
subClass(resource_geneTree,resource_Tree).
subClass(resource_reconcileTree,resource_Tree).
subClass(unresolvedRootedTree,unresolvedTree).
subClass(unresolvedUnrootedTree,unresolvedTree).
subClass(pHYLIPDataMatrix,dataMatrixFormat).
subClass(fASTADataMatrix,dataMatrixFormat).
subClass(genBankDataMatrix,dataMatrixFormat).
subClass(nexusDataBlock,dataMatrixFormat).
subClass(newickTree,treeFormat).
subClass(phyloTree,treeFormat).
subClass(sIMMAPTree,treeFormat).
subClass(nEXUSTreeBlock,treeFormat).
subClass(phylo4Tree,treeFormat).
subClass(pHYLIPTree,treeFormat).
subClass(jukesKantor,substitutionModel).
subClass(kimura2Parameters,substitutionModel).
subClass(gammaDistribution,substitutionModel).

equalClasses(clade,holophyleticGroup).
equalClasses(bifurcatingTree,fullyResolvedTree).
%=======================================================================
%PART 2 : Define classes + instances are defined Operation
%=======================================================================
%Define class of operation 
class(operationClassification).
class(species_operation).
class(names_operation).
class(taxon_operation).
class(list_operation).
class(tree_operation).
class(convert_operation).
class(look_up_operation).

class(species_information_operation).
class(names_resolution_operation).
class(names_extraction_operation).
class(taxon_to_species_operation).
class(list_update_operation).
class(list_creation_operation).
class(list_retrieval_operation).
class(tree_generation).
class(tree_information).
class(tree_comparison).
class(tree_visualization).
class(tree_transformation).
class(tree_reconciliation).
class(data_format_convertion).
class(look_up_taxonomy).
class(look_up_scientific_name).
class(look_up_location).


class(species_url_operation).
class(species_images_operation).
class(names_extraction_web).
class(names_extracion_text).
class(names_extraction_document).
class(names_extraction_tree).
class(taxon_to_species_by_genome).
class(taxon_to_species_by_country).
class(list_update_delete).
class(list_update_edit).
class(list_update_add).
class(tree_retrieval_operation).
class(tree_extraction_operation).
class(tree_support_studies).
class(branch_length_comparison_operation).
class(symmetric_comparison_operation).
class(tree_scaling_operation).
class(list_update_edit_list_content).
class(list_update_edit_list_metadata).
class(phylogeny_based_extraction).
class(taxonomy_based_extraction).
class(tree_publifications).
class(country_code_to_name).
class(scientific_name_to_taxonomy).
class(common_name_to_scientific_name).


%Define subclass of operation 
subClass(species_operation,operationClassification).
subClass(names_operation,operationClassification).
subClass(taxon_operation,operationClassification).
subClass(list_operation,operationClassification).
subClass(tree_operation,operationClassification).
subClass(convert_operation,operationClassification).
subClass(look_up_operation,operationClassification).

subClass(species_information_operation,species_operation).
subClass(names_resolution_operation,names_operation).
subClass(names_extraction_operation,names_operation).
subClass(taxon_to_species_operation,taxon_operation).
subClass(list_update_operation,list_operation).
subClass(list_creation_operation,list_operation).
subClass(list_retrieval_operation,list_operation).
subClass(tree_generation,tree_operation).
subClass(tree_information,tree_operation).
subClass(tree_comparison,tree_operation).
subClass(tree_visualization,tree_operation).
subClass(tree_transformation,tree_operation).
subClass(tree_reconciliation,tree_operation).
subClass(data_format_convertion,convert_operation).
subClass(look_up_taxonomy,look_up_operation).
subClass(look_up_scientific_name,look_up_operation).
subClass(look_up_location,look_up_operation).

subClass(species_url_operation,species_information_operation).
subClass(species_images_operation,species_information_operation).
subClass(names_extraction_web,names_extraction_operation).
subClass(names_extracion_text,names_extraction_operation).
subClass(names_extraction_document,names_extraction_operation).
subClass(names_extraction_tree,names_extraction_operation).
subClass(taxon_to_species_by_genome,taxon_to_species_operation).
subClass(taxon_to_species_by_country,taxon_to_species_operation).
subClass(list_update_delete,list_update_operation).
subClass(list_update_edit,list_update_operation).
subClass(list_update_add,list_update_operation).
subClass(tree_retrieval_operation,tree_generation).
subClass(tree_extraction_operation,tree_generation).
subClass(tree_support_studies,tree_information).
subClass(branch_length_comparison_operation,tree_comparison).
subClass(symmetric_comparison_operation,tree_comparison).
subClass(tree_scaling_operation,tree_transformation).
subClass(list_update_edit_list_content,list_update_edit).
subClass(list_update_edit_list_metadata,list_update_edit).
subClass(phylogeny_based_extraction,tree_extraction_operation).
subClass(taxonomy_based_extraction,tree_extraction_operation).
subClass(tree_publifications,tree_support_studies).
subClass(country_code_to_name,look_up_location).
subClass(scientific_name_to_taxonomy,look_up_taxonomy).
subClass(common_name_to_scientific_name,look_up_scientific_name).

%Define class of <Service Providers> Web Service methods components 
class(phylotastic_concept).
class(phylotastic_parameters).
class(phylotastic_data_structure).
class(phylotastic_resources).
class(phylotastic_data_format).
class(phylotastic_data_type).
class(phylotastic_components).
class(resource_SetOfThings).
class(resource_Object).
class(resource_SetOfNumbers).
class(resource_SetOfStrings).
class(resource_SetOfObjects).
class(resource_Document).
class(resource_Text).
class(resource_Image).
class(resource_URI).
class(resource_SetOfNames).
class(resource_SetOfURIs).
class(resource_PDF).
class(resource_MSDoc).
class(resource_String).
class(resource_Number).
class(resource_FreeText).
class(resource_SpeciesImage).
class(resource_contentURL).
class(resource_WebURL).
class(resource_SetOfScientificNames).
class(resource_Name).
class(resource_HTTPCode).
class(resource_ConnectionTime).
class(resource_SetOfResolvedName).
class(resource_SetOfTaxon).
class(resource_SetOfSciName).
class(resource_ScientificName).
class(resource_CountryName).
class(resource_CountryCode).
class(resource_resolvedName).
class(resource_taxon).
class(resource_sciName).


%Define subclass of <Service Provider> Web Service Concept 
subClass(phylotastic_parameters,phylotastic_concept).
subClass(phylotastic_data_structure,phylotastic_concept).
subClass(phylotastic_resources,phylotastic_concept).
subClass(phylotastic_data_format,phylotastic_concept).
subClass(phylotastic_data_type,phylotastic_concept).
subClass(phylotastic_components,phylotastic_concept).
subClass(resource_SetOfThings,phylotastic_resources).
subClass(resource_Object,phylotastic_resources).
subClass(resource_SetOfNumbers,resource_SetOfThings).
subClass(resource_SetOfStrings,resource_SetOfThings).
subClass(resource_SetOfObjects,resource_SetOfThings).
subClass(resource_Document,resource_Object).
subClass(resource_Text,resource_Object).
subClass(resource_Image,resource_Object).
subClass(resource_URI,resource_Object).
subClass(resource_Tree,resource_Object).
subClass(resource_SetOfNames,resource_SetOfStrings).
subClass(resource_SetOfURIs,resource_SetOfObjects).
subClass(resource_SetOfPhylogenyTrees,resource_SetOfObjects).
subClass(resource_SetOfSpeciesTrees,resource_SetOfPhylogenyTrees).
subClass(resource_SetOfGeneTrees,resource_SetOfPhylogenyTrees).
subClass(resource_PDF,resource_Document).
subClass(resource_MSDoc,resource_Document).
subClass(resource_String,resource_Text).
subClass(resource_Number,resource_Text).
subClass(resource_FreeText,resource_Text).
subClass(resource_SpeciesImage,resource_Image).
subClass(resource_contentURL,resource_URI).
subClass(resource_WebURL,resource_URI).
subClass(resource_SetOfScientificNames,resource_SetOfNames).
subClass(resource_Name,resource_String).
subClass(resource_HTTPCode,resource_Number).
subClass(resource_ConnectionTime,resource_Number).
subClass(resource_CountryCode,resource_Number).
subClass(resource_SetOfResolvedName,resource_SetOfScientificNames).
subClass(resource_SetOfTaxon,resource_SetOfScientificNames).
subClass(resource_SetOfSciName,resource_SetOfScientificNames).
subClass(resource_ScientificName,resource_Name).
subClass(resource_CountryName,resource_Name).
subClass(resource_resolvedName,resource_ScientificName).
subClass(resource_taxon,resource_ScientificName).
subClass(resource_sciName,resource_ScientificName).

%========================================================================
% PART 3 :  Instance of operations classes
%========================================================================
instance(phylotastic_ResolvedScientificNames_GNR_TNRS_GET).
instance(phylotastic_ResolvedScientificNames_GNR_TNRS_POST).
instance(phylotastic_ResolvedScientificNames_OT_TNRS_GET).
instance(phylotastic_ResolvedScientificNames_OT_TNRS_POST).
instance(phylotastic_GetAllSpeciesFromTaxon_OT_GET).
instance(phylotastic_GetPhylogeneticTree_OT_GET).
instance(phylotastic_GetPhylogeneticTree_OT_POST).
instance(phylotastic_GetInformationURLsOfSpecies_EOL_POST).
instance(phylotastic_GetInformationURLsOfSpecies_EOL_GET).
instance(phylotastic_GetImageURLsOfSpecies_EOL_GET).
instance(phylotastic_GetImageURLsOfSpecies_EOL_POST).
instance(phylotastic_FindScientificNamesFromWeb_GNRD_GET).
instance(phylotastic_FindScientificNamesFromFreeText_GNRD_GET).
instance(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET).
instance(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET).
instance(google_ConvertCountryCodeToName_GET).
instance(openTree_GetTaxonomyNameFromSciName_GET).
instance(openTree_GetScientificNameFromAName_GET).


% Add more for testing
instance(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET).
instance(phylotastic_ExtractSpeicesName_From_Gene_Tree_GET).
instance(phylotastic_GetReconciliationTree_GET).

isInstanceOf(phylotastic_ResolvedScientificNames_GNR_TNRS_GET,names_resolution_operation).
isInstanceOf(phylotastic_ResolvedScientificNames_GNR_TNRS_POST,names_resolution_operation).
isInstanceOf(phylotastic_ResolvedScientificNames_OT_TNRS_GET,names_resolution_operation).
isInstanceOf(phylotastic_ResolvedScientificNames_OT_TNRS_POST,names_resolution_operation).
isInstanceOf(phylotastic_GetAllSpeciesFromTaxon_OT_GET,taxon_to_species_operation).
%isInstanceOf(phylotastic_GetPhylogeneticTree_OT_GET,tree_generation).
%isInstanceOf(phylotastic_GetPhylogeneticTree_OT_POST,tree_generation).
isInstanceOf(phylotastic_GetInformationURLsOfSpecies_EOL_POST,species_url_operation).
isInstanceOf(phylotastic_GetInformationURLsOfSpecies_EOL_GET,species_url_operation).
isInstanceOf(phylotastic_GetImageURLsOfSpecies_EOL_GET,species_images_operation).
isInstanceOf(phylotastic_GetImageURLsOfSpecies_EOL_POST,species_images_operation).
isInstanceOf(phylotastic_FindScientificNamesFromWeb_GNRD_GET,names_extraction_web).
isInstanceOf(phylotastic_FindScientificNamesFromFreeText_GNRD_GET,names_extracion_text).
isInstanceOf(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET,taxon_to_species_by_genome).
isInstanceOf(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET,taxon_to_species_by_country).
isInstanceOf(phylotastic_GetPhylogeneticTree_OT_GET,taxonomy_based_extraction).
isInstanceOf(phylotastic_GetPhylogeneticTree_OT_POST,taxonomy_based_extraction).
isInstanceOf(google_ConvertCountryCodeToName_GET,country_code_to_name).
isInstanceOf(openTree_GetTaxonomyNameFromSciName_GET,scientific_name_to_taxonomy).
isInstanceOf(openTree_GetScientificNameFromAName_GET,common_name_to_scientific_name).


% Add more for testing
isInstanceOf(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET,names_extraction_web).
isInstanceOf(phylotastic_ExtractSpeicesName_From_Gene_Tree_GET,names_extraction_tree).
isInstanceOf(phylotastic_getReconciliationTree_GET,tree_reconciliation).

%========================================================================
% PART 4 :  Define hierarchy classes of DATA FORMAT 
%           Define which instance operation has DATA FORMAT of INPUT/Output
%========================================================================
% Class hierarchy of data format
class(list_of_things).
class(list_of_strings).
% classes of tree are defined above part.

class(number).
class(double).
class(integer).
class(http_url).
class(uri).
class(string).

class(data_format_A).
class(data_format_B).
class(data_format_C).
class(data_format_D).
class(plain_text).
class(names_format).

subClass(integer,number).
subClass(double,number).
subClass(http_url,uri).
subClass(list_of_strings,list_of_things).



% concrete operation has data format
%instance_operation_has_input_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET, resource_WebURL, http_url).
instance_operation_has_input_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET, resource_WebURL, data_format_D).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET, resource_SetOfSciName, names_format_1).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET, resource_ConnectionTime, integer).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_GNRD_GET, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET, resource_FreeText, plain_text).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET, resource_SetOfSciName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET, resource_ConnectionTime, integer).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromFreeText_GNRD_GET, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET, resource_SetOfSciName, names_format_resolved_GNR).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET, resource_SetOfTaxon, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET, resource_SetOfResolvedName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_GET, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST, resource_SetOfSciName, names_format_resolved_GNR).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST, resource_SetOfTaxon, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST, resource_SetOfResolvedName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_GNR_TNRS_POST, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET, resource_SetOfSciName, names_format_resolved_OT).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET, resource_SetOfTaxon, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET, resource_SetOfResolvedName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_GET, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST, resource_SetOfSciName, names_format_resolved_OT).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST, resource_SetOfTaxon, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST, resource_SetOfResolvedName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_ResolvedScientificNames_OT_TNRS_POST, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET, resource_taxon, string).
instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET, resource_SetOfSciName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET, resource_taxon, string).
instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_OT_GET, resource_HTTPCode, integer).

instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET, resource_SetOfTaxon, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET, resource_speciesTree, nmsu_tree_format).
instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET, resource_Tree, nmsu_tree_format).
%instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_GET, resource_HTTPCode, integer).

instance_operation_has_input_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST, resource_SetOfTaxon, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST, resource_speciesTree, nmsu_tree_format).
instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST, resource_Tree, nmsu_tree_format).
%instance_operation_has_output_has_data_format(phylotastic_GetPhylogeneticTree_OT_POST, resource_HTTPCode, integer).

instance_operation_has_input_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET, resource_taxon, string).
instance_operation_has_input_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET, resource_CountryName, string).
instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET, resource_SetOfSciName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET, resource_taxon, string).
instance_operation_has_output_has_data_format(phylotastic_GetAllSpeciesFromTaxon_Country_OT_GET, resource_HTTPCode, integer).

instance_operation_has_input_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET, resource_taxon, string).
instance_operation_has_output_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET, resource_SetOfSciName, list_of_strings).
instance_operation_has_output_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET, resource_taxon, string).
instance_operation_has_output_has_data_format(phylotastic_GetSpeciesOfTaxon_Genome_NCBI_GET, resource_HTTPCode, integer).

instance_operation_has_input_has_data_format(google_ConvertCountryCodeToName_GET, resource_CountryCode, integer).
instance_operation_has_output_has_data_format(google_ConvertCountryCodeToName_GET, resource_CountryName, string).

instance_operation_has_input_has_data_format(openTree_GetTaxonomyNameFromSciName_GET, resource_ScientificName, string).
instance_operation_has_output_has_data_format(openTree_GetTaxonomyNameFromSciName_GET, resource_taxon, string).

instance_operation_has_input_has_data_format(openTree_GetScientificNameFromAName_GET, resource_Name, string).
instance_operation_has_output_has_data_format(openTree_GetScientificNameFromAName_GET, resource_ScientificName, string).

%%%
% Add more for testing
%%%

instance_operation_has_input_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET, resource_WebURL, data_format_E).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET, resource_SetOfSciName, names_format_2).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET, resource_ConnectionTime, integer).
instance_operation_has_output_has_data_format(phylotastic_FindScientificNamesFromWeb_CS_NMSU_GET, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_ExtractSpeicesName_From_Gene_Tree_GET, resoucce_geneTree, newickTree).
instance_operation_has_output_has_data_format(phylotastic_ExtractSpeicesName_From_Gene_Tree_GET, resource_SetOfSciName, names_format_2).
instance_operation_has_output_has_data_format(phylotastic_ExtractSpeicesName_From_Gene_Tree_GET, resource_HTTPCode, integer).
instance_operation_has_output_has_data_format(phylotastic_ExtractSpeicesName_From_Gene_Tree_GET, resource_ConnectionTime, integer).
instance_operation_has_output_has_data_format(phylotastic_ExtractSpeicesName_From_Gene_Tree_GET, resource_SetOfNames, list_of_strings).

instance_operation_has_input_has_data_format(phylotastic_getReconciliationTree_GET, resoucce_geneTree, newickTree).
instance_operation_has_input_has_data_format(phylotastic_getReconciliationTree_GET, resource_speciesTree, newickTree).
instance_operation_has_output_has_data_format(phylotastic_getReconciliationTree_GET, resource_reconcileTree, newickTree).
%=======================================================================
% PART 5 : Define classes operation has INPUT and OUTPUT class
%=======================================================================
%%%%%%%%%%%%%%%%%%%
% Hierarchy Level 1
%%%%%%%%%%%%%%%%%%%
% class names_operation 
output(names_operation, set_of_names_1, resource_SetOfNames).

% class list_operation

% class species_operation

% class taxon_operation

% class tree_operation

% class convert_operation

% class look_up_operation

%%%%%%%%%%%%%%%%%%%
% Hierarchy Level 2
%%%%%%%%%%%%%%%%%%%
%%% Parent class : list_operation
% class list_creation_operation

% class list_retrieval_operation

% class list_update_operation

%%% Parent class : names_operation
% class names_extraction_operation
output(names_extraction_operation, connection_time_1, resource_ConnectionTime).
output(names_extraction_operation, http_code_1, resource_HTTPCode).
output(names_extraction_operation, set_of_names_1, resource_SetOfSciName).

% class names_resolution_operation
input(names_resolution_operation, set_of_names_1, resource_SetOfSciName).
output(names_resolution_operation, set_of_names_1, resource_SetOfTaxon).
output(names_resolution_operation, http_code_1, resource_HTTPCode).
output(names_resolution_operation, set_of_names_1, resource_SetOfResolvedName).

%%% Parent class : species_operation

%%% Parent class : taxon_operation
% class taxon_to_species_operation
input(taxon_to_species_operation, single_name_1, resource_taxon).
output(taxon_to_species_operation, set_of_names_1, resource_SetOfSciName).
output(taxon_to_species_operation, http_code_1, resource_HTTPCode).
output(taxon_to_species_operation, single_name_1, resource_taxon).

%%% Parent class : tree_operation
% class tree_comparison
input(tree_comparison, set_of_trees_1, resource_SetOfPhylogenyTrees).

% class tree_generation
output(tree_generation, phylo_tree_1, resource_Tree).

% class tree_information

% class tree_transformation
input(tree_transformation, phylo_tree_1, resource_Tree).
output(tree_transformation, phylo_tree_1, resource_Tree).

% class tree_visualization
input(tree_visualization, phylo_tree_1, resource_Tree).
output(tree_visualization, image_1, resource_Image).

% class tree_reconciliation
input(tree_reconciliation, tree_1, resource_speciesTree).
input(tree_reconciliation, tree_2, resource_geneTree).
output(tree_reconciliation, tree_3, resource_reconcileTree).

%%% Parent class : convert_operation
% class data_format_convert_operation

%%% Parent class : look_up_operation
% class look_up_taxonomy
output(look_up_taxonomy, single_name_1, resource_taxon).

% class look_up_scientific_name
output(look_up_scientific_name, single_name_1, resource_ScientificName).

% class look_up_location


%%%%%%%%%%%%%%%%%%%
% Hierarchy Level 3
%%%%%%%%%%%%%%%%%%%

%%% Parent class : list_operation/list_creation_operation

%%% Parent class : list_operation/list_retrieval_operation

%%% Parent class : list_operation/list_update_operation
% class list_update_add

% class list_update_delete

% class list_update_edit

%%% Parent class : names_operation/names_extraction_operation
% class names_extracion_text
input(names_extracion_text, free_text_1, resource_FreeText).

% class names_extraction_document
input(names_extraction_document, document_1, resource_Document).

% class names_extraction_web
input(names_extraction_web, http_url_1, resource_WebURL).

% class names_extraction_tree
input(names_extraction_tree, tree_1, resource_geneTree).

%%% Parent class : names_operation/names_resolution_operation

%%% Parent class : species_operation/species_information_operation
% class species_images_operation

% class species_url_operation

%%% Parent class : taxon_operation/taxon_to_species_operation
% class taxon_to_species_by_country
input(taxon_to_species_by_country, single_country_name_1, resource_CountryName).

% class taxon_to_species_by_genome

%%% Parent class : tree_operation/tree_comparison
% class branch_length_comparison_operation

% class symmetric_comparison_operation

%%% Parent class : tree_operation/tree_generation
% class tree_extraction_operation

% class tree_retrieval_operation

%%% Parent class : tree_operation/tree_information
% class tree_support_studies

%%% Parent class : tree_operation/tree_transformation
% class tree_scaling_operation

%%% Parent class : tree_operation/tree_visualization

%%% Parent class : convert_operation/data_format_convertion

%%% Parent class : look_up_operation/look_up_location
% class country_code_to_name
input(country_code_to_name, single_country_code_1, resource_CountryCode).
output(country_code_to_name, single_country_name_1, resource_CountryName).

%%% Parent class : look_up_operation/look_up_taxonomy
% class scientific_name_to_taxonomy
input(scientific_name_to_taxonomy, single_name_1, resource_ScientificName).

%%% Parent class : look_up_operation/look_up_scientific_name
% class common_name_to_scientific_name
input(common_name_to_scientific_name, single_name_1, resource_Name).


%%%%%%%%%%%%%%%%%%%
% Hierarchy Level 4
%%%%%%%%%%%%%%%%%%%

%%% Parent class : list_operation/list_update_operation/list_update_add

%%% Parent class : list_operation/list_update_operation/list_update_delete

%%% Parent class : list_operation/list_update_operation/list_update_edit
% class list_update_edit_list_content

% class list_update_edit_list_metadata

%%% Parent class : species_operation/species_information_operation/species_images_operation

%%% Parent class : species_operation/species_information_operation/species_url_operation

%%% Parent class : taxon_operation/taxon_to_species_operation/taxon_to_species_by_country

%%% Parent class : taxon_operation/taxon_to_species_operation/taxon_to_species_by_genome

%%% Parent class : tree_operation/tree_comparison/branch_length_comparison_operation

%%% Parent class : tree_operation/tree_comparison/symmetric_comparison_operation

%%% Parent class : tree_operation/tree_generation/tree_extraction_operation
% class taxonomy_based_extraction
input(taxonomy_based_extraction, set_of_names_1, resource_SetOfTaxon).
output(taxonomy_based_extraction, phylo_tree_1, resource_speciesTree).
output(taxonomy_based_extraction, http_code_1, resource_HTTPCode).

% class phylogeny_based_extraction
input(phylogeny_based_extraction, set_of_names_1, resource_SetOfResolvedName).
output(phylogeny_based_extraction, phylo_tree_1, resource_speciesTree).

%%% Parent class : tree_operation/tree_generation/tree_retrieval_operation

%=======================================================================
%PART 6 : Define support rules - UPDATED
%=======================================================================
subClass(X,Y) :- class(X), class(Y), class(Z), subClass(Z,Y), subClass(X,Z).
subClass(X,Y) :- class(X), class(Y), subClass(X,Z), equalClasses(Y,Z).
subClass(X,Y) :- class(X), class(Y), subClass(Z,Y), equalClasses(X,Z).
isInstanceOf(X,Y) :- isInstanceOf(X,Z), subClass(Z,Y).
equalClasses(X,Y) :- equalClasses(Y,X), class(X), class(Y).

%type_of(X,C) :- type_of(X,D), subClass(D,C).
subClass_immediate(X,Y) :- subClass(X,Y), not not_immediate(X,Y).
not_immediate(X,Y) :- subClass(X,Z), subClass(Z,Y), Z!=X, Z!=Y.  

subClass(X,X) :- class(X).
%is_not_specific(O, C) :- type_of(O, C), type_of(O, C1), subClass(C1, C), C1 != C. 
%is_most_specific(O, C) :- type_of(O, C), not is_not_specific(O, C). 

%=======================================================================
%PART 7 : Define has_input and has_output
%=======================================================================
%operation(X) :- instance(X), isInstanceOf(X,Y), class(Y), subClass(Y,operationClassification).
operation_class(X) :- class(X), subClass(X,operationClassification).

% Define has_input
has_input(C, N, I) :- input(C, N, I).
has_input(C, N, I):- subClass_immediate(C, C1),
                     has_input(C1, N, I),
                     not ab_input(C, C1, N, I).
ab_input(C, C1, N, I):- subClass_immediate(C, C1),
                        has_input(C1, N, I),
                        input(C, N, I1),
                        subClass(I1, I),
                        C1 != C,
                        not override_input(C, C1, N, I).

% Define has_ouput
has_output(C, N, O) :- output(C, N, O).
has_output(C, N, O):- subClass_immediate(C, C1),
                      has_output(C1, N, O),
                      not ab_output(C, C1, N, O).
ab_output(C, C1, N, O):- subClass_immediate(C, C1),
                         has_output(C1, N, O),
                         output(C, N, O1),
                         subClass(O1, O),
                         C1 != C,
                         not override_output(C, C1, N, O).

% Define meaning_operation
meaning_operation(A) :- has_input(A,N,I), 
                        has_output(A,N2,O), 
                        operation_class(A).
%=======================================================================
%PART 8 : Define which OUPUT and INPUT properties are OVERRIDEN or NOT
% Appear => Allow override ; disappear : do not allow overide (keep property of subclass only)
%=======================================================================
%override_output(names_extraction_operation,names_operation,set_of_names_1,resource_SetOfNames).
%override_output(names_extracion_web,names_extraction_operation,set_of_names_1,resource_SetOfNames).
%override_output(names_extracion_web,names_operation,namset_of_names_1es,resource_SetOfNames).

%=======================================================================
%PART 9 : Test to see result
%=======================================================================
%#show has_input/3.
%#show has_output/3.
%#show meaning_operation/1.
%#show instance_operation_has_input_has_data_format/3.
%#show instance_operation_has_output_has_data_format/3.

