import os

#GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL = "/Volumes/Develop_Data_MacOS/All_Workspace/Python_Workspace/Planning_Project/OWL_Ontology_App/Ontology/cdao_phylotastic.owl"
#GLOBAL_PHYLO_METHODS_ONTOLOGY_URL = "/Volumes/Develop_Data_MacOS/All_Workspace/Python_Workspace/Planning_Project/OWL_Ontology_App/Ontology/phylogenetic_methods.owl"
GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL = os.path.join(os.getcwd(),"OWL_Ontology_App","Ontology","cdao_phylotastic.owl")
GLOBAL_PHYLO_METHODS_ONTOLOGY_URL = os.path.join(os.getcwd(),"OWL_Ontology_App","Ontology","phylogenetic_methods.owl") 

#GLOBAL_CDAO_PHYLOTASTIC_ONTOLOGY_URL = "/var/web_service/Research_Planning_Ontology_Core_API/Ontology/cdao_phylotastic.owl"
#GLOBAL_PHYLO_METHODS_ONTOLOGY_URL = "/var/web_service/Research_Planning_Ontology_Core_API/Ontology/phylogenetic_methods.owl"

PREFIX_CDAO_PHYLOTASTIC_ONTOLOGY_URL = "http://www.cs.nmsu.edu/~epontell/CDAO/cdao.owl#"
PREFIX_PHYLOGENETIC_METHODS_ONTOLOGY_URL = "http://www.cs.nmsu.edu/~epontell/Ontologies/phylogenetic_methods.owl#"
PREFIX_MYGRID_MOBY_SERIVE_ONTOLOGY_URI = "http://www.mygrid.org.uk/mygrid-moby-service#"
PREFIX_RDF_SCHEMA_URL = "http://www.w3.org/2000/01/rdf-schema#"

PATH_TO_ONTOLOGY_JAR_ENGINE = "OWL_Ontology_App/JenaOWLEngine/OntologyEngine.jar"