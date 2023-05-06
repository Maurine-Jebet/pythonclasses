class Account:
    bank_name = "Cooperative"
    def __init__(self,account_number,account_type,balance,account_name):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.account_name = account_name
    def account_details(self):
        return f"my account name is {self.account_name}, and my account_number is{self.account_number}" 
    def balance(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"You Withdrew:", amount)
        else:
            print(f"Insufficient balance ")