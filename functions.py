"""
      Functions
(1) Define vs call
(2) Parametr vs Argument
(3) Keyword vs Default argumnets
(4) sCOPE

"""

#### DEFINE VS CALL ####

# define - parametr


def greet(a):
    print(f"Hello! How are you {a}")


def greeting(b):
    print("Greeting is executed!")
    return f"Hi {b}"


# Call- argument
result = greet("Martin")
result2 = greeting("Justin")

print(f"result is {result}")
print(f"result1 is {result2}")


#### Keyword and Default argument ####


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old"


result3 = give_greet("Justin")
print(f"result3 is {result3}")


#### Scope ####

b = 100


def calculate(a):
    c = a * b
    print(f"value of c is {c}")


calculate(5)
