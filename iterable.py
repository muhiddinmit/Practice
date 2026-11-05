print("==== iterable objects====")

# iterable objects : str dict tuple  range map filter

country = "France"

for letter in country:
    print("Letters are : ", letter)


numbers = range(3)

for ele in numbers:
    print("ele :", ele)

print("======dictionary====")

person = {"name": "Ali", "age": 25, "single": True}
print(person)

person2 = dict(name="Martin", age=25, single=True)
print(person2)

name = person2["name"]
print("name :", name)

"""
country = person2["country"]
print("country", country)  # it gives error !

"""

#### get method #####

print("===== get method ====")

name = person2.get("name")
hobby = person2.get("hobby")
print(f"name : {name}, hobby is {hobby}")
