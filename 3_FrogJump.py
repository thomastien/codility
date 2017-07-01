# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from __future__ import division

def solution(X, Y, D):
    # X = starting position
    # Y = destination
    # D = size of a jump
    
    #X = 10
    #Y = 101
    #D = 30
 
    distance = Y-X
    jumps = distance/D * 1.0
    
    if float(jumps) == int(jumps):
        return int(jumps)
    else:
        return int(jumps) + 1
    
