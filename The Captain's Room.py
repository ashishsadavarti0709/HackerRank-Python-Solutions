# Name: Ashish Sadavarti
# Code: TheCaptainsRoom
# Code Description: Identifies the room number of the Captain, which appears
#                   only once, while all other room numbers appear exactly 'k' times.
#                   It uses a mathematical approach based on sums of sets and lists.
# Copyright 2025

if __name__ == '__main__':
    # Read the integer 'k', which represents the number of times each non-Captain's
    # room number appears in the list.
    k = int(input())

    # Read the list of all room numbers.
    # input().split() creates a list of strings from space-separated input.
    # map(int, ...) converts each string to an integer.
    # list(...) converts the map object to a list.
    # Example: If k=3 and room_numbers are "1 2 3 1 2 3 4 1 2 3",
    # the Captain's room is 4.
    room_numbers = list(map(int, input().split()))

    # Convert the list of all room numbers to a set.
    # A set stores only unique elements. So, 'room_set' will contain each
    # distinct room number exactly once (including the Captain's room).
    # Example: room_set for the above example would be {1, 2, 3, 4}
    room_set = set(room_numbers)

    # Calculate the Captain's room number using a clever mathematical formula.
    # Let S be the sum of all unique room numbers (sum(room_set)).
    # Let L be the sum of all room numbers as they appear in the input list (sum(room_numbers)).
    # Let C be the Captain's room number.
    # Let O be the sum of all other unique room numbers (S - C).
    #
    # We know that:
    # L = C * 1 + O * k  (Captain's room appears once, others 'k' times)
    # Also, we know that if Captain's room also appeared 'k' times, the total sum would be S * k.
    # S * k = C * k + O * k
    #
    # Subtracting the actual sum L from this hypothetical sum S * k:
    # (S * k) - L = (C * k + O * k) - (C * 1 + O * k)
    # (S * k) - L = C * k - C * 1
    # (S * k) - L = C * (k - 1)
    #
    # Therefore, the Captain's room number C can be found by:
    # C = ((S * k) - L) / (k - 1)
    #
    # In Python code:
    # sum(room_set) is S
    # sum(room_numbers) is L
    # (k - 1) is the divisor
    # The '//' operator performs integer division.
    captain_room = (sum(room_set) * k - sum(room_numbers)) // (k - 1)

    # Print the calculated Captain's room number.
    print(captain_room)
