# Find the element that has the odd number of occurrences in an array
# Can assume there is always only one element that appears an odd # of times
# https://codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

# This version is a working solution, but fails the performance test

def solution(A):
    # write your code in Python 2.7
    A.sort()
    last = ''
    for elem in A:
        if last <> elem:
            numtimes = A.count(elem)
            if numtimes%2 == 1:
                return elem
            else:
                last = elem
    
    pass
    
