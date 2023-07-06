from cmath import inf

class Heap:
# This is class Heap which is based on the Data Structure Heap(used in priority Queue) the elements of Heap are 
# list containing two elements(in regards with the problem, the first element is time of collision and the 
# second element is the number of the mass).
    def __init__(self,lst = [None,None]):
        # This initializes the Heap to the input array, if there is not input then an empty Heap is initialized.
        # self._heap is the list which represents the Heap. self._size is the size of the list being used for
        # storing elements. self._len represents the length of the Heap(i.e. the position till which elements are
        # stored)
        self._heap = lst
        self._size = len(lst)
        self._dict = [None]*(self._size)
        if(lst == [None,None]):
            self._len = 0
        else:
            self._len = self._size
            self.Build_Min_Heap()
            for i in range(self._len):
                self._dict[self._heap[i][1]] = i 
            # A dictionary in initialized(int the form of a list) in this case implimentation to enable the update function int this 
            # class. This dictionary is a simple list which enables accessing and finding the location of i
            # indexed mass in constant time, the dictionary list has the index of the ith mass in the Heap at
            # the ith postion in the dictionary.
        return 
        
    def __str__(self):
        # this prints the heap in the form of its bfs order, the purpose of this function is to print the heap
        # for debugging the program.
        print(self._dict)
        return str(self._heap[:self._len])

    def append(self,x):
        # This function appends a new element into the Heap, it also accounts for resizing of the array when
        # the adding a new element exceeds the existing size of the list.
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
        # this function returns the left child's location of the element at position i.
        return 2*i + 1
    
    def right(self,i):
        # this function returns the right child's location of the element at position i.
        return 2*i + 2

    def parent(self,i):
        # this function returns the parent of element at index i.
        return ((i-1)>>1)

    def Min_Heapify(self,i):
        # This function works when the Heap property holds everywhere except possibly at position i.
        # This function is moves down the element at index i to lower position(with respect to the Tree 
        # structure of Heap) which is correct for it and satisfies the Heap property too.
        l = self.left(i)
        r = self.right(i)
        small = i
        # checking for the element among the children of i which would replace it at its position.
        if(l < self._len)and (self._heap[small] > self._heap[l]):
            small = l
        if(r < self._len) and (self._heap[small] > self._heap[r]):
            small = r
        if(small == i):
            # if i cannot be pushed down the heap that would mean the heap property holds.
            return
        # swapping the appropriate element with i.
        x = self._heap[small]
        self._heap[small] = self._heap[i]
        self._heap[i] = x
        self._dict[self._heap[small][1]] = small
        self._dict[self._heap[i][1]] = i
        self.Min_Heapify(small)

    def Insert(self,x):
        # This function inserts element x into the Heap.
        y = x[0]
        x[0] += 1
        self.append(x)
        i = self._len - 1
        return self.decrease_element(i,y)

    def decrease_element(self,i,x):
        # This function decreases the first element of the list stored in the Heap to x and the pushes this
        # element up the Heap to the appropriate position so that the Heap property is maintained.
        p = self.parent(i)
        self._heap[i][0] = x
        while(self._heap[p] > self._heap[i]) and (p > -1):
            y = self._heap[p]
            self._heap[p] = self._heap[i]
            self._heap[i] = y
            self._dict[self._heap[i][1]] = i
            self._dict[self._heap[p][1]] = p
            i = p
            p = self.parent(i)
        return

    def increase_element(self,i,x):
        # This function increases the value of the first element of the list stored in the Heap, then the function
        # self.Min_Heapify is called at this index because the Heap property was maintained before increasing the 
        # value, so the property would be true everywhere except possibly at index i, this we use our good old
        # function self._Min_Heapify.
        self._heap[i][0] = x
        self.Min_Heapify(i)

    def increase_min(self):
        # This returns the min element and changes the first element of the minimum list to infinity, and then 
        # pushes this element down the list.
        x = self._heap[0].copy()
        self.increase_element(0,inf)
        return x

    def heap_minimum(self):
        # This returns the minimum element of the Heap.
        return self._heap[0]

    def extract_minimum(self):
        # This returns the minimum element in the Heap, and rebuilds the Heap to maintain the Heap property.
        val = self._heap[0]
        self._heap[0] = self._heap[self._len - 1]
        self._len -= 1
        self.Min_Heapify(0)
        return val

    def update_element(self,i,x):
        # This function updates the first value of the element in the Heap at position i to x.
        if(x == self._heap[i][0]):
            return
        elif(x > self._heap[i][0]):
            self.increase_element(i,x)
        else:
            self.decrease_element(i,x)

    def Build_Min_Heap(self):
        # This function uses self.Min_Heapify to construct the Heap from a list of elements which satisfies the
        # Heap property.
        last = self._len - 1
        p = self.parent(last)
        while(p > -1):
            self.Min_Heapify(p)
            p -= 1
        return

