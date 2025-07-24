# Name: Ashish Sadavarti
# Code: NumPyTransposeFlatten
# Code Description: Demonstrates how to create a NumPy array from user input,
#                   and then perform transpose and flatten operations on it.
# Copyright 2025

import numpy

if __name__ == '__main__':
    # Read the dimensions (number of rows 'n' and columns 'm') from the first line of input.
    # input().strip().split(): Reads the line, removes leading/trailing whitespace, and splits by spaces.
    # map(int, ...): Converts the resulting string elements to integers.
    # Example Input: "2 3" (for a 2x3 matrix)
    n, m = map(int, input().strip().split())

    # Create a NumPy array (matrix) by reading 'n' lines of input.
    # Each line represents a row of the matrix, with space-separated integer elements.
    # [input().strip().split() for _ in range(n)]: This list comprehension
    #   reads 'n' lines, splits each into a list of strings.
    # numpy.array(..., int): Converts this list of lists into a NumPy 2D array,
    #   ensuring all elements are of integer type.
    # Example Input for a 2x3 matrix:
    # 1 2 3
    # 4 5 6
    # 'matrix' would be:
    # [[1 2 3]
    #  [4 5 6]]
    matrix = numpy.array([input().strip().split() for _ in range(n)], int)

    # Perform the transpose operation.
    # numpy.transpose(matrix): Swaps the rows and columns of the matrix.
    # The element at (i, j) in the original matrix moves to (j, i) in the transposed matrix.
    # For a 2x3 matrix, the transpose will be a 3x2 matrix.
    # Example (for 'matrix' above):
    # Transpose would be:
    # [[1 4]
    #  [2 5]
    #  [3 6]]
    print(numpy.transpose(matrix))

    # Perform the flatten operation.
    # matrix.flatten(): Returns a new 1D array (a flattened array)
    # containing all the elements of the original matrix in row-major order.
    # This means elements are taken row by row, from left to right.
    # Example (for 'matrix' above):
    # Flatten would be: [1 2 3 4 5 6]
    print(matrix.flatten())

    # Full Example Trace:
    # Input:
    # 2 3
    # 1 2 3
    # 4 5 6
    #
    # 1. n = 2, m = 3
    # 2. matrix = [[1, 2, 3], [4, 5, 6]]
    # 3. print(numpy.transpose(matrix))
    #    Output:
    #    [[1 4]
    #     [2 5]
    #     [3 6]]
    # 4. print(matrix.flatten())
    #    Output:
    #    [1 2 3 4 5 6]
