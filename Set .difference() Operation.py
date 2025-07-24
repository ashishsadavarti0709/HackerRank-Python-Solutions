# Name: Ashish Sadavarti
# Code: SetDifferenceOperation
# Code Description: Calculates the number of students subscribed to an English newspaper
#                   who are NOT subscribed to a French newspaper, using set difference.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of students who subscribed to the English newspaper.
    # This input is not directly used in the set operation itself, but it
    # often precedes the list of roll numbers in problem statements.
    n_english = int(input())

    # Read the roll numbers of students subscribed to the English newspaper.
    # input().split() reads a line of space-separated values and splits them into a list of strings.
    # set(...) converts this list into a set. Sets automatically handle unique elements.
    english_subs = set(input().split())

    # Read the number of students who subscribed to the French newspaper.
    n_french = int(input())

    # Read the roll numbers of students subscribed to the French newspaper,
    # and convert them into a set.
    french_subs = set(input().split())

    # Perform the set difference operation.
    # The .difference() method returns a new set containing elements that are
    # in 'english_subs' but NOT in 'french_subs'.
    # This effectively finds the students who only subscribed to the English newspaper.
    only_english_subs = english_subs.difference(french_subs)

    # Print the number of elements (i.e., the count of students) in the resulting set.
    # len() returns the number of items in a set (or list, tuple, string, dictionary).
    print(len(only_english_subs))

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
    # 'only_english_subs' would be {'3', '4', '5', '7', '9'}
    # len(only_english_subs) would be 5
    #
    # Output: 5
