import sys
import networkx as nx

# calculate if it's interesting to go on this street
def ratio(distance,time,coef = 1):
    return float(distance/time)*coef

def chooseEdge(graph,nodeId):
    pass

def isWayPossible(nodeStart,aNode):
    if aNode["first"] != -1:
        if aNode["first"] != nodeStart:
            return False
    return True

def getRatio(graph, nodeId, deep = 1):
    if deep <= 0:
        return 0
    
    outputVal = 0
    bestRatio = -1
    bestNode = -1
    for nextNode in graph[nodeId]:
        nextEdge = graph[nodeId][nextNode]
        currentRatio = ratio(aNode["distance"],aNode["time"],aNode["coef"]) + getRatio(graph,nextNode, deep -1)
        if bestRatio == -1:
            bestRatio = currentRatio
            bestNode = nextNode
        else:
            if currentRatio < bestRatio:
                bestRatio = currentRatio
                bestNode = nextNode
                
            
    return bestRatio