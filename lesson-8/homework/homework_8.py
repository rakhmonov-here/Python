# Homework. Lesson 8
# Exception Handling Exercises

# 1) Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
import string
import random
import os
n = 0
try:
    result = 100 / n
except ZeroDivisionError:
    print("Sen sonni 0 ga bo'la olmaysan!")

# 2) Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
user_input = input("Butun son kiriting: ")
try:
    number = int(user_input)
    print(f"Siz kiritgan butun son - {number}")
except ValueError:
    print("Siz kiritgan son butun son emas!")

# 3) Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist
try:
    file_handler = open('example.txt')
except FileNotFoundError:
    print("Bunday fayl mavjud emas!")

# 4) Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
try:
    x = float(input("Birinchi sonni kiriting: "))
    y = input("Ikkinchi sonni kiriting: ")
    result = x + y
    print("Natija:", result)

except TypeError:
    print("Turli tipdagi qiymatlarni qo'shib bo'lmaydi (masalan: son + matn).")

# 5) Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
file_path = "class1.sql"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print("Fayl mazmuni:\n", content)

except PermissionError:
    print("Xatolik: Faylni o'qish uchun ruxsat yo'q.")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")

# 6) Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
my_list = [1, 2, 5, 9]
try:
    print("Siz kiritgan listning 5-elementi - ", my_list[5])
except IndexError:
    print("Bu tartibda element mavjud emas")

# 7) Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
number = int(input("Istalgan son kiriting: "))
try:
    print(f"Siz kiritgan son - {number}")
except KeyboardInterrupt:
    print("\n Kiritish bekor qilindi!")

# 8) Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    print(1/0)
except ArithmeticError:
    print("Arifmetik xatolik!")

# 9) Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open("matn.txt", encoding='ascii') as f:
        content = f.read()
except UnicodeDecodeError:
    print("Xatolik yuz berdi!")

# 10) Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
my_list = [12, 45, 48, 456]

try:
    print(my_list.open())
except AttributeError:
    print("Attribute bilan bog'liq xatolik yuz berdi!")

# File Input/Output Exercises
# 1) Write a Python program to read an entire text file.
file_handler = open("example.txt", mode='r')

# 2) Write a Python program to read first n lines of a file.
file_path = "example.txt"
try:
    n = int(input("Nechta satr o'qishni hohlaysiz: "))
    with open("example.txt", mode='r') as file:
        for line in range(n):
            line = file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("Bunday fayl topilmadi!")
except ValueError:
    print("Butun son kiriting!")

# 3) Write a Python program to append text to a file and display the text.
with open("example.txt", mode='a') as file_handler:
    file_handler.write("Here is some more text")

# 4) Write a Python program to read last n lines of a file.


def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            last_lines = lines[-n:]  # oxirgi n qatorni olish
            for line in last_lines:
                print(line.strip())  # qatorni chiqarish
    except FileNotFoundError:
        print(f"Error: Fayl '{filename}' topilmadi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


# Foydalanuvchidan ma'lumot olish
filename = input("Fayl nomini kiriting: ")
n = int(input("Oxirgi nechta qatorni o'qish kerakligini kiriting: "))

read_last_n_lines(filename, n)

# 5) Write a Python program to read a file line by line and store it into a list.


def read_file_to_list(filename):
    try:
        lines_list = []  # Bo'sh ro'yxat yaratamiz
        with open(filename, 'r') as file:
            for line in file:
                # Har bir qatorni ro'yxatga qo'shamiz
                lines_list.append(line.strip())
        return lines_list
    except FileNotFoundError:
        print(f"Error: Fayl '{filename}' topilmadi.")
        return []
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        return []


# Foydalanuvchidan fayl nomini so'raymiz
filename = input("Fayl nomini kiriting: ")
result = read_file_to_list(filename)

# 6) Write a Python program to read a file line by line and store it into a variable.


def read_file_to_variable(filename):
    try:
        content = ""  # Bo'sh string (o'zgaruvchi) yaratamiz
        with open(filename, 'r') as file:
            for line in file:
                # Har bir qatorni qo‘shamiz (newline saqlanadi)
                content += line
        return content
    except FileNotFoundError:
        print(f"Error: Fayl '{filename}' topilmadi.")
        return ""
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        return ""


# Foydalanuvchidan fayl nomini olish
filename = input("Fayl nomini kiriting: ")
text_data = read_file_to_variable(filename)

# Natijani chiqarish
print("Fayldagi matn:")
print(text_data)

# 7) Write a Python program to read a file line by line and store it into an array.


def read_file_to_array(filename):
    try:
        with open(filename, 'r') as file:
            # Har bir qatorni tozalab ro'yxatga (arrayga) saqlaydi
            array = [line.strip() for line in file]
        return array
    except FileNotFoundError:
        print(f"Error: Fayl '{filename}' topilmadi.")
        return []
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        return []


# Foydalanuvchidan fayl nomini olish
filename = input("Fayl nomini kiriting: ")
lines_array = read_file_to_array(filename)

# Natijani chiqarish
print("Fayldagi qatorlar (array ko‘rinishida):")
print(lines_array)

# 8) Write a Python program to find the longest words.
filename = input("Fayl nomini kiriting: ")

with open(filename, 'r') as file:
    text = file.read()         # Butun matnni o‘qiydi
    words = text.split()       # So‘zlarga ajratadi

max_len = 0
longest_words = []

for word in words:
    if len(word) > max_len:
        max_len = len(word)
        longest_words = [word]
    elif len(word) == max_len:
        longest_words.append(word)

print("Eng uzun so'z(lar):")
for word in longest_words:
    print(word)

# 9) Write a Python program to count the number of lines in a text file.
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)  # Har bir qator uchun 1 qo‘shadi
    print(f"Fayldagi qatorlar soni: {line_count}")
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Boshqa xatolik: {e}")

