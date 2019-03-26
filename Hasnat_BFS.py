#Syed Hasnat Ali Shah (01-131162-029)
import time
from collections import defaultdict,deque 
class Graph:
    def __init__(self):
        self.list_neighbor = defaultdict(list)
        self.list_node =defaultdict(list)
    def add_node(self,node):
        self.list_node[node] = True

    def add_edge(self,node,nodebis):
        try :
            self.list_neighbor[node].append(nodebis)
        except :
            self.list_neighbor[node] = []
            self.list_neighbor[node].append(nodebis)
        try :
            self.list_neighbor[nodebis].append(node)
        except :
            self.list_neighbor[nodebis] = []
            self.list_neighbor[nodebis].append(node)
    def neighbors(self,node):
        try :
            return self.list_neighbor[node]
        except :
            return []
    def nodes(self):
        return self.list_node.keys()
    def delete_edge(self,node,nodebis):
        self.list_neighbor[node].remove(nodebis)
        self.list_neighbor[nodebis].remove(node)
    def delete_node(self,node):
        del self.list_node[node]
        try :
            for nodebis in self.list_neighbor[node] :
                self.list_neighbor[nodebis].remove(node)
            del self.list_neighbor[node]
        except :
            return "error"
        #s==startNode, f==finalNode
    def bfs(self, s,f):
        start = time.time()
        visited = defaultdict(bool)
        dist = defaultdict(int)
        queue = deque()
        queue.append(s)
        visited[s] = True
        dist[s] = 0

        while queue:
            d = queue.popleft()
            print(d, end=" ")
            #goal state check
            if  d==f:
                break

            for neighbor in self.list_neighbor[d]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    dist[neighbor] = dist[d] + 1
        end=time.time()
        print("Execution time:-")
        print(end - start," SECONDS")


if __name__ == "__main__":
    G = Graph()
    totalNode=int(input("Enter Total num of node:"))
    for node in range(totalNode):
        eachNode=int(input("Enter node: "))
        G.add_node(eachNode)

    totalEdges=int(input("Enter Total num of edges:"))
    for node in range(totalEdges):
        startEdge=int(input("Enter 1 Edge node: "))
        endEdge=int(input("Enter 2 Edge node: "))
        print("-"*50)
        G.add_edge(startEdge,endEdge)
    
    initialNode=int(input("Enter starting node:"))
    goalNode=int(input("Enter goal node:"))
    print( G.bfs(initialNode,goalNode))
    
