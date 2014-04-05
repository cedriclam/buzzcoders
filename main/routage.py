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
	_addCoef = 130
	
	# create some structure
	global _outputCarsMovements
	_outputCarsMovements = []
	global _totalTimeForTheCard
	_totalTimeForTheCard = []
	
	for aCarsMovements in range(1,nbCars+1):
		list = []
		_outputCarsMovements.append(list)
		_totalTimeForTheCard.append(0)

	
	# add the departure node
	for cars in _outputCarsMovements:
		cars.append(nodeStart)
	
	tmp = nodeStart
	# loop on the graph for each car
	for aCar in range(1,nbCars+1):

		# search neigbourth and chose the best one
		nodeStart = tmp
		timeIsOver = False
		while not timeIsOver:
			bestNext = nodeStart
			previousScore = -1
			for next in G[nodeStart]:
				aNode = G[nodeStart][next]
				# check if the sens of the road is possible
				if algos.isWayPossible(nodeStart,aNode): 
					isPresent = False
					for aCarMovement in _outputCarsMovements:
						if next in aCarMovement:
							isPresent = True
							break
						
					if isPresent:
						continue
					
					if previousScore == -1:
						previousScore = algos.ratio(aNode["distance"],aNode["time"],aNode["coef"])
						bestNext = next
					else :
						if algos.ratio(aNode["distance"],aNode["time"],aNode["coef"]) < previousScore :
							previousScore = algos.ratio(aNode["distance"],aNode["time"],aNode["coef"])
							bestNext = next
			
			if bestNext == nodeStart:
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
			bestEdge = G[nodeStart][bestNext]
			if (_totalTimeForTheCard[aCar-1] + bestEdge["time"]) <= Totaltime:
				# we can add this Node
				_outputCarsMovements[aCar-1].append(bestNext)
				_totalTimeForTheCard[aCar-1] = _totalTimeForTheCard[aCar-1] + bestEdge["time"]
				bestEdge["coef"] = bestEdge["coef"] + _addCoef
				nodeStart = bestNext
				print "."
			else:
				# we are done 
				timeIsOver = True
		
	outputFile = open("output.txt", "w+")

	outputFile.write(str(len(_outputCarsMovements)) + "\n")
	for cars in _outputCarsMovements:
		outputFile.write(str(len(cars)) + "\n")
		for dest in cars:
			outputFile.write(str(dest) + "\n")


	