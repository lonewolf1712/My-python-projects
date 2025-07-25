#Simple calculator with functions

def add(n,m):
    return n+m
def subtract(n,m):
    return n-m
def multiply(n,m):
    return n*m
def divide(n,m):
    return n/m

n=float(input("Enter the first number: "))
op=input("Enter the operand(+,-,*,/): ")
m=float(input("Enter the Second number: "))

if op=="+":
    result=add(n,m)
elif op=="-":
    result = subtract(n,m)
elif op=="*":
    result=multiply(n,m)
else:
    if m<0:
        print("Zero division error.")
    result=divide(n,m)
print(result)
print("Thank you for using this code: ")