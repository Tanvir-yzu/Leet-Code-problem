from icecream import ic  # Importing the ic function from the icecream module


def longest_common_prefix(
    strs,
):  # Defining a function that takes a list of strings as input
    if not strs:  # If the list is empty, return an empty string
        return ""

    # Find the length of the shortest string
    min_length = min(
        len(s) for s in strs
    )  # Using a generator expression to find the length of the shortest string

    # Binary search
    low, high = 0, min_length  # Setting the low and high bounds for the binary search
    while low < high:  # While the low bound is less than the high bound
        mid = (low + high + 1) // 2  # Calculate the midpoint
        if is_common_prefix(strs, mid):  # If the current midpoint is a common prefix
            low = mid  # Update the low bound
        else:  # If the current midpoint is not a common prefix
            high = mid - 1  # Update the high bound

    return strs[0][:low]  # Return the longest common prefix


def is_common_prefix(
    strs, length
):  # Defining a function that checks if a given length is a common prefix
    prefix = strs[0][
        :length
    ]  # Get the prefix of the first string up to the given length
    return all(
        string.startswith(prefix) for string in strs
    )  # Return True if all strings start with the prefix, False otherwise


# Test cases
strs1 = ["flower", "flow", "flight"]  # Define a list of strings
ic(
    longest_common_prefix(strs1)
)  # Call the longest_common_prefix function with the list of strings and print the result

strs2 = ["dog", "racecar", "car"]  # Define another list of strings
ic(
    longest_common_prefix(strs2)
)  # Call the longest_common_prefix function with the second list of strings and print the result
