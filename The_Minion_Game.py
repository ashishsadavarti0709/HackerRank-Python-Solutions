# Name: Ashish Sadavarti
# Code: TheMinionGame
# Code Description: Implements "The Minion Game" logic, where two players (Kevin and Stuart)
#                   score points based on substrings starting with vowels or consonants,
#                   respectively. The winner is determined by comparing their total scores.
# Copyright 2025

def minion_game(string):
    """
    Plays "The Minion Game" given an input string.
    Kevin scores points for substrings starting with vowels.
    Stuart scores points for substrings starting with consonants.
    The player with the higher score wins.

    Args:
        string (str): The string on which the game is played.
                      Assumed to be an uppercase English alphabet string.
    """
    # Define the set of vowels for quick lookup.
    vowels = 'AEIOU'
    
    # Initialize scores for both players.
    kevin_score = 0
    stuart_score = 0
    
    # Get the length of the input string.
    length = len(string)
    
    # Iterate through each character of the string using its index 'i'.
    # Each character marks the starting point of a potential substring.
    for i in range(length):
        # Check if the character at the current index 'i' is a vowel.
        if string[i] in vowels:
            # If it's a vowel, all substrings starting from this index 'i'
            # will contribute to Kevin's score.
            # The number of such substrings is 'length - i'.
            # For example, if string is "BANANA" and i=1 (A):
            # Substrings are "ANANA", "NANA", "ANA", "NA", "A".
            # Number of substrings = length (6) - current_index (1) = 5.
            kevin_score += length - i
        else:
            # If it's a consonant, all substrings starting from this index 'i'
            # will contribute to Stuart's score.
            # The number of such substrings is also 'length - i'.
            stuart_score += length - i

    # Determine the winner based on the final scores.
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    # Read the input string from the user when the script is executed directly.
    s = input()
    # Call the minion_game function with the user-provided string.
    minion_game(s)

    # Example:
    # If input string is "BANANA"
    #
    # i=0 (B): consonant -> Stuart score += 6-0 = 6 (B, BA, BAN, BANA, BANAN, BANANA)
    # i=1 (A): vowel     -> Kevin score += 6-1 = 5 (A, AN, ANA, ANAN, ANANA)
    # i=2 (N): consonant -> Stuart score += 6-2 = 4 (N, NA, NAN, NANA)
    # i=3 (A): vowel     -> Kevin score += 6-3 = 3 (A, AN, ANA)
    # i=4 (N): consonant -> Stuart score += 6-4 = 2 (N, NA)
    # i=5 (A): vowel     -> Kevin score += 6-5 = 1 (A)
    #
    # Kevin's total score = 5 + 3 + 1 = 9
    # Stuart's total score = 6 + 4 + 2 = 12
    #
    # Output: Stuart 12
