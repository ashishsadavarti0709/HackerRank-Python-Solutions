# Name: Ashish Sadavarti
# Code: SetUnionOperation
# Code Description: Calculates the total number of unique students subscribed to
#                   either an English or a French newspaper (or both), using set union.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of students who subscribed to the English newspaper.
    # This value (n_english) is typically provided in problem statements as context,
    # but it's not directly used in the set union calculation.
    n_english = int(input())

    # Read the roll numbers of students subscribed to the English newspaper.
    # input().split() reads a line of space-separated values (roll numbers)
    # and splits them into a list of strings.
    # set(...) converts this list into a set. Sets inherently store only unique elements,
    # which is ideal for counting unique subscribers.
    english_subs = set(input().split())

    # Read the number of students who subscribed to the French newspaper.
    n_french = int(input())

    # Read the roll numbers of students subscribed to the French newspaper,
    # and convert them into a set, similar to the English subscribers.
    french_subs = set(input().split())

    # Perform the set union operation.
    # The .union() method (or the | operator) returns a new set containing all
    # unique elements from both 'english_subs' and 'french_subs'.
    # This effectively finds the total number of students who subscribed to at least
    # one of the two newspapers, without double-counting students who subscribed to both.
    total_unique_students = english_subs.union(french_subs)

    # Print the number of elements (i.e., the count of unique students) in the
    # resulting union set.
    print(len(total_unique_students))

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
    # 'total_unique_students' (union) would be:
    # {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '21', '55'}
    #
    # len(total_unique_students) would be 13
    #
    # Output: 13
