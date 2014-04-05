import sys
import networkx as nx
import algos

def createNodes(G, streets):
        i = 0
        for street in streets:
                params = street.split(" ")
                G.add_node(i)
                G[i]['intersect0'] = int(params[0])
                G[i]["intersect1"] = int(params[1]) 
                G[i]['weight'] = algos.ratio(float(params[4]), float(params[3]))
                i += 1

def createEdges(G):
        i = 0
        while i < G.number_of_nodes():
               G.add_edge(G[i]["intersect0"], G[i]["intersect1"],  weight=G[i]["weight"], coef=1)
               del G[i]["intersect1"]
               del G[i]["intersect0"]
               del G[i]["weight"]
               i += 1
 
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

        G = nx.Graph()

        createNodes(G, streets)
        createEdges(G)

	return G, nbCars, Totaltime, intersections, streets, numStartIntersection



