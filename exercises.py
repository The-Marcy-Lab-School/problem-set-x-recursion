"""
Recursion Problem Set: Coding Exercises
"""

def reverse(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def fib_rec(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

cache = {}
def fib_dyn(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)
        return cache[n]

def fib_iter(n: int) -> int:
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(1,n): 
            c = a + b 
            a = b 
            b = c 
        return b 

def to_str(n: int, base: int) -> int:
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return to_str(n//base,base) + convertString[n%base]
