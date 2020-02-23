# Problem Set 11.4 - Recursion

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
**1. What is recursion?**
Recrsion is an algorithm in which it calls it self in order to break down into a smaller poblem for it to be solved in an elegant and readable way
**2. What type of problems are best solved using recursion?**
The best type of problem  to solve with recursion are those that have a repeating solution

**3. What are the benefits of writing functions recursively? What are the drawbacks?**
The benefits of using recursive functions is that they are more "elegant" in the sense that they are clearly readable and that 
### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. **_Reverse a String:_** This interview question requires you to reverse a string using recursion. Make sure to think of the base case here and make sure you use recursion to accomplish this! Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

2. **_Fibonnaci Sequence:_** Implement a Fibonnaci Sequence in three different ways - Recursively, Dynamically (Using Memoization to store results), and Iteratively. Remember the fibonacci sequence: `0,1,1,2,3,5,8,13,21,...`

3. **_Integer to String:_** Write a recursive function that takes two parameters - an integer input, `n`, and an integer base, `m` - and returns a string represenation of the number in Base `m`.
