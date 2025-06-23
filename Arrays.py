# Name: Ashish Sadavarti
# Code: array_reverse.py
# Code Description: This function converts input elements into a NumPy array of floats
#                   and returns the reversed array. Designed for HackerRank-style challenges.
# Copyright 2025

# This script defines a function that takes an input (either a list of numbers
# or a space-separated string of numbers), converts it into a NumPy array of
# floating-point numbers, and then returns that array in reverse order.
# It's particularly useful for problems where input needs to be processed
# as a float array and then reversed.

import numpy as np # Import the NumPy library, commonly aliased as 'np'

def arrays(arr):
    """
    Convert input to a NumPy float array and return its reversed version.

    This function is designed to be flexible, accepting either a list of numerical
    elements or a string of space-separated numbers. It ensures the resulting
    array contains float-type elements and is returned in reverse order.

    Parameters:
    arr : list or str
        Input elements to be converted to an array.
        If a string, it should contain numbers separated by spaces (e.g., "1 2 3 4").
        If a list, it should contain numerical values (e.g., [1, 2, 3]).

    Returns:
    numpy.ndarray
        A new NumPy array with float elements, which is the reversed version
        of the input elements.

    Example:
    >>> arrays([1, 2, 3])
    array([3., 2., 1.])
    >>> arrays("1 2 3 4")
    array([4., 3., 2., 1.])
    """
    # Check if the input 'arr' is a string.
    # If it is, it's assumed to be space-separated numbers.
    if isinstance(arr, str):
        # strip() removes leading/trailing whitespace.
        # split() divides the string into a list of substrings based on spaces.
        arr = arr.strip().split()
    
    # Create a NumPy array from the processed 'arr'.
    # dtype=float ensures that all elements in the array are stored as floating-point numbers.
    # [::-1] is a Python slice notation that creates a reversed copy of the array.
    return np.array(arr, dtype=float)[::-1]

if __name__ == '__main__':
    # This block demonstrates how the 'arrays' function can be used
    # with different types of input and handles user input from the console.

    print("--- Demonstration of 'arrays' function ---")

    # Example 1: Input as a Python list
    print("\nExample 1 - List input:")
    my_list_input = [10, 20, 30, 40]
    print(f"Original list: {my_list_input}")
    print(f"Reversed NumPy array (float): {arrays(my_list_input)}")
    
    # Example 2: Input as a space-separated string
    print("\nExample 2 - Space-separated string input:")
    my_string_input = "5 10 15 20 25"
    print(f"Original string: '{my_string_input}'")
    print(f"Reversed NumPy array (float): {arrays(my_string_input)}")
    
    # Example 3: Simulating command-line user input
    # This allows the user to directly type numbers separated by spaces.
    print("\nExample 3 - User input from console:")
    try:
        user_input_str = input("Enter numbers separated by spaces (e.g., '1.1 2.2 3.3'): ")
        # Call the 'arrays' function with the user's string input.
        reversed_array = arrays(user_input_str)
        print("Reversed array from your input:", reversed_array)
    except ValueError:
        # Catch errors if the input string contains non-numeric values
        print("Invalid input. Please enter numbers separated by spaces.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

