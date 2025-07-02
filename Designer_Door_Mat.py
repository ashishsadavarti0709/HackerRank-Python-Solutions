# Name: Ashish Sadavarti
# Code: Designer Door Mat Pattern Generator
# Code Description: Generates a symmetrical door mat pattern based on given dimensions N (rows) and M (columns).
# Copyright 2025

# This script creates a stylized door mat pattern.
# The pattern has a central "WELCOME" message.
# Above and below the message, it features symmetrical rows of '.|.' patterns
# centered with hyphens. The dimensions N (number of rows) and M (number of columns)
# must satisfy the condition that M is 3 times N.

def print_door_mat(N, M):
    """
    Prints a designer door mat pattern with given dimensions.

    The pattern consists of an upper part with increasing '.|.' patterns,
    a middle "WELCOME" message, and a lower part with decreasing '.|.' patterns.

    Parameters:
    N (int): The number of rows for the mat. N must be an odd number.
    M (int): The number of columns for the mat. M must be 3 times N.
    """
    
    # --- Upper Part of the Mat ---
    # This loop generates the rows from the top until just before the 'WELCOME' line.
    # It starts with 'i' from 1 and increments by 2 (1, 3, 5, ...), effectively
    # creating patterns with 1, 3, 5, etc., '.|.' units.
    for i in range(1, N, 2):
        # Create the repeating pattern string (e.g., '.|.', '.|.|.|.', etc.).
        # Multiply '.|.' by 'i' to get the pattern length for the current row.
        pattern_segment = ('.|.' * i)
        
        # Center the pattern segment within the total width 'M' using hyphens '-'.
        pattern = pattern_segment.center(M, '-')
        
        # Print the constructed row.
        print(pattern)

    # --- Middle Part of the Mat ---
    # Print the "WELCOME" message, centered within the total width 'M' using hyphens '-'.
    print('WELCOME'.center(M, '-'))
    
    # --- Lower Part of the Mat ---
    # This loop generates the rows from just after the 'WELCOME' line down to the bottom.
    # It starts with 'i' from N-2 (e.g., if N=7, starts with 5) and decrements by 2,
    # going down to 1 (e.g., 5, 3, 1). This mirrors the upper part.
    for i in range(N - 2, -1, -2): # Corrected range to include `i=1` when N-2 is odd and stop at 0 to generate 1. (N-2, 0, -2) for N=7 is 5,3,1
        # Create the repeating pattern string for the current row.
        pattern_segment = ('.|.' * i)
        
        # Center the pattern segment within the total width 'M' using hyphens '-'.
        pattern = pattern_segment.center(M, '-')
        
        # Print the constructed row.
        print(pattern)

if __name__ == '__main__':
    print("--- Designer Door Mat Pattern Generator ---")
    
    try:
        # Read the dimensions N (rows) and M (columns) from user input.
        # input().split() reads a line like "7 21" and splits it into ['7', '21'].
        # map(int, ...) converts these to integers.
        N_str, M_str = input("Enter N (odd number of rows) and M (3 times N), space-separated (e.g., '7 21'): ").split()
        N = int(N_str)
        M = int(M_str)

        # Validate input constraints as per typical problem requirements.
        # N must be an odd natural number.
        # M must be 3 times N.
        if N <= 0 or N % 2 == 0:
            print("Error: N must be a positive odd integer.")
        elif M != 3 * N:
            print(f"Error: M ({M}) must be exactly 3 times N ({N}), i.e., {3*N}.")
        else:
            # If inputs are valid, call the function to print the mat.
            print_door_mat(N, M)

    except ValueError:
        # Handle cases where input is not valid integers.
        print("Invalid input. Please enter two integers separated by a space.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

