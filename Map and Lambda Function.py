# Name: Ashish Sadavarti
# Code: Map & Lambda Function: Fibonacci Cubes
# Code Description: Generates a Fibonacci sequence up to 'n' terms and then uses
#                   `map()` with a `lambda` function to cube each Fibonacci number.
# Copyright 2025

# This script demonstrates the use of Python's `map()` function in conjunction
# with a `lambda` (anonymous) function. It first defines a function to generate
# a Fibonacci sequence up to a specified number of terms. Then, it uses `map()`
# and a `lambda` to efficiently apply a cubing operation to each number in
# that Fibonacci sequence.

# Define a lambda function `cube`.
# `lambda arguments: expression` creates a small, anonymous function.
# Here, it takes one argument `x` and returns `x` raised to the power of 3.
cube = lambda x: x ** 3

def fibonacci(n):
    """
    Generates the first 'n' numbers of the Fibonacci sequence.

    The Fibonacci sequence starts with 0 and 1, and each subsequent number
    is the sum of the two preceding ones (e.g., 0, 1, 1, 2, 3, 5, ...).

    Parameters:
    n (int): The number of Fibonacci terms to generate.

    Returns:
    list: A list containing the first 'n' Fibonacci numbers.
          Returns an empty list if n is 0 or less.
    """
    fib_sequence = [] # Initialize an empty list to store the sequence.
    a, b = 0, 1       # Initialize the first two Fibonacci numbers.
    
    # Loop 'n' times to generate 'n' Fibonacci numbers.
    for _ in range(n):
        fib_sequence.append(a) # Add the current 'a' (Fibonacci number) to the list.
        # Update 'a' and 'b' for the next iteration:
        # The new 'a' becomes the old 'b'.
        # The new 'b' becomes the sum of the old 'a' and old 'b'.
        a, b = b, a + b
        
    return fib_sequence

if __name__ == '__main__':
    print("--- Fibonacci Cubes Generator ---")
    print("This program generates Fibonacci numbers and then cubes them.")

    try:
        # Read the number of Fibonacci terms to generate.
        n_terms = int(input("Enter the number of Fibonacci terms to generate (n): "))

        if n_terms < 0:
            print("Error: Number of terms (n) cannot be negative.")
            exit()
        
        # Generate the Fibonacci sequence.
        fib_numbers = fibonacci(n_terms)
        
        # Use map() and the lambda function to cube each number in the Fibonacci sequence.
        # `map(function, iterable)` applies the `function` to every item of `iterable`.
        # `cube` (our lambda function) is applied to each `num` in `fib_numbers`.
        # The result of `map()` is a map object (an iterator), which we convert to a list.
        cubed_fib_numbers = list(map(cube, fib_numbers))
        
        print(f"\nFirst {n_terms} Fibonacci numbers: {fib_numbers}")
        print(f"Their cubes: {cubed_fib_numbers}")

    except ValueError:
        # Handle cases where input for 'n' is not a valid integer.
        print("Invalid input. Please enter an integer for n.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

