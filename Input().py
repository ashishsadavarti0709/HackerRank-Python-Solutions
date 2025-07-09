# Name: Ashish Sadavarti
# Code: Input and Polynomial Evaluation
# Code Description: Reads a value for 'x', a target value 'k', and a polynomial expression string 'P'.
#                   It then evaluates the polynomial at 'x' and checks if the result equals 'k'.
# Copyright 2025

# This script demonstrates how to take user input for numerical values and a string
# representing a mathematical expression (specifically, a polynomial). It uses
# Python's built-in `eval()` function to evaluate this expression and compares the
# result to a target value.

if __name__ == '__main__':
    print("--- Polynomial Evaluation Checker ---")
    print("This program evaluates a polynomial P(x) at a given x and checks if P(x) == k.")

    try:
        # Read two space-separated integers:
        # x: The value at which the polynomial P is to be evaluated.
        # k: The target value for the polynomial's result.
        x_str, k_str = input("Enter the value for x and the target value k (e.g., '1 4'): ").split()
        x = int(x_str)
        k = int(k_str)

        # Read the polynomial expression as a string.
        # The variable 'x' within this string will be substituted with the integer 'x' provided above.
        # Example: "x**3 + x**2 + x + 1"
        P_str = input("Enter the polynomial expression P(x) (e.g., 'x**3 + x**2 + x + 1'): ").strip()

        # Evaluate the polynomial expression string.
        # `eval(P_str)` parses the string `P_str` as a Python expression.
        # It has access to variables defined in the current scope, so 'x' will be used.
        # WARNING: Using `eval()` with untrusted input can be a security risk.
        # In competitive programming contexts like HackerRank, inputs are typically trusted.
        evaluated_P = eval(P_str)

        # Compare the evaluated result with the target value 'k'.
        # The result of the comparison (True or False) is then printed.
        print(evaluated_P == k)

    except ValueError:
        # Handles cases where input for x or k are not valid integers.
        print("Invalid input. Please ensure x and k are integers.")
    except SyntaxError:
        # Handles cases where the polynomial string `P` is not a valid Python expression.
        print("Invalid polynomial expression. Please check its syntax.")
    except NameError:
        # Handles cases where the polynomial string `P` refers to variables other than 'x'
        # that are not defined.
        print("Polynomial expression contains undefined variables other than 'x'.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

