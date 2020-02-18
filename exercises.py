from typing import Dict

"""
Recursion Problem Set: Coding Exercises
"""

def reverse(s: str) -> str:
	if len(s) == 1:
		return s
	else:
		return reverse(s[1:]) + reverse(s[0])

def fib_rec(n: int) -> int:
	if n < 2:
		return n
	else:
		return fib_rec(n - 2) + fib_rec(n - 1)

def fib_dyn(n: int) -> int:
	cache: Dict[int, int] = {0: 0, 1: 1}
	if n not in cache:
		cache[n] = fib_dyn(n - 2) + fib_dyn(n - 1)
	return cache[n]

def fib_iter(n: int) -> int:
	if n < 2: return n
	two_before: int = 0
	one_before: int = 1
	for _ in range(1, n):
		n = one_before + two_before
		two_before = one_before
		one_before = n
	return n

def to_str(n: int, base: int) -> str:
	conversion_chars: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if n < base:
		return conversion_chars[n]
	else:
		return to_str(n // base, base) + conversion_chars[n % base]
