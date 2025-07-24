# Name: Ashish Sadavarti
# Code: SetIntersectionOperation
# Code Description: Calculates the number of students subscribed to both an English
#                   and a French newspaper, using set intersection.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of students who subscribed to the English newspaper.
    # This input is typically provided for context but isn't directly used
    # in the set operation for calculating the intersection size.
    n_english = int(input())

    # Read the roll numbers of students subscribed to the English newspaper.
    # input().split() reads a line of space-separated values and splits them into a list of strings.
    # set(...) converts this list into a set, automatically ensuring unique elements.
    english_subs = set(input().split())

    # Read the number of students who subscribed to the French newspaper.
    n_french = int(input())

    # Read the roll numbers of students subscribed to the French newspaper,
    # and convert them into a set.
    french_subs = set(input().split())

    # Perform the set intersection operation.
    # The .intersection() method returns a new set containing only the elements
    # that are common to BOTH 'english_subs' and 'french_subs'.
    # In this context, it finds the students who subscribed to *both* newspapers.
    total_both_subs = english_subs.intersection(french_subs)

    # Print the number of elements (i.e., the count of students) in the resulting
    # intersection set.
    print(len(total_both_subs))

    # Example Usage (if run outside a problem platform, you'd provide inputs like):
    #
    # Input for n_english:
    # 9
    # Input for english_subs:
    # 1 2 3 4 5 6 7 8 9
    # Input for n_french:
    # 9
    # Input for french_subs:
    # 10 1 2 11 21 55 6 8
    #
    # Expected Output (for the above example):
    # The set 'english_subs' would be { '1', '2', '3', '4', '5', '6', '7', '8', '9' }
    # The set 'french_subs' would be { '10', '1', '2', '11', '21', '55', '6', '8' }
    # 'total_both_subs' (intersection) would be {'1', '2', '6', '8'}
    # len(total_both_subs) would be 4
    #
    # Output: 4
