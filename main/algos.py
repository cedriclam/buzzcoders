import sys
import networkx as nx

# calculate if it's interesting to go on this street
def ratio(distance,time,coef = 1):
    return float(distance/time)*coef

def chooseEdge(graph,nodeId):
    pass

    