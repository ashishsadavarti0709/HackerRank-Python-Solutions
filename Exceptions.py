# Name: Ashish Sadavarti
# Code: Exceptions Handling Tutorial
# Code Description: Demonstrates basic exception handling in Python using try-except blocks
#                   to gracefully manage ZeroDivisionError and ValueError during integer division.
# Copyright 2025

# This script is a tutorial on Python's exception handling mechanism.
# It reads pairs of inputs (a, b) and attempts to perform integer division (a // b).
# It uses `try`, `except ZeroDivisionError`, and `except ValueError` blocks
# to catch and handle potential errors that might occur during this operation,
# such as division by zero or invalid input (non-integer strings).

if __name__ == '__main__':
    print("--- Python Exceptions Handling Tutorial ---")
    print("This program performs integer division and handles common errors.")

    try:
        # Read the number of test cases.
        t = int(input("Enter the number of test cases: "))

        if t < 0:
            print("Number of test cases cannot be negative.")
            exit()

        print(f"\nFor each of the {t} test cases, enter two numbers (a b) separated by a space.")
        # Loop 't' times to process each test case.
        for i in range(t):
            print(f"\n--- Test Case {i+1} ---")
            
            try:
                # Read a line of input, which is expected to contain two space-separated values.
                # input().split() will split the string into a list of two strings.
                a_str, b_str = input("Enter two numbers (a b): ").split()

                # Attempt to convert the strings to integers.
                # This can raise a ValueError if the strings are not valid integers.
                a_int = int(a_str)
                b_int = int(b_str)

                # Attempt to perform integer division.
                # This can raise a ZeroDivisionError if b_int is 0.
                result = a_int // b_int
                
                # If no exception occurred, print the result.
                print(result)

            except ZeroDivisionError as e:
                # Catch specifically a ZeroDivisionError.
                # This occurs when trying to divide by zero (e.g., 5 // 0).
                # The 'e' variable holds the exception object, whose string representation
                # typically describes the error (e.g., "integer division or modulo by zero").
                print("Error Code:", e)
            
            except ValueError as e:
                # Catch specifically a ValueError.
                # This occurs when int() receives a string that cannot be converted to an integer
                # (e.g., int('abc')).
                print("Error Code:", e)
            
            except IndexError:
                # Catch an IndexError if the user inputs fewer than two values for 'a' and 'b'.
                print("Error Code: invalid literal for int() with base 10: '' (input requires two values)")
            
            except Exception as e:
                # A general catch-all for any other unexpected exceptions.
                print(f"An unhandled error occurred: {type(e).__name__}: {e}")

    except ValueError:
        # This outer ValueError catches if the initial 't' (number of test cases)
        # is not a valid integer.
        print("Invalid input for number of test cases. Please enter an integer.")
    except Exception as e:
        # General catch-all for outer scope.
        print(f"An unexpected error occurred in overall script execution: {e}")

