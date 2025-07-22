# Name: Ashish Sadavarti
# Code: Print Function: Concatenated Numbers
# Code Description: Takes an integer 'n' as input and prints the numbers from 1 to 'n'
#                   concatenated together without spaces, on a single line.
# Copyright 2025

# This script demonstrates a specific feature of Python's `print()` function:
# the `end` argument. By default, `print()` adds a newline character (`\n`)
# at the end of its output. By setting `end=""`, we can prevent this default
# behavior and make subsequent `print()` calls output on the same line.

if __name__ == '__main__':
    print("--- Print Function: Concatenated Numbers ---")
    print("This program prints numbers from 1 to N concatenated on one line.")

    try:
        # Read an integer 'n' from standard input.
        # This 'n' will determine the upper limit of the numbers to print (inclusive).
        n = int(input("Enter an integer N: "))

        # Validate n
        if n <= 0:
            print("Error: N must be a positive integer.")
            # If n is not positive, the range will be empty, or we want a specific behavior.
            # For this problem, usually an empty line or no output is expected for non-positive N.
            # print("") # Print an empty line if N is not positive, if that's desired behavior.
            exit()
        
        print(f"\nNumbers from 1 to {n} concatenated:")
        # Use a `for` loop with `range(1, n + 1)`.
        # `range(1, n + 1)` generates a sequence of numbers starting from 1,
        # and going up to (and including) `n`.
        # Example: if n=3, range(1, 4) generates 1, 2, 3.
        for i in range(1, n + 1):
            # Print the current number 'i'.
            # `end=""`: This argument tells the `print()` function to use an empty string
            # as the ending character, instead of the default newline.
            # This makes subsequent `print()` calls continue on the same line.
            print(i, end="")
        
        # After the loop finishes, print a final newline character
        # to ensure the next prompt or output starts on a fresh line.
        print() 

    except ValueError:
        # Handle cases where the input for 'n' is not a valid integer.
        print("Invalid input. Please enter an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

