#!/usr/bin/python


#A = [1, 2, 3, 4, 5]
#A = []

def Solution(A, K):
    for i in range(K):
        try:
            z = A.pop()
            A.insert(0,z)
        except: 
            pass
    return A

cycled = Solution(A, 3)
print cycled
