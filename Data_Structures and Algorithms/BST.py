class Node:
    def __init__(self,key,left = None,right = None):
        self.left = left
        self.right= right
        self.key = key
    
class BST:
    
    def __init__(self,lst = []):
        if(lst != []):
            self.root = Node(lst[0])
            for i in range(1,len(lst)):
                self.insert(lst[i])
        else:
            self.root = None

    def insert(self,key):
        if(self.root == None):
            self.root = Node(key)
            return
        def insert_help(root,key):
            p = root
            while(p.left or p.right):
                if(p.key < key):
                    if(p.right):
                        p = p.right
                    else:
                        break
                else:
                    if(p.left):
                        p = p.left
                    else:
                        break
            if(p.key < key):
                p.right = Node(key)
            else:
                p.left = Node(key)
            return
        insert_help(self.root,key)
        return 

    def inorder(self):    
        def inorder_help(root):
            root = root
            if(root):
                inorder_help(root.left)
                print(root.key,end = " ")
                inorder_help(root.right)
        inorder_help(self.root)
    
    def preorder(self):    
        def preorder_help(root):
            root = root
            if(root):
                print(root.key,end = " ")
                preorder_help(root.left)
                preorder_help(root.right)
        preorder_help(self.root)

    def postorder(self):    
        def postorder_help(root):
            root = root
            if(root):
                print(root.key,end = " ")
                postorder_help(root.left)
                postorder_help(root.right)
        postorder_help(self.root)

    def search(self,key):
        p = self.root
        while(p):
            if(p.key == key):
                return p
            elif(p.key < key):
                p = p.right
            else:
                p = p.left
        return None

    def max(self):
        p = self.root
        while(p.right):
            p = p.right
        return p

    def min(self):
        p = self.root
        while(p.left):
            p = p.left
        return p

    def parent(self,q):
        p = self.root
        key = q.key
        


r = BST([2, 3, 13, 7, 5, 11, 17, 29, 19, 23, 31])
# r = BST([])
# r.inorder()
# print()
# print(r.search(3))
# r.insert(2)
# r.insert(3)
# r.insert(13)
# r.insert(7)
# r.insert(5)
# r.insert(11)
# print(r.search(3))
# r.insert(17)
# r.insert(29)
# r.insert(19)
# r.insert(23)
# r.insert(31)
# r.preorder()
# print()
# print()
print(r.min().key)
