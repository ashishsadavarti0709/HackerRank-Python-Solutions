# Name: Ashish Sadavarti
# Code: List Operations Executor
# Code Description: Processes a series of commands to manipulate a Python list,
#                   including insert, print, remove, append, sort, pop, and reverse.
# Copyright 2025

# This script simulates a command-line interface for manipulating a Python list.
# It reads a number of commands from standard input, each specifying an operation
# to perform on an initially empty list. The supported operations cover common
# list methods.

if __name__ == '__main__':
    print("--- List Operations Executor ---")
    print("This program manipulates a list based on commands you provide.")
    
    lst = [] # Initialize an empty list that will be manipulated.
    
    try:
        # Read the number of commands (operations) to execute.
        n = int(input("Enter the number of commands (N): "))

        if n < 0:
            print("Number of commands cannot be negative.")
            exit()

        print("\nEnter commands (e.g., 'insert 0 5', 'print', 'remove 6', etc.):")
        # Loop 'n' times to read and execute each command.
        for i in range(n):
            # Read a command line and split it into parts by spaces.
            # Example: "insert 0 5" -> `command = ["insert", "0", "5"]`
            command_parts = input(f"Command {i+1}: ").split()
            
            # The first part of the command is the operation name.
            operation = command_parts[0]

            # Use if-elif-else to check the operation and execute the corresponding list method.
            if operation == "insert":
                # 'insert' takes two arguments: index and value.
                # Convert the string parts to integers before inserting.
                if len(command_parts) == 3:
                    index = int(command_parts[1])
                    value = int(command_parts[2])
                    lst.insert(index, value)
                else:
                    print(f"Error: 'insert' command requires 2 arguments (index, value). Got: {command_parts}")
            
            elif operation == "print":
                # 'print' takes no arguments. It prints the current state of the list.
                print(lst)
            
            elif operation == "remove":
                # 'remove' takes one argument: value to remove.
                # It removes the first occurrence of the specified value.
                # Will raise ValueError if the value is not found.
                if len(command_parts) == 2:
                    value_to_remove = int(command_parts[1])
                    try:
                        lst.remove(value_to_remove)
                    except ValueError:
                        print(f"Error: Value {value_to_remove} not found in the list for 'remove' command.")
                else:
                    print(f"Error: 'remove' command requires 1 argument (value). Got: {command_parts}")
            
            elif operation == "append":
                # 'append' takes one argument: value to append.
                # Adds the value to the end of the list.
                if len(command_parts) == 2:
                    value_to_append = int(command_parts[1])
                    lst.append(value_to_append)
                else:
                    print(f"Error: 'append' command requires 1 argument (value). Got: {command_parts}")
            
            elif operation == "sort":
                # 'sort' takes no arguments. Sorts the list in-place.
                lst.sort()
            
            elif operation == "pop":
                # 'pop' takes no arguments. Removes and returns the last item of the list.
                # Will raise IndexError if the list is empty.
                if lst: # Check if list is not empty before popping
                    lst.pop()
                else:
                    print("Error: Cannot 'pop' from an empty list.")
            
            elif operation == "reverse":
                # 'reverse' takes no arguments. Reverses the elements of the list in-place.
                lst.reverse()
            
            else:
                # Handle unknown commands.
                print(f"Error: Unknown command '{operation}'.")

    except ValueError:
        # Catch errors if integers are expected but non-integer input is provided.
        print("Invalid input. Please ensure arguments are integers where required.")
    except IndexError:
        # Catch errors if command parts are missing (e.g., "insert 0" instead of "insert 0 5").
        print("Input error: Missing arguments for the command.")
    except Exception as e:
        # Catch any other unexpected errors.
        print(f"An unexpected error occurred: {e}")

