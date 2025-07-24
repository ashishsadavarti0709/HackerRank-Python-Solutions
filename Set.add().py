# Name: Ashish Sadavarti
# Code: SetAddOperation
# Code Description: Collects country stamps from user input and counts the
#                   number of unique (distinct) stamps using a set's add() method.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of country stamps that will be entered.
    n = int(input())
    
    # Initialize an empty set to store distinct country stamps.
    # Sets are ideal for this because they automatically handle uniqueness;
    # if you try to add an element that's already present, it simply does nothing.
    distinct_stamps = set()
    
    # Loop 'n' times to read each country stamp.
    for _ in range(n):
        # Read a country stamp (e.g., "UK", "USA", "India").
        country_stamp = input()
        
        # Add the read country stamp to the 'distinct_stamps' set.
        # If the stamp is already in the set, .add() has no effect.
        # If it's a new stamp, it gets added.
        distinct_stamps.add(country_stamp)
    
    # After reading all 'n' stamps, print the total number of unique stamps
    # by getting the length of the 'distinct_stamps' set.
    print(len(distinct_stamps))

    # Example Usage:
    # If input is:
    # 5
    # UK
    # USA
    # India
    # UK
    # Japan
    #
    # The distinct_stamps set would become: {"UK", "USA", "India", "Japan"}
    # The length would be 4.
    # Output: 4
