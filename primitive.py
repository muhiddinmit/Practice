print("===== number ====")

# In Java or C, variable is a name of storage location
# In Python, variable is a named references !

count = 100
count_type = type(count)

print("Count is", count)
print(f"The count is: {count}, The type of count is {count_type}")


result1 = count.bit_count()  # method
result2 = count.numerator  # state

print(result1, result2)


print("====== String =====")

course = "AI Python Fullstack"
course_type = type(course)

result = course.title()
print(f"The result1 is {result}")


result = course.upper()
print(f"The result2 is {result}")

result = course.replace("Fullstack", "Foundation")
print(f"The result3 is {result}")

result = course.lower()
print(f"The result4 is   {result}")


print("====== boolean =====")

# Functions >  function()  type()  init() int() str() input()

x = input("Give your value of x : ")
print("x is ", x)

result = x.isnumeric()
print(f"The value of x is {result}")


# truthy and falsy
# truthu : True, 100, "MIT"
# falsy : False , None, ""

test_falsy = "" or False or None or 0
print(f" the test_falsy is {bool(test_falsy)}")


test_truthy = "MIT" or True or 100
print(f"The test_truthy is {bool(test_truthy)}")
