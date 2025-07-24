# Name: Ashish Sadavarti
# Code: SetSymmetricDifferenceOperation
# Code Description: Calculates the number of students subscribed to either an English
#                   or a French newspaper, but NOT both, using set symmetric difference.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of students who subscribed to the English newspaper.
    # This input value (n_english) is often part of problem specifications
    # but isn't directly used in the set operations for calculating the symmetric difference.
    n_english = int(input())

    # Read the roll numbers of students subscribed to the English newspaper.
    # input().split() reads the space-separated roll numbers as strings.
    # set(...) converts this list of strings into a set, which automatically
    # handles unique elements.
    english_subs = set(input().split())

    # Read the number of students who subscribed to the French newspaper.
    n_french = int(input())

    # Read the roll numbers of students subscribed to the French newspaper,
    # and convert them into a set, similar to the English subscribers.
    french_subs = set(input().split())

    # Perform the set symmetric difference operation.
    # The .symmetric_difference() method (or the ^ operator) returns a new set
    # containing elements that are in EITHER 'english_subs' OR 'french_subs',
    # but NOT in their intersection (i.e., not in both).
    # This finds students who subscribed to exactly one of the two newspapers.
    symmetric_diff = english_subs.symmetric_difference(french_subs)

    # Print the number of elements (i.e., the count of students) in the resulting
    # symmetric difference set.
    print(len(symmetric_diff))

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
    #
    # Elements in intersection: {'1', '2', '6', '8'}
    # Elements in union: {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '21', '55'}
    #
    # 'symmetric_diff' would be (union - intersection):
    # {'3', '4', '5', '7', '9', '10', '11', '21', '55'}
    #
    # len(symmetric_diff) would be 9
    #
    # Output: 9
