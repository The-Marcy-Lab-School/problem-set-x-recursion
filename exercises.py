"""
Recursion Problem Set: Coding Exercises
"""
#Reverse String
def reverse(str):
    if len(str) == 1:
        return str
    else:
        return reverse(str[1:]) + str[0]


#Fibonacci Sequence w/ recursion
def fib_rec(n):
    if n ==0 or n ==1:
        return 1
    else:
        return fib_rec(n -1) + fib_rec(n-2)
        
  
#Fibonacci Sequence w/ cache   
cache = {}
def fib_dyn(n):
    if n == 0 or n == 1:
        return 1
    
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
        return cache[n]
        

#Fibonacci Sequence w/ iteration
def fib_iter(n):
    last = 1
    minus_2 = 1
    
    if n == 0 or n == 1:
        return 1
    
    for i in range(2, n + 1):
        n = last + minus_2
        minus_2 = last
        last = n
    
    return n

#String int to base converter
def to_str(n, base):
    conv_str = "0123456789ABCDEF"
    if n < base:
        return conv_str[n]

    else:
      return to_str(n//base, base) + conv_str[n%base]