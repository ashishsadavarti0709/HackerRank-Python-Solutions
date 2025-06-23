# Name: Ashish Sadavarti
# Code: Any or All List Checker
# Code description: Checks if all numbers in a list are positive AND if at least one number is a palindrome.
# Copyright 2025

# This script reads an integer 'n' (which is the expected number of elements, though not explicitly used for list length validation here),
# then reads a space-separated list of integers, and finally prints a boolean result
# based on two conditions:
# 1. All elements in the list are strictly greater than 0 (positive).
# 2. At least one element in the list is a palindrome (reads the same forwards and backwards when converted to a string).

if __name__ == '__main__':
    try:
        # Read the first line of input, which is expected to be an integer 'n'.
        # In this specific problem, 'n' often represents the number of elements that follow,
        # but the list conversion below handles the actual number of elements.
        n = int(input("Enter the number of elements (n): "))

        # Read the second line of input, which is a space-separated string of integers.
        # map(int, input().split()) converts each string element to an integer.
        # list(...) converts the map object into a list.
        lst = list(map(int, input("Enter space-separated integers: ").split()))

        # Condition 1: Check if all elements in the list are positive.
        # (x > 0 for x in lst) creates a generator that yields True if x is positive, False otherwise.
        # all(...) returns True if all elements yielded by the generator are True.
        all_positive = all(x > 0 for x in lst)

        # Condition 2: Check if any element in the list is a palindrome.
        # str(x) converts the integer to a string.
        # str(x)[::-1] reverses the string representation of the integer.
        # str(x) == str(x)[::-1] checks if the original string is equal to its reverse (i.e., it's a palindrome).
        # any(...) returns True if at least one element yielded by the generator is True.
        any_palindrome = any(str(x) == str(x)[::-1] for x in lst)

        # The final result is True if BOTH conditions are met (all positive AND any palindrome).
        print(all_positive and any_palindrome)

    except ValueError:
        # Handle cases where the input for 'n' or the list elements are not valid integers.
        print("Invalid input. Please ensure 'n' is an integer and list elements are space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An error occurred: {e}")

