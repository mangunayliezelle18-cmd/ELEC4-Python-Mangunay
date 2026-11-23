# Name: Liezelle Mangunay
# Course/Section: BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 17, 2026

PASSING_SCORE = 75

def validate_scores(s1, s2, s3):
    # Ensure all three subject scores fall within the valid 0-100 range
    return (0 <= s1 <= 100) and (0 <= s2 <= 100) and (0 <= s3 <= 100)

def compute_average(s1, s2, s3):
    # Sum the three scores and divide by 3 to get the floating-point average
    total = s1 + s2 + s3
    return total / 3

def get_letter_grade(avg):
    # Determine letter grade equivalent using nested conditional branches
    if avg >= 90:
        return "A"
    else:
        if avg >= 80:
            return "B"
        else:
            if avg >= 70:
                return "C"
            else:
                if avg >= 60:
                    return "D"
                else:
                    return "F"

def get_remark(avg):
    # Compare average against the global passing threshold
    if avg >= PASSING_SCORE:
        return "Passed"
    else:
        return "Failed"

def main():
    print("========================================")
    print("       STUDENT GRADE CALCULATOR         ")
    print("========================================")

    # Loop continuously until the user chooses to exit
    while True:
        full_name = input("\nEnter Student's Full Name: ").strip()
        student_id = input("Enter Student ID: ").strip()

        try:
            # Convert user score inputs into floating-point numbers
            score1 = float(input("Enter Subject 1 Score (0-100): "))
            score2 = float(input("Enter Subject 2 Score (0-100): "))
            score3 = float(input("Enter Subject 3 Score (0-100): "))
        except ValueError:
            # Catch non-numeric inputs and restart the prompt
            print("Invalid input! Please enter numeric values for scores.")
            continue

        # Reject out-of-range scores before computing grades
        if not validate_scores(score1, score2, score3):
            print("Error: All three scores must be between 0 and 100.")
            continue

        # Compute final average, letter grade, and pass/fail remark
        average = compute_average(score1, score2, score3)
        letter_grade = get_letter_grade(average)
        remark = get_remark(average)

        # Display formatted student grade summary
        print("\n----------------------------------------")
        print(f"Student Name : {full_name}")
        print(f"Student ID   : {student_id}")
        print(f"Scores       : {score1:.2f}, {score2:.2f}, {score3:.2f}")
        print(f"Average      : {average:.2f}")
        print(f"Letter Grade : {letter_grade}")
        print(f"Remark       : {remark}")
        print("----------------------------------------")

        # Ask user whether to process another student or exit
        choice = input("\nCalculate another student? (yes / no / exit): ").strip().lower()
        if choice == "no" or choice == "exit":
            print("\nExiting Student Grade Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()

# A local variable is declared inside a function and can only be used within that specific
# function, such as 'total' inside compute_average() and 'average' inside main(). A global
# variable is declared outside all functions and can be accessed throughout the entire program,
# such as 'PASSING_SCORE' at the top of this file. Separating local variables from global ones
# keeps each function independent and prevents unintended changes to shared values.