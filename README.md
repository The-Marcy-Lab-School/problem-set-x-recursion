# Problem Set 11.4 - Recursion

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
**1. What is recursion?**
Answer: Recursion is a method or process of breaking down problems into smaller and smaller subproblems. You continue to do this until it gets small enough that it can be solved with ease. 

**2. What type of problems are best solved using recursion?**
Answer: The type of problems that are best solved using recursion are problems where you are repeating steps until you find what you are looking for.

**3. What are the benefits of writing functions recursively? What are the drawbacks?**
Answer: The benefit of writing functions recursively is that they  allow us to write elegant solutions to problems that may be very difficult to program. One drawback of writing recursive functions is that if you do not state a base case, you can cause an infinite loop on your cpu that will eventullay make your computer crash if you do not kill the script.


### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.

1. **_Reverse a String:_** This interview question requires you to reverse a string using recursion. Make sure to think of the base case here and make sure you use recursion to accomplish this! Do not slice (e.g. string[::-1]) or use iteration, there must be a recursive call for the function.

2. **_Fibonnaci Sequence:_** Implement a Fibonnaci Sequence in three different ways - Recursively, Dynamically (Using Memoization to store results), and Iteratively. Remember the fibonacci sequence: `0,1,1,2,3,5,8,13,21,...`

3. **_Integer to String:_** Write a recursive function that takes two parameters - an integer input, `n`, and an integer base, `m` - and returns a string represenation of the number in Base `m`.
