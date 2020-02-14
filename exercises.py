"""Recursion Problem Set: Coding Exercises"""

# Short-hand PEDAC.
# Note to self: Dont make this a habit

# Reverse
# 1. Functions takes a string
# 2. Put the base condition that if the length of the string is equal to 0 or 1, the string is returned.
#    You cant reverse a string with 1 or no characters. Has to be a first and last character.
# 3. Recursively call the reverse function to slice the string until its reversed.

def reverse(s: str) -> str:

    if len(s) == 0 or len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]    
    # this is Correct, but still confused on how it knows when to stop.
        


def fib_rec(n: int) -> int:
    """Recursive fibonacci"""
    

def fib_dyn(n: int) -> int:
    """Fibonacci using dynamic programming (w/ a cache)"""
    
# fib_iter
# 1. Starting from 1, add the 2 previous numbers in this sequence and return a new number. That number is the next in the sequence.
# 2. if the num is 1 or 0, just return 1 because there are no previous numbers.
# 3. Loop over each number in the sequence from 2 to whatever the argument is.
# 4. num is now a combo of the previous number and the last number, just add and then return.
# 5. last_number becomes num.
# 6. return num or last_number to get the new number in the sequence.

# add the two previous numbers continuously until 0.


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

    