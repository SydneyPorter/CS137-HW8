import math


class Edge:

    def __init__(self, start, end, weight):
        if(start == end and weight != 0):
            raise IndexError("No self-edges allowed")
        self.__s = start # An integer representing a vertex index
        self.__e = end # An integer representing a vertex index
        self.__w = weight #An integer representing an edge weight between the vertices

    def getWeight(self):
        return self.__w

    def getStart(self):
        return self.__s

    def getEnd(self):
        return self.__e
    
    def __repr__(self):
        return str(self.__s) + " --("+ str(self.__w) +")--> " +str(self.__e)

class Graph:
    def __init__(self,n):
        self.__numVertices = n
        self.__matrix = [ [ "inf" for i in range(n) ] for j in range(n) ] 

    def setEdge(self,e):
        self.__matrix[e.getStart()-1][e.getEnd()-1] = e.getWeight()

    def getEdge(self,e):
        return self.__matrix[e.getStart()-1][e.getEnd()-1]

    def getNumVert(self):
        return self.__numVertices

    def __repr__(self):
        return str(self.__matrix)

    def __str__(self):
        return '\n'.join([','.join(str(c) for c in row) for row in self.__matrix])

def Dijkstra(W):
    F = None
    n = W.getNumVert()
    i = None 
    vnear = None
    e = None
    touch = [None] * n
    length = [None] * n

    i = 2
    for i in range(n):
        touch[i] = 1
        length[i] = W.getEdge(i).weight
    
    i = 0
    for i in range(n-1):
        
        min = math.inf
        j = 2
        for j in range(n):
            if 0 <= length[j] < min:
                min = length[j]
                vnear = j
        e = W.getEdge(touch[vnear])
        F.append(e)
        
        j = 2
        for j in range(n):
            if length[vnear] + W.weight[j] < length[j]:
                length[i] = length[vnear] + W.weight[j]
                touch[j] = vnear
                
        length[vnear] = -1

    return F
    
# Example - Neapolitan p. 171
W = Graph(5)

W.setEdge(Edge(1,5,1))
W.setEdge(Edge(1,4,6))
W.setEdge(Edge(1,3,4))
W.setEdge(Edge(1,2,7))
W.setEdge(Edge(3,2,2))
W.setEdge(Edge(3,4,5))
W.setEdge(Edge(4,2,3))
W.setEdge(Edge(5,4,1))

print(Edge(4,5,9))

for i in range(W.getNumVert()):
    W.setEdge(Edge(i+1,i+1,0))

print(W) #Print the graph itself
print(Dijkstra(W)) #Should print the set of edges v1->v5, v5->v4, v1->v3, v4->v2
