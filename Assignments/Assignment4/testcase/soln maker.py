import a4

f = open('testcase.txt','r')
g = open('mine.txt','w')

inp = []
lines = f.readlines()
for line in lines:
    inp.append(line.split(','))

for i in inp:
    out = a4.modPatternMatchWildcard(int(i[0]),i[1],i[2])
    if len(out) == 0:
        g.write('[]')
    else:
        g.write('[' + str(out[0]))
        for j in range(1,len(out)):
            g.write(',' + str(out[j]))
        g.write(']')
    g.write('\n')
g.close()
        
