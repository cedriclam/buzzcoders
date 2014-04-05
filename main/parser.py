import sys
import networkx as nx

def parseFile(inputFile):
        inputFile = open(inputFile)
        print "Name of the file : ", inputFile.name
        lines = inputFile.readlines()


        params = lines[0].split(" ")
        nbIntersections = int(params[0])
        nbStreets = int(params[1])
        Totaltime = int(params[2])
        nbCars = int(params[3])
        numStartIntersection = int(params[4])

        endIntersection = nbIntersections + 1
        intersections = lines[1:endIntersection]
        streets = lines[endIntersection +1 : endIntersection + 1 + nbStreets]


        G=nx.Graph()
	return G, nbCars, Totaltime, intersections, streets

