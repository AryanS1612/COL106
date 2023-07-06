import a4
import time

f = open('testcase.txt','r')
g = open('mine.txt','r')

inp = []
lines = f.readlines()
for line in lines:
    inp.append(line.split(','))

compare = g.readlines()
data = []
for line in compare:
    lst1 = (((line.rstrip(']').rstrip(']\n')).lstrip('[')).split(','))
    lst2 = []
    for i in lst1:
        lst2.append(int(i))
    data.append(lst2)
    
f.close()
g.close()
k = 0

st = time.time()
for i in inp:
    out = a4.modPatternMatchWildcard(int(i[0]),i[1],i[2])
    if out != data[k]:
        print('Wrong answer for i = ', k)

    k+=1

print('time taken:', time.time()-st)
        
