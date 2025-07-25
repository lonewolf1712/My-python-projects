# Student Management System (Console-Based)

# A dictionary to store student records.
# Key: Student ID (integer)
# Value: Dictionary containing student details (Name, Age, Grade)
students = {}

def add_student():
    """Adds a new student record to the system."""
    try:
        student_id = int(input("Enter Student ID: "))
        if student_id in students:
            print("Error: Student with this ID already exists.")
            return

        name = input("Enter Student Name: ").strip()
        if not name:
            print("Error: Student name cannot be empty.")
            return

        age = int(input("Enter Student Age: "))
        if age <= 0:
            print("Error: Age must be a positive number.")
            return

        grade = input("Enter Student Grade: ").strip()
        if not grade:
            print("Error: Grade cannot be empty.")
            return

        students[student_id] = {
            "Name": name,
            "Age": age,
            "Grade": grade
        }
        print(f"Student {name} (ID: {student_id}) added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number for ID and Age.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def view_student():
    """Displays details of a specific student or all students."""
    if not students:
        print("\nNo student records available.")
        return

    while True:
        choice = input("View (S)pecific student or (A)ll students? (S/A): ").strip().lower()
        if choice == 's':
            try:
                student_id = int(input("Enter Student ID to view: "))
                if student_id in students:
                    print(f"\n--- Details for Student ID: {student_id} ---")
                    for key, value in students[student_id].items():
                        print(f"{key}: {value}")
                    print("---------------------------------")
                else:
                    print("Student not found.")
                break # Exit loop after viewing specific student
            except ValueError:
                print("Invalid input. Please enter a valid number for Student ID.")
        elif choice == 'a':
            print("\n--- All Student Records ---")
            for student_id, details in students.items():
                print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}")
            print("---------------------------")
            break # Exit loop after viewing all students
        else:
            print("Invalid choice. Please enter 'S' or 'A'.")


def update_student():
    """Updates an existing student's record."""
    if not students:
        print("No student records to update.")
        return

    try:
        student_id = int(input("Enter Student ID to update: "))
        if student_id not in students:
            print("Student not found.")
            return

        print(f"\n--- Current Details for ID: {student_id} ---")
        for key, value in students[student_id].items():
            print(f"{key}: {value}")
        print("---------------------------------")

        print("\nWhat would you like to update?")
        print("1. Name")
        print("2. Age")
        print("3. Grade")
        update_choice = input("Enter your choice (1-3): ").strip()

        if update_choice == '1':
            new_name = input("Enter new Name: ").strip()
            if new_name:
                students[student_id]["Name"] = new_name
                print("Name updated successfully.")
            else:
                print("Name cannot be empty.")
        elif update_choice == '2':
            try:
                new_age = int(input("Enter new Age: "))
                if new_age > 0:
                    students[student_id]["Age"] = new_age
                    print("Age updated successfully.")
                else:
                    print("Age must be a positive number.")
            except ValueError:
                print("Invalid input for Age.")
        elif update_choice == '3':
            new_grade = input("Enter new Grade: ").strip()
            if new_grade:
                students[student_id]["Grade"] = new_grade
                print("Grade updated successfully.")
            else:
                print("Grade cannot be empty.")
        else:
            print("Invalid update choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number for Student ID.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def delete_student():
    """Deletes a student record from the system."""
    if not students:
        print("No student records to delete.")
        return

    try:
        student_id = int(input("Enter Student ID to delete: "))
        if student_id in students:
            del students[student_id]
            print(f"Student ID {student_id} deleted successfully.")
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number for Student ID.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the Student Management System."""
    print("--- Welcome to Student Management System ---")
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. View Student(s)")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
