# Set from a string
string="hello world"
vowels="aeiouAEIOU"
vowels_set=set(char for char in string if char in vowels)
print(vowels_set)