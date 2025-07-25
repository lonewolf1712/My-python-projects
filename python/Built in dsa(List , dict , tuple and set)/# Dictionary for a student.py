# Dictionary for a student
student={
    "Name" : "Daksh",
    "roll no." : 16,
    "marks" : 86
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("Name"))
student.update({"age" : 19,
               "Gender" : "Male"})
print(student)
