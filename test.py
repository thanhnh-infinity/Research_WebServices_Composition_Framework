WORKFLOW_1 = [{"service_class_index": 3, "service_class_name": "names_resolution_operation", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#names_resolution_operation", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_SetOfSciName", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfSciName", "map": {"from": "names_extraction_tree", "at_step": 2, "resource_ontology_id": "resource_SetOfSciName"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_SetOfTaxon", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfTaxon"}, {"resource_ontology_id": "resource_HTTPCode", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_HTTPCode"}, {"resource_ontology_id": "resource_SetOfResolvedName", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfResolvedName"}]}}}, {"service_class_index": 5, "service_class_name": "tree_reconciliation", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#tree_reconciliation", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_speciesTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree", "map": {"from": "phylogeny_based_extraction", "at_step": 5, "resource_ontology_id": "resource_speciesTree"}}, {"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree", "map": {"from": "gene_tree_scaling", "at_step": 3, "resource_ontology_id": "resource_geneTree"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_reconcileTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_reconcileTree"}, {"resource_ontology_id": "resource_Tree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_Tree"}]}}}, {"service_class_index": 4, "service_class_name": "phylogeny_based_extraction", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#phylogeny_based_extraction", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_SetOfResolvedName", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfResolvedName", "map": {"from": "names_resolution_operation", "at_step": 4, "resource_ontology_id": "resource_SetOfResolvedName"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_speciesTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree"}, {"resource_ontology_id": "resource_HTTPCode", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_HTTPCode"}]}}}, {"service_class_index": 0, "service_class_name": "gene_based_extraction", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#gene_based_extraction", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_SetOfGeneStrings", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings", "map": {"from": "initial_state", "at_step": 0, "resource_ontology_id": "resource_SetOfGeneStrings"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree"}, {"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree"}]}}}, {"service_class_index": 2, "service_class_name": "gene_tree_scaling", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#gene_tree_scaling", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree", "map": {"from": "gene_based_extraction", "at_step": 1, "resource_ontology_id": "resource_geneTree"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree"}]}}}, {"service_class_index": 1, "service_class_name": "names_extraction_tree", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#names_extraction_tree", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree", "map": {"from": "gene_based_extraction", "at_step": 1, "resource_ontology_id": "resource_geneTree"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_SetOfSciName", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfSciName"}, {"resource_ontology_id": "resource_HTTPCode", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_HTTPCode"}, {"resource_ontology_id": "resource_ConnectionTime", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_ConnectionTime"}]}}}]

WORKFLOW_2 = [{"service_class_index": 3, "service_class_name": "names_resolution_operation", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#names_resolution_operation", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_SetOfSciName", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfSciName", "map": {"from": "names_extraction_tree", "at_step": 2, "resource_ontology_id": "resource_SetOfSciName"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_SetOfTaxon", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfTaxon"}, {"resource_ontology_id": "resource_HTTPCode", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_HTTPCode"}, {"resource_ontology_id": "resource_SetOfResolvedName", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfResolvedName"}]}}}, {"service_class_index": 5, "service_class_name": "tree_reconciliation", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#tree_reconciliation", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_speciesTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree", "map": {"from": "taxonomy_based_extraction", "at_step": 5, "resource_ontology_id": "resource_speciesTree"}}, {"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree", "map": {"from": "gene_tree_scaling", "at_step": 3, "resource_ontology_id": "resource_geneTree"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_reconcileTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_reconcileTree"}, {"resource_ontology_id": "resource_Tree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_Tree"}]}}}, {"service_class_index": 4, "service_class_name": "taxonomy_based_extraction", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#taxonomy_based_extraction", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_SetOfTaxon", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfTaxon", "map": {"from": "names_resolution_operation", "at_step": 4, "resource_ontology_id": "resource_SetOfTaxon"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_speciesTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_speciesTree"}, {"resource_ontology_id": "resource_HTTPCode", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_HTTPCode"}]}}}, {"service_class_index": 0, "service_class_name": "gene_based_extraction", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#gene_based_extraction", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_SetOfGeneStrings", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfGeneStrings", "map": {"from": "initial_state", "at_step": 0, "resource_ontology_id": "resource_SetOfGeneStrings"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree"}, {"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree"}]}}}, {"service_class_index": 2, "service_class_name": "gene_tree_scaling", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#gene_tree_scaling", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree", "map": {"from": "gene_based_extraction", "at_step": 1, "resource_ontology_id": "resource_geneTree"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree"}]}}}, {"service_class_index": 1, "service_class_name": "names_extraction_tree", "service_class_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#names_extraction_tree", "service_class_parameters": {"input": {"info": {"data_format": "x-www-urlencoded(Fixed)"}, "components": [{"resource_ontology_id": "resource_geneTree", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_geneTree", "map": {"from": "gene_based_extraction", "at_step": 1, "resource_ontology_id": "resource_geneTree"}}]}, "output": {"info": {"data_format": "application/json"}, "components": [{"resource_ontology_id": "resource_SetOfSciName", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_SetOfSciName"}, {"resource_ontology_id": "resource_HTTPCode", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_HTTPCode"}, {"resource_ontology_id": "resource_ConnectionTime", "resource_ontology_uri": "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#resource_ConnectionTime"}]}}}]