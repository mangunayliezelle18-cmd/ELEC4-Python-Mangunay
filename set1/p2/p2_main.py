# Name: Liezelle Mangunay
# Section: IV-BSIT [Your Section]
# Activity: P2 - Main Program using Custom Module
# Date: November 21, 2026

# Import style 1: import module
import datetime
import student_utils

# Import style 2: from module import name
from student_utils import get_highest, get_lowest

print("=== Student Grade Report (Using Custom Module) ===")
student_name = input("Enter Student Name: ")

# Ask how many subjects to enter
count = int(input("How many grades will you enter? "))
grades = []

i = 0
while i < count:
    grade = float(input("Enter grade #" + str(i + 1) + " (0-100): "))
    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a number between 0 and 100.")
    else:
        grades.append(grade)
        i = i + 1

# Use functions from student_utils (both import styles)
avg = student_utils.compute_average(grades)
status = student_utils.get_status(avg)
highest = get_highest(grades)
lowest = get_lowest(grades)

# Use built-in datetime module to get current date and time
now = datetime.datetime.now()
date_generated = now.strftime("%Y-%m-%d %H:%M:%S")

# Display the report
print("\n--- Grade Summary ---")
print("Student Name:", student_name)
print("Grades Entered:", grades)
print("Average:", round(avg, 2))
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Status:", status)
print("Report Generated On:", date_generated)