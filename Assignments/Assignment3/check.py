import random 
import time
import a3_Aniket as a3
n = 1000
a = random.randint(0,100)
b = random.randint(0,100)
# d = random.randint(0,100)
d = 2000000
l1 = []
l2 = []
l11 = []
l22 = []
for i in range(-d,d):
    l11.append(a+i)
    l22.append(b+i)
for i in range(-d-1000000,-d):
    l1.append(a+i)
    l2.append(b+i)
for i in range(d+1,d + 1000000):
    l1.append(a+i)
    l2.append(b+i)
x = random.sample(l1,100000) + random.sample(l11,100000)
y = random.sample(l22,100000)+ random.sample(l2,100000)
p = list(zip(x,y))
# print(p)
st = time.time()
pi = a3.PointDatabase(p)
t1 = time.time() - st
print(t1)
st = time.time()
print(pi.searchNearby((a,b),d))
# for _ in range(10**4):
#     a = random.randint(0,100)
#     b = random.randint(0,100)
#     print(pi.searchNearby((a,b),d))
t2 = time.time() - st
print(t2)