# Ontology API

#### Service 1.

__Service Name:__     Get all instances of a directed class

__Resource URI - Parser 1:__      http://<service_host>/query?request=get_all_instances_of_a_class&parser_engine=1&owl_class_uri={}

__Resource URI - Parser 2:__      http://<service_host>/query?request=get_all_instances_of_a_class&parser_engine=2&owlclass={}}&ontology={}

__HTTP Method:__    GET,POST
    
__Examples:__ 
```
http://127.0.0.1:8000/query?request=get_all_instances_of_a_class&parser_engine=1&owl_class_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23tree_generation
```
```
http://127.0.0.1:8000/query?request=get_all_instances_of_a_class&parser_engine=2&owlclass=phylotastic_resources&ontology=cdao_phylotastic
```
```
http://127.0.0.1:8000/query?request=get_all_instances_of_a_class&parser_engine=2&owlclass=NameResolution_Operation&ontology=cdao_phylotastic
```

#### Service 2.

__Service Name:__     Get all directed sub-class of a class

__Resource URI Parser engine 1 :__    http://<service_host>/query?request=get_all_directed_subclass_of_a_class&parser_engine=1&owl_class_uri={}

__Resource URI Parser engine 2 :__    http://<service_host>/query?request=get_all_directed_subclass_of_a_class&parser_engine=2&owlclass={}&ontology={}

__HTTP Method:__    GET,POST
    
__Examples:__ 
```
http://127.0.0.1:8000/query?request=get_all_directed_subclass_of_a_class&parser_engine=1&owl_class_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23names_operation
```
```
http://127.0.0.1:8000/query?request=get_all_directed_subclass_of_a_class&parser_engine=2&owlclass=operationClassification&ontology=phylo_methods
```
```
http://127.0.0.1:8000/query?request=get_all_directed_subclass_of_a_class&parser_engine=2&owlclass=list_operation&ontology=phylo_methods
```

#### Service 3.

__Service Name:__     Get hierarchy sub-classes of a root class

__Resource URI:__     http://<service_host>/query?request=get_hierarchy_subclasses_of_a_class&owlclass={}&ontology={}

__HTTP Method:__    GET,POST
    
__Examples:__ 
```
http://127.0.0.1:8000/query?request=get_hierarchy_subclasses_of_a_class&owlclass=operationClassification&ontology=phylo_methods
```
```
http://127.0.0.1:8000/query?request=get_hierarchy_subclasses_of_a_class&owlclass=list_operation&ontology=phylo_methods
```

#### Service 4.

__Service Name:__     Get detail information of an operation instance

__Resource URI Engine 1:__      http://<service_host>/request=get_detail_information_of_a_operation&parser_engine=1&owl_operation_uri={}

__Resource URI Engine 2:__      http://<service_host>/request=get_detail_information_of_a_operation&parser_engine=2&owl_operation_name={}&ontology={}

__HTTP Method:__    GET,POST
    
__Examples:__ 
```
http://127.0.0.1:8000/query?request=get_detail_information_of_a_operation&parser_engine=1&owl_operation_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23phylotastic_GetPhylogeneticTree_OT_POST
```
```
http://127.0.0.1:8000/query?request=get_detail_information_of_a_operation&parser_engine=2&owl_operation_name=phylotastic_FindScientificNamesFromFreeText_GNRD_GET&ontology=cdao_phylotastic
```

#### Service 5.

__Service Name:__     Get detail information of an resource instance

__Resource URI Engine 1:__      http://<service_host>/request=get_detail_information_of_a_resource&parser_engine=1&owl_operation_uri={}

__Resource URI Engine 2:__      http://<service_host>/request=get_detail_information_of_a_resource&parser_engine=2&owl_resource_name={}&ontology={}

__HTTP Method:__    GET,POST
    
__Examples:__ 
```
http://127.0.0.1:8000/query?request=get_detail_information_of_a_resource&parser_engine=1&owl_resource_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa
```
```
http://127.0.0.1:8000/query?request=get_detail_information_of_a_resource&parser_engine=2&owl_resource_name=free_text&ontology=cdao_phylotastic
```

#### Service 6.

__Service Name:__     Get detail information of an component instance

__Resource URI Engine 1:__      http://<service_host>/request=get_detail_information_of_a_component&parser_engine=1&owl_component_uri={}

__Resource URI Engine 2:__      http://<service_host>/request=get_detail_information_of_a_component&parser_engine=2&owl_component_name={}&ontology={}

__HTTP Method:__    GET,POST
    
__Examples:__ 
```
http://127.0.0.1:8000/query?request=get_detail_information_of_a_component&parser_engine=1&owl_component_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23param_resolved_names
```
```
http://127.0.0.1:8000/query?request=get_detail_information_of_a_component&parser_engine=2&owl_component_name=param_species&ontology=cdao_phylotastic
```

#### Service 7. (IN-PROGRESSIVE)

__Service Name:__     Get detail workflow after running composition

__Resource URI Engine 1:__      http://<service_host>/request=get_detail_workflow_after_perform_composition

__HTTP Method:__    POST

__INPUT:__ [{"resource_id":"","resource_uri":""},{"resource_id":"","resource_uri":""},{"resource_id":"","resource_uri":""},{"resource_id":"","resource_uri":""}]

__OUTPUT:__ <inprogressive> 

__Examples:__ 
```
curl - X POST "http://127.0.0.1:8000/query?request=get_detail_workflow_after_perform_composition" -H "content-type:application/json" -d '<input>' 
```

#### Service 8.

__Service Name:__     Get triples data from input

__Resource URI :__      http://<service_host>/getTriples?triple_type={}

__HTTP Method:__    GET,POST

__Parameters:__       
* *triple_type:*    Type of triple want to get.


__If ```triple_type=1```, provide ```owl_subject_uri``` parameter, returned values are ```predicates``` and ```objects```__ 
```
http://127.0.0.1:8000/getTriples?triple_type=1&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa 
```

__If ```triple_type=2```, provide ```owl_object_uri``` parameter, returned values are ```subjects``` and ```predicates```__ 
```
http://127.0.0.1:8000/getTriples?triple_type=2&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa 
```

__If ```triple_type=3```, provide ```owl_predicate_uri``` parameter, returned values are ```subjects``` and ```objects```__ 
```
http://127.0.0.1:8000/getTriples?triple_type=3&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23has_Element 
```

__If ```triple_type=4```, provide ```owl_subject_uri``` and ```owl_predicate_uri``` parameter, returned values are ```objects```__ 
```
http://127.0.0.1:8000/getTriples?triple_type=4&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23has_Element 
```
```
http://127.0.0.1:8000/getTriples?triple_type=4&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23param_resolved_names&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/Ontologies/phylogenetic_methods.owl%23is_a
```

__If ```triple_type=5```, provide ```owl_object_uri``` and ```owl_predicate_uri``` parameter, returned values are ```subjects```__ 
```
http://127.0.0.1:8000/getTriples?triple_type=5&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxon&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23has_Element 
```
```
http://127.0.0.1:8000/getTriples?triple_type=5&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa&owl_predicate_uri=http://www.cs.nmsu.edu/~epontell/Ontologies/phylogenetic_methods.owl%23is_a
```

__If ```triple_type=6```, provide ```owl_subject_uri``` and ```owl_object_uri``` parameter, returned values are ```predicates```__ 
```
http://127.0.0.1:8000/getTriples?triple_type=6&owl_subject_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxa&owl_object_uri=http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl%23bio_taxon
```