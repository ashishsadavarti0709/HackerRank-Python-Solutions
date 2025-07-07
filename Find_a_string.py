# Name: Ashish Sadavarti
# Code: Find a String: Substring Counter
# Code Description: Counts the number of occurrences of a given substring within a larger string.
# Copyright 2025

# This script defines a function `count_substring` that efficiently counts
# how many times a smaller string (sub_string) appears within a larger string.
# It performs a character-by-character comparison in a sliding window manner.

def count_substring(string, sub_string):
    """
    Counts the number of times `sub_string` appears in `string`.

    This function iterates through the `string` and checks if the `sub_string`
    matches at each possible starting position. The search is case-sensitive.

    Parameters:
    string (str): The main string to search within.
    sub_string (str): The substring to search for.

    Returns:
    int: The total count of non-overlapping occurrences of `sub_string` in `string`.

    Example:
    >>> count_substring("ABCDCDC", "CDC")
    2
    >>> count_substring("banana", "ana")
    2
    """
    count = 0 # Initialize a counter for the occurrences.
    
    # Iterate through the main string using a loop.
    # The loop needs to go up to `len(string) - len(sub_string) + 1`
    # because that's the last possible starting index where `sub_string` could fit.
    # For example, if string="abcde" (len=5) and sub_string="cde" (len=3),
    # the last possible start index is 2 (string[2:2+3] = "cde").
    # Loop range: range(5 - 3 + 1) = range(3), so i will be 0, 1, 2.
    for i in range(len(string) - len(sub_string) + 1):
        # Extract a slice from the `string` starting at index `i`
        # and with a length equal to `len(sub_string)`.
        current_slice = string[i : i + len(sub_string)]
        
        # Compare the extracted slice with the `sub_string`.
        if current_slice == sub_string:
            # If they match, increment the counter.
            count += 1
            
    return count

if __name__ == '__main__':
    print("--- Substring Counter ---")
    print("This program counts occurrences of a substring within a main string.")
    
    try:
        # Get the main string from user input.
        # .strip() removes any leading or trailing whitespace.
        main_string = input("Enter the main string: ").strip()
        
        # Get the substring to search for from user input.
        sub_string_to_find = input("Enter the substring to find: ").strip()
        
        # Handle cases where substring is longer than main string or empty.
        if len(sub_string_to_find) > len(main_string):
            print("Substring cannot be longer than the main string. Count is 0.")
            final_count = 0
        elif not sub_string_to_find:
            # If substring is empty, typically it "occurs" at every position plus one more.
            # However, for competitive programming, an empty substring match is usually 0.
            # Or depends on specific problem definition. Assuming 0 for a practical scenario.
            print("Substring is empty. Count is 0.")
            final_count = 0
        else:
            # Call the function to count occurrences.
            final_count = count_substring(main_string, sub_string_to_find)
            
        # Print the final count.
        print(f"Number of occurrences: {final_count}")

    except Exception as e:
        # Catch any unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

