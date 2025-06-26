# Name: Ashish Sadavarti
# Code: Collections Deque Demonstration
# Code Description: Demonstrates basic operations of collections.deque, a double-ended queue,
#                   which supports efficient appending and popping from both ends.
# Copyright 2025

# This script showcases the `collections.deque` data structure.
# A deque (double-ended queue) is a list-like container with fast appends and pops
# on either end. It's suitable for implementing queues and stacks.

from collections import deque # Import the deque class from the collections module.

if __name__ == '__main__':
    print("--- collections.deque Demonstration ---")
    
    try:
        # Initialize a deque
        # A deque can be initialized with an iterable (like a list) or empty.
        # Example: deque_example = deque([10, 20, 30])
        
        print("\n1. Creating a deque:")
        initial_elements_str = input("Enter initial elements for deque (space-separated, e.g., '1 2 3'): ")
        if initial_elements_str.strip():
            # Convert input strings to integers for the deque elements
            initial_elements = list(map(int, initial_elements_str.split()))
            d = deque(initial_elements)
        else:
            d = deque() # Create an empty deque if no input
            print("Created an empty deque.")
        print(f"Initial deque: {d}")

        # Basic Operations:
        print("\n2. Appending elements:")
        # append(x): Add x to the right side of the deque.
        d.append(int(input("Enter an integer to append to the right (e.g., 4): ")))
        print(f"Deque after append: {d}")

        # appendleft(x): Add x to the left side of the deque.
        d.appendleft(int(input("Enter an integer to append to the left (e.g., 0): ")))
        print(f"Deque after appendleft: {d}")

        print("\n3. Popping elements:")
        if d: # Check if deque is not empty before popping
            # pop(): Remove and return an element from the right side.
            popped_right = d.pop()
            print(f"Popped from right: {popped_right}")
            print(f"Deque after pop(): {d}")
        else:
            print("Deque is empty, cannot pop from right.")

        if d: # Check if deque is not empty before popping
            # popleft(): Remove and return an element from the left side.
            popped_left = d.popleft()
            print(f"Popped from left: {popped_left}")
            print(f"Deque after popleft(): {d}")
        else:
            print("Deque is empty, cannot pop from left.")

        print("\n4. Extending elements:")
        # extend(iterable): Extend the right side of the deque with elements from the iterable.
        extend_right_str = input("Enter elements to extend to the right (space-separated, e.g., '5 6'): ")
        if extend_right_str.strip():
            d.extend(map(int, extend_right_str.split()))
            print(f"Deque after extend(): {d}")

        # extendleft(iterable): Extend the left side of the deque with elements from the iterable.
        # Note: Elements are added one by one, so order is reversed.
        # Example: d.extendleft([7, 8]) adds 8 then 7.
        extend_left_str = input("Enter elements to extend to the left (space-separated, e.g., '7 8'): ")
        if extend_left_str.strip():
            d.extendleft(map(int, extend_left_str.split()))
            print(f"Deque after extendleft(): {d}")

        print("\n5. Removing specific elements:")
        # remove(value): Remove the first occurrence of value. Raises ValueError if not found.
        if d:
            try:
                val_to_remove = int(input(f"Enter an integer to remove (e.g., {d[0] if d else '1'}): "))
                d.remove(val_to_remove)
                print(f"Deque after removing {val_to_remove}: {d}")
            except ValueError:
                print(f"Value {val_to_remove} not found in deque.")
        else:
            print("Deque is empty, no elements to remove.")

        print("\n6. Rotating the deque:")
        # rotate(n=1): Rotate the deque by n steps. Positive n shifts right, negative n shifts left.
        rotate_steps = int(input("Enter number of steps to rotate (positive for right, negative for left, e.g., 1 or -1): "))
        d.rotate(rotate_steps)
        print(f"Deque after rotating {rotate_steps} steps: {d}")

        print("\n7. Final deque state:")
        print(f"Current deque: {d}")

    except ValueError:
        print("Invalid input. Please ensure you enter integers as requested.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

