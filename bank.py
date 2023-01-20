class Bank_account:
    def __init__(self):
      self.balance=0
      print("Hello!!! welcome to the Deposite & withdrawn Machine")
    def deposit(self):
        amount=float(input("Enter amount to be Deposited"))
        self.balance += amount

    def withdraw(self):
            amount = float(input("Enter amount to be Withdrawn: "))
            if self.balance >= amount:
                self.balance -= amount
                print("\n You Withdraw:", amount)
            else:
                print("\n Insufficient balance ")

    def display(self):
            print("\n Net Available Balance=", self.balance)


s=Bank_account()
s.deposit()
s.withdraw()
s.display()

