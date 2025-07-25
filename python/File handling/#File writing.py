#File writing
for i in range(5):
    try:
         with open(r"C:\Users\Hp\OneDrive\Desktop\Daku record system.txt","a") as file:
             context = file.write(input("Enter what you want to add in the file: "))
             print(context)
    except FileNotFoundError:
        print("The file you are trying to find does not exist.")