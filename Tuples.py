# Name: Ashish Sadavarti
# Code: TupleHashing
# Code Description: Reads a list of integers from user input, converts them into a tuple,
#                   and then calculates and prints the hash value of that tuple.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of integers.
    # While 'n' is read, its value is not directly used in the current problem's logic
    # beyond implicitly defining how many integers to expect in the next line.
    n = int(input())
    
    # Read a line of space-separated integers, convert them to integers,
    # and create a map object.
    # Example Input: "1 2 3 4 5"
    integer_list = map(int, input().split())
    
    # Convert the map object (which behaves like an iterable) into a tuple.
    # Tuples are ordered, immutable collections of items.
    # Being immutable, tuples can be hashed and used as keys in dictionaries
    # or as elements in sets.
    t = tuple(integer_list)
    
    # Calculate and print the hash value of the tuple.
    # hash(): Returns the hash value of an object if it is hashable.
    # Hashable objects have a hash value that never changes during their lifetime
    # and can be compared to other objects.
    # Immutable types like tuples (if their contents are also immutable), strings,
    # and numbers are hashable. Mutable types like lists and dictionaries are not.
    print(hash(t))

    # Example:
    # Input:
    # 3
    # 1 2 3
    #
    # Trace:
    # n = 3
    # integer_list (map object for) [1, 2, 3]
    # t = (1, 2, 3)
    # print(hash((1, 2, 3)))
    #
    # The hash value will be an integer, which might vary between Python runs/versions.
    # Example Output: (A specific integer value, e.g., 2528502973977322830)
