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
	
	# create some structure
	_outputCarsMovements = []
	_totalTimeForTheCard = []
	for aCarsMovements in range(1,nbCars+1):
		list = []
		_outputCarsMovements.append(list)
		_totalTimeForTheCard.append(0)
		print "create movement list for Gcars"
	
	# get the start node 
	_startNode = G.node[nodeStart]
	
	# loop on the graph for each car
	for aCar in range(1,nbCars+1):
		print aCar
		bestNext = nodeStart
		previousScore = -1
		# search neigbourth and chose the best one
		#print G[nodeStart]
		for next in G[nodeStart]:
			aNode = G[nodeStart][next]
			# check if the sens of the road is possible
			if algos.isWayPossible(nodeStart,aNode): 
				if previousScore == -1:
					
					previousScore = algos.ratio(aNode["distance"],aNode["time"],aNode["coef"])
					bestNext = next
				else :
					if algos.ratio(aNode["distance"],aNode["time"],aNode["coef"]) < previousScore :
						previousScore = algos.ratio(aNode["distance"],aNode["time"],aNode["coef"])
						bestNext = next
		
		# now we have the best node, we can add it in the list of node for this car
		G[nodeStart][bestNext]
		


	