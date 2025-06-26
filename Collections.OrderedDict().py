# Name: Ashish Sadavarti
# Code: Collections OrderedDict: Item Sales Aggregator
# Code Description: Aggregates item prices from input, maintaining insertion order,
#                   using collections.OrderedDict.
# Copyright 2025

# This script demonstrates the use of `collections.OrderedDict` to process a list
# of sales entries. For each entry, it extracts the item name and its price.
# If an item appears multiple times, its prices are summed up.
# Crucially, `OrderedDict` ensures that the items are stored and printed
# in the order they were first encountered (insertion order).

from collections import OrderedDict # Import OrderedDict from the collections module.

if __name__ == '__main__':
    try:
        # Read the number of entries (lines of item sales data).
        n = int(input("Enter the total number of item entries (N): ").strip())

        # Create an OrderedDict instance.
        # OrderedDict maintains the order in which items are inserted.
        items = OrderedDict()

        print(f"Enter {n} item entries (e.g., 'BANANA FRIES 12', 'POTATO CHIPS 30'):")
        # Loop 'n' times to read each item entry.
        for i in range(n):
            # Read a line representing an item entry.
            # .strip() removes leading/trailing whitespace.
            # .split() splits the line into a list of strings by spaces.
            # Example input: "BANANA FRIES 1000" -> entry = ['BANANA', 'FRIES', '1000']
            entry_str = input(f"Entry {i+1}: ").strip()
            entry = entry_str.split()
            
            # The item name can consist of multiple words, but the price is always the last element.
            # ' '.join(entry[:-1]) reconstructs the item name by joining all parts except the last one.
            # entry[:-1] creates a slice of the list containing all elements except the last.
            item_name = ' '.join(entry[:-1])
            
            # The last element is the price; convert it to an integer.
            price = int(entry[-1])
            
            # Check if the item_name already exists as a key in the OrderedDict.
            if item_name in items:
                # If it exists, add the current price to its existing total.
                items[item_name] += price
            else:
                # If it's a new item, add it to the OrderedDict with its price.
                # This insertion maintains the order.
                items[item_name] = price

        print("\nAggregated Item Sales (in insertion order):")
        # Iterate through the OrderedDict.
        # .items() returns a view of key-value pairs.
        # Due to OrderedDict's nature, this loop processes items in their insertion order.
        for item_name, net_price in items.items():
            # Print each item name and its aggregated price, separated by a space.
            print(item_name, net_price)

    except ValueError:
        # Handle cases where N or the price part of an entry is not a valid integer.
        print("Invalid input. Please ensure N and prices are integers.")
    except IndexError:
        # Handle cases where an entry line doesn't contain enough parts (e.g., just a name without price).
        print("Input error: Each entry must have an item name and a price.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

