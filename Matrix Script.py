# Name: Ashish Sadavarti
# Code: Matrix Script Decoder
# Code Description: Decodes a character matrix into a single string by reading columns vertically,
#                   and then cleans up the decoded string using a regular expression to
#                   replace inter-alphanumeric symbols with single spaces.
# Copyright 2025

# This script is designed to process a matrix of characters (represented as lines of text).
# It first "transposes" or "decodes" the matrix by reading its characters column by column
# (from top to bottom, then left to right for the next column) into a single long string.
# After decoding, it uses a regular expression to clean up the string, specifically
# replacing sequences of certain symbols (like '!', '@', '#', '$', '%', '&', space)
# that appear between alphanumeric characters with a single space.

import re # Import the regular expression module for string manipulation.

if __name__ == '__main__':
    print("--- Matrix Script Decoder ---")
    print("This program decodes a character matrix and cleans up the resulting string.")

    try:
        # Read the dimensions of the matrix: n (rows) and m (columns).
        # input().split() reads a line like "7 3" and splits into ['7', '3'].
        # map(int, ...) converts these to integers.
        n_str, m_str = input("Enter matrix dimensions N (rows) and M (columns), space-separated (e.g., '7 3'): ").split()
        n = int(n_str)
        m = int(m_str)

        # Basic validation for dimensions.
        if n <= 0 or m <= 0:
            print("Error: N and M must be positive integers.")
            exit()

        # Initialize a 1D list to store characters in the decoded order.
        # The size is n * m (total number of characters in the matrix).
        # It's pre-filled with empty strings, which will be replaced.
        character_ar = [''] * (n * m)

        print(f"\nEnter {n} lines, each with exactly {m} characters, for the matrix:")
        # Read the matrix row by row.
        for i in range(n):
            line = input(f"Row {i+1} (M characters): ")
            
            # Basic validation for line length.
            if len(line) != m:
                print(f"Error: Row {i+1} has {len(line)} characters, but {m} were expected. Please restart.")
                exit() # Exit if line length is incorrect, as it would cause IndexError.

            # Populate the `character_ar` list by reading characters in a transposed manner.
            # This logic effectively reads the matrix column by column (top to bottom, then next column).
            # For a matrix A[row][col], the characters are stored in a 1D array such that
            # A[0][0], A[1][0], ..., A[n-1][0], A[0][1], A[1][1], ..., A[n-1][1], ...
            # The formula `i + (j * n)` calculates the 1D index:
            # - `i` represents the row index (0 to n-1).
            # - `j` represents the column index (0 to m-1).
            # - `j * n` offsets to the start of the current column's block in `character_ar`.
            # - `+ i` adds the row offset within that block.
            for j in range(m):
                character_ar[i + (j * n)] = line[j]
        
        # Join all characters in `character_ar` to form the initial decoded string.
        decoded_str = ''.join(character_ar)

        # Apply the regular expression to clean up the decoded string.
        # Regex pattern: `r'(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])'`
        # - `(?<=[A-Za-z0-9])`: This is a positive lookbehind assertion.
        #   It asserts that the current position in the string must be immediately preceded
        #   by an alphanumeric character (a-z, A-Z, 0-9). This part is not consumed by the match.
        # - `([ !@#$%&]+)`: This is the main capturing group.
        #   - `[ !@#$%&]`: Matches any single character that is a space or one of `!@#$%&`.
        #   - `+`: Matches one or more occurrences of the preceding character set.
        #   This part captures the sequence of symbols that we want to replace.
        # - `(?=[A-Za-z0-9])`: This is a positive lookahead assertion.
        #   It asserts that the current position in the string must be immediately followed
        #   by an alphanumeric character. This part is also not consumed by the match.
        # The `re.sub()` function replaces all occurrences of the pattern's match
        # (the captured symbols) with a single space `' '`.
        final_decoded_str = re.sub(r'(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])',' ', decoded_str)

        print("\nDecoded and cleaned string:")
        # Print the final cleaned string.
        print(final_decoded_str)

    except ValueError:
        # Handle cases where input for N or M is not a valid integer.
        print("Invalid input. Please ensure N and M are integers.")
    except IndexError:
        # This might occur if a row has fewer characters than M, or other indexing issues.
        print("Input error: The provided matrix rows do not match the specified column count (M).")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

