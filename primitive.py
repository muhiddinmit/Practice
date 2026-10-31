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
