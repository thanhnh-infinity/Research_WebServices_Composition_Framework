import json
from similarity import edge_similarity
from similarity import node_similarity
from similarity import topology_similarity

def test():
  return "Worked"

print "Thanh Tested " + str(edge_similarity.getSim_EdgeSets(1,2))
print "Thanh Tested " + str(node_similarity.getSim_btw_2_descriptions("generate graph from names","generate tree from names"))