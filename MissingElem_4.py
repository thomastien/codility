def solution(A):
    # write your code in Python 2.7
    # assume N=5 elements in array, e.g. [1,2,3,5]
    # So we'll just substract the sum of A from sum of A..N

    # If there were 3 elements, [1, 2, 3]  len would be 3
    # Unfortunately, sum(xrange(1, 4)) excludes, 4, so we actually need length + 2
    sumN = sum(xrange(1, len(A)+2))
    sumA = sum(A)
    return sumN-sumA
