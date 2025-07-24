# Name: Ashish Sadavarti
# Code: EmailFilterValidator
# Code Description: Demonstrates email validation using a regular expression
#                   and Python's built-in filter() function to select valid emails
#                   from a list of input email addresses.
# Copyright 2025

import re # Import the regular expression module

def fun(s):
    """
    Validates if a given string 's' is a valid email address according to specific rules.

    Email validation rules typically assumed for this type of problem:
    1.  The username (part before '@') can contain alphanumeric characters, underscores (_), and hyphens (-).
    2.  The domain name (part between '@' and '.') can contain only alphanumeric characters.
    3.  The top-level domain (TLD, part after the last '.') must be 1 to 3 English alphabet characters.

    Args:
        s (str): The string to be validated as an email address.

    Returns:
        bool: True if 's' is a valid email, False otherwise.
    """
    # Define the regular expression pattern for email validation.
    # ^[a-zA-Z0-9_-]+:
    #   - ^: Asserts the start of the string.
    #   - [a-zA-Z0-9_-]+: Matches one or more alphanumeric characters, underscores, or hyphens.
    #                     This defines the valid characters for the username part.
    # @: Matches the literal '@' character.
    # [a-zA-Z0-9]+:
    #   - Matches one or more alphanumeric characters. This defines the valid characters
    #     for the domain name (e.g., 'gmail', 'hotmail').
    # \.: Matches the literal dot ('.') before the TLD. The backslash '\' escapes the dot,
    #     as '.' is a special regex character that matches any character.
    # [a-zA-Z]{1,3}$:
    #   - [a-zA-Z]: Matches any English alphabet character.
    #   - {1,3}: Specifies that the preceding character set must appear 1 to 3 times.
    #            This limits the TLD length (e.g., 'com', 'org', 'net', but not 'info').
    #   - $: Asserts the end of the string.
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    
    # re.match(pattern, s):
    #   - Attempts to match the pattern from the *beginning* of the string 's'.
    #   - Returns a Match object if a match is found at the beginning, otherwise returns None.
    # We check if the result of re.match is not None, which means the string 's'
    # conforms to the entire pattern from start to end.
    return re.match(pattern, s) is not None

def filter_emails(emails):
    """
    Filters a list of email strings, returning only those that are valid
    according to the `fun` validation function.

    Args:
        emails (list): A list of email address strings.

    Returns:
        list: A sorted list of valid email address strings.
    """
    # filter(function, iterable):
    #   - Constructs an iterator from elements of 'iterable' for which 'function' returns true.
    #   - Here, 'fun' is the function that validates each email string.
    #   - 'emails' is the list of strings to filter.
    # list(...): Converts the filter object (an iterator) into a list.
    valid_emails = list(filter(fun, emails))
    
    # Sort the valid emails alphabetically before returning.
    return sorted(valid_emails)

if __name__ == '__main__':
    # Read the number of email addresses to process.
    n = int(input())
    
    # Read 'n' email addresses, one per line, and store them in a list.
    emails = []
    for _ in range(n):
        emails.append(input())
    
    # Call the filter_emails function to get the sorted list of valid emails.
    filtered_emails = filter_emails(emails)
    
    # Print each valid email on a new line.
    for email_addr in filtered_emails:
        print(email_addr)

    # Example Usage:
    # Input:
    # 3
    # lisa@gmail.com
    # bob#hotmail.com
    # alex@yahoo.co.in

    # Trace:
    # fun("lisa@gmail.com") -> True
    # fun("bob#hotmail.com") -> False (due to '#')
    # fun("alex@yahoo.co.in") -> True ('.co.in' might fail depending on TLD length, here max 3 is used)

    # If the TLD rule is strict (1-3 chars for .com, .org etc.):
    # "alex@yahoo.co.in" might be invalid if the problem expects only single TLDs of length 1-3.
    # The current regex `.[a-zA-Z]{1,3}$` will pass 'alex@yahoo.com' but fail 'alex@yahoo.co.in'
    # The given code's regex pattern: ^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$
    # This specific regex will consider 'alex@yahoo.co.in' as invalid because 'co' and 'in' are separate TLDs
    # and it expects only one TLD of 1-3 chars after the last dot.

    # Assuming 'alex@yahoo.com' in example:
    # Valid emails list: ["alex@yahoo.com", "lisa@gmail.com"]
    # Sorted valid emails: ["alex@yahoo.com", "lisa@gmail.com"]

    # Output for the corrected example (assuming "alex@yahoo.com" for third email):
    # alex@yahoo.com
    # lisa@gmail.com
