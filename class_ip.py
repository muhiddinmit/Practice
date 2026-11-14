""" Class deep dive

(1) Encapsulation
(2) Inheritance 
(3) Polymorphism

"""

print("====== Inheritance =====")
# parent ---> child
# parent provides only public & protected properties (method, state) to child !!!

description = "This class "

class Animal():
    # static
    description = " this class is parent class to child classes! "

    #constructor 
    def __init__(self, voice ):
        self._status = "Animal is alive"
        self.voice = voice 

    # method

    def make_voice (self):
        print(f"This animal can make voice: {self.voice} ")


class Dog(Animal):   # child

    def __init__(self,name, sound, voice):
        self.name = name
        self.sound = sound
        
        super().__init__(voice)

    def introduce(self):
        print(f"This dog {self.name} says {self.sound}-{self.sound}")

    def protect(self):
        print(f"Hey yes I can protect you")


    def make_voice (self):
            print(f"This {self.name} can make voice: {self.voice} ")
    

class Cat(Animal):  # child

    def __init__(self,name,sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
            print(f"This cat {self.name} says {self.sound}-{self.sound}")
     

    def play(self):
        print("Hey! I can play with you dude!!")

class Fish(Animal):

    def __init__(self,name,sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
            print(f"This fish {self.name} says {self.sound}")


dog = Dog("Rex", "Waw", True)
cat = Cat("Tom","Myeow", True)
fish = Fish("Nemo","ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print(" -------------- ")

dog.make_voice()
fish.make_voice()

print(" -------------- ")

print(Animal.description)
print(Dog.description)

print(dog.voice,cat.voice)
print("status :",dog._status)



print("------- Polymorphism -------")

dog.make_voice()
fish.make_voice()

print("------------")

# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(Animal, object)
d = isinstance("MIT", object)
result = a and b and c and False
print("result :", result)

# Fish > Animal > object
print("----------------------------")
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("Result:" ,data1,data2)