# 10) Write a Python program to count the frequency of words in a file.
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        text = file.read()
        words = text.lower().split()  # So‘zlarni kichik harfga o‘tkazamiz

        word_freq = {}  # So‘z chastotasi uchun bo‘sh lug‘at

        for word in words:
            # Belgilarni olib tashlash
            clean_word = word.strip(".,!?;:\"()[]{}")
            if clean_word in word_freq:
                word_freq[clean_word] += 1
            else:
                word_freq[clean_word] = 1

        print("So'zlar chastotasi:")
        for word, count in word_freq.items():
            print(f"{word}: {count}")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 11) Write a Python program to get the file size of a plain file.

filename = input("Fayl nomini kiriting: ")

try:
    file_size = os.path.getsize(filename)  # Fayl hajmini baytlarda oladi
    print(f"Fayl hajmi: {file_size} bayt")
except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 12) Write a Python program to write a list to a file.
# Yoziladigan ro'yxat
my_list = ['apple', 'banana', 'cherry', 'date']

# Foydalanuvchidan fayl nomini olish
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(item + '\n')  # Har bir element yangi qatorda yoziladi
    print("Ro'yxat faylga muvaffaqiyatli yozildi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 13) Write a Python program to copy the contents of a file to another file.
# Manba va nusxa fayl nomlarini so'raymiz
source_file = input("Nusxa olinadigan fayl nomi (manba): ")
destination_file = input("Yangi fayl nomi (qayerga nusxalash): ")

try:
    # Manba faylni o'qish rejimida ochamiz
    with open(source_file, 'r') as src:
        content = src.read()  # Butun matnni o'qib olamiz

    # Yangi faylga yozamiz
    with open(destination_file, 'w') as dest:
        dest.write(content)

    print("Fayl muvaffaqiyatli nusxalandi.")
except FileNotFoundError:
    print("Xatolik: Manba fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 14) Write a Python program to combine each line from the first file with the corresponding line in the second file.
# Ikkita fayl nomini so'raymiz
file1 = input("1-fayl nomini kiriting: ")
file2 = input("2-fayl nomini kiriting: ")

try:
    # Har ikki fayldagi qatorlarni o'qib olish
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Eng qisqa fayl uzunligiga qarab chegaralaymiz
    min_length = min(len(lines1), len(lines2))

    print("Birlashtirilgan qatorlar:")
    for i in range(min_length):
        combined = lines1[i].strip() + " " + lines2[i].strip()
        print(combined)

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 15) Write a Python program to read a random line from a file.

filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()  # Barcha qatorlarni o'qib olamiz

        if lines:
            random_line = random.choice(lines)  # Tasodifiy qatorni tanlaymiz
            print("Tasodifiy qator:")
            print(random_line.strip())
        else:
            print("Fayl bo'sh.")

except FileNotFoundError:
    print("Xatolik: Fayl topilmadi.")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 16) Write a Python program to assess if a file is closed or not.
# Fayl ochiladi
file = open("example.txt", "w")

# Fayl ochilganmi yoki yopilganmi tekshiramiz
print("Fayl yopilganmi?", file.closed)  # False bo'lishi kerak

# Faylni yopamiz
file.close()

# Endi yana tekshiramiz
print("Fayl yopilganmi?", file.closed)  # True bo'lishi kerak

# 17) Write a Python program to remove newline characters from a file.
# Kiruvchi faylni o'qib, barcha '\n' belgilarini olib tashlaymiz
with open("input.txt", "r") as infile:
    content = infile.read().replace('\n', '')

# Tozalangan matnni yangi faylga yozamiz
with open("output.txt", "w") as outfile:
    outfile.write(content)

# 18) Write a Python program that takes a text file as input and returns the number of words in a given text file.
# Foydalanuvchidan fayl nomini so'raymiz
filename = input("Fayl nomini kiriting: ")

try:
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        print("So'zlar soni:", len(words))
except FileNotFoundError:
    print("Bunday fayl topilmadi.")

# 19) Write a Python program to extract characters from various text files and put them into a list.
# Fayllar ro'yxati
filenames = ["file1.txt", "file2.txt", "file3.txt"]

# Belgilarni yig'ish uchun bo'sh ro'yxat
all_characters = []

# Har bir fayldan belgilarni o'qib olamiz
for fname in filenames:
    try:
        with open(fname, 'r') as file:
            content = file.read()
            all_characters.extend(list(content))
    except FileNotFoundError:
        print(f"{fname} topilmadi.")

# Natijani chiqaramiz
print("Belgilar ro'yxati:", all_characters)

# 20) Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

# Har bir harf uchun fayl yaratamiz
for letter in string.ascii_uppercase:  # 'A' dan 'Z' gacha
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write(f"This is {filename}\n")

# 21) Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

# Foydalanuvchidan bir qatorda nechta harf bo'lishini so'raymiz
n = int(input("Har bir qatorda nechta harf bo'lsin? "))

letters = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'

with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        line = letters[i:i+n]
        file.write(line + '\n')

print("Fayl yaratildi: alphabet.txt")
