import math

class Graph:
    
    def __init__(self, n):
        self.n = n
        self.numEdges = 0
        self.edges = []
    
    def setEdge(self, edge):
        self.edges.append(edge)
        self.numEdges += 1
        
    def getWeight(self, start, end):
        i = 0
        for i in range(self.numEdges):
            temp = self.edges[i]
            if temp.start == start and temp.end == end:
                return temp.weight
            i += 1
        return 0
        
class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
    
    def __repr__(self):
        return str([self.start, self.end, self.weight])
    
def Dijkstra(graph):
    touch = [0] * graph.n
    length = [0] * graph.n
    newGraph = []
    
    i = 2
    for i in range(graph.n):
        if i == 2:
            touch[i] = 1
            length[i] = graph.getWeight(1,i)
        i += 1
    
    i = 0  
    for i in range(graph.n - 1):
        min = math.inf
        
        j = 2
        for j in range(graph.n):
            if 0 <= length[j] < min:
                min = length[j]
                vnear = j
            j += 1

        e = [touch[vnear], vnear]
        newGraph.append(e)
        
        j = 2
        for j in range(graph.n):
            if length[vnear] + graph.getWeight(vnear, j) < length[j]:
                length[j] = length[vnear] + graph.getWeight(vnear,j)
                touch[j] = vnear
            j+= 1
        
        length[vnear] = -1
        i += 1

    return newGraph

Example = Graph(5)

Example.setEdge(Edge(1,2,7))
Example.setEdge(Edge(1,3,4))
Example.setEdge(Edge(1,4,6))
Example.setEdge(Edge(1,5,1))
Example.setEdge(Edge(3,2,2))
Example.setEdge(Edge(3,4,5))
Example.setEdge(Edge(4,2,3))
Example.setEdge(Edge(5,4,1))

# should print [(0,4),(4,3),(0,2),(3,1)]
print(Dijkstra(Example))
