# Name: Ashish Sadavarti
# Code: Finding the Percentage (Average Score)
# Code Description: Reads student names and their scores, then calculates and prints
#                   the average score for a queried student.
# Copyright 2025

# This script calculates the average percentage score for a specific student.
# It first takes input for multiple students, each with a name and a list of scores.
# This data is stored in a dictionary where keys are student names and values are their scores.
# Finally, it takes a query student name and prints their average score, formatted to two decimal places.

if __name__ == '__main__':
    print("--- Student Average Score Calculator ---")
    
    try:
        # Read the number of students.
        n = int(input("Enter the number of students: "))

        if n < 0:
            print("Number of students cannot be negative.")
            exit()

        # Initialize an empty dictionary to store student marks.
        # Key: student name (str), Value: list of scores (floats).
        student_marks = {}

        print(f"\nEnter data for {n} students (Name Score1 Score2 ...):")
        # Loop 'n' times to read data for each student.
        for i in range(n):
            # Read a line of input. Example: "Harry 85.5 90.0 78.5"
            # .split() splits the line by spaces.
            # `name, *line` uses extended unpacking: `name` gets the first part,
            # and `*line` collects all remaining parts into a list.
            student_data_str = input(f"Student {i+1} (Name Score1 Score2 ...): ").split()
            name = student_data_str[0] # The first part is the name.
            
            # The rest of the parts are scores. Convert them to floats.
            # If `student_data_str[1:]` is empty (only name provided), `scores` will be an empty list.
            scores = list(map(float, student_data_str[1:]))
            
            # Store the name and scores in the dictionary.
            student_marks[name] = scores

        # Get the name of the student for whom to calculate the average.
        query_name = input("\nEnter the name of the student to query: ").strip()

        # Check if the queried student exists in the dictionary.
        if query_name not in student_marks:
            print(f"Error: Student '{query_name}' not found in records.")
            exit()
            
        # Retrieve the list of scores for the queried student.
        # It's explicitly converted to a list here, though it's already a list from `student_marks[query_name]`.
        list_of_scores = list(student_marks[query_name])
        
        # Check if the student has any scores recorded.
        if not list_of_scores:
            print(f"Student '{query_name}' has no scores recorded.")
            exit()

        # Calculate the sum of scores.
        total_score = sum(list_of_scores)
        
        # Calculate the average (result).
        # Division by `len(list_of_scores)` gives the average.
        average_score = total_score / len(list_of_scores)
        
        # Print the result formatted to two decimal places.
        # '%.2f' % average_score is an older but common way to format floats.
        print('%.2f' % average_score)

    except ValueError:
        # Handle cases where scores are not valid numbers.
        print("Invalid input. Please ensure scores are numeric.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

