# Name: Liezelle Mangunay
# Section: IV-BSIT C
# Activity: P2 - Custom Module (student_utils)
# Date: November 21, 2026

def compute_average(grades):
    total = sum(grades)
    count = len(grades)
    return total / count

def get_status(average):
    if average >= 75:
        return "Passed"
    else:
        return "Failed"

def get_highest(grades):
    return max(grades)

def get_lowest(grades):
    return min(grades)