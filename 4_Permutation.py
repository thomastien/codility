from collections import Counter
    
def solution(A):
    #A=[1,2,3,4,2]
    # write your code in Python 2.7
    Z = Counter(A)
    highest = max(A)
    for i in xrange(1,highest+1):
        #print i, "appears", Z[i], "times"
        if Z[i] <> 1:
            return 0
    
    return 1
