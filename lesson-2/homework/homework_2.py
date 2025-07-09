#Homework. Lesson 2
#1)Age Calculator. Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

from datetime import datetime

name = input("Sizning ismingiz: ")
birth_year = int(input("Sizning tug'ilgan yilingiz: "))

current_year = datetime.now().year  #Hozirgi yil

age = current_year - birth_year   #Yoshni topish (Hozirgi yildan tug'ilgan yilni ayirib)

print(f"{name},siz {age} yoshdasiz.")

#2)Extract Car Names. Extract car names from the following text:

txt = 'LMaasleitbtui'

print(txt[:13:2])  #Lasetti 
print(txt[1:12:2])  #Malibu

#3)Extract Car Names. Extract car names from the following text:

txt = 'MsaatmiazD'

print(txt[:10:2])  #Matiz

txt1 = txt[::-1]  #matnni teskari tartibda yozish

print(txt1[:10:2]) #Damas

#4)Extract Residence Area. Extract the residence area from the following text:

txt = "I'am John. I am from London"

residence = txt.split("from")[1].strip() 

print("Residence area: ", residence)

#5)Reverse String. Write a Python program that takes a user input string and prints it in reverse order.

string = input("Matn kiriting: ")

print(string[::-1])  #teskari tartibda chiqarish

#6) Count Vowels. Write a Python program that counts the number of vowels in a given string.

text = input("Matn kiriting: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Unli harflar soni:", count)


#7)Find Maximum Value. Write a Python program that takes a list of numbers as input and prints the maximum value.

numbers = input("Sonlarni kiriting (vergul bilan): ")

# Matnni ro'yxatga aylantiramiz va har bir elementni butun songa aylantiramiz
num_list = [int(x) for x in numbers.split(",")]

# Maksimal qiymatni topamiz
max_value = max(num_list)

print("Eng katta son:", max_value)


#8)Check Palindrome. Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

word = input("So'zni kiriting: ")

drow = word[::-1]  #berilgan so'zni teskari tartibda chiqarish

if word == drow:  
    print("Bu so'z palindrom") #berilgan so'z teskarisiga teng bo'lsa, 'Bu so'z palindrom' deb chiqsin
else: 
    print("Bu so'z palindrom emas") #aks holda, 'Bu so'z palindrom emas' deb chiqsin

#9)Extract Email Domain. Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input("Email manzilini kiriting: ")

domain = email.split("@")[1]

print("Email domeni:", domain)

#10)Generate Random Password. Write a Python program to generate a random password containing letters, digits, and special characters.

import random
import string

# Belgilar to'plami: harflar, raqamlar, maxsus belgilar
letters = string.ascii_letters
digits = string.digits
specials = string.punctuation

all_chars = letters + digits + specials

# Parol uzunligi
password_length = 12

# Tasodifiy belgilar tanlanadi
password = ''.join(random.sample(all_chars, password_length))

print("Tasodifiy parol:", password)
