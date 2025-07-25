try:
    n = int(input("Enter a numerator: "))
    m = int(input("Enter a denominator: "))
    print("The answer for division of the given 2 numbers is:\n")
    print(n / m)
except ZeroDivisionError:
    print("Denominator can't be zero.")
except ValueError:
    print("Given value is invalid. Please try again!")
