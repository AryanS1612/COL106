import a5 as a5
import pickle
import time
def checkpath(li,links,n):
    max_capacity = li[0]
    path = li[1]
    l = [[]]
    for i in range(n):
        for j in range(n):
            l[i].append(0)
        l.append([])
    for i in range(len(links)):
        l[links[i][0]][links[i][1]] = max(links[i][2],l[links[i][0]][links[i][1]])
        l[links[i][1]][links[i][0]] = max(links[i][2],l[links[i][1]][links[i][0]])
    com = l[path[0]][path[1]]
    for i in range(1,len(path)-1):
        com = min(com,l[path[i]][path[i+1]])
    if com == max_capacity:
        return True
    else:
        return False
    

test = open("tt.bin","rb")
testcases = pickle.load(test)
y_o = []
st = time.time()
for i in testcases:
    p = a5.findMaxCapacity(i[0],i[1],i[2][0],i[2][1])
    y_o.append(p)
end = time.time()
print(end-st)
file  = open("ans.bin","rb")
ans = pickle.load(file)
if len(ans) != len(y_o):
    print("Failed")
else:
    k = 0
    for i in range(len(ans)):
        if ans[i][0] != y_o[i][0]:
            print("Failed (maximum capacity mismatch)")
            k = 1
            break
    if k == 0:
        for i in range(len(ans)):
            kk = 0
            if not(checkpath(y_o[i],testcases[i][1],testcases[i][0])):
                print("Failed (maximum capacity of the returned path doesn't match with the returned value)")
                kk = 1
        if kk == 0:
            print("Passed")