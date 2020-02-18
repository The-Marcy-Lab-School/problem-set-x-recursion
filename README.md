# Problem Set 11.4 - Recursion

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
**1. What is recursion?**
	- Recursion is a method of solving problems by having a function invoke itself to find the solution of increasinly trivial and smaller versions of the same problem, building up to the solution. Recursion can also happen when data structures use instances of themselves when defined.

**2. What type of problems are best solved using recursion?**
	- Recursion is best fit for problems when the repitition of tasks is needed but iterative loops are not ideal. These problems are easily represented in terms of smaller or simpler instances of the same problem.

**3. What are the benefits of writing functions recursively? What are the drawbacks?**
	- For the right problem, recursion offers an intuitive and readable solution. The benefits of recursion, however, come at the cost of memory and efficiency. Each function call, of which a recursive program might make many of, is added to the call stack, a data structure limited in size. Memoization, a technique in which the result of previous function calls are saved, also requires more space.

### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. **_Reverse a String:_** This interview question requires you to reverse a string using recursion. Make sure to think of the base case here and make sure you use recursion to accomplish this! Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

2. **_Fibonnaci Sequence:_** Implement a Fibonnaci Sequence in three different ways - Recursively, Dynamically (Using Memoization to store results), and Iteratively. Remember the fibonacci sequence: `0,1,1,2,3,5,8,13,21,...`

3. **_Integer to String:_** Write a recursive function that takes two parameters - an integer input, `n`, and an integer base, `m` - and returns a string represenation of the number in Base `m`.
