# Problem Set 11.4 - Recursion

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
**1. What is recursion?**
- Recursion is when a function calls itself to perform a task. It requires 2 things, however: one being a base case, which prevents the recursion from making an infinite loop, and one being a way to shorten the problem into smaller bits, so that it can actually reach the base case.

**2. What type of problems are best solved using recursion?**
- Problems that require you to iterate or loop through a lot of information are the best cases for using recursion. For example, you can use recursion for finding factorials, as you need to progressively go down the chain of factorials until you reach a base case, then multiply each product to get one singular product.

**3. What are the benefits of writing functions recursively? What are the drawbacks?**
- Recursions can make your code readable, and elegant, especially if you're going to be looping or iterating through too much information at once. However, it takes up a lot of space, so sometimes looping or iterating through a problem can be more beneficial. Use recursion if you're willing to spare space, use loops if you can't risk losing anymore space.

### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. **_Reverse a String:_** This interview question requires you to reverse a string using recursion. Make sure to think of the base case here and make sure you use recursion to accomplish this! Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

2. **_Fibonnaci Sequence:_** Implement a Fibonnaci Sequence in three different ways - Recursively, Dynamically (Using Memoization to store results), and Iteratively. Remember the fibonacci sequence: `0,1,1,2,3,5,8,13,21,...`

3. **_Integer to String:_** Write a recursive function that takes two parameters - an integer input, `n`, and an integer base, `m` - and returns a string represenation of the number in Base `m`.