def Collisions(x,v):
    # This function calculates the future time of collision for each consecutive pair of masses colliding and
    # adds it to a list named time.
    n = len(x)
    time = [None]*(n-1)
    for i in range(n-1):
        if(v[i+1] >= v[i]):
            time[i] = [inf,i]
        else:
            t = -(x[i+1]-x[i])/(v[i+1]-v[i])
            time[i] = [t,i]
    return time

def do_collision(i,M,v):
    # This function updates the velocities of i and (i+1)th masses after the collision of these two masses. 
    a = ((2*M[i+1]*v[i+1])/(M[i] + M[i+1])) + ((M[i]-M[i+1])/(M[i]+M[i+1]))*v[i]
    b = ((2*M[i]*v[i])/(M[i] + M[i+1])) - ((M[i]-M[i+1])/(M[i]+M[i+1]))*v[i+1]
    v[i] = a
    v[i+1] = b
    return

def update_Queue(Queue,i,updt):
    # This function updates the time value of ith element of the heap list to updt.
    index = Queue._dict[i]
    Queue.update_element(index,updt)
    return

def Collide(Queue,M,v,x,ans,n,T,reference):
    # This function removes the topmost element of the Heap(minimum element) and updates the future time of 
    # collision between i-1,i and i+1,i+2 using update_queue.The collision time is updated in a list reference.
    y = Queue.increase_min()
    i = y[1]
    t = y[0] - reference[i]
    reference[i] = reference[i+1] = y[0]
    time = y[0]
    if(time > T):
        return False
    ans.append((time,i,x[i]+v[i]*t))
    if(n == 2):
        return True
    x[i] += v[i]*t
    x[i+1] = x[i]
    do_collision(y[1],M,v)
    if(i == 0):
        if(v[i+2] >= v[i+1]):
            update_Queue(Queue,i+1,inf)
        else:
            updt = time - (x[i+2]+(v[i+2]*(time-reference[i+2]))-x[i+1])/(v[i+2]-v[i+1])
            update_Queue(Queue,i+1,updt)
    elif(i == n-2):
        if(v[i] >= v[i-1]):
            update_Queue(Queue,i-1,inf)
        else:
            updt = time - (x[i] - x[i-1] - v[i-1]*(time-reference[i-1]))/(v[i]-v[i-1])
            update_Queue(Queue,i-1,updt)
    else:
        if(v[i+2] >= v[i+1]):
            update_Queue(Queue,i+1,inf)
        else:
            updt = time - (x[i+2]+(v[i+2]*(time-reference[i+2]))-x[i+1])/(v[i+2]-v[i+1])
            update_Queue(Queue,i+1,updt)
        if(v[i] >= v[i-1]):
            update_Queue(Queue,i-1,inf)
        else:
            updt = time - (x[i] - x[i-1] - v[i-1]*(time-reference[i-1]))/(v[i]-v[i-1])
            update_Queue(Queue,i-1,updt)
    return True

def listCollisions(M,x,v,m,T):
    Queue = Heap(Collisions(x,v))# Heap is constructed.
    n = Queue._len + 1
    if(n == 1):
        return []
    reference = [0]*n
    ans = []
    col_num = 0
    while(col_num < m):
        # Collide function is called multiple times until there are no more collisions to be done or m or T are
        # exceeded.
        if(Collide(Queue,M,v,x,ans,n,T,reference)):
            col_num += 1
        else:
            break
    return ans

# print(listCollisions([940.1440594570123, 342.32941684559046, 686.1000355388383, 520.8309066514597, 870.9632698994412, 727.2119773442081], [2.5912045650076445, 3.3979994719550377, 5.247957197003846, 5.383388625251065, 5.440818809376985, 6.415333653364417], [99.79672039800879, 94.19054127616612, 25.977729855078213, 25.5959601276192, 31.543951443609476, 25.267596192531126], 8, 4.531827813401554))
# print(listCollisions([100000000000.0, 1.0,1.0,100000000000.0], [-3.0, -1.0, 1.0,3.0], [0.0, 1.0, -1.0,0.0], 1000, 1000))
# print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 6, 10.0))
# print(listCollisions([1,1],[0,1],[1,-1],3,1))
M = [100000.0, 1.0, 100000.0, 1.0, 100000.0]
x = [0.0, -2.3, 0.0, -2.5, 0.0]
v = [0.0, 10.0, 20.0, 30.0, 40.0]
m = 100
T = 100.0
print(listCollisions(M, x, v, m, T))