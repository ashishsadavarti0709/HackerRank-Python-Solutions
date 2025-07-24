# Name: Ashish Sadavarti
# Code: NumberBaseFormatter
# Code Description: Takes an integer 'n' and prints numbers from 1 to 'n'
#                   in decimal, octal, hexadecimal, and binary formats,
#                   right-justified to a consistent width.
# Copyright 2025

def print_formatted(number):
    """
    Prints numbers from 1 to 'number' in decimal, octal, hexadecimal, and binary formats.
    Each number is right-justified to a width determined by the binary representation
    of the input 'number'.

    Args:
        number (int): The upper limit (inclusive) for printing numbers.
    """
    # Calculate the maximum width needed for formatting.
    # len(bin(number)): Gives the length of the binary string (e.g., '0b101' for 5 is 5 characters).
    # - 2: Subtract 2 to remove the '0b' prefix from the binary string.
    # This ensures all columns are aligned based on the width of the binary representation
    # of the largest number (the input 'number' itself).
    width = len(bin(number)) - 2

    # Loop from 1 up to and including the input 'number'.
    for i in range(1, number + 1):
        # Format the decimal representation:
        # str(i): Convert the integer 'i' to its string representation.
        # .rjust(width): Right-justifies the string within the calculated 'width'.
        #               Pads with spaces on the left if the string is shorter than 'width'.
        decimal = str(i).rjust(width)
        
        # Format the octal representation:
        # oct(i): Converts 'i' to an octal string, prefixed with '0o' (e.g., '0o5').
        # [2:]: Slices the string to remove the '0o' prefix.
        # .rjust(width): Right-justifies the octal string.
        octal = oct(i)[2:].rjust(width)
        
        # Format the hexadecimal representation:
        # hex(i): Converts 'i' to a hexadecimal string, prefixed with '0x' (e.g., '0x5').
        # [2:]: Slices the string to remove the '0x' prefix.
        # .upper(): Converts hexadecimal characters (a-f) to uppercase (A-F).
        # .rjust(width): Right-justifies the hexadecimal string.
        hexadecimal = hex(i)[2:].upper().rjust(width)
        
        # Format the binary representation:
        # bin(i): Converts 'i' to a binary string, prefixed with '0b' (e.g., '0b101').
        # [2:]: Slices the string to remove the '0b' prefix.
        # .rjust(width): Right-justifies the binary string.
        binary = bin(i)[2:].rjust(width)
        
        # Print the formatted strings, separated by a single space.
        # Using an f-string for concise and readable formatting.
        print(f"{decimal} {octal} {hexadecimal} {binary}")

if __name__ == '__main__':
    # Read the integer 'n' from user input.
    n = int(input())
    # Call the print_formatted function with the input 'n'.
    print_formatted(n)

    # Example:
    # If user input is:
    # 5
    #
    # Expected output:
    #   1   1   1   1
    #   2   2   2  10
    #   3   3   3  11
    #   4   4   4 100
    #   5   5   5 101
