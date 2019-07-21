#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'spiralOrderPrimes' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#
import math

def spiralOrderPrimes(grid):
    m = len(grid)
    n = len(grid[0])
    output = []
    res=[]
    k = 0
    l = 0
    while(k<m and l<n):
        for i in range(l, n):
            output.append(grid[k][i])
        k+=1
        for i in range(k,m):
            output.append(grid[i][n-1])
        n-=1

        if(k<m):
            for i in range(n-1, (l-1), -1):
                output.append(grid[m-1][i])
            m-=1
        if(l<n):
            for i in range(m-1, k-1, -1):
                output.append(grid[i][l])
            l+=1
    
    for i in output:
        if(is_prime(i)== True):
            res.append(i)
    return res
            
    
    
def is_prime(n): 
    if n <= 1: 
        return False
  
    max = math.floor(math.sqrt(n)) 
    for i in range(2, 1 + max): 
        if n % i == 0: 
            return False
    return True

a =[[7, 7, 3, 8, 1], [13, 5, 4, 5, 2], [9, 2, 12, 3, 9], [6, 12, 1, 11, 41]]
print(spiralOrderPrimes(a))

    

