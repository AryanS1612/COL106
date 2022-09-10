from time import time
from a1 import findPositionandDistance
import time
m = 0
d = open("check.txt", "r")
r = d.readlines()
print("Starting Checker")
st = time.time()
for i in open("testcases.txt", "r"):
    # print('testcase',m,'passed')
    if str(findPositionandDistance(str(i).replace("\n", ""))) != str(r[m]).rstrip():
        print(f"Testcase {m+1} didnt match")
    m += 1
print(f"Time taken for normal testcases is {time.time()-st}")
print()
print("Checking Big Testcases")
st = time.time()
for i in open("testcases_big.txt", "r"):
    # print('testcase',m,'passed')
    if str(findPositionandDistance(str(i).replace("\n", ""))) != str(r[m]).rstrip():
        print(f"Testcase {m+1} didnt match")
    m += 1
print(f"Time taken for big testcases is {time.time()-st}")
