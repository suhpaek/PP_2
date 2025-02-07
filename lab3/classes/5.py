class Account:
    def __init__(self):
        self.owner = str(input("owner's name: "))
        self.balance = 0

    def deposit(self):
        dep = int(input("Enter the sum you would like to deposit: "))
        self.balance += dep

    def withdraw(self):
        withd = int(input("Enter the sum you would like to withdraw: "))
        if self. balance >= withd:
            self.balance -= withd
            print("Remaining balance is: ", self.balance)
        else:
            print("You don't have enough money")

person1 = Account()
person1.deposit()
person1.withdraw()