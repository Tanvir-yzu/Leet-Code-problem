# Second Largest Unique Salary

This Python code is designed to find the second largest unique salary from a list of salaries. Here's a step-by-step explanation:

1. The list of salaries is defined as `sal = [50000, 50000, 67000, 35000, 70000]`.

2. The `set()` function is used to remove duplicate salaries from the list. This is because the code is looking for the second largest unique salary, not the second largest salary overall.

3. The `sorted()` function is used to sort the unique salaries in descending order. The `reverse=True` argument sorts the list in descending order.

4. The `[1]` index is used to select the second largest salary from the sorted list. In Python, list indices start at 0, so `[1]` selects the second item in the list.

5. The `ic()` function from the `icecream` library is used to print the result. The `ic()` function is a more powerful version of the `print()` function that also shows the line number and the source code that called it.

So, the output of this code will be the second largest unique salary, which is 67000.