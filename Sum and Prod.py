# Name: Ashish Sadavarti
# Code: NumPySumProdOperations
# Code Description: Demonstrates how to use NumPy to perform a sum along a specific
#                   axis of a 2D array, and then calculate the product of the
#                   elements in the resulting 1D array.
# Copyright 2025

import numpy as np

if __name__ == '__main__':
    # Read the dimensions (rows and columns) of the array from a single line of input.
    # input().strip().split() gets the line, removes whitespace, and splits by spaces.
    # map(int, ...) converts the resulting strings to integers.
    # list(...) converts the map object to a list.
    # Example Input: "2 3" (for a 2x3 matrix)
    dimensions = list(map(int, input().strip().split()))
    rows, cols = dimensions[0], dimensions[1]

    # Create a NumPy array by reading 'rows' number of lines.
    # Each line represents a row of the array, with space-separated integers.
    # [list(map(int, input().strip().split())) for _ in range(rows)]
    #   - This is a list comprehension that iterates 'rows' times.
    #   - In each iteration, it reads a line, processes it into a list of integers,
    #     and adds that list as a row to the main list.
    # np.array(...) converts this list of lists into a NumPy 2D array.
    # Example Input for a 2x3 array:
    # 1 2 3
    # 4 5 6
    # my_array would be:
    # [[1 2 3]
    #  [4 5 6]]
    my_array = np.array([list(map(int, input().strip().split())) for _ in range(rows)])

    # Perform a sum operation along a specific axis.
    # np.sum(array, axis=0):
    #   - 'array' is the input NumPy array.
    #   - 'axis=0' indicates that the sum should be performed vertically,
    #     across the rows. This means it sums up elements in each column.
    #   - For a 2D array, summing along axis=0 results in a 1D array where
    #     each element is the sum of the corresponding column.
    # Example (for my_array above):
    # Column 0 sum: 1 + 4 = 5
    # Column 1 sum: 2 + 5 = 7
    # Column 2 sum: 3 + 6 = 9
    # sum_result would be: [5 7 9]
    sum_result = np.sum(my_array, axis=0)

    # Perform a product operation on the sum_result.
    # np.prod(array):
    #   - Calculates the product of all elements in the input array.
    #   - If the input is a 1D array, it multiplies all its elements together.
    # Example (for sum_result = [5 7 9]):
    # Product: 5 * 7 * 9 = 315
    product_result = np.prod(sum_result)

    # Print the final product result.
    print(product_result)

    # Full Example Trace:
    # Input:
    # 2 3
    # 1 2 3
    # 4 5 6
    #
    # 1. dimensions = [2, 3], rows = 2, cols = 3
    # 2. my_array = [[1, 2, 3], [4, 5, 6]]
    # 3. sum_result = np.sum([[1, 2, 3], [4, 5, 6]], axis=0)
    #               = [1+4, 2+5, 3+6]
    #               = [5, 7, 9]
    # 4. product_result = np.prod([5, 7, 9])
    #                   = 5 * 7 * 9
    #                   = 315
    # 5. print(315)
    #
    # Output:
    # 315
