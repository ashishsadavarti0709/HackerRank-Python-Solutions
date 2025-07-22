# Name: Ashish Sadavarti
# Code: ReduceFunctionProduct
# Code Description: Demonstrates the use of Python's functools.reduce() to calculate
#                   the product of a list of fractions (Fraction objects).
# Copyright 2025

from fractions import Fraction
from functools import reduce

def product(fracs):
    """
    Calculates the product of a list of Fraction objects using the reduce function.

    Args:
        fracs (list): A list of fractions.Fraction objects.

    Returns:
        tuple: A tuple containing the numerator and denominator of the product.
    """
    # The reduce function applies a given function (lambda x, y: x * y)
    # cumulatively to the items of a sequence (fracs), from left to right,
    # so as to reduce the sequence to a single value.
    #
    # Here, it takes the first two fractions, multiplies them, then takes that
    # result and multiplies it by the third fraction, and so on, until all
    # fractions in the list have been multiplied together.
    #
    # For example, if fracs = [Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]:
    # 1. reduce starts with x = Fraction(1, 2), y = Fraction(2, 3). Result: Fraction(1, 3)
    # 2. Next, x = Fraction(1, 3), y = Fraction(3, 4). Result: Fraction(1, 4)
    # The final result 't' will be Fraction(1, 4).
    t = reduce(lambda x, y: x * y, fracs)
    
    # Return the numerator and denominator of the resulting fraction 't'.
    return t.numerator, t.denominator

if __name__ == '__main__':
    # Example usage:
    # Get the number of fractions from the user.
    num_fractions = int(input("Enter the number of fractions: "))
    
    # Create an empty list to store Fraction objects.
    fractions_list = []
    
    # Loop to get numerator and denominator for each fraction from the user.
    print("Enter each fraction as 'numerator denominator' (e.g., '1 2'):")
    for i in range(num_fractions):
        # Read the numerator and denominator as integers from a single line.
        n, d = map(int, input(f"Fraction {i+1}: ").split())
        # Create a Fraction object and add it to the list.
        fractions_list.append(Fraction(n, d))

    # Calculate the product of the fractions.
    numerator_result, denominator_result = product(fractions_list)
    
    # Print the result.
    print(f"\nThe product of the fractions is: {numerator_result}/{denominator_result}")
    print(f"As a single fraction: {Fraction(numerator_result, denominator_result)}")

    # Another example:
    # sample_fracs = [Fraction(1, 2), Fraction(3, 4), Fraction(5, 6)]
    # num, den = product(sample_fracs)
    # print(f"Product of [1/2, 3/4, 5/6]: {num}/{den}") # Expected: 15/48, simplified by Fraction class
