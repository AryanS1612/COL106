import random
f = open("tt.bin","wb")
import pickle
import math
array = []
# ? we are first constructing a tree with the given number of vertices and then add additional edges to it to make it a connected graph
n = 1000													# ! number of vertices
m = 1000000								# ! m is the number of additional edges to be added
weights_l = 1											# ! lower bound of the weights
weights_u = 1000											# ! upper bound of the weights


def generate_tree(n: int):
	l = []
	for i in range(n):
		l.append(i)
	edges = []
	covered_l = [0]
	l.remove(0)
	for i in range(n-1):
		r = random.sample(l,1)[0]
		l.remove(r)
		s = random.sample(covered_l,1)[0]	
		covered_l.append(r)
		edges.append((s,r,random.randint(weights_l,weights_u)))
	return edges


def generate_graph(n: int,m: int):
	l = generate_tree(n)
	li = []
	for i in range(n):
		li.append(i)
	for i in range(m):
		a = random.sample(li,1)[0]
		b = random.sample(li,1)[0]
		if a != b:
			l.append((a,b,random.randint(weights_l,weights_u)))
	return l


l = []
for i in range(n):
	l.append(i)
for i in range(1):
	a = generate_graph(n,m)
	b = random.sample(l,2)
	print("STEP: ", i+1)
	array.append([n,a,b])
# print(array)
pickle.dump(array, f) 				# & converts array to binary and writes to output
print("Done!!")
# import pickle
# f1 = open("t1.bin","rb")
# f2 = open("t2.bin","rb")
# f3 = open("t3.bin","rb")
# f4 = open("t4.bin","rb")
# f5 = open("t5.bin","rb")
# f6 = open("t6.bin","rb")
# f7 = open("t7.bin","rb")
# l1 = pickle.load(f1)
# l2 = pickle.load(f2)
# l3 = pickle.load(f3)
# l4 = pickle.load(f4)
# l5 = pickle.load(f5)
# l6 = pickle.load(f6)
# l7 = pickle.load(f7)
# l = l1+l2+l3+l4+l5+l6+l7
# f = open("tt.bin","wb")
# pickle.dump(l,f)
# print("Done!!")
