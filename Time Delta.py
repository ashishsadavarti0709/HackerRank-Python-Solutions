# Name: Ashish Sadavarti
# Code: TimeDeltaCalculator
# Code Description: Calculates the absolute difference in seconds between two
#                   given timestamps, handling time zones correctly.
# Copyright 2025

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime # Import the datetime module for date and time operations

def time_delta(t1, t2):
    """
    Calculates the absolute difference in seconds between two given timestamps.

    Args:
        t1 (str): The first timestamp string.
        t2 (str): The second timestamp string.

    Returns:
        str: The absolute difference in seconds as a string.
    """
    # Define the format string for parsing the timestamps.
    # %a: Weekday as locale’s abbreviated name. (e.g., Mon)
    # %d: Day of the month as a zero-padded decimal number. (e.g., 01)
    # %b: Month as locale’s abbreviated name. (e.g., Jan)
    # %Y: Year with century as a decimal number. (e.g., 2023)
    # %H: Hour (24-hour clock) as a zero-padded decimal number. (e.g., 09)
    # %M: Minute as a zero-padded decimal number. (e.g., 30)
    # %S: Second as a zero-padded decimal number. (e.g., 00)
    # %z: UTC offset in the form +HHMM or -HHMM. (e.g., +0530, -0400)
    fmt = "%a %d %b %Y %H:%M:%S %z"
    
    # Parse the first timestamp string into a datetime object.
    time1 = datetime.strptime(t1, fmt)
    
    # Parse the second timestamp string into a datetime object.
    time2 = datetime.strptime(t2, fmt)
    
    # Calculate the difference between the two datetime objects.
    # This results in a timedelta object.
    time_difference = time1 - time2
    
    # Get the total difference in seconds from the timedelta object.
    # .total_seconds() returns the total duration in seconds.
    # abs(...) takes the absolute value, ensuring the result is non-negative.
    # int(...) converts the result to an integer (as total_seconds() can return float).
    # str(...) converts the integer result to a string as required by the problem.
    return str(abs(int(time_difference.total_seconds())))

if __name__ == '__main__':
    # This part handles input/output redirection typically found in competitive programming.
    # If 'OUTPUT_PATH' environment variable is set, it writes to that file.
    # Otherwise, it defaults to standard output (sys.stdout).
    if 'OUTPUT_PATH' in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    else:
        # Fallback to sys.stdout for local execution if OUTPUT_PATH is not set.
        fptr = sys.stdout

    # Read the number of test cases.
    t = int(input())

    # Iterate through each test case.
    for t_itr in range(t):
        # Read the first timestamp string for the current test case.
        t1 = input()

        # Read the second timestamp string for the current test case.
        t2 = input()

        # Call the time_delta function to calculate the difference.
        delta = time_delta(t1, t2)

        # Write the calculated delta followed by a newline to the output.
        fptr.write(delta + '\n')

    # Close the file pointer if it's not sys.stdout.
    if fptr != sys.stdout:
        fptr.close()
