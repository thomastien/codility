#!/usr/bin/python


# should return 1
testsetA = [1,1,2,4,-1]

# should return 12, NOT 10
testsetB = [1,-11]


def solution(A):
    # write your code in Python 2.7
    #total = sum(A)
    
    #A = [1,1,2, 4, -1]
    total = sum(A)
    counter = 0
    minimum = 0
    subsum1 = 0
    
    for i in xrange(0,len(A)-1):
        subsum1 = subsum1+A[i]
        subsum2 = total-subsum1
        difference = abs(subsum2 - subsum1)
        if counter ==0 or difference < minimum:
            minimum = difference
        counter = counter + 1
        #print i, subsum1, subsum2
    return minimum

print solution(testsetA)
print solution(testsetB)
