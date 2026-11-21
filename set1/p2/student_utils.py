# Name: Liezelle Mangunay
# Section: IV-BSIT [Your Section]
# Activity: P2 - Custom Module (student_utils)
# Date: November 21, 2026

# Function to compute the average of a list of grades
def compute_average(grades):
    total = sum(grades)
    count = len(grades)
    return total / count

# Function to determine if the average is Passed or Failed (passing is 75)
def get_status(average):
    if average >= 75:
        return "Passed"
    else:
        return "Failed"

# Function to get the highest grade
def get_highest(grades):
    return max(grades)

# Function to get the lowest grade
def get_lowest(grades):
    return min(grades)