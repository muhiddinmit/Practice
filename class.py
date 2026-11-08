print("====== Class=======")


class Person():
    def __init__(self,name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def introduce(self) :
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"I am from {self.country}")

person1 = Person("Muhiddin", 26, "Uzbekistan")
person2 = Person("John", 30, "USA")

person1.introduce()
person2.introduce()




print("====== class=====")

class Laptop:
    def __init__(self, brand, model, ram, price ):
        self.brand = brand
        self.model = model
        self.ram = ram 
        self.price = price


    def show_info(self):
        print(f"The laptop brand is {self.brand}")
        print(f"The laptop model is {self.model}")
        print(f"The laptop ram is {self.ram}")
        print(f"The laptop brand is {self.price}")

    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        print("The ram of laptop is updated {new_ram} and but the price is not changed")

 


laptop1 = Laptop("Apple", "air pro 2", 16, "1500 usd")
laptop2 = Laptop("Apple", "air pro 2", 8, "1000 usd")

print("=====laptop1 =====")
laptop1.show_info()

    
print("====== updated laptop1 ========")
laptop1.upgrade_ram(32)
laptop1.show_info()
    
print("==== laptop2=====")
laptop2.show_info()


