#Roots of quadratic equation
print("This is a standard quadratic equation: ax^2 + bx + c")
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))

d = b**2 - 4*a*c  # Discriminant (b² - 4ac)
print(f"Discriminant (d) is: {d}")

if d > 0:
    print("There are two distinct real roots.")
    x1 = (-b + d**0.5) / (2 * a)
    print(f"First root is {x1}.")
    x2 = (-b - d**0.5) / (2 * a)
    print(f"Second root is {x2}.")
elif d == 0:
    print('There is exactly one real root.')
    x3 = -b / (2 * a)
    print(f'The root is {x3}.')
else:
    print('There are two complex roots.')
    real_part = -b / (2 * a)
    imaginary_part = (abs(d)**0.5) / (2 * a)
    x4 = f"{real_part} + {imaginary_part}i"
    x5 = f"{real_part} - {imaginary_part}i"
    print(f"First root is {x4}.")
    print(f"Second root is {x5}.")

print("Thank you for using this code.")
