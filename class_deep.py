''' --- Class deep dive ----

   (1) Encapsulation
   (2) Inheritance
   (3) Polimorphism
    
'''
      # enapsulation -> public -> prvate -> protected
print("#### Encapsulation #####")

class Account():
    # state
    description = "The class makes bank accounts"


    #contrustors
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount  = amount
       
    #method
    def get_balance(self):
         print(f"The account owner {self.__owner} has now {self.__amount} usd")

    def deposit(self, amount):
        print(f"The owner made {amount} desposit")
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw amount : ", amount)
        self.__amount -= amount

    @property      # getter 
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        print("---Holder setter---", new_owner)
        self.__owner = new_owner

    def change_ownership(self, new_owner):
          print("---chnage ownership executed:", new_owner)
          self.__owner = new_owner


my_account = Account("Martin", 1500)
my_account.get_balance()



print("---- deposit has been made -----")

my_account.deposit(10000)
my_account.get_balance()
print("Thank you! Transaction has been completed ")



print(f"----- Owner made withdraw ------ ")

my_account.withdraw(500)
my_account.get_balance()

print("----Trying to access private attribute -------")


try:

    result = my_account.__amount
    print("result : ", result)
except Exception as err:
    print("Private attribute cannot be accessed directly !", err)

account_owner = my_account.holder  #state
print("owner before :", account_owner)


my_account.change_ownership("Muhiddin")   #state
print("owner after :", my_account.holder)
              
my_account.holder = "John"
print("current owner :", my_account.holder)
    

    

