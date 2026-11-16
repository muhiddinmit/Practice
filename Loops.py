"""
    Loop operators:

    (1) For loop
    (2) break/else
    (3) While loop
    
"""
print("==== for loop =====")
name = "MIT"
number = [10,20,30]
dic_object = dict(brand="Mercedes", year=2026, made ="Germany")
numbers  = range(10)

for char in name:
    print("The chars:", char)

for num in number:
    print(f"the number ---> {num}")

for key in dic_object:
    print(f"the keys of dictionary are: {key}")

for i in number:
    print(i)

print('------')
for k in range(10):
    if k > 10:
        print("You reached !",k)
        break
else:
        print(" Completed!")

print("--- while loop ----")

count = 0
while count < 50 :
     count +=10
     print("count is ",count)
     
print("-------- guess password -----")

password = 120130

attempt = 0
while True:
     attempt +=1
     x = int(input("enter the password :"))

    
     if x == password:
          print(f"Congrats! you passed in {attempt} attempts")
          break

print("------ finding magic word game -----")

magic_word = "engineer"
attempts = 0

max_attempts = 5

while attempts <= max_attempts:
     attempts +=1 
     guess = str(input("enter the word you think magic: "))

     if guess ==  magic_word:
          print("Oo You found magic word! Great attempt")
          break
     else:
          print("wrong word! please try again")

else:
     print("you reached maximum attempt, please try again later!")