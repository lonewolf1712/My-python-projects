#Simple note taker
def create_file(file_path=r"C:\Users\Hp\OneDrive\Desktop\Default.txt"):
    try:
        with open(file_path, "w") as file:
            file.write(input("Start writing: "))
            print("File created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    except FileExistsError:
        print("The file you are trying to create already exist.")

def append_file(file_path=r"C:\Users\Hp\OneDrive\Desktop\Default.txt"):
    try:
        with open(file_path, "a") as file:
            file.write(input("What else do you want to write?\n"))
            print("Content appended successfully.")
    except FileNotFoundError:
        print("The file you are trying to find does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_path=r"C:\Users\Hp\OneDrive\Desktop\Default.txt"):
    try:
        with open(file_path, "r") as file:
            context = file.read()
            print("File content:\n", context)
    except FileNotFoundError:
        print("The file you are trying to find does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    print("\n--- Simple Note Taker ---")
    print("1. Create a file.")
    print("2. Write in the existing file.")
    print("3. Read the file")
    print("4. Exit...")
    
    try:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("You want a new file?(Yes/no)\n").strip().lower()
            answer=input()
            if answer == "yes":
                create_file(input("Enter the complete path of where you want your new file: "))
            else:
                create_file()
        
        elif choice == 2:
            print("You want to write in existing default file?(Yes/no)\n").strip().lower()
            answer=input()
            if answer == "yes":
                append_file()
            else:
                append_file(input("Enter the complete path of which existing file you want to write in: "))

        elif choice == 3:
            print("You want to read the existing default file?(Yes/no)\n").strip().lower()
            answer=input()
            if answer == "yes":
                read_file()
            else:
                read_file(input("Enter the complete path of which existing file you want to read: "))

        elif choice == 4:
            print("Thank you for using this code.")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
