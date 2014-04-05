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
	global _addCoef
	_addCoef = 1
	
	# create some structure
	global _outputCarsMovements
	_outputCarsMovements = []
	global _totalTimeForTheCard
	_totalTimeForTheCard = []
	
	for aCarsMovements in range(1,nbCars+1):
		list = []
		_outputCarsMovements.append(list)
		_totalTimeForTheCard.append(0)
		print aCarsMovements

	for cars in _outputCarsMovements:
		cars.append(nodeStart)
	
	# get the start node 
	_startNode = G.node[nodeStart]
	
	# loop on the graph for each car
	for aCar in range(1,nbCars+1):
		print aCar
		bestNext = nodeStart
		
		# search neigbourth and chose the best one
		#print G[nodeStart]
		timeIsOver = False
		while not timeIsOver:
			previousScore = -1
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
			#print G[nodeStart]
			#print bestNext
			bestEdge = G[nodeStart][bestNext]
			if (_totalTimeForTheCard[aCar-1] + bestEdge["time"]) <= Totaltime:
				# we can add this Node
				_outputCarsMovements[aCar-1].append(bestNext)
				_totalTimeForTheCard[aCar-1] = _totalTimeForTheCard[aCar-1] + bestEdge["time"]
				bestEdge["coef"] = bestEdge["coef"] + _addCoef
				nodeStart = bestNext
			#	print "add to car:" + str(aCar) + " node:" + str(bestNext)
			else:
				# we are done 
				timeIsOver = True
		
		
	print len(_outputCarsMovements)
	for cars in _outputCarsMovements:
		print len(cars)
		for dest in cars:
			print dest


	