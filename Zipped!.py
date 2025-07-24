# Name: Ashish Sadavarti
# Code: ZippedScoresAverager
# Code Description: Reads student scores across multiple subjects, then uses
#                   the zip() function to group scores by student and calculates
#                   the average score for each student.
# Copyright 2025

if __name__ == '__main__':
    # Read the number of students (n) and the number of subjects (m) from the first line.
    # input().split(): Reads the line and splits it by whitespace into a list of strings.
    # map(int, ...): Converts each string to an integer.
    # Example Input: "2 3" (2 students, 3 subjects)
    n, m = map(int, input().split())

    # Read 'm' lines of scores. Each line represents the scores of all 'n' students for one subject.
    # The outer list comprehension iterates 'm' times (once for each subject).
    # Inside, input().split() reads a line of space-separated scores.
    # map(float, ...) converts these to float numbers (since scores can be decimals).
    # Example Input (for n=2, m=3):
    # 10 20
    # 30 40
    # 50 60
    # 'scores' would become: [[10.0, 20.0], [30.0, 40.0], [50.0, 60.0]]
    # (Each inner list is a subject's scores for students 1, 2, ..., n)
    scores = [list(map(float, input().split())) for _ in range(m)]

    # Use the zip() function with the unpack (*) operator to transpose the 'scores' list.
    # zip(*scores) takes the 'm' lists (each representing a subject's scores) and
    # groups the i-th element from each list together.
    # This effectively transforms the data from (subject-wise scores) to (student-wise scores).
    #
    # Example (for 'scores' above):
    # scores:
    # [ [10.0, 20.0],  <- Subject 1 scores
    #   [30.0, 40.0],  <- Subject 2 scores
    #   [50.0, 60.0] ] <- Subject 3 scores
    #
    # zip(*scores) will yield:
    # (10.0, 30.0, 50.0)  <- All scores for Student 1
    # (20.0, 40.0, 60.0)  <- All scores for Student 2
    #
    # The list comprehension then iterates through each of these student score tuples.
    # For each 'student_scores' tuple (e.g., (10.0, 30.0, 50.0)):
    #   sum(student_scores) calculates the sum of scores for that student.
    #   / m divides by the total number of subjects ('m') to get the average.
    # 'averages' will be a list of floating-point average scores for each student.
    averages = [sum(student_scores) / m for student_scores in zip(*scores)]

    # Iterate through the list of calculated averages and print each one.
    # f"{average:.1f}": Uses an f-string to format the average to one decimal place.
    # Example (if averages = [30.0, 40.0]):
    # Output:
    # 30.0
    # 40.0
    for average in averages:
        print(f"{average:.1f}")

    # Full Example Trace:
    # Input:
    # 2 3
    # 10 20
    # 30 40
    # 50 60
    #
    # 1. n=2, m=3
    # 2. scores = [[10.0, 20.0], [30.0, 40.0], [50.0, 60.0]]
    # 3. zip(*scores) yields: (10.0, 30.0, 50.0), then (20.0, 40.0, 60.0)
    # 4. For (10.0, 30.0, 50.0): sum = 90.0, avg = 90.0 / 3 = 30.0
    # 5. For (20.0, 40.0, 60.0): sum = 120.0, avg = 120.0 / 3 = 40.0
    # 6. averages = [30.0, 40.0]
    # 7. Print:
    #    30.0
    #    40.0
