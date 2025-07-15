#Homework. Lesson 4
# Dictionary exercises
#1) Sort a Dictionary by Value. Write a Python script to sort (ascending and descending) a dictionary by value.

# Dictionary
my_dict = {'apple': 10, 'banana': 5, 'cherry': 20, 'date': 15}

# Ascending sort by value
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", ascending)

# Descending sort by value
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", descending)

#2) Add a Key to a Dictionary. Write a Python script to add a key to a dictionary.

sample_dict = {0: 10, 1: 20}

# Add key to sample_dict

sample_dict[2] = 30

# Result
print(sample_dict)

#3)Concatenate Multiple Dictionaries. Write a Python script to concatenate the following dictionaries to create a new one. 

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
new_dict = {}

for d in [dic1, dic2, dic3]:
    for key in d:
        new_dict[key] = d[key]


# Result
print(new_dict)

#4) Generate a Dictionary with Squares. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

# n sonini so'rash
n = int(input("n sonini kiriting:"))

# Dictionary yaratish
squares = {}

for x in range(1, n + 1):
    squares[x] = x * x

# Result
print(squares)

#5) Dictionary of Squares (1 to 15). Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

# Yangi dictionary yaratish
squares = {}

# 1 dan 15 gacha bo‘lgan sonlar uchun kvadrat hisoblaymiz
for i in range(1, 16):
    squares[i] = i * i

# Result
print(squares)

# Set exercises
#1)  Create a Set. Write a Python program to create a set.

# Set yaratish
my_set = {"a","b","d"}

# Result
print("Yaratilgan set",my_set)

#2) Iterate Over a Set. Write a Python program to iterate over sets.

# Set  yaratish
my_set = {'apple', 'banana', 'cherry'}

# Set ustida aylanish
for fruit in my_set:
    print(fruit)

#3) Add Member(s) to a Set. Write a Python program to add member(s) to a set.

my_set = {"phone","laptop","book"}

# Add member to my_set
my_set.add("desk")

# Result
print(my_set)

#4)Remove Item(s) from a Set. Write a Python program to remove item(s) from a given set.

animals = {"lion", "tiger", "elephant", "giraffe", "zebra"}

# Remove item from animals

animals.remove("lion")

# Result
print(animals)

#5)Remove an Item if Present in the Set. Write a Python program to remove an item from a set if it is present in the set.

animals = {"lion", "tiger", "elephant", "giraffe"}

# O'chiriladigan item
animal_to_remove = "tiger"

# Agar setda mavjud bo‘lsa, olib tashlash
if animal_to_remove in animals:
    animals.remove(animal_to_remove)
    print(f"{animal_to_remove} o‘chirildi.")
else:
    print(f"{animal_to_remove} to‘plamda mavjud emas.")

# Result
print("Updated set:", animals)


