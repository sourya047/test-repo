class BankAcc:
    def __init__(self):
        self.balance = 0
        print(" Welcome to ABC Bank ")

    def deposite(self):
        amount = float(input(" Enter deposite amount : "))
        self.balance += amount
        print(" \nAmount Deposited : ",amount)

    def withdraw(self):
        amount = float(input(" Enter withdraw amount : "))
        if self.balance >= amount:
            self.balance -=amount
            print("\nAmount Withdrew : ",amount)
        else:
            print("\nInsufficient Balance")

    def display(self):
        print("\nNet Available Balance : ",self.balance)


if __name__== "__main__":
    s = BankAcc()

    s.deposite()
    s.withdraw()
    s.display()