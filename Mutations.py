# Name: Ashish Sadavarti
# Code: String Mutations
# Code Description: Demonstrates how to "mutate" a string by replacing a character
#                   at a specific position. Python strings are immutable, so this
#                   is achieved by creating a new string.
# Copyright 2025

# This script defines a function `mutate_string` that simulates changing a character
# within a string at a given position. Since strings in Python are immutable (cannot
# be changed after creation), this operation is performed by constructing a *new*
# string using slicing and concatenation.

def mutate_string(string, position, character):
    """
    "Mutates" a string by replacing the character at `position` with `character`.
    Returns a new string with the modification.

    Parameters:
    string (str): The original string.
    position (int): The 0-based index at which to replace the character.
    character (str): The new character (expected to be a single character string).

    Returns:
    str: A new string with the character replaced.
    """
    # Create the new string by concatenating three parts:
    # 1. `string[:position]`: The part of the original string from the beginning
    #    up to (but not including) the `position`.
    # 2. `character`: The new character to insert.
    # 3. `string[position+1:]`: The part of the original string from the character
    #    *after* the `position` to the end.
    
    # Example: string="abracadabra", position=5, character='k'
    # string[:5]    -> "abrac"
    # character     -> "k"
    # string[5+1:]  -> "adabra" (from index 6 onwards)
    # Result        -> "abrackadabra"
    
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    print("--- String Mutations ---")
    print("This program replaces a character in a string at a given position.")

    try:
        # Read the original string.
        original_string = input("Enter the original string: ").strip()
        
        # Read the position (index) and the new character, space-separated.
        # Example: "5 k"
        position_str, char_to_insert = input("Enter position (integer) and new character (space-separated, e.g., '5 k'): ").split()
        
        position = int(position_str) # Convert position to an integer.

        # Basic input validation.
        if position < 0 or position >= len(original_string):
            print(f"Error: Position {position} is out of bounds for string of length {len(original_string)}.")
            exit()
        if len(char_to_insert) != 1:
            print("Error: The replacement must be a single character.")
            exit()
            
        # Call the function to get the new (mutated) string.
        new_string = mutate_string(original_string, position, char_to_insert)
        
        # Print the new string.
        print("\nOriginal String:", original_string)
        print("New String:", new_string)

    except ValueError:
        # Handle cases where position is not a valid integer.
        print("Invalid input. Please ensure position is an integer and inputs are space-separated.")
    except IndexError:
        # Handle cases where input.split() doesn't yield two parts.
        print("Input error: Please provide both position and a character, space-separated.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

