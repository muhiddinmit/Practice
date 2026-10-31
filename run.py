# Dunder __buiiltin__, __init__

message = "In Python, everything is object"
result = type(message)

print(message)
print(f"The type of message is {result}")


"""
In Python, there are builtin tools

(1) TYPES ->  int  str  bool  list dict
(2) FUNCTIONS --> print()  len()  input()  type() 
(3) constants ->  True False None 

"""

print(dir(__builtins__))
