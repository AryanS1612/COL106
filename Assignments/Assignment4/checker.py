import time
import a4 as a4
import KMP 
# import findN
import random
import math

#To generate random prime less than N
def Primes(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

def modPatternMatch_testing_module(eps):                  #? modPatternMatch testing module
    print("Building Testcases...")
    testcase = []                       # list of tuples, (text, pattern), length :- l
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = 100
    n = 100000
    m = 100
    
    length_of_pattern = []              # list of length of patterns (contains l elements)
    length_of_text = []
    for i in range(l):
        length_of_pattern.append(random.randint(1, m))
    for i in range(l):                  #? Building testcases
        length_of_text.append(random.randint(length_of_pattern[i], n))
        curr_length_of_text = length_of_text[i]
        curr_text = ""
        curr_pattern = ""
        for j in range(length_of_pattern[i]):
            curr_pattern = curr_pattern + alphabets[random.randint(0, 25)]
        if (random.randint(1,5) == 1):
            curr_text = curr_text + curr_pattern
        for j in range(curr_length_of_text):
            if (random.randint(1,100) == 1):
                curr_text = curr_text + curr_pattern
            else:
                curr_text = curr_text + alphabets[random.randint(0, 25)]
        if (random.randint(1,10) == 1):
            curr_text = curr_text + curr_pattern
        testcase.append((curr_text, curr_pattern))

    print("Running Testcases...")
    t_KMP = 0
    t_modPatternMatch = 0
    N = a4.findN(eps, length_of_pattern[i])
    print("N: ", N)
    primes = Primes(N)
    print("length of list of primes: ",len(primes))
    for i in range(l):
        print("Running on subtestcase: ", i+1)
        t1 = time.time()
        KMP_output = KMP.KMP_probing(testcase[i][1], testcase[i][0]) 
        t2 = time.time()
        t_KMP += (t2 - t1)
        t3 = time.time()
        modPatternMatch_output = a4.randPatternMatch(eps, testcase[i][1], testcase[i][0])
        t4 = time.time()
        t_modPatternMatch += (t4 - t3)
        
        if (len(KMP_output) > 0):
            a = 0                                   # index of KMP_output
            b = 0                                   # index of modPatternMatch_output
            while (a < len(KMP_output)):
                if (KMP_output[a] == modPatternMatch_output[b]):
                    a += 1
                    b += 1
                else:
                    b += 1
                if (b == len(modPatternMatch_output) and a < len(KMP_output)):
                    print("Failed on subtestcase: ", i+1)
                    return 
        print("length of KMP_output: ",len(KMP_output))
        print("length of modPatternMatch_output: ", len(modPatternMatch_output))

    print("Passed")
    print("KMP_time: ", t_KMP)
    print("modPatternMatch: ", t_modPatternMatch)
    print("Ratio of time_taken by modPatternMatch and KMP: ", t_modPatternMatch/t_KMP)
    if (t_modPatternMatch/t_KMP > 10):
        print("Too slow")
    else:
        print("Passed within the time limit")
    return
    

if (__name__ == "__main__"):
    eps = 0.3 + 0.1*random.random()
    print("eps: ", eps)
    modPatternMatch_testing_module(eps)
