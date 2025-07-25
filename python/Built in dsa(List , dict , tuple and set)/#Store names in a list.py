#Store names in a list

friends=["Daksh","krishna","Gaurav","Sujal"]

friends.insert(1,input("Enter your name: "))
print(friends)

friends.append(input("Enter your name: "))
print(friends)

friends.remove("Sujal")
print(friends)

friends.pop(2)
print(friends)

friends.sort()
print(friends)

friends.reverse()
print(friends)

print(friends.__len__())

print("Thank you for using this code.")