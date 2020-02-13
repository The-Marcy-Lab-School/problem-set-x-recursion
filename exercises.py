"""
Recursion Problem Set: Coding Exercises
"""
from functools import lru_cache

def reverse(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:])  + s[0]

def fib_rec(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 1)
    
    
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
    last_number = 1
    two_before = 1
    if n == 1 or n == 0:
        return 1
    
    for i in range(2,n + 1):
        n = last_number + two_before
        two_before = last_number
        last_number = n 
    return n

def to_str(n: int, base: int) -> int:
    #Base Case
    pass