#print first n natural numbers

def printN(n): 
    if n>0:
        printN(n-1)
        print(n,end=' ')
def revPrintN(n): 
    if n>0:
        print(n,end=' ')
        revPrintN(n-1)
def printNOdd(n): 
    if n>0:
        printNOdd(n-1)
        print(2*n-1,end=' ')

def printNEven(n): 
    if n>0:
        printNOdd(n-1)
        print(2*n,end=' ')
def revprintNOdd(n): 
    if n>0:
        print(2*n-1,end=' ')
        printNOdd(n-1)
        

def revprintNEven(n): 
    if n>0:
        print(2*n,end=' ')
        printNOdd(n-1)
        


printN(5)
revPrintN(6)
printNOdd(7)
printNEven(8)