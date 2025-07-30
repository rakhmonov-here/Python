# Homework. Lesson 11
# 1) Create your own virtual environment and install some python packages.

# Virtual environment yaratish
python -m venv myenv 
# Virtual environment ni faollashtirish
myenv\Scripts\activate 
# Python paketlarini o'rnatish
pip install numpy pandas 

# 2) Create custom modules

# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# main.py

import math_operations
import string_utils

print(math_operations.add(10, 5))         # ➜ 15
print(math_operations.divide(10, 2))      # ➜ 5.0

print(string_utils.reverse_string("hello"))    # ➜ "olleh"
print(string_utils.count_vowels("hello"))      # ➜ 2

# 3) Create custom packages.

# geometry/__init__.py
from .circle import calculate_area, calculate_circumference
# geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

# file_operations/__init__.py
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error: {e}"

# file_operations/file_reader.py
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error: {e}"
# file_operations/file_writer.py
def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return "Write successful."
    except Exception as e:
        return f"Error: {e}"
# main.py
from geometry import calculate_area, calculate_circumference
from file_operations import read_file, write_file

# Geometry test
print("Area:", calculate_area(5))                    # ➜ 78.5398...
print("Circumference:", calculate_circumference(5))  # ➜ 31.4159...

# File operations test
file_path = "test.txt"
write_file(file_path, "Hello, custom packages!")
print(read_file(file_path))                          # ➜ "Hello, custom packages!"


