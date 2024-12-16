##OOP_Tuto_Modelling_a_Bank_Account
class BankAccount():
    def __init__(self,account_number,name,interest,balance):
        
        self.account_number= account_number
        self.name =name
        self.balance= balance
        self.interest = interest
        type_of_transaction = ""
        self.transaction = {"name": self.name, "type": "deposit", "balance": self.balance}
        self.transactions= []
        
        
    def deposit(self,amount):
        self.balance +=amount
        self.transaction ={"name":self.name,"type":"deposit","balance":self.balance}
        self.transactions.append(self.transaction)
    
    def withdraw(self,amount):
        
        if self.balance >= amount:
            
            self.balance -= amount
            self.transaction ={"name":self.name,"type":"Withdraw Successful","balance":self.balance}
            self.transactions.append(self.transaction)
        else:
            print("Insufficient funds for ",self.name)
            self.transaction ={"name":self.name,"type":"Withdraw Failed","balance":self.balance}
            self.transactions.append(self.transaction)
 
    def check_balance(self):
        print(f"the actual balance is {self.balance} ")
    
    def calculate_interest(self):
        self.balance += ((self.balance * self.interest )/100 )
        return print(f"the balance after the interest is {self.balance}")

    def print_transactions_history(self):
        
        print(f"Transactions for {self.name}")
        for i,transaction in enumerate(self.transactions,1):
            print(f"{i}. Type: {transaction['type']}|Balance: {transaction ['balance']}")
           
#Testing:

Amine_Konto = BankAccount(1234,"Amine",2.5,5000)
Safa_Konto = BankAccount(1678,"Safa",2.5,800)

Amine_Konto.deposit(500)
Amine_Konto.check_balance()
Amine_Konto.withdraw(1000)
Amine_Konto.print_transactions_history()


Amine_Konto.calculate_interest()
Amine_Konto.withdraw(1000)
Amine_Konto.print_transactions_history()


 