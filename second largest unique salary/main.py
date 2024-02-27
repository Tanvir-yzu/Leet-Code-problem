from icecream import ic 

# Define a list of salaries
sal = [50000, 50000, 67000, 35000, 70000]

# Use set to remove duplicates, then sort the unique salaries in descending order
unique_salaries = sorted(set(sal), reverse=True)

# The second element in the sorted unique salaries list is the second largest unique salary
second_largest_salary = unique_salaries[1]

# Print the second largest unique salary
ic(second_largest_salary)  # Output will be 67000
