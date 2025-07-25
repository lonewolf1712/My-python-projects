# Student record system
Students={
    101 : {
    "Name" : "Daksh",
    "Class" : 12,
    "marks" : 86
},
    102 : {
    "Name" : "Stuti",
    "Class" : 12,
    "marks" : 92
},
    103 : {
    "Name" : "Krishna",
    "Class" : 12,
    "marks" : 66
}
}
def display_student():
    roll = int(input("Enter roll number to display: "))
    if roll in Students:
        print(f"Details of roll {roll}:")
        for key, value in Students[roll].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Student not found!")
display_student()