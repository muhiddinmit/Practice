quantity = int(input("How many entries do you have! "))

numbers =[ ]

for i in range(quantity):
    if quantity > 0:
        num = float(input("The entries {i+1}"))
        numbers.append(num)

    else :
        print("Value Error: The number of your entries must be positive!!")

average = sum(numbers)/quantity

print(f"The average of {numbers} is {average:.2f}")