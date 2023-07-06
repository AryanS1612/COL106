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
        self.append(x-1)
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