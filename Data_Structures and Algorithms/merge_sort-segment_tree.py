class Node:
    def __init__(self,tup,lst,left = None,right = None):
        self.tuple = tup
        self.sort = lst
        self.left = left
        self.right = right

def segment_tree_y(lst):
    def Merge_Sort(lst,l,r):
        mid = int((l+r)/2)
        if(l == r):
            a = lst[l:l+1].copy()
            node = Node((l,l),a)
            return node
        else:
            left = Merge_Sort(lst,l,mid)
            right = Merge_Sort(lst,mid+1,r)
            Merge(lst,l,mid,r)
            a = lst[l:r].copy()
            node = Node((l,r),a,left[1],right[1])
            return node
            
    def Merge(lst,l,mid,r):
        a = lst[l:mid+1]
        b = lst[mid+1:r+1]
        i =0;j = 0
        k = l
        while(i < mid+1-l) and (j < r-mid):
            if(a[i] < b[j]):
                lst[k] = a[i]
                k += 1
                i += 1
            else:
                lst[k] = b[j]
                k += 1
                j += 1
        while(i < mid-l+1):
            lst[k] = a[i]
            k += 1
            i += 1
        while(j < r-mid):
            lst[k] = b[j]
            k += 1
            j += 1
        return lst[l:r+1]
    root = Merge_Sort(lst,0,len(lst)-1)
    return root