# Name: Liezelle Mangunay
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 23, 2026

def divide_numbers():
    try:
        # Convert user inputs to float and compute the quotient
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
    except ValueError:
        # Handle non-numeric inputs (e.g., letters or symbols)
        print("Error: Invalid input. Please enter numeric values only.")
    except ZeroDivisionError:
        # Prevent crash when the second number is zero
        print("Error: Cannot divide by zero.")
    else:
        # Runs only when division succeeds without raising an exception
        print(f"Result: {num1} / {num2} = {result:.2f}")
    finally:
        # Always executes regardless of whether an error occurred
        print("Division operation finished.\n")


def open_text_file():
    filename = input("Enter file name to open (e.g., README.md): ").strip()
    try:
        # Attempt to open and read the specified file safely
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: The file '{filename}' was not found.\n")
    except PermissionError:
        # Handle restricted file access permissions
        print(f"Error: Permission denied when opening '{filename}'.\n")
    else:
        # Display file contents if reading succeeded
        print("\n--- File Contents ---")
        print(content if content else "(File is empty)")
        print("---------------------\n")
    finally:
        # Runs after file operation completes or fails
        print("File read operation finished.\n")


def display_menu():
    # Display the main menu options
    print("=== Safe Menu Program ===")
    print("1. Divide Two Numbers")
    print("2. Open and Read a File")
    print("3. Exit")


def main():
    # Loop menu continuously until the user selects option 3 to exit
    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()

        # Route user choice to the corresponding function or re-prompt on invalid input
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_text_file()
        elif choice == "3":
            print("Exiting Safe Menu Program. Goodbye!")
            break
        else:
            print("Invalid menu selection. Please choose 1, 2, or 3.\n")


if __name__ == "__main__":
    main()