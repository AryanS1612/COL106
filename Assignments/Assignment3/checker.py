import raghav
import time
import pickle

f = open("testcase.bin", "rb")
test = pickle.load(f)
f = open("testcase2.bin", "rb")
test2 = pickle.load(f)

f = open("check.bin", "rb")
check = pickle.load(f)

out = []


def compare(out, check):
    if (len(out) != len(check)):
        return False
    for j in range(len(out)):
        if (len(out[j]) != len(check[j])):
            return False
        for i in range(len(out[j])):
            if abs(out[j][i][0] - check[j][i][0]) > 0.0001 or out[j][i][1] != check[j][i][1] or abs(out[j][i][2] - check[j][i][2]) > 0.0001:
                print(f"Testcase number {j+1}", ", your answer, ", out[j][i])
                print(f"Testcase number {j+1}",
                      ", checker answer, ", check[j][i])
                return False
    return True


print("Starting Checker")
print("Checking Normal Cases...")
st = time.time()
for i in test:
    out.append(raghav.listCollisions(i[0], i[1], i[2], i[3], i[4]))
print("Time taken: ", time.time()-st)
print()
print("Checking Large Cases...")
st = time.time()
for i in test2:
    out.append(raghav.listCollisions(i[0], i[1], i[2], i[3], i[4]))
print("Time taken: ", time.time()-st)


if compare(out, check):
    print("Passed")
else:
    print("Failed")
