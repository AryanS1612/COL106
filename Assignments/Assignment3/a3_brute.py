class PointDatabase:
    def __init__(self,pointlist):
        pointlists = [None]*len(pointlist)
        for i in range(len(pointlist)):
            pointlists[i] = list(pointlist[i])
        self.sort_x = self.sort(pointlists)

    def sort(self,lst):
        def Merge_Sort(lst,l,r):
            mid = int((l+r)/2)
            if(l != r):
                Merge_Sort(lst,l,mid)
                Merge_Sort(lst,mid+1,r)
                Merge(lst,l,mid,r)
            return
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
        Merge_Sort(lst,0,len(lst)-1)
        return lst

    def search_min_x(self,x):
        lst = self.sort_x
        def search_min_help(lst,l,r,x):
            mid = int((l+r+1)/2)
            if(lst[mid][0] < x):
                if(mid == len(lst)-1):
                    return -1
                else:
                    return search_min_help(lst,mid+1,r,x)
            else:
                if(mid == 0):
                    return mid
                elif(lst[mid-1][0] < x):
                    return mid
                else:
                    return search_min_help(lst,l,mid-1,x)
        return search_min_help(lst,0,len(lst)-1,x)

    def search_max_x(self,x):
        lst = self.sort_x
        def search_max_help(lst,l,r,x):
            mid = int((l+r+1)/2)
            if(lst[mid][0] > x):
                if(mid == 0):
                    return -1
                else:
                    return search_max_help(lst,l,mid-1,x)
            else:
                if(mid == len(lst)-1):
                    return len(lst)-1
                elif(lst[mid+1][0] > x):
                    return mid
                else:
                    return search_max_help(lst,mid+1,r,x)
        return search_max_help(lst,0,len(lst)-1,x)

    def searchNearby(self,tup,d):
        lower_range_x = tup[0] - d
        upper_range_x = tup[0] + d
        lower_range_y = tup[1] - d
        upper_range_y = tup[1] + d
        lower_index = self.search_min_x(lower_range_x)
        upper_index = self.search_max_x(upper_range_x)
        ans = []
        if(lower_index == -1) or (upper_index == -1):
            return ans
        else:
            for i in range(lower_index,upper_index+1):
                if(self.sort_x[i][1] <= upper_range_y) and (self.sort_x[i][1] >= lower_range_y):
                    ans.append(tuple(self.sort_x[i]))
        return ans

