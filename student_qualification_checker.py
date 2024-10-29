# Author: Joshua Nobel
# File: student_qualification_checker.py
# Description: This application accepts student names and GPA, then determines if they qualify for the Dean's List or Honor Roll. 
# The program stops when the user enters 'ZZZ' for the last name.

def main():
    while True:
        # Get the student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name.upper() == 'ZZZ':
            print("Exiting the application.")
            break

        # Get the student's first name
        first_name = input("Enter the student's first name: ")

        # Get the student's GPA
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input for GPA. Please enter a numeric value.")
            continue

        # Check qualifications for Dean's List and Honor Roll
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

# Run the main function
if __name__ == "__main__":
    main()
