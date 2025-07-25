#Even number till n
n = int(input("Enter any number: "))
if n <= 0:
    print("Try again.")
else:
    print("Even numbers up to", n, "are:")
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)
print("Thank you for using this code.")
