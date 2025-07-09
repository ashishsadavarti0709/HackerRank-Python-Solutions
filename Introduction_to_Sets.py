# Name: Ashish Sadavarti
# Code: Introduction to Sets: Average of Distinct Elements
# Code Description: Calculates the average of distinct (unique) elements in a numerical array.
#                   Demonstrates the use of Python's `set` data structure.
# Copyright 2025

# This script introduces the concept of Python's `set` data structure.
# A set is an unordered collection of unique elements. It's highly efficient
# for operations like checking for membership, removing duplicates, and performing
# set theory operations (union, intersection, etc.).
# Here, it's used to find the average of only the *distinct* elements in an array.

def average(array):
    """
    Calculates the average of the distinct (unique) elements in a numerical array.

    Parameters:
    array (list or tuple): A collection of numerical values (integers or floats).

    Returns:
    float: The average of the unique elements, rounded to three decimal places.

    Example:
    >>> average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    5.5
    """
    # Convert the input array (which can be a list or tuple) into a set.
    # This automatically removes all duplicate elements, leaving only unique values.
    # Example: [1, 2, 2, 3, 1] -> {1, 2, 3}
    distinct_elements = set(array)
    
    # Calculate the sum of the distinct elements.
    # sum() works directly on sets.
    sum_distinct = sum(distinct_elements)
    
    # Calculate the number of distinct elements.
    # len() works directly on sets.
    count_distinct = len(distinct_elements)
    
    # Handle case where there are no distinct elements (e.g., empty input array)
    if count_distinct == 0:
        # It's good practice to return 0.0 or raise an error for division by zero.
        # For average calculation, 0.0 for an empty set is reasonable.
        return 0.0

    # Calculate the average.
    avg = sum_distinct / count_distinct
    
    # Round the average to three decimal places.
    # round() function is used for this.
    return round(avg, 3)

if __name__ == '__main__':
    print("--- Average of Distinct Elements ---")
    print("This program calculates the average of unique numbers in a list.")

    try:
        # Read the number of elements (N).
        # This is often provided in competitive programming problems but not strictly used
        # to constrain the length of the actual array input.
        n = int(input("Enter the number of elements (N): "))

        if n < 0:
            print("Number of elements cannot be negative.")
            exit()

        # Read the space-separated elements for the array.
        # map(int, ...) converts them to integers.
        # list(...) creates a list from the mapped objects.
        array_str = input(f"Enter {n} space-separated numbers: ")
        arr = list(map(int, array_str.split()))

        # Check if the actual number of elements matches 'n' (optional validation)
        if len(arr) != n:
            print(f"Warning: Expected {n} elements but received {len(arr)}. Proceeding with available elements.")
            
        # Calculate the average of distinct elements using the defined function.
        result_average = average(arr)
        
        # Print the result.
        print(f"Average of distinct elements: {result_average}")

    except ValueError:
        # Handle cases where input elements cannot be converted to integers.
        print("Invalid input. Please enter space-separated integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

