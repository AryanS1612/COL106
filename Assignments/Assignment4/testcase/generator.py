import random
import math

def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
#can change the lower limit of primes here
	return primes[random.randint(0,len(primes)-1)]

def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

def generator():
        char = [chr(65 + i) for i in range(0,26)]

        x,p = '',''
        #change 10**5 to get appropriate upper prime limit
        #keeping q large will get mostly empty output, try smaller q
        #to get more diverse/errored results
        q = randPrime(10**5)

        #n is length of x string and m the length of p
        #again try to keep m small for more outputs
        n = 10**6
        m = random.randint(10,20)

        for i in range(0,n):
            x += char[random.randint(0,25)]

        pt = random.randint(0,m)
        for i in range(0,m):
            if i == pt:
                    p += '?'
            else:
                    p += char[random.randint(0,25)]

        return([q,p,x])

def generate(t):
        f = open('testcase.txt','w')
        for i in range(0,t):
                [q,p,x] = generator()
                f.write(str(q) + ',' + str(p) + ',' + str(x) + '\n')

        f.close()

generate(100)
    
