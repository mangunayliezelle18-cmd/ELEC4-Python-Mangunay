# Name: Liezelle Mangunay
# Section: IV-BSIT C
# Activity: P2 - Custom Module (student_utils)
# Date: November 21, 2026

def compute_average(grades):
    # Add all grades and divide by the total count to get the average
    total = sum(grades)
    count = len(grades)
    return total / count

def get_status(average):
    # Return Passed if average is 75 or above, otherwise Failed
    if average >= 75:
        return "Passed"
    else:
        return "Failed"

def get_highest(grades):
    # Find and return the highest score in the list
    return max(grades)

def get_lowest(grades):
    # Find and return the lowest score in the list
    return min(grades)