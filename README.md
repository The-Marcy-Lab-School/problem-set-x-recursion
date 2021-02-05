# Problem Set: Recursion

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

Complete code challenges in `exercises.js` or `exercises.py`. 

Use Test Driven Development to guide you. For JavaScript, run `npm install` to download dependencies. Run `npm test` to run tests locally. For Python, run `pytest`. Ensure all tests are passing before submitting this problem set.

### Short Response Questions

**1. What is recursion?**

**2. What type of problems are best solved using recursion?**

**3. What are the benefits of writing functions recursively? What are the drawbacks?**

### Coding Exercises

1. **_Reverse a String:_** This interview question requires you to reverse a string using recursion. Make sure to think of the base case here and make sure you use recursion to accomplish this! Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

2. **_Fibonnaci Sequence:_** Implement a Fibonnaci Sequence in two different ways - Iteratively and Recursively. Remember the fibonacci sequence: `0,1,1,2,3,5,8,13,21,...`. Your function should take in a number `n` and return the `nth` number in the Fibonnaci Sequence. For example, `fib(0) = 0`, `fib(1) = 1`, `fib(2) = 1`, `fib(3) = 2`, `fib(4) = 3`, `fib(5) = 5`, `fib(6) = 8`, `fib(7) = 13`, and so on. 

3. **_Integer to String:_** Write a recursive function that takes two parameters - an integer input, `n`, and an integer base, `m` - and returns a string represenation of the number in Base `m`.
