"""  
     Operations (1)
     Conditions (2)
     Logical Operators (3)

"""
print("===== Operations ======")

a = 25
b = 30

print(f"a * b is {a*b}")
print(a-b)
print(b//a)

#reminder
c = b % a
print(f"Reminder of b/a is {c}")

# a +=100
#print(a)
#print(b**2)
#print(b**3)

data1 = dict(name="Muhiddin", age = 26)
data2 = dict(name="Muhiddin", age = 26)
print(f" data1 is data2 : {data1 == data2}")

print("====== Condition =====")

if a > b:
    print ("True")

else:
    print("False")

grade = 90

if grade >= 90 :
    print("Grade : A ")

elif grade >= 80:
    print("grade : B")

elif grade >= 70:
    print("Grade : C")
else:
    print("grade : F")

print("========== Logical operators =======")
# Ternary condition

age = 26
person = "adult" if age >=18 else "minor"
print("Person :",person)

print("--------------")

is_student = True
is_admin = True
is_female = False
is_guest = True

if not is_student :
    print("Executed! Do you want to be student")

# elif is_admin or is_female:
  #print("Congrats! You are hired")

else:
    print("No match found! ")




