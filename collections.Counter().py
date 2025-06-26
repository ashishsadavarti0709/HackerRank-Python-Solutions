# Name: Ashish Sadavarti
# Code: Shoe Shop Sales Calculator
# Code Description: Calculates the total earnings for a shoe shop based on available
#                   shoe sizes and customer requests, utilizing the collections.Counter.
# Copyright 2025

# This script simulates a shoe shop's sales. It takes an initial inventory of shoe sizes,
# then processes customer requests. For each customer, it checks if the requested shoe
# size is available. If it is, the shoe is sold, and the price is added to the total earnings.
# The `collections.Counter` class is used for efficient management of shoe inventory.

from collections import Counter # Import the Counter class from the collections module.

if __name__ == '__main__':
    try:
        # Read the total number of shoes in the shop (N).
        # Although N is read, it's implicitly handled by the next input line for shoe sizes.
        n = int(input("Enter the total number of shoes (N): "))

        # Read the space-separated list of available shoe sizes.
        # map(int, input().split()) converts the string of numbers to a list of integers.
        shoe_sizes_str = input("Enter the space-separated shoe sizes available: ")
        shoe_sizes = list(map(int, shoe_sizes_str.split()))

        # Create a Counter object from the list of shoe sizes.
        # This efficiently stores the count of each shoe size available in inventory.
        # Example: Counter([10, 9, 10, 8, 9, 10]) -> {10: 3, 9: 2, 8: 1}
        available_shoes = Counter(shoe_sizes)

        # Read the number of customers (X).
        customer_count = int(input("Enter the number of customers (X): "))

        total_earned = 0 # Initialize the total earnings to zero.

        print(f"Enter {customer_count} customer requests (size price):")
        # Loop through each customer's request.
        for i in range(customer_count):
            # Read the customer's requested shoe size and the price they are willing to pay.
            # Example input: "10 200" means size 10, price 200.
            size_str, price_str = input(f"Customer {i+1} request (size price): ").split()
            size = int(size_str)
            price = int(price_str)
            
            # Check if the requested 'size' is available in the inventory (i.e., its count is > 0).
            if available_shoes[size] > 0:
                # If available, add the 'price' to the 'total_earned'.
                total_earned += price
                # Decrement the count of the sold shoe size in the inventory.
                available_shoes[size] -= 1
            # If the shoe size is not available (count is 0), nothing happens, and the loop continues.

        # Print the final total amount earned.
        print("\nTotal amount earned:", total_earned)

    except ValueError:
        # Handle cases where input is not a valid integer or format is incorrect.
        print("Invalid input. Please ensure all numbers are integers and formats are correct.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

