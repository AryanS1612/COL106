dict_alpha={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
    N = findN(eps,len(p))
    q = randPrime(N)
    print(q)
    return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

# return appropriate N that satisfies the error bounds
def findN(eps,m):
    z=((2*m)/eps)*math.log2(26)
    N=int(2*z*math.log2(z))
    return N

# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
    mod_26=1%q
    mod_sum_pattern=0
    mod_sum_text=0
    list_index=[]
    for alpha in range(len(p)-1,-1,-1):
        mod_sum_pattern=(mod_sum_pattern + (dict_alpha[p[alpha]]*mod_26)%q)%q
        mod_sum_text= (mod_sum_text + (dict_alpha[x[alpha]]*mod_26)%q)%q
        mod_26=(mod_26*26)%q
    if mod_sum_pattern==mod_sum_text:
        list_index.append(0)
    for i in range(len(p),len(x)):
        mod_sum_text=(((26*mod_sum_text)%q)-((mod_26*dict_alpha[x[i-len(p)]])%q) + (dict_alpha[x[i]]%q))%q
        if mod_sum_pattern==mod_sum_text:
            list_index.append(i-(len(p)-1))
    return list_index
# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
    mod_26=1%q
    mod_questionmark=0
    mod_sum_pattern=0
    mod_sum_text=0
    mod_sum_textcopy=0
    list_index=[]
    index=0
    for alpha in range(len(p)-1,-1,-1):
        if p[alpha]=="?":
            index=alpha
            mod_questionmark=mod_26
        else:
            mod_sum_pattern= (mod_sum_pattern + (dict_alpha[p[alpha]]*mod_26)%q)%q
        mod_sum_text =(mod_sum_text + (dict_alpha[x[alpha]]*mod_26)%q)%q
        mod_26=(mod_26*26)%q
    mod_sum_textcopy=mod_sum_text
    mod_sum_text=(mod_sum_text - ((dict_alpha[x[index]]*mod_questionmark)%q))%q
    if mod_sum_pattern==mod_sum_text:
        list_index.append(0)
    mod_sum_text=mod_sum_textcopy
    for i in range(len(p),len(x)):
        mod_sum_text=(((26*mod_sum_text)%q)-((mod_26*dict_alpha[x[i-len(p)]])%q) + (dict_alpha[x[i]]%q))%q
        mod_sum_textcopy=mod_sum_text
        mod_sum_text=(mod_sum_text - ((dict_alpha[x[i+index-(len(p)-1)]]*mod_questionmark)%q))%q
        if mod_sum_pattern==mod_sum_text:
            list_index.append(i-(len(p)-1))
        mod_sum_text=mod_sum_textcopy
    return list_index