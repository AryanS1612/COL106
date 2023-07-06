# We aim at wrtiting a program for string matching using discrete finite automaton(DFA), here Sigma will be considered to be the set of
# lower_case alphabets. 
def DFA_match(delta,T,final_state):   # here delta is a 2-D array, delta[q][a] gives the next transition, delta is a mapping from (Sigam*Q)
    # to Q.
    i = 1
    q = 0
    for each in T:
        q = delta[q][each]
        if(q == final_state):
            print("Pattern occours at",i-final_state)
        i += 1


def delta_construct()