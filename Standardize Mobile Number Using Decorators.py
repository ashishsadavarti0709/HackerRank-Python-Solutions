# Name: Ashish Sadavarti
# Code: StandardizeMobileNumberDecorator
# Code Description: Demonstrates how to use a Python decorator to standardize
#                   a list of mobile numbers to a specific format (+91 xxxxx xxxxx)
#                   before passing them to the decorated function.
# Copyright 2025

def wrapper(f):
    """
    A decorator function that standardizes mobile numbers in a list.
    It formats each number to "+91 xxxxx xxxxx" before passing the
    modified list to the original function 'f'.

    Args:
        f (function): The function to be decorated. This function is expected
                      to accept a list of strings (mobile numbers).

    Returns:
        function: The decorated function 'fun'.
    """
    def fun(l):
        """
        The inner wrapper function that performs the mobile number standardization.

        Args:
            l (list): A list of strings, where each string is a mobile number.
                      Numbers can be in various formats (e.g., 0XXXXXXXXXX, +91XXXXXXXXXX,
                      +91 XXXXXXXXXX, etc.).
        """
        # Create a new list 'standardized_numbers' by iterating through the input list 'l'.
        # For each number 'c' in 'l':
        # 1. c[-10:-5]: Slices the string to get the 6th to 10th digits from the end.
        #                This assumes the last 10 digits are the actual mobile number.
        #                Example: for "07895462130", it would get "54621".
        # 2. c[-5:]: Slices the string to get the last 5 digits.
        #             Example: for "07895462130", it would get "2130".
        # 3. "+91 " + ... + " " + ...: Concatenates these parts with the "+91 " prefix
        #                               and a space in between the two 5-digit segments.
        standardized_numbers = ["+91 " + c[-10:-5] + " " + c[-5:] for c in l]
        
        # Call the original function 'f' with the newly standardized list of numbers.
        f(standardized_numbers)
    return fun

# Example Usage:
@wrapper
def sort_phone(l):
    """
    This function is decorated by 'wrapper'. It expects a list of standardized
    phone numbers and prints them after sorting.
    """
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    # Get the number of mobile numbers to process.
    n = int(input("Enter the number of mobile numbers: "))
    
    # Read 'n' mobile numbers from the user and store them in a list.
    phone_numbers = [input() for _ in range(n)]

    # Call the decorated function.
    # The 'wrapper' decorator will intercept this call, standardize the numbers,
    # and then pass the standardized list to 'sort_phone'.
    sort_phone(phone_numbers)

    # Example Input:
    # 3
    # 07895462130
    # 919875641230
    # 917890123456

    # Expected Output (after standardization and sorting):
    # +91 78901 23456
    # +91 78954 62130
    # +91 98756 41230
