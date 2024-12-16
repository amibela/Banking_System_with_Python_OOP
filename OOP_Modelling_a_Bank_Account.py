#OOP_Tuto_Modelling_a_Bank_Account
from datetime import *
from dateutil.relativedelta import relativedelta, MO
today_date = date.today()
class BankAccount():
    def __init__(self,account_number,name,interest,balance):
        
        self.account_number= account_number
        self.name =name
        self.balance= balance
        self.interest = interest
        amount=0 
        self.type_of_transaction = ""
        self.transaction = {"name": self.name, "type": "deposit", "amount:":amount,"balance": self.balance, "date":today_date}
        self.transactions= []
        
        
    def deposit(self,amount):
        self.balance +=amount
        self.transaction = {"name": self.name, "type": "deposit", "amount:":amount,"balance": self.balance, "date":today_date}
        self.transactions.append(self.transaction)

    def withdraw(self,amount):
        
        if self.balance >= amount:
            
            self.balance -= amount
            self.transaction ={"name":self.name,"type":"Withdraw Successful", "amount:":amount,"balance":self.balance, "date":today_date}
            self.transactions.append(self.transaction)
        else:
            print("Insufficient funds for ",self.name)
            self.transaction ={"name":self.name,"type":"Withdraw Failed","amount:":amount,"balance":self.balance, "date":today_date}
            self.transactions.append(self.transaction)
 
    def check_balance(self):
        print(f"the actual balance is {self.balance} ")
    
    def calculate_interest(self):
        self.balance += ((self.balance * self.interest )/100 )
        return print(f"the balance after the interest is {self.balance}")

    def print_transactions_history(self):
        
        print(f"Transactions for {self.name}")
        for i,transaction in enumerate(self.transactions,1):
            print(f"{i}. Type: {transaction['type']}|amount: {transaction['amount:']}|Balance: {transaction ['balance']} x Date: {transaction['date']}")
           
class SavingAccount(BankAccount):
    def __init__(self, account_number, name, interest, balance, annual_rate):
        super().__init__(account_number, name, interest, balance)
        self.annual_rate = annual_rate
            
    def withdraw(self,amount):
            if amount >200:
                
                print(f"Withdraw should be maximum 200 ")
            elif amount > self.balance: 
                print("Error")
            else:
                super().withdraw(amount)
                
    def get_monthly_interest(self):
        print(f"Monthly interest applied: {self.monthly_interest_amount:.2f}")
        print(f"The balance after the monthly interest is {self.balance:.2f}")
            
    def apply_monthly_interest(self):
            
            if today_date >= self.last_interest_date + relativedelta(months=1):
            # Apply interest
          
                self.monthly_interest_amount =(self.balance *(self.annual_rate/12))/100
                self.last_interest_date = today_date
                self.balance +=  self.monthly_interest_amount
                self.last_interest_date= today_date
                self.get_monthly_interest()
                
            else:
                print("Monthly Interest is not yet applicable")           
            
#class CurrentAccount(BankAccount):    
    
#    return 1    
#####Testing:#####

print(today_date, type(today_date))

# Amine_Konto = BankAccount(1234,"Amine",2.5,5000)
Illy_Konto = SavingAccount(1678,"Illy",2.5,800,15)

Illy_Konto.deposit(500)
Illy_Konto.check_balance()
Illy_Konto.withdraw(1000)
Illy_Konto.check_balance()
Illy_Konto.last_interest_date = today_date - relativedelta(months=6)  # Simulate last interest 6 months ago
Illy_Konto.apply_monthly_interest()  # Apply interest
Illy_Konto.check_balance()  # Check updated balance
Illy_Konto.print_transactions_history()  # View transaction history

# Amine_Konto.deposit(500)
# Amine_Konto.check_balance()
# Amine_Konto.withdraw(1000)
# Amine_Konto.print_transactions_history()


# Amine_Konto.apply_mont_interest()
# Amine_Konto.withdraw(1000)
# Amine_Konto.print_transactions_history()


 