# Name: Ashish Sadavarti
# Code: arithmetic_operations.py
# Code Description: This program performs basic arithmetic operations (addition, subtraction,
#                   multiplication, division, and modulus) on two integer inputs and displays the results.
# Copyright 2025

# This script takes two integer inputs from the user and
# then prints the results of their addition, subtraction, multiplication,
# division (if the second number is not zero), and modulus (if the second number is not zero).

if __name__ == '__main__':
    try:
        # Get user input for two numbers
        print("Enter two numbers to perform arithmetic operations:")
        # Prompt the user to enter the first integer.
        # The input() function reads a line from stdin as a string.
        # int() converts this string to an integer.
        a = int(input("First number: "))

        # Prompt the user to enter the second integer.
        b = int(input("Second number: "))
        
        # Perform and display arithmetic operations
        print("\nResults:")
        # Print the sum of 'a' and 'b'.
        print(f"{a} + {b} =", a + b)
        
        # Print the difference between 'a' and 'b'.
        print(f"{a} - {b} =", a - b)
        
        # Print the product of 'a' and 'b'. The '×' symbol is used for better readability in output.
        print(f"{a} × {b} =", a * b)
        
        # Additional operations (division and modulus) are performed only if the second number (b) is not zero
        if b != 0:
            # Print the result of division.
            # Note: In Python 3, '/' performs float division, even for integers.
            print(f"{a} ÷ {b} =", a / b)
            
            # Print the result of the modulus operation (remainder of the division).
            print(f"{a} % {b} =", a % b)
        else:
            # Inform the user if division and modulus are skipped due to division by zero.
            print("Cannot divide by zero (division and modulus skipped)")

    except ValueError:
        # Handle cases where the user input for 'a' or 'b' is not a valid integer.
        print("Invalid input. Please enter integers only.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

