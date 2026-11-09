''' --- Class deep dive ----

   (1) Encapsulation
   (2) Inheritance
   (3) Polimorphism
    
'''

print("#### Encapsulation #####")

class Account():

    def __init__(self, owner, amount):
        self.owner = owner
        self.amount  = amount
       

    def get_balance(self):
         print(f"The account owner {self.owner} has now {self.amount} usd")

    def deposit(self, amount):
        print(f"The owner made {amount} desposit")
        self.amount += amount

    def withdraw(self, amount):
        print("withdraw amount : ", amount)
        self.amount -= amount

my_account = Account("Martin", 1500)
my_account.get_balance()



print("---- deposit has been made -----")

my_account.deposit(10000)
my_account.get_balance()
print("Thank you! Transaction has been completed ")


print(f"----- Owner made withdraw ------ ")

my_account.withdraw(500)
my_account.get_balance()



              

    

    

