"""
Name: Ashish Sadavarti
Code: rangoli_pattern.py
Code Description: This program prints an alphabet rangoli pattern of given size.
Copyright 2025
"""

# Define the alphabet string for pattern generation
a = "abcdefghijklmnopqrstuvwxyz"

def print_rangoli(size):
    """
    Prints an alphabet rangoli pattern of the specified size.
    
    The pattern is symmetric and consists of lowercase letters arranged in 
    a diamond shape, with the middle line being the first 'size' letters 
    of the alphabet in reverse order.
    
    Parameters:
    size (int): Determines the width and height of the rangoli pattern.
                Should be between 1 and 26 (inclusive).
    
    Returns:
    None: Outputs the pattern directly to console
    """
    
    # List to store each line of the pattern
    lines = []
    
    # Generate the top half lines of the pattern
    for row in range(size):
        # Create the right half of the current line
        right_half = "-".join(a[row:size])
        # Mirror the right half to create the full line
        full_line = right_half[::-1] + right_half[1:]
        lines.append(full_line)
    
    # Determine the maximum width for center alignment
    max_width = len(lines[0])
    
    # Print the bottom half (in reverse order)
    for row in range(size-1, 0, -1):
        print(lines[row].center(max_width, '-'))
    
    # Print the top half
    for row in range(size):
        print(lines[row].center(max_width, '-'))

# Main execution
if __name__ == '__main__':
    # Get user input for pattern size
    n = int(input("Enter the size of rangoli (1-26): "))
    
    # Validate input
    if n < 1 or n > 26:
        print("Error: Size must be between 1 and 26")
    else:
        print_rangoli(n)