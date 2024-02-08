"""Bank Account Management System"""


class BankAccount:
    password = "admin"
    
    def __init__(self, account_number, name):
        self.account_number = account_number
        self.account_holder_name = name
        self.__balance = 0
        
    def check_password(self):
        password = input("Enter your password to proceed: ")
        if BankAccount.password == password:
            return True
        else:
            return False
    
    def get_balance(self):
        print(f"Balance of {self.account_holder_name} is: {self.__balance}")
    
    def set_balance(self, balance):
        if(self.check_password()):
            if balance < 0:
                print("Negative values are not allowed")
            else:
                self.__balance += balance
            
    def check_balance(self):
        self.get_balance()
        
    def deposit(self):
        amount = float(input('Enter the amount to be deposited: '))
        self.set_balance(amount)
        print(f'Deposit successful! New Balance: {self.__balance}')
        
    def withdrawal(self):
        amount = float(input("Enter the amount to be withdrawn: "))
        if(self.check_password()):
            if amount > self.__balance:
                print("Insufficient balance")
            else:
                self.__balance -= amount
                print(f"Withdrawal Successful! Remaining Balance: {self.__balance}")
            
    def display_account_details(self):
        print(f"Name: {self.account_holder_name}\nAccount Number: {self.account_number}\nCurrent Balance: {self.__balance}")
        

Account1 = BankAccount(1234567890, "John Doe")
Account1.display_account_details()
Account1.deposit()
Account1.display_account_details()
Account1.withdrawal()
Account1.display_account_details()
