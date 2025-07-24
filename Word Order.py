# Name: Ashish Sadavarti
# Code: WordOrderCounter
# Code Description: Reads a sequence of words, counts the occurrences of each unique word,
#                   and then prints the total number of unique words followed by
#                   their counts in the order of their first appearance.
# Copyright 2025

# For competitive programming platforms, the main logic is typically within
# an if __name__ == '__main__': block.

if __name__ == '__main__':
    # Read the number of words that will be provided as input.
    n = int(input())

    # Initialize an empty list to store words in their original input order.
    # This list is technically not strictly necessary for this specific problem's output
    # (as dict preserves insertion order in Python 3.7+), but it helps in understanding
    # the flow if direct order preservation was a concern without dictionary guarantee.
    # For this problem, we'll rely on dictionary's insertion order.
    # words = []

    # Initialize an empty dictionary to store word counts.
    # In Python 3.7+, dictionaries preserve insertion order. This means that
    # the keys will be iterated in the order they were first added to the dictionary.
    # This is crucial for the second part of the output (counts in order of appearance).
    word_count = {}

    # Loop 'n' times to read each word.
    for _ in range(n):
        # Read a word from input and remove any leading/trailing whitespace.
        word = input().strip()
        
        # Add the word to the 'words' list (optional, for explicit order tracking).
        # words.append(word)

        # Update the word count in the dictionary.
        # If the word is already a key in 'word_count', increment its value.
        # Otherwise, add the word as a new key with an initial count of 1.
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Print the total number of unique words.
    # len(word_count) gives the number of unique keys in the dictionary.
    print(len(word_count))

    # Print the counts of words in the order of their first appearance.
    # (str(word_count[word]) for word in word_count):
    #   - This is a generator expression. It iterates through the keys of 'word_count'
    #     (which are in insertion order).
    #   - For each word, it retrieves its count from 'word_count' and converts it to a string.
    # ' '.join(...): Joins all the string counts together, separated by a single space.
    print(' '.join(str(word_count[word]) for word in word_count))

    # Example:
    # Input:
    # 4
    # bcdef
    # abcdefg
    # bcdef
    # bcdef
    #
    # Trace:
    # n = 4
    #
    # Loop 1: word = "bcdef"
    #   word_count = {"bcdef": 1}
    #
    # Loop 2: word = "abcdefg"
    #   word_count = {"bcdef": 1, "abcdefg": 1}
    #
    # Loop 3: word = "bcdef"
    #   word_count = {"bcdef": 2, "abcdefg": 1}
    #
    # Loop 4: word = "bcdef"
    #   word_count = {"bcdef": 3, "abcdefg": 1}
    #
    # print(len(word_count)) -> print(2) (unique words: "bcdef", "abcdefg")
    #
    # print(' '.join(str(word_count[word]) for word in word_count))
    #   - Iterates 'bcdef', 'abcdefg' (in that order).
    #   - Gets counts: 3, 1
    #   - Prints: "3 1"
    #
    # Output:
    # 2
    # 3 1
