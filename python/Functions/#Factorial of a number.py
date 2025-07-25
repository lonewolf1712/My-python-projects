#Factorial of a given number
def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, x + 1):
        result *= i               #this code go from back to front,1*1->1*2...
    return result

result = factorial(int(input("Enter a number: ")))
print(f"Factorial of the given number is {result}")
