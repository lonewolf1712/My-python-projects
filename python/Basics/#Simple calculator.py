#Simple calculator without fumctions
n=float(input("Enter the first number: "))
op=input("Enter the operand(+,-,*,/): ")
m=float(input("Enter the Second number: "))

if op=="+":
    print(f"Result: {n+m}")
elif op=="-":
    print(f"Result: {n-m}")
elif op=="*":
    print(f"Result: {n*m}")
else:
    print(f"Result: {n/m}")
print("Thank you for using this code: ")