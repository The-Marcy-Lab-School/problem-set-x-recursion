"""Recursion Problem Set: Coding Exercises"""

def reverse(s: str) -> str:

    if len(s) == 0 or len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]    
        
def fib_rec(n: int) -> int:
    """Recursive fibonacci"""
    if n == 1 or n == 0:
        return 1
    
    return fib_rec(n - 1) + fib_rec(n-2)

def fib_dyn(n: int) -> int:
    """Fibonacci using dynamic programming (w/ a cache)"""
    cache = {}
    
    if n == 1 or n == 0:
        return 1
    
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)
        return cache[n]

def fib_iter(n: int) -> int:
    """Iterative approach to solving the fibonacci problem"""
    
    last_number = 1
    two_before = 1
    
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        n = last_number + two_before
        two_before = last_number
        last_number = n
    
    return n

def to_str(n: int, base: int) -> int:
    """convert integer to a string of a given base"""

    convert = '0123456789ABCDEF'
    if n < base:
        return convert[n]
    else:
        return to_str(n // base, base) + convert[n % base]