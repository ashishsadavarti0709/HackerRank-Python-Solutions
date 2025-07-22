# Name: Ashish Sadavarti
# Code: Nested Lists: Second Lowest Score Students
# Code Description: Processes a list of student names and scores to find all students
#                   who have the second lowest unique score, and prints their names alphabetically.
# Copyright 2025

# This script demonstrates how to work with nested lists in Python, specifically
# to solve a common problem: finding elements based on a ranked numerical value.
# It identifies the second lowest unique score among a group of students and then
# lists the names of all students who achieved that score, sorted alphabetically.

if __name__ == '__main__':
    print("--- Second Lowest Score Students ---")
    print("This program finds students with the second lowest unique score.")
    
    students = [] # Initialize an empty list to store student data.
                  # Each element will be a list: [name (str), score (float)].
    
    try:
        # Read the number of students.
        num_students = int(input("Enter the number of students: "))

        if num_students < 0:
            print("Number of students cannot be negative.")
            exit()

        print(f"\nEnter data for {num_students} students (Name then Score, each on a new line):")
        # Loop to read data for each student.
        for i in range(num_students):
            name = input(f"Enter name for student {i+1}: ").strip()
            score = float(input(f"Enter score for {name}: "))
            students.append([name, score]) # Append the [name, score] pair as a sub-list.
        
        # Check if there are enough students to find a second lowest score.
        # Need at least two unique scores.
        if not students:
            print("No student data entered.")
            exit()

        # Step 1: Find the second lowest unique score.
        # - `[score for name, score in students]`: Extracts all scores into a new list.
        # - `set(...)`: Converts the list of scores into a set, automatically removing duplicates.
        # - `sorted(...)`: Sorts the unique scores in ascending order.
        # - `[1]`: Accesses the element at index 1 (the second element), which will be the
        #   second lowest unique score after sorting.
        
        # Ensure there are at least two unique scores after removing duplicates.
        unique_scores_set = set([score for name, score in students])
        if len(unique_scores_set) < 2:
            print("Error: Not enough unique scores to determine a second lowest score.")
            exit()
            
        sorted_unique_scores = sorted(unique_scores_set)
        second_lowest_score = sorted_unique_scores[1]
        
        # Step 2: Find all students who have this `second_lowest_score`.
        # - `[name for name, score in students if score == second_lowest_score]`:
        #   This list comprehension iterates through the original `students` list.
        #   For each `[name, score]` pair, it checks if `score` is equal to the
        #   `second_lowest_score` we found. If True, it includes `name` in the new list.
        second_lowest_students_names = [name for name, score in students if score == second_lowest_score]
        
        # Step 3: Sort the names of these students alphabetically.
        # `sorted(...)` sorts the list of names in alphabetical order.
        final_sorted_names = sorted(second_lowest_students_names)
        
        print(f"\nStudents with the second lowest score ({second_lowest_score:.2f}):")
        # Print each student name on a new line.
        for student_name in final_sorted_names:
            print(student_name)

    except ValueError:
        # Handle cases where score input is not a valid float.
        print("Invalid input. Please ensure scores are numeric.")
    except IndexError:
        # This might occur if `sorted(set(...))[1]` is attempted on a list with less than 2 unique elements.
        print("Error: Could not find a second lowest score. Make sure you enter at least two distinct scores.")
    except Exception as e:
        # Catch any other unexpected errors during execution.
        print(f"An unexpected error occurred: {e}")

