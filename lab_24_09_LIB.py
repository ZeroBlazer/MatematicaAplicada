from numpy import *

def leeeA(n) :
        A = (-1) * ones((n,n))
        for k in range (1, n+1) :
                A[k-1][k-1] = k
        print(A)
