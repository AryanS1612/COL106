def build_failure_function(P):
    """Builds the failure function for the given pattern 'P'."""
    n = len(P)              # length of pattern/text
    fail = [0]*n            # list of failure_function output for inputs as indexes
    i = 1                   # index of text  
    j = 0                   # index of pattern
    while (i < n):          #? index of text should be less than length of text
        if (P[i] == P[j]):  #? j+1 elements matched so far
            fail[i] = j+1
            i += 1
            j += 1
        elif (j > 0):       #? element at ith index didn't match
            j = fail[j-1]
        else:               #? if first element of pattern doesn't match with ith element of text
            i += 1
    return fail

def test_build_failure_function():                #? build_failure_function testing module
    print(build_failure_function("aba"))
    print(build_failure_function("amalgamation"))
    print(build_failure_function("ababababababa"))
    print(build_failure_function("aaaaaaaaaaaaaaa"))
    print(build_failure_function(""))

def KMP_probing(P, T):
    """Returns all the occurrences of pattern 'P' in the given text 'T'."""
    
    n = len(T)                                      # length of text
    m = len(P)                                      # length of pattern
    if (m == 0):                                        #? if no pattern return empty list
        return []
    else:                                               #? else -> find pattern
        occurences = []                                 # list of indexes of occurences
        failure_function = build_failure_function(P)    # failure_function for P
        i = 0                                           # index of text
        j = 0                                           # index of pattern
        while (i < n):                                  #? index of text should be less than the length of text
            if (T[i] == P[j]):                          #? j+1 elements matched so far
                if (j == m-1):                          #? complete pattern was found
                    occurences.append(i-j)
                    i += 1
                    j = 0
                else:                                   #? partial pattern is found so far -> continue matching
                    i += 1
                    j += 1
            elif (j > 0):                               #? partial pattern was matched , we need to shift by the failure function
                j = failure_function[j-1]
            else:                                       #? no elements matched -> continue search
                i += 1
        return occurences

def test_KMP_probing():                             #? KMP_probing testing module
    print(KMP_probing("ama", "amalgamation"))
    print(KMP_probing("ab","abdababdsabababab"))
    print(KMP_probing("a", "aaaaaaaaa"))
    print(KMP_probing("adfs","asd"))
    print(KMP_probing("", "asdg"))
    
    

if (__name__ == "__main__"):                    #? test all the functions here
    # test_build_failure_function()
    test_KMP_probing()