def KMP_string_matcher(T,P):
    n = len(T)
    m = len(P)
    # fail_func = failure_function(P)
    fail_func = [-1,0,1]
    i = 0
    q = 0
    while(i < n):
        if(P[q] == T[i]):
            q += 1
            i += 1
        else:
            if(q == 0):
                i += 1
            else:
                while(P[q] != T[i]) and (q > 0):
                    q = fail_func[q-1] + 1
                if(P[q] == T[i]):
                    q += 1
                    i += 1
                else:
                    i += 1
        if(q == m):
            print("Pattern Occurs at",i-m)
            q = fail_func[q-1] + 1

def failure_function(P):
    

P = input()
T = input()
KMP_string_matcher(T, P)