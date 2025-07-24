# Name: Ashish Sadavarti
# Code: PostalCodeValidator
# Code Description: Validates a given postal code string based on two regular
#                   expression rules: valid format/range and no more than one
#                   alternating repetitive digit pair.
# Copyright 2025

import re

# Regex for validating the overall format and range of the postal code.
# r"^[1-9][\d]{5}$":
#   - ^: Asserts the start of the string.
#   - [1-9]: Matches a single digit from 1 to 9 (ensuring it's not zero at the start).
#   - [\d]{5}: Matches exactly five digits (0-9).
#   - $: Asserts the end of the string.
# This ensures the postal code is exactly 6 digits long and does not start with 0.
regex_integer_in_range = r"^[1-9][\d]{5}$"

# Regex for detecting alternating repetitive digit pairs.
# r"(\d)(?=\d\1)":
#   - (\d): Captures any single digit (e.g., '1', '2'). This is Group 1.
#   - (?=\d\1): This is a positive lookahead assertion.
#     - \d: Matches any digit immediately following the captured digit.
#     - \1: Matches the content of Group 1 (the first captured digit).
#     - The lookahead means it asserts that the captured digit is followed by
#       any digit and then by itself again (e.g., 1_1, 2_2, where '_' is any digit).
#     - Crucially, the lookahead is zero-width, meaning it does not consume characters.
#       This allows for overlapping matches to be found correctly.
#       Example: In "1212", it finds '1' at index 0 (followed by 2 then 1) and
#                then '2' at index 1 (followed by 1 then 2).
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

if __name__ == '__main__':
    # Read the postal code string from the user.
    P = input()

    # Rule 1: Check if the postal code is a 6-digit number starting with 1-9.
    # re.match() checks for a match only at the beginning of the string.
    # bool(...) converts the Match object (or None) to a boolean.
    is_valid_format = bool(re.match(regex_integer_in_range, P))

    # Rule 2: Count the number of alternating repetitive digit pairs.
    # re.findall() returns a list of all non-overlapping matches.
    # Because our pattern uses a lookahead, the captured group (\d) is what's returned.
    # We count how many such patterns exist.
    # For "1212", it would find '1' (at index 0) and '2' (at index 1). Count = 2.
    # For "1100", it finds nothing that matches 'DxD'.
    # For "1234", it finds nothing.
    # For "121", it would find '1' (at index 0). Count = 1.
    alternating_pairs_count = len(re.findall(regex_alternating_repetitive_digit_pair, P))

    # The postal code is valid if:
    # 1. It adheres to the basic 6-digit, non-zero-start format.
    # AND
    # 2. It has *not* more than one alternating repetitive digit pair (i.e., 0 or 1 pair).
    #    So, alternating_pairs_count <= 1
    is_valid_postal_code = is_valid_format and (alternating_pairs_count <= 1)

    # Print the final validation result (True or False).
    print(is_valid_postal_code)

    # Example Test Cases:
    # Input: 110000
    # Expected: False (alternating_pairs_count for '110000' is 2 for '1' at index 0 and '0' at index 3: 1(1)0(0)00 -> 1(0)1, 0(0)0. Lookahead means first part is 1, followed by 1, 1. In '110000', findall will detect:
    # '1' at index 0 (110) => match for (\d) followed by \d\1. Yes, 1 is followed by 1, then 1.
    # '1' at index 1 (100) => no match
    # '0' at index 2 (000) => yes, 0 followed by 0, then 0.
    # The current regex `(\d)(?=\d\1)` means (digit) followed by (any digit) and then (first digit again).
    # For "110000":
    # At index 0 (1): followed by 1, then 1 => match (1)
    # At index 1 (1): followed by 0, then 1 => no match
    # At index 2 (0): followed by 0, then 0 => match (0)
    # At index 3 (0): followed by 0, then 0 => match (0)
    # The problem typically implies "no more than one" for patterns like 1212, 1313, 1414 etc.
    # A single repeating digit like '1111' usually means it has *one* such pair.
    # A common misunderstanding of the problem statement for `regex_alternating_repetitive_digit_pair`
    # leads to the provided regex being more specific than often needed.
    # The common test cases usually check for patterns like '1212' or '1331' which contain two
    # overlapping "alternating repetitive digit pairs" using this lookahead.
    #
    # Let's verify the example 110000:
    # The question's common examples for `regex_alternating_repetitive_digit_pair` are about `1212` or `1010`.
    # For `1212`:
    # `(\d)` = 1, `(?=\d\1)` => `(?=21)` (found at index 0)
    # `(\d)` = 2, `(?=\d\1)` => `(?=12)` (found at index 1)
    # Count is 2. So it's invalid.
    #
    # For `110000`:
    # Index 0: `(\d)` = 1. Lookahead `(?=\d\1)` means `(?=\d1)`. Is `1` followed by any digit and then `1`? Yes, `1` (at index 1) `0` (at index 2). `1` `0` `1`
    # `(\d)` = 1, `(?=\d\1)` => `(?=11)` for `110`. No. This regex finds `XYX` patterns.
    #
    # Let's re-evaluate the regex `r"(\d)(?=\d\1)"` for "110000".
    # P = "110000"
    # re.findall(r"(\d)(?=\d\1)", P)
    # i=0, P[0]='1'. Lookahead (?=\d\1) on "10000" means is '1' followed by (\d) and then '1'? No. ('1' is followed by '1', then '0').
    # i=1, P[1]='1'. Lookahead (?=\d\1) on "0000" means is '1' followed by (\d) and then '1'? No. ('1' is followed by '0', then '0').
    # i=2, P[2]='0'. Lookahead (?=\d\1) on "000" means is '0' followed by (\d) and then '0'? Yes. '0' is followed by '0', then '0'. Match '0'.
    # i=3, P[3]='0'. Lookahead (?=\d\1) on "00" means is '0' followed by (\d) and then '0'? Yes. '0' is followed by '0', then '0'. Match '0'.
    # i=4, P[4]='0'. Lookahead (?=\d\1) on "0" means is '0' followed by (\d) and then '0'? No.
    # The matches are ['0', '0']. The count is 2. So "110000" would be Invalid. This is consistent with typical problem interpretations.

    # Input: 121412
    # re.findall(r"(\d)(?=\d\1)", "121412")
    # i=0, '1', (?=\d\1) -> (?=21) -> match '1'
    # i=1, '2', (?=\d\1) -> (?=12) -> match '2'
    # i=2, '1', (?=\d\1) -> (?=41) -> no
    # i=3, '4', (?=\d\1) -> (?=14) -> no
    # i=4, '1', (?=\d\1) -> (?=21) -> match '1'
    # Count = 3. Invalid.

    # Input: 123456
    # re.findall -> []
    # Count = 0. Valid.

    # Input: 121345
    # re.findall -> ['1']
    # Count = 1. Valid.
