# Name: Ashish Sadavarti
# Code: StringSplitJoin
# Code Description: Demonstrates how to split a string by spaces and then
#                   join the resulting words back together with hyphens.
# Copyright 2025

def split_and_join(line):
    """
    Splits a given string by spaces and then joins the resulting words
    back together using a hyphen (-) as a separator.

    Args:
        line (str): The input string to be processed.

    Returns:
        str: The modified string with words joined by hyphens.
    """
    # line.split():
    #   - This method splits the string 'line' by whitespace characters (spaces, tabs, newlines)
    #     by default.
    #   - If no argument is given, it also handles multiple spaces between words correctly,
    #     treating sequences of whitespace as a single delimiter and removing empty strings.
    #   - It returns a list of substrings (words).
    #   Example: "this is a string" -> ["this", "is", "a", "string"]

    # "-".join(...):
    #   - This is a string method that concatenates the elements of an iterable (like a list)
    #     into a single string.
    #   - The string on which .join() is called ("-") becomes the separator between the elements.
    #   Example: "-".join(["this", "is", "a", "string"]) -> "this-is-a-string"
    
    return "-".join(line.split())

if __name__ == '__main__':
    # Read a line of input from the user.
    line = input()
    
    # Call the split_and_join function with the input line.
    result = split_and_join(line)
    
    # Print the result.
    print(result)

    # Example:
    # If user input is:
    # This is a string
    #
    # Expected output:
    # This-is-a-string
    #
    # If user input is:
    # Hello   World
    #
    # Expected output:
    # Hello-World (due to split() handling multiple spaces)
