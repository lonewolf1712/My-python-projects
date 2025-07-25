#Prime numbers
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
    else:
        print(f"Prime numbers up to {x} are:")
        for i in range(2, x + 1):
            if is_prime(i):
                print(i, end=',')
        print() 

def print_total_n_primes(y):
    if y < 1:
        print("There is no non-positive number of primes.")
        return
    else:
        print(f"First {y} prime numbers are:")
        count = 0
        num = 2 
        while count < y:
            if is_prime(num):
                print(num, end=',')
                count += 1
            num += 1 
        print() 

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"The given number {number} is prime.")
else:
    print(f"The given number {number} is not prime.")

print_primes_up_to(number)
print_total_n_primes(number)
