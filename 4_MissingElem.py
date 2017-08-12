from collections import Counter

def solution(A):
    Z = Counter(A)
    # write your code in Python 2.7
    for i in xrange(1,100000):
        if Z[i] == 0:
            return i

    return 100001
    pass

