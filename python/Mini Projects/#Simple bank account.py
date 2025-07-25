#Simple bank account
class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def credit(self, amount):
        if amount > 0:
            self.__balance += amount

    def debit(self, amount):
        if 0 < amount <= self.get_balance():
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

acc1 = Bank("daksh", 4000)

while True:
    print("\n--- Simple Bank Account ---")
    print("1. Check balance.")
    print("2. Deposit money.")
    print("3. Withdraw money.")
    print("4. Exit")

    try:
        choice = int(input("What do you want to do?\n"))
        
        if choice == 1:
            print(f"Your balance is: {acc1.get_balance()}")
            
        elif choice == 2:
            n = int(input("How much money do you want to deposit?\n"))
            acc1.credit(n)
            print(f"New balance after deposit: {acc1.get_balance()}")
            
        elif choice == 3:
            m = int(input("How much money do you want to withdraw?\n"))
            acc1.debit(m)
            print(f"New balance after withdrawal: {acc1.get_balance()}")
            
        elif choice == 4:
            print("Thank you for using this service.")
            break
            
        else:
            print("Enter a valid option between 1-4.")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")