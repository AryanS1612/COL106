from Queue import Queue
from cmath import inf
class Graph:
    # Graph has n vertices and m edges.
    # Space used = O(n + m).
    def __init__(self,n,links):
        # This initializes the elements of the ADT Graph, this data structure has the following accesor elements:
        # (c) visit, this stores wether a particular vertex has been visited or not.
        # (d) edges, the edges of the graph are represented in terms of an adjacency list.
        self.edges = []
        self.visit = []
        for i in range(n):
            # Initializing all the above mentioned properties.
            self.edges.append([])
            self.visit.append(False)
        for each in links:
            # Creating the adjacency list.
            self.edges[each[0]].append([each[1],each[2]])
            self.edges[each[1]].append([each[0],each[2]])

    def BFS(self,s):
        pred = []
        bfs_distance = []
        for i in range(len(self.visit)):
            pred.append(None)
            bfs_distance.append(inf)
        queue = Queue()
        queue.Enqueue(s)
        bfs_distance[s] = 0
        while(queue.len() != 0):
            curr = queue.Dequeue()
            self.visit[curr] = True
            for i in range(len(self.edges[curr])):
                if(bfs_distance[self.edges[curr][i][0]] == inf):
                    if(self.visit[self.edges[curr][i][0]] == False):
                        queue.Enqueue(self.edges[curr][i][0])
                        bfs_distance[self.edges[curr][i][0]] = bfs_distance[curr] + 1
                        pred[self.edges[curr][i][0]] = curr
        return (bfs_distance,pred)

    # def components(self,)

    
n = 8
links = [[0,1,6],[0,3,1],[0,2,7],[1,4,3],[4,5,2],[5,2,13],[5,3,6],[2,7,4],[3,7,9],[3,6,17]]
# links = [[0,1,6],[0,3,1],[0,2,7],[1,4,3],[3,7,9],[3,6,17],[5,3,6]]
G = Graph(n, links)
# (d,paths) = G.BFS(0)
# print(d)
# print(paths)
