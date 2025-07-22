# Name: Ashish Sadavarti
# Code: Loops: Squares Generator
# Code Description: Takes an integer 'n' as input and prints the square of each non-negative integer less than 'n'.
# Copyright 2025

# This script provides a basic demonstration of a `for` loop in Python.
# It reads an integer 'n' from the user and then iterates from 0 up to (but not including) 'n'.
# In each iteration, it calculates the square of the current loop variable and prints it.

if __name__ == '__main__':
    print("--- Loops: Squares Generator ---")
    print("This program prints the square of each integer from 0 up to N-1.")

    try:
        # Read an integer 'n' from standard input.
        # This 'n' will determine the upper limit of the loop (exclusive).
        n = int(input("Enter an integer N: "))

        # Validate n
        if n < 0:
            print("Error: N must be a non-negative integer.")
            # If n is negative, the range will be empty, so no squares will be printed.
            # We can choose to exit or let the empty loop run. For clarity, let's exit.
            exit()
        
        print(f"\nSquares from 0 to {n-1}:")
        # Use a `for` loop with `range(0, n)`.
        # `range(0, n)` generates a sequence of numbers starting from 0,
        # and going up to (but not including) `n`.
        # Example: if n=3, range(0, 3) generates 0, 1, 2.
        for i in range(0, n):
            # Calculate the square of the current number 'i'.
            # `i ** 2` is equivalent to `i * i`.
            square = i ** 2
            
            # Print the calculated square.
            print(square)

    except ValueError:
        # Handle cases where the input for 'n' is not a valid integer.
        print("Invalid input. Please enter an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

