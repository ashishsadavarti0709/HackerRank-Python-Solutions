# Name: Ashish Sadavarti
# Code: Merge the Tools! (Unique Substring Generator)
# Code Description: Divides a string into equal-sized substrings, removes duplicate
#                   characters from each substring while preserving order, and prints the result.
# Copyright 2025

# This script implements a string processing function `merge_the_tools` that
# takes a main string and an integer `k`. It divides the main string into
# segments of length `k`. For each segment, it then constructs a new string
# containing only the unique characters from that segment, maintaining their
# original order of first appearance. Each resulting unique-character substring
# is printed on a new line.

def merge_the_tools(string, k):
    """
    Processes a string by dividing it into chunks of size `k`,
    and for each chunk, prints a new string containing only its unique characters
    in their order of first appearance.

    Parameters:
    string (str): The main input string.
    k (int): The length of each substring chunk. The string length must be
             a multiple of k.
    """
    # Iterate through the main string with a step of `k`.
    # `range(0, len(string), k)` generates start indices for each chunk:
    # 0, k, 2*k, ... until the end of the string.
    for i in range(0, len(string), k):
        # Extract the current substring chunk of length `k`.
        # `string[i : i + k]` slices the string from index `i` up to `i + k` (exclusive).
        substring = string[i : i + k]
        
        unique_chars = [] # Initialize an empty list to store unique characters for this substring.
        
        # Iterate through each character in the current `substring`.
        for char in substring:
            # Check if the `char` is NOT already present in `unique_chars`.
            if char not in unique_chars:
                # If it's a new unique character, append it to the list.
                unique_chars.append(char)
        
        # Join the unique characters list to form a string and print it.
        # This string will contain only the unique characters from the current chunk,
        # in the order they first appeared.
        print(''.join(unique_chars))
        
if __name__ == '__main__':
    print("--- Merge the Tools! ---")
    print("This program processes a string into unique-character chunks.")

    try:
        # Read the main string from the user.
        string_input = input("Enter the main string: ").strip()
        
        # Read the integer 'k' (chunk size).
        k_input = int(input("Enter the chunk size (k): "))

        # Basic input validation.
        if k_input <= 0:
            print("Error: k must be a positive integer.")
            exit()
        if len(string_input) % k_input != 0:
            print("Error: The length of the string must be a multiple of k.")
            exit()
        if not string_input:
            print("Input string cannot be empty.")
            exit()
            
        # Call the function to perform the operations.
        print("\nProcessed chunks:")
        merge_the_tools(string_input, k_input)

    except ValueError:
        # Handle cases where input for 'k' is not a valid integer.
        print("Invalid input. Please ensure k is an integer.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

