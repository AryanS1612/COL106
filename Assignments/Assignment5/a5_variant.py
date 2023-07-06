from cmath import inf
class Heap:
    def __init__(self,lst = []):
        # This is the constrictor for Max_Heap
        self._heap = lst
        self._size = len(lst)
        if(lst == []):
            self._len = 0
        else:
            self._len = self._size
            self.Build_Max_Heap()
        return 
        
    def __str__(self):
        # this prints the heap in the form of its bfs order, the purpose of this function is to print the heap for debugging the program.
        return str(self._heap[:self._len])

    def append(self,x):
        # append function has been implemented here by scratch by copying list.
        if(self._size == 0):
            self._size = 1
            self._len = 1
            self._heap = [x]
        else:
            if(self._len == self._size):
                self._size *= 2
                lst = [None]*self._size
                for i in range(self._len):
                    lst[i] = self._heap[i]
                self._heap = lst
                self._heap[self._len] = x
                self._len += 1
                return
            else:
                self._heap[self._len] = x
                self._len += 1
                return

    def left(self,i):
        # Time Complexity : O(1)
        # Auxillary Space : O(1)
        return 2*i + 1
    
    def right(self,i):
        # Time Complexity : O(1)
        # Auxillary Space : O(1)
        return 2*i + 2

    def parent(self,i):
        # Time Complexity : O(1)
        # Auxillary Space : O(1)
        return ((i-1)>>1)

    def Max_Heapify(self,i):
        # This function pushes up an heap element up where heap property is violated.
        # Time Complexity : O(logn)
        # Auxillary Space : O(1)
        l = self.left(i)
        r = self.right(i)
        large = i
        if(l < self._len) and (self._heap[large] < self._heap[l]):
            large = l
        if(r < self._len) and (self._heap[large] < self._heap[r]):
            large = r
        if(large == i):
            return
        x = self._heap[large]
        self._heap[large] = self._heap[i]
        self._heap[i] = x
        self.Max_Heapify(large)

    def Insert(self,x):
        # Inserts a new element into the Heap, the element with reduced value is added at the end of the heap and then increase_element
        # operation is applied at that index.
        # Time Complexity : O(logn)
        # Auxillary Space : O(1)
        self.append([x[0]-1,x[1]])
        i = self._len - 1
        return self.increase_element(i,x)

    def increase_element(self,i,x):
        # This function increases the value of the element stored at index i to x
        # Time Complexity : O(logn)
        # Auxillary Space = O(1)
        p = self.parent(i)
        self._heap[i] = x
        while(p > -1) and (self._heap[p] < self._heap[i]):
            y = self._heap[p]
            self._heap[p] = self._heap[i]
            self._heap[i] = y
            i = p
            p = self.parent(i)
        return

    def heap_maximum(self):
        # Can access maximum element with this function.
        # Time Complexity : O(1)
        # Auxillary Space : O(1)
        return self._heap[0]

    def extract_maximum(self):
        # Removes the Heap maximum element, the maximum element is first swapped with the last element, and then length of heap is reduced
        # by 1, after this we use Heapify function at the top(as it contains the last element of the heap at this time).
        # Time Complexity : O(logn)
        # Auxillary Space : O(1)
        val = self._heap[0].copy()
        self._heap[0] = self._heap[self._len - 1]
        self._len -= 1
        self.Max_Heapify(0)
        return val

    def Build_Max_Heap(self):
        # This Builds the heap in O(n) time, we repeatedly apply heapify operation repeatedly many times, starting from gif(n/2).
        # Time Complexity : O(n)
        # Auxillary Space : O(1)
        last = self._len - 1
        p = self.parent(last)
        while(p > -1):
            self.Max_Heapify(p)
            p -= 1
        return

class Graph:
    # Graph has n vertices and m edges.
    # Space used = O(n + m).
    def __init__(self,n,links):
        # This initializes the elements of the ADT Graph, this data structure has the following accesor elements:
        # (a) cost, this represents some attribute between two vertex pair (u,v).The meaning of this term may vary form case to case, in 
        #     this instance it represents the amount of data that can be transmitted from a given source to some other vertex.
        # (b) pred, this gives the predecessor of the element i in the paths that were visited).
        # (c) visit, this stores wether a particular vertex has been visited or not.
        # (d) edges, the edges of the graph are represented in terms of an adjacency list.
        self.cost = []
        self.pred = []
        self.edges = []
        self.visit = []
        for i in range(n):
            # Initializing all the above mentioned properties.
            self.cost.append(inf)
            self.pred.append(None)
            self.edges.append([])
            self.visit.append(False)
        for each in links:
            # Creating the adjacency list.
            self.edges[each[0]].append([each[1],each[2]])
            self.edges[each[1]].append([each[0],each[2]])
    
    def init_source(self,s):
        # Intializing the source.
        self.cost[s] = 0
        self.visit[s] = True

def findMaxCapacity(n,links,s,t):
    G = Graph(n,links)
    G.init_source(s)
    queue = Heap()
    # for each in G.edges[s]:
    #     queue.Insert([each[1],each[0]])
    #     G.pred[each[0]] = s
    #     G.cost[each[0]] = each[1]
    queue.Insert([inf,s])
    while(queue.heap_maximum()[1] != t):
        curr = queue.extract_maximum()
        for each in G.edges[curr[1]]:
            if(G.visit[each[0]] == False):
                if(G.cost[each[0]] == inf):
                    queue.Insert([min(each[1],curr[0]),each[0]])
                    G.cost[each[0]] = min(each[1],curr[0])
                    G.pred[each[0]] = curr[1]                   
                elif(min(each[1],curr[0]) > G.cost[each[0]]):
                    queue.Insert([min(each[1],curr[0]),each[0]])
                    G.cost[each[0]] = min(each[1],curr[0])
                    G.pred[each[0]] = curr[1]
        G.visit[curr[1]] = True
    cost = queue.heap_maximum()[0]
    path_temp = []
    curr = t
    while(curr != s):
        path_temp.append(curr)
        curr = G.pred[curr]
    path = []
    path.append(s)
    for i in range(len(path_temp)):
        path.append(path_temp[len(path_temp)-i-1])
    return (cost,path)

# print(findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3))
# print(findMaxCapacity(3,[(0,1,1),(1,2,1)],0,1))
# print(findMaxCapacity(4,[(0,1,30),(1,2,40),(2,3,50),(0,3,10)],0,3))
print(findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2))
# print(findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5))