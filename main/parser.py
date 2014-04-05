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
                G[i]['way'] = bool(int(params[2]) - 1)
                G[i]['time'] = float(params[3]) 
                G[i]['distance'] = float(params[4])

                i += 1

def createEdges(G):
        i = 0
        while i < G.number_of_nodes():
               if (G[i]["way"] == False):
                        G.add_edge(G[i]["intersect0"], G[i]["intersect1"], distance=G[i]['distance'] , time=G[i]['time'], coef = 1, first=G[i]["intersect0"])
               else:
                        G.add_edge(G[i]["intersect0"], G[i]["intersect1"], distance=G[i]['distance'] , time=G[i]['time'], coef = 1)

               del G[i]["intersect1"]
               del G[i]["intersect0"]
               del G[i]["distance"]
               del G[i]["time"]
               del G[i]["way"]
               
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



