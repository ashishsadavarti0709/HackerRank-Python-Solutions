# Name: Ashish Sadavarti
# Code: NumPy Polynomial Evaluation
# Code Description: Evaluates a polynomial at a given value of x using NumPy's `polyval` function.
# Copyright 2025

# This script demonstrates the use of NumPy's `np.polyval()` function, which is
# designed for efficient evaluation of a polynomial at a specific value or set of values.
# It takes the coefficients of a polynomial as input (from highest degree to constant term)
# and a value for 'x', then calculates the polynomial's value at that 'x'.

import numpy as np # Import the NumPy library.

if __name__ == '__main__':
    print("--- NumPy Polynomial Evaluation ---")
    print("This program evaluates a polynomial at a given x value.")

    try:
        # Read the polynomial coefficients.
        # The coefficients should be entered space-separated, from the highest degree
        # term down to the constant term.
        # Example: for polynomial 2x^2 + 3x + 1, coefficients would be "2 3 1"
        coefficients_str = input("Enter polynomial coefficients (highest degree first, space-separated, e.g., '2 3 1'): ").strip()
        coefficients = list(map(float, coefficients_str.split()))

        # Validate that coefficients were provided.
        if not coefficients:
            print("Error: No coefficients provided. A polynomial needs at least one coefficient.")
            exit()

        # Read the value of 'x' at which to evaluate the polynomial.
        x_value_str = input("Enter the value of x to evaluate the polynomial at: ").strip()
        x_value = float(x_value_str)

        # Evaluate the polynomial using `np.polyval()`.
        # `np.polyval(p, x)`:
        # - `p`: A 1-D array of polynomial coefficients (from highest degree).
        # - `x`: The value(s) at which to evaluate the polynomial.
        # Example: `np.polyval([2, 3, 1], 5)` evaluates 2*(5^2) + 3*5 + 1
        result = np.polyval(coefficients, x_value)

        print("\nPolynomial coefficients:", coefficients)
        print("Value of x:", x_value)
        print("\nResult of polynomial evaluation:")
        print(result)

    except ValueError:
        # Handle cases where input for coefficients or x_value are not valid numbers.
        print("Invalid input. Please ensure coefficients and x are valid numbers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

