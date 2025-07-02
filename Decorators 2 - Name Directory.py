# Name: Ashish Sadavarti
# Code: Decorators: Person Lister and Name Directory
# Code Description: Demonstrates a Python decorator that sorts a list of people
#                   by age and then applies a formatting function to each person.
# Copyright 2025

# This script illustrates the concept of decorators in Python.
# Specifically, it defines a decorator `person_lister` that can be applied
# to a function. When a list of people's data is passed to the decorated function,
# the decorator first sorts these people based on their age (assumed to be at index 2
# in their data). After sorting, it applies the original (decorated) function
# to each person and returns a list of the results.

def person_lister(f):
    """
    A decorator that sorts a list of people by their age (assumed to be
    the third element, index 2, in each person's data) before applying
    the decorated function to each person.

    Parameters:
    f (function): The function to be decorated. This function is expected
                  to take a single 'person' data structure (e.g., a list/tuple)
                  as its argument.

    Returns:
    function: An inner function that takes a list of 'people' as an argument.
              This inner function will sort the 'people' and then apply 'f'
              to each person.
    """
    def inner(people):
        """
        The inner function returned by the person_lister decorator.
        It sorts the input 'people' list by age and then applies the
        decorated function 'f' to each sorted person.

        Parameters:
        people (list of lists/tuples): A list where each element is a person's data.
                                       Each person's data is expected to be
                                       [first_name, last_name, age_str, gender_char].
        """
        # Sort the 'people' list in-place.
        # The 'key' argument uses a lambda function:
        #   `lambda person: int(person[2])`
        # This means for each `person` (which is a sub-list/tuple like ['John', 'Doe', '30', 'M']),
        # it extracts the element at index 2 (the age string, e.g., '30'), converts it to an integer,
        # and uses this integer for sorting. This ensures numerical sorting by age.
        people.sort(key=lambda person: int(person[2]))

        # After sorting, apply the original function 'f' to each 'person' in the sorted list.
        # A list comprehension `[f(person) for person in people]` builds the new list
        # containing the results of applying 'f' to each person.
        return [f(person) for person in people]
    return inner

# Example Usage:
# Define a function that will be decorated.
# This function 'name_format' takes a person's data (list) and formats their name.
# It assumes person data is in the format: [first_name, last_name, age, gender]
@person_lister
def name_format(person):
    """
    Formats a person's name based on their gender.
    Assumes person = [first_name, last_name, age_str, gender_char].
    """
    first_name = person[0]
    last_name = person[1]
    gender = person[3] # 'M' or 'F'

    if gender == 'M':
        return "Mr. " + first_name + " " + last_name
    else: # Assuming 'F' or any other character for female
        return "Ms. " + first_name + " " + last_name

if __name__ == '__main__':
    print("--- Decorator: Person Lister Example ---")
    print("This program will sort a list of people by age and format their names.")
    
    try:
        # Get the number of people from user input.
        n = int(input("Enter the number of people: "))

        # Prepare a list to store raw person data.
        raw_people_data = []
        print("Enter data for each person (first_name last_name age gender, e.g., 'John Doe 30 M'):")
        for i in range(n):
            person_info = input(f"Person {i+1}: ").strip().split()
            # Basic validation to ensure sufficient data points
            if len(person_info) < 4:
                print("Warning: Insufficient data for person. Skipping this entry.")
                continue
            raw_people_data.append(person_info)

        # Call the decorated function with the raw people data.
        # The `person_lister` decorator will first sort `raw_people_data` by age,
        # and then call `name_format` on each sorted person.
        formatted_names = name_format(raw_people_data)

        print("\nFormatted names (sorted by age):")
        for name in formatted_names:
            print(name)

    except ValueError:
        print("Invalid input. Please ensure age is an integer and inputs are space-separated.")
    except IndexError:
        print("Input format error. Ensure each person's data has at least 4 parts (first_name, last_name, age, gender).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

