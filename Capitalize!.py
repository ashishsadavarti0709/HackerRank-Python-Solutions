# Name: Ashish Sadavarti
# Code: Capitalize Words in a String
# Code Description: Takes a string as input and capitalizes the first letter of each word in it.
#                   Handles multiple spaces and empty words correctly.
# Copyright 2025

# This script defines a function `solve` that capitalizes the first letter of each word
# in an input string. It's designed to correctly handle scenarios with multiple spaces
# between words or leading/trailing spaces.

import math   # Not used in this specific code, but often included in HackerRank templates.
import os     # Used for file path manipulation (e.g., setting output path).
import random # Not used in this specific code.
import re     # Not used in this specific code.
import sys    # Not used in this specific code directly, but implicit for input/output.

def solve(s):
    """
    Capitalizes the first letter of each word in the input string 's'.

    This function splits the string by spaces, capitalizes each resulting word,
    and then joins them back with a single space. It intelligently handles
    empty strings (resulting from multiple spaces) by keeping them as is,
    which preserves the original spacing structure when re-joined.

    Parameters:
    s (str): The input string to be processed.

    Returns:
    str: The string with the first letter of each word capitalized.

    Example:
    >>> solve("hello world")
    "Hello World"
    >>> solve("this is a test")
    "This Is A Test"
    >>> solve("  leading and trailing spaces  ")
    "  Leading And Trailing Spaces  "
    >>> solve("multiple   spaces")
    "Multiple   Spaces"
    """
    # Split the input string 's' by spaces. This will create a list of words.
    # If there are multiple spaces, split() will create empty strings in the list.
    # Example: "hello   world".split(' ') -> ['hello', '', '', 'world']
    words = s.split(' ')

    # Use a generator expression to process each word:
    # word.capitalize() will capitalize the first letter of a word (e.g., "hello" -> "Hello").
    # If a word is an empty string (from multiple spaces), `if word else word`
    # ensures it remains an empty string, which is crucial for preserving original spacing.
    # ' '.join(...) then joins these processed words back together with a single space.
    # Note: This method effectively preserves the original spacing, as ' '.join
    # will put a space between *every* element of the list, including empty strings.
    # For instance, ['Hello', '', '', 'World'] joined by ' ' will become "Hello   World".
    capitalized_string = ' '.join(word.capitalize() if word else word for word in words)

    return capitalized_string

if __name__ == '__main__':
    # This block is typically used in competitive programming environments
    # to handle input/output redirection.
    # 'os.environ['OUTPUT_PATH']' usually points to a file where the output should be written.

    # Open the output file in write mode.
    # It's good practice to use try-finally or 'with' statement for file handling.
    # For a local run, you might replace this with a direct print to console.
    
    # In a typical local execution, you might just do:
    # s = input("Enter a string to capitalize: ")
    # result = solve(s)
    # print(result)

    # Simulating HackerRank environment for completeness:
    try:
        # Create a dummy output file for local testing if OUTPUT_PATH is not set
        # In a real HackerRank environment, os.environ['OUTPUT_PATH'] would be defined.
        output_path = os.environ.get('OUTPUT_PATH', 'output.txt')
        
        with open(output_path, 'w') as fptr:
            # Read the input string from stdin.
            s = input("Enter a string to capitalize: ")

            # Call the solve function with the input string.
            result = solve(s)

            # Write the result to the output file, followed by a newline character.
            fptr.write(result + '\n')
            
        print(f"Result written to {output_path}") # Inform user about output location
        # Optionally, print to console for immediate feedback during local testing
        print(f"Console Output: {result}")

    except KeyError:
        print("OUTPUT_PATH environment variable not set. Running in console mode.")
        s = input("Enter a string to capitalize: ")
        result = solve(s)
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

