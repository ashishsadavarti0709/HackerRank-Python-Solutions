# Name: Ashish Sadavarti
# Code: EmailValidatorParser
# Code Description: Parses email addresses from formatted strings and validates
#                   the email part using a regular expression. If valid, it prints
#                   the name and email in the standard format.
# Copyright 2025

import re
import email.utils # Provides utilities for parsing email addresses

def is_valid_email(email_address):
    """
    Validates an email address string using a regular expression.

    Constraints from typical problem statements for simple email validation:
    - It must start with an English alphabet character.
    - It can contain only alphanumeric characters, '-', '_' and '.'.
    - The part before '@' (username) can contain hyphens, underscores, and periods.
    - The part after '@' (website name) can only contain English alphabet characters.
    - The TLD (Top-Level Domain) must be of length 1 to 3.

    Args:
        email_address (str): The email address string to validate.

    Returns:
        bool: True if the email address is valid according to the pattern, False otherwise.
    """
    # Define the regex pattern for email validation.
    # ^[a-zA-Z]: Asserts that the string starts with an English alphabet character (case-insensitive).
    # [\w._-]*: Matches zero or more word characters (alphanumeric + underscore), periods (.), or hyphens (-).
    # @: Matches the literal '@' character.
    # [a-zA-Z]+: Matches one or more English alphabet characters for the domain name part.
    # \.: Matches the literal dot ('.') separating the domain from the TLD.
    # [a-zA-Z]{1,3}$: Matches 1 to 3 English alphabet characters at the end of the string for the TLD.
    # The whole pattern ensures the structure username@domain.tld.
    pattern = r'^[a-zA-Z][\w._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    
    # re.match(pattern, string):
    #   - Attempts to match the pattern only at the beginning of the string.
    #   - Returns a Match object if successful, None otherwise.
    # We check if the result is not None, indicating a match.
    return re.match(pattern, email_address) is not None

if __name__ == '__main__':
    # Read the number of email lines to process.
    n = int(input())

    # Loop 'n' times to process each email line.
    for _ in range(n):
        # Read a line, which can be in the format "Name <email@example.com>".
        line = input()
        
        # Use email.utils.parseaddr() to parse the line into a (name, email_address) tuple.
        # This utility correctly handles quoted names and extracts the email part.
        name, email_address = email.utils.parseaddr(line)
        
        # Validate the extracted email_address using our custom validation function.
        if is_valid_email(email_address):
            # If the email is valid, print the name and email in the specified format.
            print(f"{name} <{email_address}>")

    # Example Input:
    # 2
    # DEXTER <dexter@hotmail.com>
    # VIRUS <virus!@variable.com>

    # Trace:
    # Line 1: "DEXTER <dexter@hotmail.com>"
    #   name = "DEXTER", email_address = "dexter@hotmail.com"
    #   is_valid_email("dexter@hotmail.com") -> True (matches regex)
    #   Prints: DEXTER <dexter@hotmail.com>

    # Line 2: "VIRUS <virus!@variable.com>"
    #   name = "VIRUS", email_address = "virus!@variable.com"
    #   is_valid_email("virus!@variable.com") -> False (because of '!' in username)
    #   Nothing is printed for this line.
