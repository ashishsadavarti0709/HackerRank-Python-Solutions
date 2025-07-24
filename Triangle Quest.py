# Name: Ashish Sadavarti
# Code: TriangleQuest
# Code Description: Prints a pattern of repeating digits (e.g., 1, 22, 333)
#                   up to a given integer 'n' using a specific mathematical formula.
# Copyright 2025

# Read the integer 'n' from the user.
# The loop will iterate from 1 up to (but not including) 'n'.
# For example, if input is 5, loop runs for i = 1, 2, 3, 4.
for i in range(1, int(input())):
    # This line generates the desired repeating digit pattern for each row 'i'.
    # It leverages a mathematical property for generating numbers like 1, 22, 333, etc.
    #
    # (10**i - 1): Generates a number consisting of 'i' nines.
    #              e.g., if i=1, 10**1 - 1 = 9
    #              e.g., if i=2, 10**2 - 1 = 99
    #              e.g., if i=3, 10**3 - 1 = 999
    #
    # (...) // 9: Integer division by 9.
    #             This converts the string of nines into a string of ones.
    #             e.g., 9 // 9 = 1
    #             e.g., 99 // 9 = 11
    #             e.g., 999 // 9 = 111
    #
    # i * (...): Multiplies the current loop variable 'i' by the result
    #            (which is a number consisting of 'i' ones).
    #            e.g., if i=1, 1 * 1 = 1
    #            e.g., if i=2, 2 * 11 = 22
    #            e.g., if i=3, 3 * 111 = 333
    #
    # This formula efficiently generates the sequence 1, 22, 333, 4444, and so on.
    print(i * (10**i - 1) // 9)

