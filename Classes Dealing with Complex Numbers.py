# Name: Ashish Sadavarti
# Code: Classes Dealing with Complex Numbers
# Code Description: Implements a Complex number class with methods for addition,
#                   subtraction, multiplication, true division, and modulus,
#                   along with a custom string representation.
# Copyright 2025

# This script defines a 'Complex' class that allows for arithmetic operations
# on complex numbers. It overloads standard operators (+, -, *, /) and includes
# a method for calculating the modulus (absolute value) of a complex number,
# as well as a custom string representation for printing.

import math # Import the math module for square root (used in modulus calculation).

class Complex(object):
    """
    Represents a complex number with a real and an imaginary part.
    Supports basic arithmetic operations and modulus calculation.
    """
    def __init__(self, real, imaginary):
        """
        Initializes a Complex object.

        Parameters:
        real (float or int): The real part of the complex number.
        imaginary (float or int): The imaginary part of the complex number.
        """
        self.real = float(real)      # Store real part as float.
        self.imaginary = float(imaginary) # Store imaginary part as float.

    def __add__(self, no):
        """
        Overloads the addition operator (+).
        Adds two complex numbers: (a + bi) + (c + di) = (a+c) + (b+d)i.
        """
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        """
        Overloads the subtraction operator (-).
        Subtracts two complex numbers: (a + bi) - (c + di) = (a-c) + (b-d)i.
        """
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        """
        Overloads the multiplication operator (*).
        Multiplies two complex numbers: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i.
        """
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imaginary_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imaginary_part)

    def __truediv__(self, no):
        """
        Overloads the true division operator (/).
        Divides two complex numbers: (a + bi) / (c + di) = [(ac + bd) / (c^2 + d^2)] + [(bc - ad) / (c^2 + d^2)]i.
        Handles division by zero for the denominator (c^2 + d^2) implicitly by float division,
        but a check for no.real and no.imaginary both being zero could be added for explicit error handling.
        """
        # Denominator is c^2 + d^2
        denom = no.real**2 + no.imaginary**2
        
        # Check for division by zero (if the divisor complex number is 0 + 0i)
        if denom == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number (0 + 0i)")

        real_part = (self.real * no.real + self.imaginary * no.imaginary) / denom
        imaginary_part = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(real_part, imaginary_part)

    def mod(self):
        """
        Calculates the modulus (absolute value or magnitude) of the complex number.
        The modulus of (a + bi) is sqrt(a^2 + b^2).
        Returns a new Complex object with the modulus as the real part and 0 as the imaginary part.
        """
        # Magnitude = sqrt(real^2 + imaginary^2)
        magnitude = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(magnitude, 0) # Modulus is always a real number.

    def __str__(self):
        """
        Provides a string representation of the Complex object, formatted to two decimal places.
        Handles cases where real or imaginary parts are zero to ensure correct formatting
        (e.g., "3.00+0.00i", "0.00+2.50i", "1.00-1.00i").
        """
        if self.imaginary == 0:
            # If imaginary part is zero, format as "X.XX+0.00i"
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            # If real part is zero, format as "0.00+X.XXi" or "0.00-X.XXi"
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % abs(self.imaginary) # Use abs for negative imaginary to print as positive after '-'
        elif self.imaginary > 0:
            # If imaginary part is positive, format as "X.XX+Y.YYi"
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            # If imaginary part is negative, format as "X.XX-Y.YYi" (Y.YY will be abs of imaginary)
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

# Example Usage:
if __name__ == '__main__':
    print("--- Complex Number Operations ---")
    try:
        # Get input for the first complex number
        c1_str = input("Enter real and imaginary parts for Complex 1 (e.g., '1 2'): ").split()
        c1 = Complex(float(c1_str[0]), float(c1_str[1]))

        # Get input for the second complex number
        c2_str = input("Enter real and imaginary parts for Complex 2 (e.g., '3 4'): ").split()
        c2 = Complex(float(c2_str[0]), float(c2_str[1]))

        print("\nOperations:")
        # Addition
        print(f"{c1} + {c2} = {c1 + c2}")
        # Subtraction
        print(f"{c1} - {c2} = {c1 - c2}")
        # Multiplication
        print(f"{c1} * {c2} = {c1 * c2}")
        # Division
        print(f"{c1} / {c2} = {c1 / c2}")
        # Modulus of C1
        print(f"Modulus of {c1} = {c1.mod()}")
        # Modulus of C2
        print(f"Modulus of {c2} = {c2.mod()}")

    except ValueError:
        print("Invalid input. Please enter two numbers (real and imaginary parts) separated by a space.")
    except IndexError:
        print("Input error: Please provide both real and imaginary parts.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

