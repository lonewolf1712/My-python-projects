#Multiplication table of any number
n=int(input("Enter the number of which table you want: "))
i=1
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
print("Thank you for using this code.")