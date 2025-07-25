#To check the greatest number
p=int(input("Enter the first number: "))
q=int(input("Enter the second number: "))
r=int(input("Enter the third number: "))

if (p>q&p>r):
    print("FIrst number is largest.")
elif (q>p&q>r):
    print("Second number is largest.")
else:
    print("Third number is the largest.")

print("Thank you for using this code.")