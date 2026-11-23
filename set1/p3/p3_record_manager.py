# Name: Liezelle Mangunay
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 21, 2026

def add_student(students, names_set):
    # Read student name and reject blank inputs
    name = input("Enter student name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    # Check lowercase set to prevent case-insensitive duplicate entries
    if name.lower() in names_set:
        print(name + " is already in the list.")
    else:
        students.append(name)
        names_set.add(name.lower())
        print(name + " added.")

def remove_student(students, names_set):
    # Verify if the student exists in the set before searching the list
    name = input("Enter student name to remove: ").strip()
    if name.lower() not in names_set:
        print(name + " not found.")
        return

    # Remove matching student from both the list and the tracking set
    for s in students:
        if s.lower() == name.lower():
            students.remove(s)
            names_set.remove(name.lower())
            print(s + " removed.")
            break

def search_student(students):
    # Collect all student names matching the search keyword (case-insensitive)
    keyword = input("Search name: ").strip().lower()
    found = []

    for s in students:
        if keyword in s.lower():
            found.append(s)

    # Sort and display numbered matches, or inform the user if none were found
    if len(found) == 0:
        print("No student matched your search.")
    else:
        found.sort()
        for i in range(len(found)):
            print(str(i + 1) + ". " + found[i])

def display_students(students):
    # Sort student names alphabetically and print numbered entries with total count
    if len(students) == 0:
        print("No records yet.")
    else:
        sorted_students = sorted(students)
        for i in range(len(sorted_students)):
            print(str(i + 1) + ". " + sorted_students[i])
        print("Total students:", len(sorted_students))

# Initialize list for ordered student records and set for fast duplicate checks
students = []
names_set = set()
choice = ""

# Loop main menu until user selects option 5 to exit
while choice != "5":
    print("\n--- Student Record Manager ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")
    choice = input("Select (1-5): ").strip()

    # Route selected menu choice to the corresponding handler function
    if choice == "1":
        add_student(students, names_set)
    else:
        if choice == "2":
            remove_student(students, names_set)
        else:
            if choice == "3":
                search_student(students)
            else:
                if choice == "4":
                    display_students(students)
                else:
                    if choice == "5":
                        print("Program ended.")
                    else:
                        print("Invalid choice, try again.")

# A list keeps items in order, allows duplicates, and can be sorted, while a set only stores
# unique values and checks if an item already exists much faster. In this program, I used a list
# to hold the actual student names so they can be sorted alphabetically when displayed. I used a
# set to store the lowercase versions of the names so I can easily block duplicate entries even
# if the user types different capitalizations.