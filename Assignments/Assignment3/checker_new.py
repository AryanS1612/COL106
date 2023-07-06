import a3
import pickle
import time
print("Starting Checker")
f = open("testcase.bin", "rb")
l = pickle.load(f)
check = []
out = pickle.load(open("check.bin", "rb"))
# st=time.time()
t, t1, p = 0, 0, 0
for i in l:
    z, q = i[0], i[1]
    st = time.time()
    a = a3.PointDatabase(z)
    t += time.time()-st
    for i in q:
        st = time.time()
        m = a.searchNearby(i[0], i[1])
        t1 += time.time()-st
        m.sort()
        check.append(m)
        if not out[p] == m:
            print(p, len(out[p]), len(m), i[0], i[1], m)
        p += 1

# print(time.time()-st)
print("Preprocessing Time (__init__): ", t, "Query RunTime:", t1)
if check == pickle.load(open("check.bin", "rb")):
    print("Yay")
else:
    print("Nay")
