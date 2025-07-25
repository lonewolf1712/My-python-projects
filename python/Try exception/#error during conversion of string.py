#Robust input collector
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

age = get_int("Enter your age: ")
print("You entered:", age)
