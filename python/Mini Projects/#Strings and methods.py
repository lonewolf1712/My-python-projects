string = input("Write an introduction line about yourself (must include name Daksh): ")

while True:
    print("\n--- String converter ---")
    print("1. Print it in lowercase.")
    print("2. Print it in uppercase.")
    print("3. Remove extra space")
    print("4. Replace a specific word")
    print("5. Find an index of a particular word.")
    print("6. Split the string into a list")
    print("7. Capitalize the string")
    print("8. Count a specific word")
    print("9. Reverse the string")
    print("10. Word counter")
    print("11. Exit...")
    
    choice = int(input("Enter your option: "))
    
    if choice == 1:
        print(string.lower())
    
    elif choice == 2:
        print(string.upper())

    elif choice == 3:
        print(string.strip())

    elif choice == 4:
        old_word = input("Enter the word you want to replace: ")
        new_word = input("Enter the new word: ")
        print(string.replace(old_word, new_word))

    elif choice == 5:
        word_to_find = input("Enter what you want to find: ")
        index = string.find(word_to_find)
        if index != -1:
            print(f"The word '{word_to_find}' is found at index: {index}")
        else:
            print(f"The word '{word_to_find}' is not found in the string.")
            
    elif choice == 6:
        print(string.split())

    elif choice == 7:
        print(string.capitalize())
        
    elif choice == 8:
        word_to_count = input("Enter the word you want to count: ")
        print(f"The word '{word_to_count}' appears {string.count(word_to_count)} times.")

    elif choice == 9:
        print(string[::-1])

    elif choice == 10:
        string=string.strip().split()
        print(f"Total words in this paragraph is {len(string)}")

    elif choice == 11:
        print("Thank you for using this code.")
        break

    else:
        print("Value error!\nPlease try again.")
