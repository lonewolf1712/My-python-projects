#To check if the average of 3 subject is > 40

Maths=int(input("Enter the marks of Maths: "))
Science=int(input("Enter the marks of Science: "))
SST=int(input("Enter the marks of SST: "))

if (Maths+Science+SST)/3>=40:
    print("Student is pass.")
else:
    print("Student is fail.")

print("Thank you for using this code.")