def sumN(n):
    if n==0:
        return 1
    return n+sumN(n-1)
def sumNOdd(n):
    if n==1: 
        return 1
    return 2*n-1+sumNOdd(n-1)
def sumNEven(n):
    if n==1: 
        return 1
    return 2*n+sumNOdd(n-1)
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
def sumNsquare(n):
    if n==0:
        return 1
    return n*n+sumN(n-1)