# Name: Ashish Sadavarti
# Code: List Comprehensions: 3D Coordinate Generator
# Code Description: Generates a list of all possible 3D coordinates (i, j, k)
#                   within a specified cuboid, excluding those where their sum equals a given value 'n'.
# Copyright 2025

# This script demonstrates the powerful and concise syntax of Python's list comprehensions.
# It generates a list of all coordinates (i, j, k) such that:
# - `0 <= i <= x`
# - `0 <= j <= y`
# - `0 <= k <= z`
# And critically, it excludes any coordinates where the sum `i + j + k` is equal to a given integer `n`.

if __name__ == '__main__':
    print("--- List Comprehensions: 3D Coordinate Generator ---")
    print("This program generates coordinates (i, j, k) where i+j+k is not equal to N.")

    try:
        # Read the maximum values for x, y, and z dimensions.
        x = int(input("Enter the maximum value for i (x): "))
        y = int(input("Enter the maximum value for j (y): "))
        z = int(input("Enter the maximum value for k (z): "))
        
        # Read the target sum 'n' to exclude.
        n = int(input("Enter the sum to exclude (n): "))

        # Validate inputs to ensure they are non-negative for range()
        if x < 0 or y < 0 or z < 0:
            print("Error: x, y, and z must be non-negative integers.")
            exit()

        # List comprehension to generate the coordinates.
        # It's structured as nested loops with a conditional filter:
        # - `for i in range(x + 1)`: Iterates `i` from 0 up to `x` (inclusive).
        # - `for j in range(y + 1)`: Iterates `j` from 0 up to `y` (inclusive).
        # - `for k in range(z + 1)`: Iterates `k` from 0 up to `z` (inclusive).
        # - `if i + j + k != n`: This is the filter condition. Only coordinates (i, j, k)
        #   for which this condition is True will be included in the final list.
        # - `[i, j, k]`: The expression defining what each element in the new list will be.
        result_coordinates = [[i, j, k] for i in range(x + 1) 
                                        for j in range(y + 1)
                                        for k in range(z + 1) 
                                        if i + j + k != n]

        # Print the resulting list of coordinates.
        print("\nGenerated coordinates where i + j + k != n:")
        print(result_coordinates)

    except ValueError:
        # Handle cases where input is not a valid integer.
        print("Invalid input. Please enter integers for x, y, z, and n.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

