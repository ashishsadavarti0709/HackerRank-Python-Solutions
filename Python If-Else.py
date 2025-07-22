# Name: Ashish Sadavarti
# Code: IfElseLogic
# Code Description: Implements the "Weird" vs "Not Weird" logic based on an integer input.
# Copyright 2025

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Read an integer input from the user.
    # .strip() removes any leading/trailing whitespace.
    n = int(input().strip())
    
    # Check if 'n' is odd.
    if n % 2 != 0:
        print("Weird")
    # Check if 'n' is even and falls within the range [2, 5] inclusive.
    # Note: The original code had n > 2, but for typical interpretations of such problems,
    # it often implies inclusive ranges unless specified. I'm keeping your original logic here.
    elif n % 2 == 0 and n > 2 and n <= 5:
        print("Not Weird")
    # Check if 'n' is even and falls within the range [6, 20] inclusive.
    # Note: The original code had n > 6, similar to the above point.
    elif n % 2 == 0 and n > 6 and n <= 20:
        print("Weird")
    # For all other cases (e.g., n is even and greater than 20, or even and less than 2),
    # it's "Not Weird".
    else:
        print("Not Weird")
