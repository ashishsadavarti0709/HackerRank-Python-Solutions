# Name: Ashish Sadavarti
# Code: DefaultDict Tutorial: Word Indexer
# Code Description: Demonstrates collections.defaultdict to find the indices of
#                   words from one list within another, and prints results.
# Copyright 2025

# This script showcases the utility of `collections.defaultdict`.
# It processes two groups of words: Group A and Group B.
# For each word in Group A, it records all its 1-based indices where it appears.
# Then, for each word in Group B, it looks up its recorded indices from Group A.
# If a word from Group B is found in Group A, its indices are printed; otherwise, -1 is printed.

from collections import defaultdict # Import defaultdict from the collections module.

if __name__ == '__main__':
    try:
        # Read the number of elements in Group A (n) and Group B (m).
        # input().strip().split() reads a line, removes whitespace, and splits it.
        # map(int, ...) converts the parts to integers.
        n_str, m_str = input("Enter N (size of Group A) and M (size of Group B) space-separated: ").strip().split()
        n = int(n_str)
        m = int(m_str)

        # Validate N and M
        if n < 0 or m < 0:
            print("Error: N and M must be non-negative integers.")
            exit()

        print(f"Enter {n} words for Group A (each on a new line):")
        # Read 'n' words for group_a, stripping whitespace from each.
        group_a = [input().strip() for _ in range(n)]

        print(f"Enter {m} words for Group B (each on a new line):")
        # Read 'm' words for group_b, stripping whitespace from each.
        group_b = [input().strip() for _ in range(m)]

        # Initialize a defaultdict where the default factory is 'list'.
        # This means if you try to access a key that doesn't exist, it will automatically
        # create an empty list for that key, rather than raising a KeyError.
        # This is perfect for collecting multiple indices for each word.
        positions = defaultdict(list)

        # Populate the 'positions' defaultdict with words from group_a and their indices.
        # enumerate(group_a, start=1) iterates through group_a, providing both
        # the 0-based index and the word, but we explicitly start counting from 1.
        for index, word in enumerate(group_a, start=1):
            # Append the current (1-based) index to the list associated with 'word'.
            # If 'word' is encountered for the first time, an empty list is created by defaultdict,
            # and then the index is appended to it.
            positions[word].append(index)

        print("\nResults for words in Group B (indices from Group A):")
        # For each word in group_b, check its presence and print indices.
        for word in group_b:
            # Check if the 'word' from group_b exists as a key in our 'positions' dictionary.
            if word in positions:
                # If the word is found, retrieve its list of indices.
                # map(str, ...) converts each integer index to a string.
                # ' '.join(...) joins these string indices with a space.
                print(' '.join(map(str, positions[word])))
            else:
                # If the word is not found in group_a, print -1 as specified.
                print(-1)

    except ValueError:
        print("Invalid input. Please ensure N, M are integers and words are correctly formatted.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

