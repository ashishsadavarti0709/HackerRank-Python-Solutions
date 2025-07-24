# Name: Ashish Sadavarti
# Code: SetMutationOperations
# Code Description: Demonstrates in-place set mutation operations (update, intersection_update,
#                   difference_update, symmetric_difference_update) on an initial set
#                   based on user commands, then prints the sum of the final set elements.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of elements for the initial set.
    n = int(input())
    
    # Read the initial elements and create the main set.
    initial_set = set(map(int, input().split()))
    
    # Read the number of mutation operations to perform.
    m = int(input())

    # Loop through each mutation command.
    for _ in range(m):
        # Read the operation command (e.g., "update 3") and split it.
        operation_data = input().split()
        # The first part is the name of the operation.
        operation = operation_data[0]
        # The second part (if any) might be a count, but for these operations,
        # we immediately read the elements for the 'other_set' on the next line.

        # Read the elements for the 'other_set' which will be used in the mutation.
        other_set = set(map(int, input().split()))
        
        # Perform the specified set mutation operation.
        if operation == "update":
            # initial_set.update(other_set):
            #   - Adds all elements from 'other_set' into 'initial_set'.
            #   - Equivalent to initial_set = initial_set | other_set (but in-place).
            initial_set.update(other_set)
        elif operation == "intersection_update":
            # initial_set.intersection_update(other_set):
            #   - Keeps only the elements that are present in BOTH 'initial_set' and 'other_set'.
            #   - Removes elements from 'initial_set' that are not in 'other_set'.
            #   - Equivalent to initial_set = initial_set & other_set (but in-place).
            initial_set.intersection_update(other_set)
        elif operation == "difference_update":
            # initial_set.difference_update(other_set):
            #   - Removes all elements from 'initial_set' that are also found in 'other_set'.
            #   - Equivalent to initial_set = initial_set - other_set (but in-place).
            initial_set.difference_update(other_set)
        elif operation == "symmetric_difference_update":
            # initial_set.symmetric_difference_update(other_set):
            #   - Updates 'initial_set' to contain only elements that are in EITHER
            #     'initial_set' OR 'other_set', but NOT in their intersection.
            #   - Removes common elements and adds unique elements from 'other_set'.
            #   - Equivalent to initial_set = initial_set ^ other_set (but in-place).
            initial_set.symmetric_difference_update(other_set)

    # After all operations are done, calculate the sum of all elements remaining in the initial set.
    result_sum = sum(initial_set)
    # Print the final sum.
    print(result_sum)
