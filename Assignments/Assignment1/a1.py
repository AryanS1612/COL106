import string
# from time import time
# import time

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

def ord_string(s,k,len):
    # it is iterator, x,y,z and d are x,y,z co-ordinate and distance respectively.
    # this function converts a series of commands(which contain only +,- operations followed by alphabets and
    # no brackets and numerals) for the drone to the vector by which it's position co-ordinate changes and
    # the distance travelled in the same. It takes as input the string and does the above until there is a + or
    # -.
    it = k;x = 0;y = 0;z = 0;d =0
    while(it < len) and (s[it] == '+' or s[it] ==  '-'):
        if(s[it] == '+'):
            if(s[it+1] == 'X'):
                x += 1
            elif s[it+1] == 'Y':
                y += 1
            else:
                z += 1
        else:
            if(s[it+1] == 'X'):
                x -= 1
            elif s[it+1] == 'Y':
                y -= 1
            else:
                z -= 1
        it += 2
        d += 1
    return [x,y,z,d]

def num(s,k,len):
    # k is the iterator in the loop,j stores the initial index if the string
    # this function read string of digits and converts then into numbers of int type, it returns a Tuple
    # with elements as the number and the end value of the iterated section of the list.
    j = k
    while (s[k].isdigit()) and (k < len):
        # loop runs till we are reading digits.
        k += 1
    return (int(s[j:k]),k)

def evaluate(a):
    # This function converts all the lists when a closing bracket is read, all the lists in the stack till a 
    # number is read are added and then the number is multiplied with the list obtained after adding lists.
    lst = a.pop()# removes the top-most list.
    x = a.pop()# removes the element below the list form the stack.
    while(type(x)==list): # this loop keeps adding list elements until a number is obtained.
        for i in range(4):
            lst[i] += x[i]
        x = a.pop()
    # finally the number is multiplied to all the elements of the list obtained after adding the lists ahead of
    # the number.
    for i in range(4):
        lst[i] *= x
    a.push(lst)
    return

def final_solve(a):
    # this function is called in the end and it simply adds all the lists iin the stack as in the end there
    # would be no numbers left, as they are removed whenever the function evaluate is called.
    lst = a.pop()# removes the top-most list.
    while(a.is_empty() == False):
        # keeps adding the lists until the stack becomes empty.
        x = a.pop()
        for i in range(4):
            lst[i] += x[i]
    return lst

def findPositionandDistance(s):
    # it is the iterator which iterates through the string, l is the length of the string,lst is the lst which
    # stores the changes in the co-ordinates of the drone as the program string s in read.a is the stack in
    # which we add and remove elements.
    it = 0
    l = len(s)
    lst = [0]*4
    a = Stack()
    if(s == ''):
        # If the string is empty then the finction retrurns [0,0,0,0] as the drone doesn't move at all.
        return [0,0,0,0]
    else:
        while(it < l):
            if (s[it] == '+') or (s[it] == '-'):
                # when a '+' or '-' is read, the function ord_string is called and it's return value id pushed
                # into the stack.
                a.push(ord_string(s,it,l))
                it += 2*a.top()[3]
                # the iterator(it) will advance by exactly 2*(distance travelled by drone).
            elif s[it].isdigit():
                (val,it) = num(s,it,l)# this changes the iterator to appropriate value and finds the numeral.
                a.push(val)# the numeral is pushed into the stack.
                if(s[it+1] == ')'):
                    # this if condition checks for sections of string s cotaining substrings like numeral()
                    # in this case an empty list(i.e. [0,0,0,0]) is pushed into the stack.
                    a.push([0,0,0,0])
                    evaluate(a)
                    # as this if being true means that the bracket has ended, thus we evaluate the stack.
                    it += 2# the iterator is advacned by 2 as the closing bracket has already been accounted for.
            elif s[it] == ')':
                # on reading an closing bracket the stack is evaluated.
                evaluate(a)
                it += 1
            else:
                it += 1
        return final_solve(a)# this finally adds all the lists in the stack.

# s = input()
# st = time.time()
# print("Starting Time")
# for i in open("testcase5000.txt", "r"):
#     findPositionandDistance(str(i).replace("\n", ""))
# print(time.time()-st)