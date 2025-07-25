#File reading 
try:
    with open(r"C:\Users\Hp\OneDrive\Desktop\Daku record system.txt","r") as file:
        context = file.readlines()
        print(context) 
except FileNotFoundError:
    print("The file you are trying to find does not exist.")