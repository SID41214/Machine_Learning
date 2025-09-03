## Exercise: Python Exception Handling

1. Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding letter grade:

```
90–100 → A  
80–89  → B  
70–79  → C  
60–69  → D  
<60    → F
```

2. Your program should handle the following exceptions:
   - If the user enters a non-numeric value, catch the `ValueError` and display a user-friendly message.
   - If the user enters a number outside the valid range (0 to 100), raise a `ValueError` yourself with a custom message.

3. Use the `try–except–else–finally` structure:
   - `try`: Attempt to parse the input and compute the letter grade.
   - `except`: Handle conversion errors and invalid ranges.
   - `else`: Print the final grade if everything was successful.
   - `finally`: Print a goodbye message like `"Thank you for using the Grade Calculator. Goodbye!"` no matter what.

[Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/15_exception_handling/exception_handling_solution.py)
