#Generating random password
import random
import string

def generate_random_password(length=9):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

random_password = generate_random_password()
print("Generated Password:", random_password)

import random
import string

# Define the character set
characters = string.ascii_letters + string.digits

# Initialize an empty password
password = ""

# Generate a random password of length 9
for _ in range(9):
    password += random.choice(characters)

# Print the generated password
print("Generated Password:", password)
