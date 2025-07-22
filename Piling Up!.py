# Name: Ashish Sadavarti
# Code: Piling Up! (Block Stacking Puzzle)
# Code Description: Determines if a sequence of blocks can be stacked from left and right ends,
#                   such that each block placed is smaller than or equal to the previous one.
# Copyright 2025

# This script solves the "Piling Up!" problem, which is a classic greedy algorithm puzzle.
# You are given a row of blocks of varying side lengths. You need to determine if it's
# possible to stack all the blocks one by one onto a vertical pile, subject to these rules:
# 1. You can only take blocks from either the leftmost or the rightmost end of the current row.
# 2. Each block you add to the pile must be smaller than or equal to the block directly below it.

if __name__ == '__main__':
    print("--- Piling Up! (Block Stacking Puzzle) ---")
    print("This program determines if blocks can be stacked according to rules.")

    try:
        # Read the number of test cases.
        t = int(input("Enter the number of test cases (T): "))

        if t < 0:
            print("Number of test cases cannot be negative.")
            exit()

        print(f"\nFor each of the {t} test cases:")
        # Loop through each test case.
        for case_num in range(t):
            print(f"\n--- Test Case {case_num+1} ---")
            
            # Read the number of blocks for the current test case.
            n = int(input("Enter the number of blocks (N): "))

            if n <= 0:
                print("No") # Cannot pile up if no blocks or negative blocks
                continue # Move to next test case
            
            # Read the space-separated side lengths of the blocks.
            blocks_str = input(f"Enter {n} space-separated block side lengths: ")
            blocks = list(map(int, blocks_str.split()))

            # Basic validation: check if number of blocks matches N
            if len(blocks) != n:
                print(f"Warning: Expected {n} blocks but received {len(blocks)}. Processing with available blocks.")
                # If length is mismatch, it might indicate bad input; depends on problem strictness.
                # For this problem, we'll continue with the provided `blocks` list.

            # Initialize two pointers: one at the leftmost block and one at the rightmost.
            left = 0
            right = n - 1
            
            # Initialize `last_picked` to a very large value (infinity).
            # This ensures that the first block picked can always be placed,
            # as any block side length will be less than or equal to infinity.
            last_picked = float('inf')
            
            # Loop as long as the left pointer has not crossed the right pointer.
            while left <= right:
                # Greedy strategy:
                # Prioritize picking the larger block if it's still smaller than or equal to `last_picked`.
                # This is because we want to remove larger blocks first to leave smaller ones for later.

                # If the leftmost block is greater than or equal to the rightmost block,
                # AND the leftmost block is smaller than or equal to the `last_picked` block:
                if blocks[left] >= blocks[right] and blocks[left] <= last_picked:
                    last_picked = blocks[left] # Take the leftmost block.
                    left += 1                   # Move the left pointer to the right.
                
                # Else (if the leftmost block is NOT the preferred choice):
                # If the rightmost block is smaller than or equal to the `last_picked` block:
                elif blocks[right] <= last_picked:
                    last_picked = blocks[right] # Take the rightmost block.
                    right -= 1                  # Move the right pointer to the left.
                
                # If neither the leftmost nor the rightmost block can be placed (i.e., both are too large):
                else:
                    print("No") # It's not possible to stack the blocks.
                    break       # Exit the while loop.
            
            # The `else` block for the `while` loop executes only if the loop completes
            # normally (i.e., without hitting the `break` statement).
            # This means all blocks were successfully placed.
            else:
                print("Yes") # All blocks were stacked.

    except ValueError:
        # Handle cases where input elements are not valid integers.
        print("Invalid input. Please ensure N and block lengths are integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

