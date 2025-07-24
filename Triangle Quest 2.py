# Name: Ashish Sadavarti
# Code: TriangleQuest2
# Code Description: Prints a palindromic triangle pattern of numbers up to a given integer 'n'
#                   using a mathematical formula involving powers of 10.
# Copyright 2025

# Read the integer 'n' from the user. This 'n' defines the number of rows to print.
# The problem statement typically limits this 'n' to ensure efficient calculation
# and fitting within score constraints.
# For example, if n = 5, the output should be:
# 1
# 121
# 12321
# 1234321
# 123454321
for i in range(1, int(input()) + 1):
    # This line generates the desired palindromic number for each row 'i'.
    # It leverages a mathematical property:
    #
    # 10**i: Calculates 10 raised to the power of 'i'.
    #        e.g., if i=1, 10**1 = 10
    #        e.g., if i=2, 10**2 = 100
    #        e.g., if i=3, 10**3 = 1000
    #
    # // 9: Integer division by 9.
    #       This is the key step. Dividing a number like 10, 100, 1000 by 9 (integer division)
    #       generates a sequence of 1s:
    #       10 // 9 = 1
    #       100 // 9 = 11
    #       1000 // 9 = 111
    #       10000 // 9 = 1111
    #
    # (... )**2: Squares the result.
    #       1**2 = 1
    #       11**2 = 121
    #       111**2 = 12321
    #       1111**2 = 1234321
    #       11111**2 = 123454321
    # This precisely generates the palindromic numbers required for the pattern.
    print((10**i // 9)**2)

