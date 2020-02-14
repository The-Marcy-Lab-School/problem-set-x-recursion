"""
Recursion Problem Set: Coding Exercises
"""

def reverse(s: str) -> str:
#Reverse string using recursive approach

# Short-hand PEDAC.
# Note to self: Dont make this a habit


# 1. Functions takes a string

# 2. Put the base condition that if the length of the string is equal to 0 or 1, the string is returned.
#    You cant reverse a string with 1 or no characters. Has to be a first and last character.

# 3. Recursively call the reverse function to slice the part of the string except the first character 
and concatenate the first character to the end of the sliced string.
5. Print the reversed string.
6. Exit.

if len(string) == 0:
        return string
    else:
        pass        
        

def fib_rec(n: int) -> int:
    """
    Recursive fibonacci
    """

def fib_dyn(n: int) -> int:
    """
    Fibonacci using dynamic programming (w/ a cache)
    """

def fib_iter(n: int) -> int:
    """
    Iterative approach to solving the fibonacci problem
    """

def to_str(n: int, base: int) -> int:
    """
    convert integer to a string of a given base
    """
