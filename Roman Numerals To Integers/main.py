from icecream import ic

def romanToInt(s: str) -> int:
    # Dictionary mapping Roman numerals to their integer values
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Initialize the result and previous value
    result = 0
    prev_value = 0

    # Iterate through the string in reverse order
    for char in s[::-1]:
        # Get the integer value of the current Roman numeral
        value = roman_values[char]

        # If the current value is less than the previous value, subtract it
        if value < prev_value:
            result -= value
        # Otherwise, add it to the result
        else:
            result += value

        # Update the previous value for the next iteration
        prev_value = value

    # Return the final result
    return result


# Test cases
ic(romanToInt("III"))  # Output: 3
ic(romanToInt("LVIII"))  # Output: 58
ic(romanToInt("MCMXCIV"))  # Output: 1994
