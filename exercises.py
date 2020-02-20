"""
Recursion Problem Set: Coding Exercises
"""

def reverse(s: str) -> str:
    if len(s) <= 1:
	    return s
	else:
	    return reverse(s[1:])  + s[0]

def fib_rec(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

cache = {}
def fib_dyn(n: int) -> int:
     if n == 0 or n == 1:
        return 1
    if n in cache:
        return cache[n]
    else:
        cache[num] = fib_dyn(n - 1) + fib_dyn(n - 2) 
        return cache[num]


def fib_iter(n: int) -> int:
    last = 1
    two_before = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        n = last + two_before
        two_before = last
        last = n
    return n

def to_str(n: int, base: int) -> int:
     if num <= base:
        return str(num)
    else:
        next_num = num // base
        value = num % base
        # str(value)
        return to_str(next_num, base) + str(value)
