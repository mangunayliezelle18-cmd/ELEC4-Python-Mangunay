# Name: Liezelle Mangunay
# Section: IV-BSIT C
# Activity: P2 - Main Program using Custom Module
# Date: November 21, 2026

import datetime
import student_utils
from student_utils import get_highest, get_lowest

print("=== Student Grade Report (Using Custom Module) ===")
student_name = input("Enter Student Name: ")

# Ask how many grades to process and initialize an empty list
count = int(input("How many grades will you enter? "))
grades = []

# Loop until the requested number of valid grades (0-100) are collected
i = 0
while i < count:
    grade = float(input("Enter grade #" + str(i + 1) + " (0-100): "))
    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a number between 0 and 100.")
    else:
        grades.append(grade)
        i = i + 1

# Compute grade metrics using both module-level and directly imported functions
avg = student_utils.compute_average(grades)
status = student_utils.get_status(avg)
highest = get_highest(grades)
lowest = get_lowest(grades)

# Capture and format the current timestamp for the report
now = datetime.datetime.now()
date_generated = now.strftime("%Y-%m-%d %H:%M:%S")

# Display the complete student grade summary
print("\n--- Grade Summary ---")
print("Student Name:", student_name)
print("Grades Entered:", grades)
print("Average:", round(avg, 2))
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Status:", status)
print("Report Generated On:", date_generated)