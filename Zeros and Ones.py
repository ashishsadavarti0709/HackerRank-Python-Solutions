# Name: Ashish Sadavarti
# Code: NumPyZerosOnesArrays
# Code Description: Demonstrates how to create NumPy arrays filled with zeros
#                   and ones, respectively, given a specified shape from user input.
# Copyright 2025

import numpy

if __name__ == '__main__':
    # Read the desired shape of the array from the first line of input.
    # The input will be space-separated integers (e.g., "3 2" for a 3x2 matrix).
    # input().strip().split(): Reads the line, removes whitespace, and splits by spaces.
    # map(int, ...): Converts the resulting string elements to integers.
    # tuple(...): Converts the map object into a tuple, which is the required
    #             format for the 'shape' argument in NumPy functions like zeros() and ones().
    shape = tuple(map(int, input().strip().split()))

    # Create a NumPy array filled with zeros.
    # numpy.zeros(shape, dtype=int):
    #   - 'shape': The dimensions of the array (e.g., (3, 2) for 3 rows, 2 columns).
    #   - 'dtype=int': Specifies that the elements of the array should be integers.
    #                  By default, NumPy creates float arrays.
    # Example for shape=(3, 2):
    # [[0 0]
    #  [0 0]
    #  [0 0]]
    print(numpy.zeros(shape, dtype=int))

    # Create a NumPy array filled with ones.
    # numpy.ones(shape, dtype=int):
    #   - Similar to zeros(), but fills the array with ones.
    # Example for shape=(3, 2):
    # [[1 1]
    #  [1 1]
    #  [1 1]]
    print(numpy.ones(shape, dtype=int))

    # Full Example Trace:
    # Input:
    # 3 2
    #
    # 1. shape = (3, 2)
    # 2. print(numpy.zeros((3, 2), dtype=int))
    #    Output:
    #    [[0 0]
    #     [0 0]
    #     [0 0]]
    # 3. print(numpy.ones((3, 2), dtype=int))
    #    Output:
    #    [[1 1]
    #     [1 1]
    #     [1 1]]
