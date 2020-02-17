"""
Recursion Problem Set: Coding Exercises
"""

def reverse(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def fib_rec(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

cache = {}
def fib_dyn(n: int) -> int:
    if n == 0 or n == 1:
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)
        return cache[n]

def fib_iter(n: int) -> int:
    first = 0
    second = 1

    for _ in range(n):
        third = first + second
        first = second
        second = third
    return first

def to_str(n: int, base: int) -> int:
    rem = n % base

    if n <= 1:
        return str(n)
    else:
        return str(to_str(n//base, base)) + str(rem)