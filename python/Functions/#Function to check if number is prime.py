#Function to check if number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_up_to(x):
    if x < 0:
        print("There is no negative prime number.")
        return
    for i in range(2, x + 1):
        if is_prime(i):
            print(i)

number = int(input("Enter a number: "))
print_primes_up_to(number)