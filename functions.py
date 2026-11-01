"""
      Functions
(1) Define vs call
(2) Parametr vs Argument
(3) Keyword vs Default argumnets
(4) sCOPE

"""

#### DEFINE VS CALL ####

# define


def greet(a):
    print(f"Hello! How are you {a}")


def greeting(b):
    print("Greeting is executed!")
    return f"Hi {b}"


# Call
result = greet("Martin")
result2 = greeting("Justin")

print(f"result is {result}")
print(f"result1 is {result2}")
