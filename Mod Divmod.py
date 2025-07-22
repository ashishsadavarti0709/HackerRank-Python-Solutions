# Name: Ashish Sadavarti
# Code: Mod and Divmod Operations
# Code Description: Takes two integers, performs integer division (floor division),
#                   modulo operation, and demonstrates the `divmod()` function.
# Copyright 2025

# This script illustrates three related mathematical operations in Python for integers:
# 1. Integer Division (`//` operator): Performs floor division, returning the quotient.
# 2. Modulo Operation (`%` operator): Returns the remainder of the division.
# 3. `divmod()` function: Returns both the quotient and the remainder as a tuple.
# These operations are fundamental for working with integers and their divisibility properties.

if __name__ == '__main__':
    print("--- Mod and Divmod Operations ---")
    print("This program demonstrates integer division, modulo, and divmod().")

    try:
        # Read the first integer 'a'.
        a = int(input("Enter integer 'a' (numerator): "))
        
        # Read the second integer 'b'.
        b = int(input("Enter integer 'b' (denominator): "))

        # Validate for division by zero.
        if b == 0:
            print("Error: Cannot divide by zero.")
            exit()
        
        # Perform integer division (floor division).
        # `a // b` calculates the quotient, rounding down to the nearest integer.
        # Example: 17 // 3 = 5, -17 // 3 = -6
        floor_division_result = a // b
        print("\nInteger Division (a // b):")
        print(floor_division_result)

        # Perform the modulo operation.
        # `a % b` calculates the remainder of the division.
        # The sign of the remainder matches the sign of the divisor `b`.
        # Example: 17 % 3 = 2, -17 % 3 = 1, 17 % -3 = -1, -17 % -3 = -2
        modulo_result = a % b
        print("\nModulo Operation (a % b):")
        print(modulo_result)

        # Use the `divmod()` function.
        # `divmod(a, b)` returns a tuple containing the quotient and the remainder.
        # It's equivalent to (a // b, a % b).
        divmod_result = divmod(a, b)
        print("\nDivmod (a, b) result (quotient, remainder):")
        print(divmod_result)

    except ValueError:
        # Handle cases where input is not a valid integer.
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

