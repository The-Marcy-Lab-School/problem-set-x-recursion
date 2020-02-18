"""
Recursion Problem Set: Coding Exercises
"""

def reverse(s: str) -> str:
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

def fib_rec(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n-2)


def memoize(f):
    cache = {}
    def helper(num):
        if num not in cache:            
            cache[num] = f(num)
        return cache[num]
    return helper
    

def fib_dyn(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fib_rec(n - 1) + fib_rec(n-2)

fib_dyn = memoize(fib_dyn)

def fib_iter(n: int) -> int:
   old = 0
   new = 1
   count = 0
   while count < n:
       old_new = new 
       new = old + new
       old = old_new
       count += 1
   return new
       

"""
Below is an MVP, should be refactored to be recursive soon
"""
def to_str(n: int, base: int) -> int:
    new_int = ""
    
    if base == 10:
        return str(n)
        
    while n > 1:
        new_int = str(int(n % base)) + new_int
        n = n/base
    return new_int
    
