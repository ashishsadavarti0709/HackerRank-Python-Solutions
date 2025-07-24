# Name: Ashish Sadavarti
# Code: SetManipulationOperations
# Code Description: Demonstrates the use of set.pop(), set.remove(), and set.discard()
#                   methods to modify a set based on user commands, and then prints
#                   the sum of the remaining elements.
# Copyright 2025

if __name__ == '__main__':
    # Read the initial number of elements for the set.
    n = int(input())
    
    # Read the initial elements of the set.
    # input().split() reads a line of space-separated strings.
    # map(int, ...) converts each string to an integer.
    # set(...) converts the mapped integers into a set.
    s = set(map(int, input().split()))
    
    # Read the number of commands to execute on the set.
    commands_count = int(input())
    
    # Loop through each command.
    for _ in range(commands_count):
        # Read the command line. It will be space-separated, e.g., "pop" or "remove 5".
        command = input().split()
        
        # The first part of the command list is the operation name (e.g., "pop", "remove", "discard").
        operation = command[0]
        
        # Execute the corresponding set operation based on the command.
        if operation == 'pop':
            # s.pop():
            #   - Removes an arbitrary element from the set and returns it.
            #   - Sets are unordered, so there's no guarantee which element will be removed.
            #   - If the set is empty, it raises a KeyError.
            if s: # Check if the set is not empty before popping to avoid KeyError
                s.pop()
            # else:
            #   print("Cannot pop from an empty set.") # Optional: add error handling for empty set
        elif operation == 'remove':
            # s.remove(element):
            #   - Removes the specified 'element' from the set.
            #   - If the 'element' is not found in the set, it raises a KeyError.
            #   - The element to remove is the second part of the command list, converted to an integer.
            element_to_remove = int(command[1])
            try:
                s.remove(element_to_remove)
            except KeyError:
                # print(f"Element {element_to_remove} not found in set. 'remove' operation ignored.") # Optional: handle missing element
                pass # As per typical competitive programming, often silently ignore or follow problem's error spec
        elif operation == 'discard':
            # s.discard(element):
            #   - Removes the specified 'element' from the set if it is present.
            #   - If the 'element' is NOT found in the set, it does nothing and does NOT raise an error.
            #   - This is the key difference from .remove().
            #   - The element to discard is the second part of the command list, converted to an integer.
            element_to_discard = int(command[1])
            s.discard(element_to_discard)
            
    # After all commands are executed, calculate the sum of the remaining elements in the set.
    print(sum(s))
