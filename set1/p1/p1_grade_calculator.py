# Name: Liezelle Mangunay
# Course/Section: BSIT - [Your Section]
# Activity: P1 - Student Grade Calculator
# Date: November 17, 2026

def main():
    print("========================================")
    print("       STUDENT GRADE CALCULATOR         ")
    print("========================================")

    while True:
        full_name = input("\nEnter Student's Full Name: ").strip()
        student_id = input("Enter Student ID: ").strip()

        try:
            score1 = float(input("Enter Subject 1 Score (0-100): "))
            score2 = float(input("Enter Subject 2 Score (0-100): "))
            score3 = float(input("Enter Subject 3 Score (0-100): "))
        except ValueError:
            print("Invalid input! Please enter numeric values for scores.")
            continue

        is_valid = (
            (0 <= score1 <= 100)
            and (0 <= score2 <= 100)
            and (0 <= score3 <= 100)
        )

        if not is_valid:
            print("Error: All three scores must be between 0 and 100.")
            continue

        average = (score1 + score2 + score3) / 3

        if average >= 90:
            letter_grade = "A"
        elif average >= 80:
            letter_grade = "B"
        elif average >= 70:
            letter_grade = "C"
        elif average >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"

        remark = "Passed" if average >= 75 else "Failed"

        print("\n----------------------------------------")
        print(f"Student Name : {full_name}")
        print(f"Student ID   : {student_id}")
        print(f"Scores       : {score1:.2f}, {score2:.2f}, {score3:.2f}")
        print(f"Average      : {average:.2f}")
        print(f"Letter Grade : {letter_grade}")
        print(f"Remark       : {remark}")
        print("----------------------------------------")

        choice = input("\nCalculate another student? (yes / no / exit): ").strip().lower()
        if choice == "no" or choice == "exit":
            print("\nExiting Student Grade Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()