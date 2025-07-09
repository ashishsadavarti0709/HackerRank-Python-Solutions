# Name: Ashish Sadavarti
# Code: Integers Come In All Sizes: Large Power Sum
# Code Description: Calculates the sum of two large integer powers (a^b + c^d).
#                   Python's arbitrary-precision integers handle very large numbers automatically.
# Copyright 2025

# This script demonstrates Python's inherent capability to handle integers of arbitrary size.
# Unlike some other programming languages, Python integers automatically adjust their precision
# to accommodate numbers of any magnitude, limited only by available memory.
# The problem involves calculating (a^b + c^d) where a, b, c, d can be very large.

if __name__ == '__main__':
    print("--- Integers Come In All Sizes: Large Power Sum ---")
    print("This program calculates a^b + c^d for potentially very large integers.")

    try:
        # Read four integers from separate lines.
        # These integers can be very large.
        a = int(input("Enter integer a: "))
        b = int(input("Enter integer b: "))
        c = int(input("Enter integer c: "))
        d = int(input("Enter integer d: "))

        # Calculate a^b using the `pow()` function.
        # Python's `pow()` (or `**` operator) handles large integer exponents automatically.
        power_ab = pow(a, b)
        
        # Calculate c^d.
        power_cd = pow(c, d)
        
        # Calculate the sum of the two powers.
        # The sum will also be an arbitrary-precision integer.
        result = power_ab + power_cd
        
        # Print the final result.
        print("\nResult of a^b + c^d:")
        print(result)

    except ValueError:
        # Handle cases where input is not a valid integer.
        print("Invalid input. Please enter integers only.")
    except OverflowError as e:
        # While Python integers handle arbitrary size, for extremely large exponents,
        # memory limits might theoretically be hit, though `OverflowError` for int
        # is rare in practical competitive programming for this specific calculation.
        print(f"Calculation resulted in an overflow error: {e}")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

