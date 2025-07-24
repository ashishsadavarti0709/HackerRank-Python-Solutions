# Name: Ashish Sadavarti
# Code: SortedSymmetricDifference
# Code Description: Calculates the symmetric difference between two sets of integers
#                   and then prints the elements of the resulting set in ascending order,
#                   each on a new line.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of elements for the first set.
    # This value (m) is often given in problem statements but not directly used
    # in the set operations themselves.
    m = int(input())
    
    # Read the elements of the first set.
    # input().split() reads a line of space-separated strings.
    # map(int, ...) converts these strings to integers.
    # set(...) creates a set from these integers, automatically handling uniqueness.
    a = set(map(int, input().split()))
    
    # Read the number of elements for the second set.
    n = int(input())
    
    # Read the elements of the second set, similar to the first set.
    b = set(map(int, input().split()))
    
    # Calculate the symmetric difference between set 'a' and set 'b'.
    # The .symmetric_difference() method returns a new set containing elements
    # that are in 'a' OR 'b', but NOT in both (i.e., elements unique to either set).
    #
    # Alternatively, the XOR operator ^ can be used: a ^ b
    #
    # The result is then sorted using sorted(). This function returns a new
    # sorted list from the elements of the iterable (the set in this case).
    symmetric_diff = sorted(a.symmetric_difference(b))
    
    # Iterate through the sorted list of elements from the symmetric difference
    # and print each element on a new line.
    for num in symmetric_diff:
        print(num)

    # Example Usage:
    # Input:
    # 9
    # 1 2 3 4 5 6 7 8 9
    # 9
    # 10 1 2 11 21 55 6 8
    #
    # Trace:
    # a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # b = {10, 1, 2, 11, 21, 55, 6, 8}
    #
    # Intersection (elements in both): {1, 2, 6, 8}
    # Union (all unique elements): {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 55}
    #
    # Symmetric Difference (union - intersection):
    # {3, 4, 5, 7, 9, 10, 11, 21, 55}
    #
    # Sorted Symmetric Difference:
    # [3, 4, 5, 7, 9, 10, 11, 21, 55]
    #
    # Output:
    # 3
    # 4
    # 5
    # 7
    # 9
    # 10
    # 11
    # 21
    # 55
