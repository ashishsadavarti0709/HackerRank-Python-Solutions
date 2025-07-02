# Name: Ashish Sadavarti
# Code: Default Arguments: Stream Processor
# Code Description: Demonstrates default arguments in Python by processing
#                   numerical streams (even/odd) and handling custom stream inputs.
# Copyright 2025

# This script illustrates the concept of default arguments in Python functions,
# specifically how they are evaluated once when the function is defined,
# and how to handle mutable default arguments (e.g., by using None as a sentinel).
# It simulates processing data from different types of numerical streams.

class Stream(object):
    """
    Base class for a numerical stream.
    Subclasses should implement the `get_next()` method.
    """
    def __init__(self):
        self.current = 0 # Initialize a counter or current value for the stream.

    def get_next(self):
        """
        Abstract method: Should return the next value in the stream.
        This method must be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement 'get_next' method.")

class EvenStream(Stream):
    """
    A stream that generates consecutive even numbers.
    Starts from 0, then 2, 4, 6, ...
    """
    def __init__(self):
        super().__init__() # Call the base class constructor.
        self.current = 0   # Even numbers start from 0.

    def get_next(self):
        """
        Returns the next even number in the stream.
        """
        val = self.current
        self.current += 2 # Increment by 2 for the next even number.
        return val

class OddStream(Stream):
    """
    A stream that generates consecutive odd numbers.
    Starts from 1, then 3, 5, 7, ...
    """
    def __init__(self):
        super().__init__() # Call the base class constructor.
        self.current = 1   # Odd numbers start from 1.

    def get_next(self):
        """
        Returns the next odd number in the stream.
        """
        val = self.current
        self.current += 2 # Increment by 2 for the next odd number.
        return val

def print_from_stream(n, stream=None):
    """
    Prints 'n' numbers from a given stream.

    If no stream is provided (i.e., `stream` is None), it defaults to an
    `EvenStream` instance. This is a common pattern to handle mutable default
    arguments: using `None` as a sentinel and assigning the default inside
    the function body, ensuring a new instance is created on each call if needed.

    Parameters:
    n (int): The number of values to print from the stream.
    stream (Stream, optional): An instance of a Stream subclass (e.g., EvenStream, OddStream).
                               Defaults to a new EvenStream if not provided.
    """
    if stream is None:
        # If no stream object is explicitly passed, create a new EvenStream.
        # This prevents issues with a single mutable default object being shared across calls.
        stream = EvenStream()
    
    # Loop 'n' times to get and print 'n' numbers from the stream.
    for _ in range(n):
        print(stream.get_next())

if __name__ == '__main__':
    print("--- Default Arguments: Stream Processor Example ---")
    print("This program demonstrates using default arguments with stream objects.")
    
    try:
        # Read the number of test cases.
        queries = int(input("Enter the number of test cases: "))
        
        print("\nFor each test case, enter two lines:")
        print("1. Query type (e.g., 'even', 'odd', 'custom')")
        print("2. The number of values to print (n)")

        # Process each test case.
        for i in range(queries):
            print(f"\n--- Test Case {i+1} ---")
            query_type = input("Enter query type ('even', 'odd', or 'custom' for no explicit stream): ").strip().lower()
            n_values = int(input("Enter number of values to print (n): "))

            if query_type == "even":
                # Explicitly pass an EvenStream instance.
                print("Printing from EvenStream:")
                print_from_stream(n_values, EvenStream())
            elif query_type == "odd":
                # Explicitly pass an OddStream instance.
                print("Printing from OddStream:")
                print_from_stream(n_values, OddStream())
            elif query_type == "custom":
                # No stream passed, so print_from_stream will use its default (EvenStream).
                print("Printing with default stream (EvenStream):")
                print_from_stream(n_values)
            else:
                print("Invalid query type. Skipping this test case.")
                
    except ValueError:
        print("Invalid input. Please ensure 'n' is an integer and query type is valid.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

