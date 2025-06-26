# Name: Ashish Sadavarti
# Code: Collections Namedtuple: Student Marks Calculator
# Code Description: Demonstrates collections.namedtuple to calculate the average
#                   marks of students from tabular data input.
# Copyright 2025

# This script utilizes `collections.namedtuple` to represent student records.
# It reads student data (including marks) and calculates the average marks
# across all students. `namedtuple` provides a lightweight, immutable object type
# that allows accessing fields by name, making the code more readable than
# using plain tuples or dictionary lookups.

from collections import namedtuple # Import the namedtuple factory function.

if __name__ == '__main__':
    try:
        # Read the total number of students.
        # This determines how many student records will follow.
        n = int(input("Enter the total number of students (N): "))

        # Read the column headers (field names) for the student data.
        # These will be used to define the namedtuple fields.
        # Example: "ID MARKS NAME CLASS"
        columns_str = input("Enter column headers (space-separated, e.g., 'ID MARKS NAME CLASS'): ")
        columns = columns_str.split()

        # Check if 'MARKS' is one of the columns. If not, the script will fail later.
        if 'MARKS' not in columns:
            print("Error: 'MARKS' column not found in provided headers. Please ensure 'MARKS' is included.")
            # Exit or raise an error to prevent further execution with incorrect setup.
            exit() 

        # Dynamically create a namedtuple class named 'Student'.
        # The first argument is the type name, the second is a list of field names.
        # This makes each student record an object with accessible attributes like student.ID, student.MARKS.
        Student = namedtuple('Student', columns)

        total_marks = 0 # Initialize a variable to accumulate total marks.

        print(f"Enter data for {n} students, matching the order of headers ('{columns_str}'):")
        # Loop 'n' times to read data for each student.
        for i in range(n):
            # Read a line of student data (e.g., "1 90 John 12").
            # Student(*input().split()) creates a Student namedtuple instance.
            # The '*' unpacks the list of strings from split() as arguments to the namedtuple constructor.
            # Example: Student('1', '90', 'John', '12')
            
            student_data_str = input(f"Enter data for student {i+1} (space-separated): ")
            current_student = Student(*student_data_str.split())
            
            # Access the 'MARKS' field using dot notation and convert it to an integer.
            # Add these marks to the total.
            total_marks += int(current_student.MARKS)

        # Calculate the average marks.
        # If n is 0, this would lead to ZeroDivisionError, so handle that case.
        if n > 0:
            average_marks = total_marks / n
            # Print the average marks, formatted to two decimal places for clarity.
            print(f"\nAverage Marks: {average_marks:.2f}")
        else:
            print("\nNo student data entered. Average marks cannot be calculated.")

    except ValueError:
        # Handle cases where input for N or marks are not valid integers.
        print("Invalid input. Please ensure N and MARK values are integers.")
    except Exception as e:
        # Catch any other unexpected errors during execution (e.g., mismatch in columns).
        print(f"An unexpected error occurred: {e}. Make sure input matches headers.")

