class Stack: #  this is the data structure stack.
    def __init__(self): 
        # initializes the Stack with Size 2,list(store) with length 2 with elements None and head to 0, the
        # 0th element of the list will not contain any element and will only have None at that index, head
        # stores the index of the top-most element.
        self._store = [None]*2
        self._head = 0
        self._Size = 2
    
    def is_empty(self):
        # this function checks wether the stack is empty(i.e. has any element stored or not) or not.
        if self._head == 0:
            return True
        return False

    def __str__(self):
        # this prints the stack, the purpose of this function is to print the stack for debugging the program.
        return str(self._store[1:self._head + 1])

    def Resize(self):
        # When the Stack get filled this doubles the size of the list and copies the elments of the list to the
        # new list of double the size.
        self._Size *= 2 # size of list is doubled.
        lst = [None]*self._Size # new list with double the size is created.
        it = 0
        for i in self._store:
            lst[it] = i
            it += 1
        # elements of old list are copied to the new list.
        self._store = lst # new list is stored as self._store.

    def pop(self):
        # this function removes the top most element of the stack and returns it.
        if self.is_empty(): # checking for validity of the pop command.
            return 'Error,Invalid Command'
        x = self._store[self._head]
        self._store[self._head] = None # top most element is assigned the value None. 
        self._head -= 1 # value of head is reduced by one, now pointing to the element before the previous top
        # -most element.
        return x

    def top(self):
        # this function returns the top-most element of the stack.
        if self.is_empty():# checking for validity of the pop command.
            return 'Error,Invalid Command'
        return self._store[self._head] # the top-most elment is simpy returned.

    def push(self,x):
        # this adds a new element at the top of the stack.
        if self._head == self._Size - 1: # this if condition cheks if the stack is full and does not have
            # any empty index.
            self.Resize() # inside the if condition, if the list self._store has all it's indexes occupied
            # then we resize the stack using the Resize() function.
            self._store[self._head + 1] = x
            # if the stack has indexes without any element stored in them then we simply increase head by one
            # and store the value x at the new head.
            self._head += 1
        
        else: 
            # if the stack has indexes without any element stored in them then we simply increase head by one
            # and store the value x at the new head.
            self._store[self._head + 1] = x
            self._head += 1