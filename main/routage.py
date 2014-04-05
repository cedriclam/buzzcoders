import parser
import algos

import networkx as nx

if __name__ == '__main__':
	# Call parser
	G = nx.Graph()
	G, nbCars, Totaltime, intersections, streets, nodeStart = parser.parseFile("paris_54000.txt")
	
	print "totaltime : ", str(Totaltime)
	print "nbCars : ", str(nbCars)
	print "streets nb : ", str(len(streets))
	print "intersections nb : ", str(len(intersections))
	
	# street info a Street[Distance,Time]
	
	# get the start node 
	_startNode = G.node[nodeStart]
	
	# loop on the graph for each car
	for aCar in range(1,nbCars):
		_startNode.items()
		
		
		
		
	