# Problem Set 11.4 - Recursion

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
**1. What is recursion?**

Recursion is essentially the process through which something is done over and over. An example of this is recursive functions that actually invoke themselves within themselves with the output of the previous iteration.

**2. What type of problems are best solved using recursion?**

the problems best solved with recursion are ones that need to be completed over multiple iterations but lose the advantage of readability when formatted into a loop.

**3. What are the benefits of writing functions recursively? What are the drawbacks?**

One of the benefits of using recursive functions is readability, it allows a programmer to write code that can be read intuitively rather than a loop that is less transparent in is operations. One of the drawbacks however is that with each nested invocation of a recursive function, a function is added to the call stack, which for functions with larger inputs/outputs would be disadvantgeous.
    
### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. **_Reverse a String:_** This interview question requires you to reverse a string using recursion. Make sure to think of the base case here and make sure you use recursion to accomplish this! Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

2. **_Fibonnaci Sequence:_** Implement a Fibonnaci Sequence in three different ways - Recursively, Dynamically (Using Memoization to store results), and Iteratively. Remember the fibonacci sequence: `0,1,1,2,3,5,8,13,21,...`

3. **_Integer to String:_** Write a recursive function that takes two parameters - an integer input, `n`, and an integer base, `m` - and returns a string represenation of the number in Base `m`.
