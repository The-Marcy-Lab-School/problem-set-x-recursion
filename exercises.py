"""
Recursion Problem Set: Coding Exercises
"""

def reverse(string):
    if  len(string) == 1:
        return string
    else:
        return reverse(string[1:]) + string[0]
        
def fib_rec(num: int) -> int:
    if num == 0 or num == 1 or num == 2:
        return 1
    else:
        return fib_rec(num - 2) + fib_rec(num - 1)


def fib_dyn(n: int) -> int:
    pass

def fib_iter(num: int) -> int:
    first = 0
    second = 1
    
    for i in range(num):
        nth = first + second
        first = second
        second = nth
    return first

def to_str(num: int, base: int) -> int:
    convert = "0123456789ABCDEF"
    if num < base:
        return convert[num]
    else:
        return to_str(num//base, base) + convert[num%base]
