import random
import math
# Key Assumption : a + b takes min(loga,logb) time, thus a + 1 takes O(1) time


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
	# The aim is to choose a N such that, x[i...i+m-1] is not equal to p then Pr(i belongs to L) <= eps.
	# Let us consider the equality(or matching) of strings soleley in terms of f(x[i...i+m-1]) = f(p).
	# Thus in a more mathematical way, what we need to do is, Pr(f(x[i...i+m-1])modulo q = f(p)modulo q|f(x[i...i+m-1]) != f(p)) <= eps.
	# The above expression is equivalent to Pr(q divides (f(x[i...i+m-1]) - f(p))| f(x[i...i+m-1]) != f(p)) <= eps.
	# We aim at bounding the expression Pr(q divides (f(x[i...i+m-1]) - f(p))| f(x[i...i+m-1]) != f(p)) by an expression in terms of N and m
	# Now, we get a random prime less than N from the fucntion randPrime(N), this means that the above expression of Probability can be 
	# simplified using the fact that number of prime factors of (f(x[i...i+m-1]) - f(p)) are log(f(x[i...i+m-1]) - f(p)) and we have a 
	# random distribution of primes less than N from findPrime(N), thus probability that the prime from randPrime(N) is a factor of 
	# (f(x[i...i+m-1]) - f(p)) is log(f(x[i...i+m-1]) - f(p))/pi(N), the maximum possible difference f(x[i...i+m-1]) - f(p) can be 26^m - 1.
	# thus Pr(q divides (f(x[i...i+m-1]) - f(p))| f(x[i...i+m-1]) != f(p)) <= mlog(26)/pi(N). We know pi(N) > N/2logN, thus, 
	# Pr(q divides (f(x[i...i+m-1]) - f(p))| f(x[i...i+m-1]) != f(p)) <= mlog(26)/(N/2logN) <= eps. Thus, 2mlog(26)/eps <= N/logN.
	# Now let 2mlog(26)/eps = k, we approximate N to be aklogk(more tighter may exist, this is just a sensible guess(as k*k is quite big)),
	# k <= aklog(k)/(loga + logk + log(logk)) implies, loga + log(logk) <= (a-1)logk,By plotting this on a graphing calculator and varying a,
	# it can be found that for a ~ 1.79 for all k >= 2log(26) ~ 9.4
	k = 2*(m/eps)*(math.log(26,2))
	return int(1.79*k*(math.log(k,2)))

# Return sorted list of starting indices where p matches x
# In this function we first compute f(p)modulo q, in O(mlogq) and also simultaneously compute first m length sub-string of x, then for each
# subsequent m length substring starting at index i, we just subtract 26^(m-1)*(x[i-1]) from previous value at index i-1, and multiply this
# by 26 and then add x[i+m-1] to this value.
def modPatternMatch(q,p,x): # Overall Run Time : O(k + (n+m)logq), Auxillary Space : O(k + log(n) + log(q)) = O(k + log(n) + log(m/eps) + log(log(m/eps)))
	# which is equivalent to an overall space complexity, Auxillay Space : O(log(n) + log(m/eps))
	it = len(p)-1        # Auxillary Space : O(log(n-m)) as in further steps it goes up till n-m
	val = 1				 # Auxillary Space : O(logq)
	pattern = 0			 # Auxillary Space : O(logq)
	curr = 0			 # Auxillary Space : O(logq)
	while(it > -1): # Run Time for entire loop : O(2mlogq)
		pattern = (pattern + (((ord(p[it])-65)%q)*val)%q)%q    # Time : O(logq)
		curr = (curr + (((ord(x[it])-65)%q)*val)%q)%q		   # Time : O(logq)
		if(it == 0):
			break
		val = (val*26)%q									   # Time : O(logq)
		it -= 1
	ans = []
	prev = it - 1											   # Auxillary Space : O(log(n-m))
	it = 0
	end_it = it + len(p) - 1								   # Auxillary Space : O(log(n))
	if(curr == pattern):
		ans.append(it)
	it += 1
	prev += 1
	end_it += 1
	while(it < len(x)-len(p)+1): # Run Time for entire loop : O(k + (n-m)logq)
		curr = ((((curr-(((ord(x[prev])-65)%q)*val)%q)%q)*(26%q))%q + (ord(x[end_it])-65)%q)%q    # Time : O(logq)
		if(curr < 0):
			curr += q
		if(curr == pattern):
			ans.append(it)																			   # Time : O(1)
		# all below operations take O(1) time
		it += 1
		end_it += 1
		prev += 1
	return ans

# Return sorted list of starting indices where p matches x
# This function works just like the previous one, but, in the place of ? we treat it as 0, also in every sub-string of text x, the index
# corresponding to ? of pattern is treated as 0 while calculating f(s) for that sub-string, thus we maintain two indexes iterator and wild_index
# Thus, the total running time is O(k + (n+m)logq), and Auxillary Space : O(k + log(n) + log(q))
def modPatternMatchWildcard(q,p,x):
	wild_index = 0											#  Auxillary Space : O(log(n))
	while(wild_index< len(p)): # Run time for this loop is O(m)
		if(p[wild_index] == '?'):
			break
		wild_index += 1
	it = len(p) - 1											# Auxillary Space : O(log(n-m))
	val = 1													# Auxillary Space : O(log(q))
	pattern = 0
	curr = 0												# Auxillary Space : O(log(q))
	wild_val = 0											# Auxillary Space : O(log(q))
	while(it > -1): # This loop computes the value of the pattern and initial m length of the text, thus running in O(2mlogq)
		if(it == wild_index):
			wild_val = val
			val = (val*26)%q
			it -= 1
			continue
		pattern += (((ord(p[it])-65)%q)*val)%q				# Time Complexity : O(logq)
		pattern = (pattern)%q								# Time Complexity : O(logq)
		curr += (((ord(x[it])-65)%q)*val)%q					# Time Complexity : O(logq)
		curr = (curr)%q										# Time Complexity : O(logq)
		if(it == 0):
			break
		val = (val*26)%q
		it -= 1
	it = 0
	prev = -1
	end_it = it + len(p) - 1							    # Auxillary Space : O(logn)
	ans = []
	if(curr == pattern):
		ans.append(it)
	it += 1
	prev += 1
	end_it += 1
	wild_index += 1
	while(it < len(x)-len(p)+1): # This loop runs in O(k + (n-m)logq)
		# All the below operations run in O(logq) time.
		curr = (curr-(((ord(x[it-1])-65)%q)*val)%q)%q
		curr = (curr*(26%q))%q
		curr = (curr+(ord(x[it+len(p)-1])-65)%q)%q
		curr = (curr + ((ord(x[wild_index-1])-65)%q)*((wild_val*(26%q))%q))%q
		curr = (curr - ((ord(x[wild_index])-65)%q)*((wild_val)%q))%q
		if(curr < 0):
			curr += q
		if(curr == pattern):
			ans.append(it)									# Time complexity : O(1)
		# the below operations take O(1) time
		it += 1
		wild_index += 1
		prev += 1
		end_it += 1
	return ans

# In all the above space and complexity analysis we can replace logq by log(m/eps) as q < 1.79(2mlog(26)/eps)log(2mlog(26)/eps)
# Thus, O(logq) will get replaced by O(log(m/eps)).
# check = (curr - (((ord(x[wild_index])-65)%q)*(wild_val))%q)%q