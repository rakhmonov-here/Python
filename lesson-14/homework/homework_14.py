# Homework. Lesson 14
# 1) write a Python script that reads the students.jon JSON file and prints details of each student.
import json

with open('students.json') as f:
    my_data = json.load(f)

for student in my_data['students']:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")
    print(f"Subjects: {', '.join(student['subjects'])}")
    address = student['address']
    print(f"Address: {address['street']}, {address['city']}, {address['state']} {address['zipcode']}")
    print("-" * 40)

# 2) Weather API
import requests

city = 'Kokand'
my_api_key = 'aa99ca5ae0b95a03a713f3b1f7a64642'
my_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api_key}&units=metric'
response = requests.get(my_url)
my_data = response.json()
print(f"City name: {my_data['name']}. Description: {my_data['weather'][0]['description']}, temperature: {my_data['main']['temp']},\
humidity: {my_data['main']['humidity']}")

# 3) Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
with open ('books.json') as f:
    my_dict = json.load(f)
    
book_id = int(input('Kitobning idsini kiriting: '))
book_name = input("Kitob nomini kiriting: ")
author_name = input("Kitob muallifini kiriting: ")

for my_list in my_dict.values():
    my_list.append({'book_id':book_id, 'name':book_name, 'author_name':author_name})

print(my_list)

# 4) Movie Recommendation System
my_genre = input("Kino janrini kiriting: ")
my_url = f'http://www.omdbapi.com/?s={my_genre}&apikey=ff1d53aa'

response = requests.get(my_url)
my_data = response.json()

print(my_data)
for dict in my_data['Search']:
    print(dict['Title'], str(dict['Year']), dict["Type"])