# Name: Ashish Sadavarti
# Code: Polar Coordinates of a Complex Number
# Code Description: Takes a complex number as input and calculates its magnitude (absolute value)
#                   and phase (argument) in radians.
# Copyright 2025

# This script demonstrates how to work with complex numbers in Python,
# specifically how to convert them from rectangular form (a + bj) to
# polar coordinates (magnitude, phase). It uses the `cmath` module,
# which provides functions for complex number mathematics.

import cmath # Import the cmath module for complex number functions.

if __name__ == '__main__':
    print("--- Polar Coordinates of a Complex Number ---")
    print("This program calculates the magnitude and phase of a complex number.")

    try:
        # Read the complex number as a string.
        # Python's built-in `complex()` constructor can parse strings like "1+2j", "-3.5+0j", etc.
        complex_number_str = input("Enter a complex number (e.g., '1+2j', '-1-1j'): ").strip()
        z = complex(complex_number_str)

        print(f"\nComplex number entered: {z}")

        # Calculate the magnitude (absolute value) of the complex number.
        # `abs(z)` returns the magnitude, which is the distance from the origin to the point
        # (real, imaginary) in the complex plane. It's equivalent to `sqrt(real**2 + imag**2)`.
        magnitude = abs(z)
        print("Magnitude (absolute value):")
        print(magnitude)

        # Calculate the phase (argument) of the complex number.
        # `cmath.phase(z)` returns the angle of the complex number in the complex plane,
        # measured in radians from the positive real axis. The result is in the range (-pi, pi].
        phase = cmath.phase(z)
        print("\nPhase (argument in radians):")
        print(phase)

    except ValueError:
        # Handle cases where the input string cannot be parsed as a complex number.
        print("Invalid input. Please enter a valid complex number string (e.g., '1+2j').")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

