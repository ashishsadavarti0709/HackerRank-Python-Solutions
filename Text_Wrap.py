# Name: Ashish Sadavarti
# Code: TextWrapper
# Code Description: Demonstrates how to wrap a long string into multiple lines,
#                   with each line having a maximum specified width, using
#                   Python's built-in 'textwrap' module.
# Copyright 2025

import textwrap

def wrap(string, max_width):
    """
    Wraps a given input string into multiple lines, where each line
    does not exceed the specified maximum width.

    Args:
        string (str): The input string to be wrapped.
        max_width (int): The maximum number of characters allowed per line.

    Returns:
        str: The wrapped string, with lines separated by newline characters ('\n').
    """
    # textwrap.fill(text, width):
    #   - This function from the 'textwrap' module wraps the input 'text'
    #     into paragraphs, each line no longer than 'width' characters.
    #   - It returns a single string containing the wrapped text, with
    #     newline characters ('\n') inserted where lines are broken.
    #   - It intelligently breaks lines at word boundaries if possible.
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    # Read the input string from the user.
    # Example Input: "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    string = input()
    
    # Read the maximum width for each line from the user, converting it to an integer.
    # Example Input: 4
    max_width = int(input())
    
    # Call the wrap function with the input string and maximum width.
    result = wrap(string, max_width)
    
    # Print the wrapped string.
    print(result)

    # Example Output for string="ABCDEFGHIJKLIMNOQRSTUVWXYZ", max_width=4:
    # ABCD
    # EFGH
    # IJkl
    # IMNO
    # QRST
    # UVWX
    # YZ
