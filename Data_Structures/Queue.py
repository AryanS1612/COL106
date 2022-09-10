class Queue:
    def __init__(self):
        # initializes the Queue to length 2 and with head set as 0 and tail set as 0 head points at the position
        # in the array which was occupied first and has not been dequeued yet, tail points at the element which
        # has an empty position and would be occupied next
        self._head = 0
        self._tail = 0
        self._Size = 4
        self._Queue = [None]*4

    def Resize(self):
        # When the entire list gets filled, this function creates a new list of Size double the filled list, then
        # all the elements of the old list are copied to the new one such that head is 0 and tail is (od Size)+1
        # head and tail values of Self are then changed to the corresponding ones as mentioned above
        size = self._Size
        self._Size *= 2
        lst = [None]*self._Size
        it = self._head
        i = 0
        while(it != self._tail):
            lst[i] = self._Queue[it]
            if(it == size - 1):
                it = 0
            else:
                it += 1
            i += 1
        self._head = 0
        self._tail = size+1
    
    def Enqueue(self,x):
        # This functions adds the element x to the end of the Queue
        check = True
        if(self._tail == self._Size):
            
        if(self._tail == self._head - 1):
            self.Resize()
            self._Queue[self._tail] = x
            self._tail += 1
        else:
            if(self._tail == self._Size - 1):
                self._Queue[self._tail] = x
                self._tail = 0
            else:
                self._Queue[self._tail] = x
                self._tail += 1
    
    def Dequeue(self):
        # This function removes(by remove we simply mean that the head pointer no longer points to that element
        # but to the one next to it in the Queue) the element at head and returns it.
        x = self._Queue[self._head]
        if(self._head == self._Size - 1):
            self._head = 0
        else:
            self._head += 1
        return x
    
    def len(self):
        # This function returns the length of the Queue(Note : the length of the queue and the Size of the list
        # we are currently using are not the same).
        if(self._tail > self._head):
            return self._tail - self._head
        else:
            return self._Size-self._head+self._tail


a = Queue()
n = int(input())
for i in range(n):
    s = input()
    if(s == 'enq'):
        x = int(input())
        a.Enqueue(x)
    else:
        print(a.Dequeue())
    


            
