# Name: Ashish Sadavarti
# Code: Array Sorting by Column
# Code Description: Reads a 2D array (matrix) and sorts its rows based on the values
#                   in a specified column (k-th index).
# Copyright 2025

# This script is designed to take a matrix (represented as a list of lists)
# as input, along with a column index 'k'. It then sorts the rows of the
# matrix in ascending order based on the values present in that 'k'-th column.
# Finally, it prints the sorted matrix, with elements of each row space-separated.

import math # Not used in this specific code, but often included in HackerRank templates.
import os   # Not used in this specific code.
import random # Not used in this specific code.
import re   # Not used in this specific code.
import sys  # Not used in this specific code directly, but implicit for input/output.


if __name__ == '__main__':
    try:
        # Read the dimensions of the array (n rows, m columns).
        # input().split() reads a line of space-separated values (e.g., "3 2")
        # map(int, ...) converts these string values to integers.
        # n, m = ... unpacks the two integers into variables n and m.
        n_str, m_str = input("Enter the number of rows and columns (e.g., '3 2'): ").split()
        n = int(n_str)
        m = int(m_str)

        arr = [] # Initialize an empty list to store the rows of the array.

        print(f"Enter {n} rows, each with {m} space-separated integers:")
        # Loop 'n' times to read each row of the array.
        for i in range(n):
            # Read a line of input for the current row.
            # .rstrip() removes any trailing whitespace (like newline characters).
            # .split() splits the string into a list of substrings by spaces.
            # map(int, ...) converts each substring to an integer.
            # list(...) converts the map object to a list.
            # append the list of integers (representing a row) to the 'arr'.
            arr.append(list(map(int, input(f"Row {i+1}: ").rstrip().split())))
            
            # Optional: Basic validation for column count per row
            if len(arr[-1]) != m:
                print(f"Warning: Row {i+1} has {len(arr[-1])} columns, but {m} were expected. Proceeding anyway.")


        # Read the integer 'k', which is the index of the column to sort by.
        # k is 0-indexed, meaning 0 for the first column, 1 for the second, etc.
        k = int(input(f"Enter the 0-indexed column number (0 to {m-1}) to sort by: "))

        # Validate k to ensure it's within the valid range of columns.
        if not (0 <= k < m):
            print(f"Error: Column index 'k' ({k}) is out of bounds for an array with {m} columns. Exiting.")
            sys.exit(1) # Exit the script if k is invalid.

        # Sort the array 'arr' in-place.
        # The 'key' argument specifies a function to be called on each element
        # of the list prior to making comparisons.
        # lambda x: x[k] is an anonymous function that takes a row (x) and returns
        # the element at the 'k'-th index of that row. This means the sorting
        # will be based on the values in the 'k'-th column of each row.
        arr.sort(key=lambda x: x[k])

        print("\nSorted Array:")
        # Iterate through each 'athlete' (which is a row) in the sorted 'arr'.
        for athlete in arr:
            # Convert each integer element in the 'athlete' (row) back to a string.
            # Join these string elements with a space and print the resulting string.
            # This effectively prints each sorted row on a new line with space-separated values.
            print(' '.join(map(str, athlete)))

    except ValueError:
        # Handle cases where input is not in the expected integer format.
        print("Invalid input. Please ensure dimensions and array elements are integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

