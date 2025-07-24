# Name: Ashish Sadavarti
# Code: FullNameGreeter
# Code Description: Takes a first name and a last name as input and prints a
#                   greeting message incorporating the full name.
# Copyright 2025

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#   1. STRING first
#   2. STRING last
#

def print_full_name(first, last):
    """
    Constructs and prints a greeting message using a first and last name.

    Args:
        first (str): The first name.
        last (str): The last name.
    """
    # Create the full greeting message using an f-string.
    # F-strings provide a concise and readable way to embed expressions inside string literals.
    # {first} and {last} are replaced by the values of the 'first' and 'last' variables.
    full_name = f"Hello {first} {last}! You just delved into python."
    
    # Print the constructed full name message to the console.
    print(full_name)

if __name__ == '__main__':
    # Read the first name from user input.
    first_name = input()
    
    # Read the last name from user input.
    last_name = input()
    
    # Call the print_full_name function with the obtained first and last names.
    print_full_name(first_name, last_name)

    # Example:
    # If input for first_name is "Guido"
    # If input for last_name is "van Rossum"
    #
    # Expected output:
    # Hello Guido van Rossum! You just delved into python.
