# Name: Ashish Sadavarti
# Code: Power and Modulo Power
# Code Description: Demonstrates Python's built-in `pow()` function for calculating
#                   (a^b) and (a^b % m) efficiently, especially for large numbers.
# Copyright 2025

# This script showcases Python's versatile `pow()` function.
# It reads three integers: `a` (base), `b` (exponent), and `m` (modulus).
# It then calculates and prints:
# 1. `a` raised to the power of `b` (`a^b`).
# 2. `a` raised to the power of `b`, modulo `m` (`a^b % m`).
# The three-argument version of `pow()` is highly efficient for modular exponentiation,
# as it avoids computing the potentially very large intermediate result of `a^b`.

if __name__ == '__main__':
    print("--- Power and Modulo Power ---")
    print("This program calculates a^b and (a^b) % m.")

    try:
        # Read the base 'a'.
        a = int(input("Enter integer 'a' (base): "))
        
        # Read the exponent 'b'.
        b = int(input("Enter integer 'b' (exponent): "))
        
        # Read the modulus 'm'.
        m = int(input("Enter integer 'm' (modulus): "))

        # Validate inputs for typical problem constraints.
        if b < 0:
            print("Error: Exponent 'b' must be non-negative.")
            # For negative b, pow(a, b) would return float and pow(a, b, m) would error.
            exit()
        if m <= 0:
            print("Error: Modulus 'm' must be a positive integer.")
            exit()
        if a == 0 and b == 0:
            print("Warning: 0^0 is undefined. Python's pow(0,0) returns 1.")
        
        # Calculate a^b.
        # Python's `pow(a, b)` (or `a ** b`) handles large integers automatically.
        result_power = pow(a, b)
        print("\nResult of a^b:")
        print(result_power)

        # Calculate a^b % m.
        # The three-argument `pow(a, b, m)` is optimized for modular exponentiation.
        # It computes (a^b) % m efficiently without computing the full `a^b` first,
        # which can be astronomically large and cause memory issues if not handled this way.
        result_mod_power = pow(a, b, m)
        print("\nResult of (a^b) % m:")
        print(result_mod_power)

    except ValueError:
        # Handle cases where input is not a valid integer.
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

