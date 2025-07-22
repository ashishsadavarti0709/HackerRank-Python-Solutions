# Name: Ashish Sadavarti
# Code: Python Division Operations
# Code Description: Demonstrates two types of division in Python: integer division (floor division)
#                   and float division (true division).
# Copyright 2025

# This script illustrates the difference between two division operators in Python:
# 1. Floor Division (`//`): Performs division and rounds the result down to the nearest integer.
# 2. True Division (`/`): Performs standard division, always returning a float result.
# It takes two integers as input and then applies both types of division.

if __name__ == '__main__':
    print("--- Python Division Operations ---")
    print("This program demonstrates integer (floor) division and float (true) division.")

    try:
        # Read the first integer 'a' (numerator).
        a = int(input("Enter integer 'a' (numerator): "))
        
        # Read the second integer 'b' (denominator).
        b = int(input("Enter integer 'b' (denominator): "))

        # Validate for division by zero.
        if b == 0:
            print("Error: Cannot divide by zero.")
            exit()
        
        # Perform integer division (floor division).
        # `a // b` returns the quotient of the division, rounded down to the nearest whole number.
        # Example: 5 // 2 = 2, -5 // 2 = -3
        floor_division_result = a // b
        print("\nInteger (Floor) Division (a // b):")
        print(floor_division_result)

        # Perform float division (true division).
        # `a / b` always returns a floating-point result, even if the division is exact.
        # Example: 5 / 2 = 2.5, 4 / 2 = 2.0
        true_division_result = a / b
        print("\nFloat (True) Division (a / b):")
        print(true_division_result)

    except ValueError:
        # Handle cases where input is not a valid integer.
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

