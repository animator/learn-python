# Recursion

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iter(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
    
A1= factorial_iter(5)
A2=factorial_recursive(5)
print(A1)
print(A2)