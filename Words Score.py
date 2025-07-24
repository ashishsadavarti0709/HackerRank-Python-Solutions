# Name: Ashish Sadavarti
# Code: WordsScore
# Code Description: Calculates a total score for a list of words based on the
#                   number of vowels in each word: +2 if even vowels, +1 if odd vowels.
# Copyright 2025

def is_vowel(letter):
    """
    Checks if a given letter is a vowel (a, e, i, o, u, y).

    Args:
        letter (str): A single character string.

    Returns:
        bool: True if the letter is a vowel, False otherwise.
    """
    # The 'in' operator efficiently checks if 'letter' exists within the string of vowels.
    # It implicitly handles case if the input 'letter' is always expected to be lowercase,
    # or you might convert 'letter.lower()' for case-insensitivity.
    # For this problem, 'y' is included as a vowel.
    return letter in 'aeiouy'

def score_words(words):
    """
    Calculates the total score for a list of words based on their vowel counts.
    Each word with an even number of vowels adds 2 to the score.
    Each word with an odd number of vowels adds 1 to the score.

    Args:
        words (list): A list of strings (words).

    Returns:
        int: The total calculated score.
    """
    score = 0 # Initialize the total score to 0
    
    # Iterate through each word in the input list of words.
    for word in words:
        # Calculate the number of vowels in the current word.
        # sum(1 for letter in word if is_vowel(letter)):
        #   - This is a generator expression.
        #   - It iterates through each 'letter' in the 'word'.
        #   - For each letter, it calls is_vowel(letter).
        #   - If is_vowel() returns True, it yields 1.
        #   - sum() then sums all these 1s, effectively counting the vowels.
        num_vowels = sum(1 for letter in word if is_vowel(letter))
        
        # Check if the number of vowels is even or odd.
        if num_vowels % 2 == 0:
            # If even, add 2 to the total score.
            score += 2
        else:
            # If odd, add 1 to the total score.
            score += 1
            
    return score # Return the final calculated score

if __name__ == '__main__':
    # This block is for executing the code directly and taking input.
    # Read the number of words (though not strictly used by score_words function).
    # n = int(input()) # Often present in competitive programming problems.
    
    # Read the line of words and split them into a list.
    # Example Input: "programming is awesome"
    words_input = input("Enter words separated by spaces: ").split()
    
    # Calculate the score using the score_words function.
    final_score = score_words(words_input)
    
    # Print the final score.
    print(f"Total score: {final_score}")

    # Example Trace for input "programming is awesome":
    # words = ["programming", "is", "awesome"]
    #
    # Word "programming":
    #   Vowels: o, a, i (3 vowels, odd) -> score += 1
    # Word "is":
    #   Vowels: i (1 vowel, odd) -> score += 1
    # Word "awesome":
    #   Vowels: a, e, o, e (4 vowels, even) -> score += 2
    #
    # Total score = 1 + 1 + 2 = 4
