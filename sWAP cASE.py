# Name: Ashish Sadavarti
# Code: StringCaseSwapper
# Code Description: Demonstrates the use of the string.swapcase() method to
#                   convert all uppercase letters to lowercase and vice versa
#                   in an input string.
# Copyright 2025

def swap_case(s):
    """
    Converts all uppercase characters in a string to lowercase and
    all lowercase characters to uppercase. Non-alphabetic characters
    remain unchanged.

    Args:
        s (str): The input string to be processed.

    Returns:
        str: The string with the case of its alphabetic characters swapped.
    """
    # s.swapcase():
    #   - This is a built-in string method in Python.
    #   - It creates and returns a new string where:
    #     - All uppercase letters are converted to their lowercase equivalents.
    #     - All lowercase letters are converted to their uppercase equivalents.
    #     - Any other characters (digits, symbols, spaces, etc.) are left as they are.
    #   - It does not modify the original string 's' (strings are immutable in Python).
    return s.swapcase()

if __name__ == '__main__':
    # Read the input string from the user.
    # Example Input: "HackerRank.com presents 'Pythonist 2'."
    s = input()
    
    # Call the swap_case function with the input string.
    result = swap_case(s)
    
    # Print the resulting string with swapped cases.
    print(result)

    # Example Output for "HackerRank.com presents 'Pythonist 2'.":
    # hACKERrANK.COM PRESENTS 'pYTHONIST 2'.
