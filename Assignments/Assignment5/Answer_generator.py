import a5_variant as a5
import pickle
test = open("tt.bin","rb")
testcases = pickle.load(test)
y_o = []
for i in testcases:
    p = a5.findMaxCapacity(i[0],i[1],i[2][0],i[2][1])
    y_o.append(p)
file  = open("ans.bin","wb")
pickle.dump(y_o, file) # converts array to binary and writes to output
print("Done!!")
# import pickle
# f = open("ans.bin","rb")
# l = pickle.load(f)
# print("Done!!")