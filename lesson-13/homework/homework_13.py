# Homework. Lesson 13
# 1) Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import pytz
# # Foydalanuvchidan tug'ilgan sana so'raymiz
# birth_date_str = input("Tug'ilgan kuningizni kiriting: (Example:2025-08-05)")
# birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
# # Hozirgi sana
# current_date = datetime.today().date()
# # Yoshni hisoblash
# age = relativedelta(current_date, birth_date)
# # Natijani chiqarish
# print(f"Sizning yoshingiz {age.years} yil, {age.months} oy, {age.days} kun.")

# 2) Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

# # Foydalanuvchidan tug'ilgan sana so'raymiz
# birth_date_str = input("Tug'ilgan kuningizni kiriting: (Example:2025-08-05)")
# birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
# # Hozirgi sana
# current_date = date.today()
# # Tug'ilgan oy va kunni hozirgi yilga qo'shamiz
# next_birthday = date(current_date.year, birth_date.month, birth_date.day)
# # Agar tug‘ilgan kun allaqachon o‘tgan bo‘lsa, keyingi yilga o‘tkazamiz
# if next_birthday < current_date:
#     next_birthday = date(current_date.year + 1,
#                          birth_date.month, birth_date.day)
# # Farqni hisoblash
# days_remaining = (next_birthday - current_date).days
# # Natijani chiqarish
# print(f"Keyingi tug'ilgan kuningizgacha {days_remaining} kun qoldi")

# 3) Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

# # Foydalanuvchidan hozirgi sana va vaqtni kiritishini so'raymiz
# current_datetime_str = input("Hozirgi sana va vaqtni kiriting: \n>>>>>(Example: 2025-08-06 19:07)")
# current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")
# # Uchrashuv davomiyligini so'raymiz
# hours = int(input("Uchrashuv davomiyligini kiriting (soat): "))
# minutes = int(input("Uchrashuv davomiyligini kiriting (minut): "))
# # Davomiylikni qo'shish
# duration_time = timedelta(hours=hours, minutes=minutes)
# end_datetime = current_datetime + duration_time
# # Natijani chiqarish
# print("Uchrashuv tugaydigan vaqt: ", end_datetime.strftime("%Y-%m-%d %H:%M"))

# 4) Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

# # Foydalanuvchidan sana va vaqt kiritishini so'raymiz
# date_str = input("Sana va vaqtni kiriting (YYYY-mm-dd HH:MM): ")
# # Hozirgi vaqt zonasini kiritishini so'raymiz
# from_timezone_str = input(
#     "Hozirgi vaqt zonangizni kiriting (masalan: Asia/Tashkent): ")
# # Qaysi vaqt zonasini ko'rishni hohlashini so'raymiz
# to_timezone_str = input(
#     "Qaysi vaqt zonasiga o'tmoqchisiz? (masalan: America/New_York): ")
# # 1. Kiruvchi vaqtni parsing qilish
# # Kiruvchi vaqtni parsing qilish
# naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
# # Vaqt zonasini aniqlash
# from_tz = pytz.timezone(from_timezone_str)
# to_tz = pytz.timezone(to_timezone_str)
# # Vaqtni vaqt zonasiga "aware" qilish
# from_dt = from_tz.localize(naive_dt)
# # Maqsadli vaqt zonasiga o‘girish
# converted_dt = from_dt.astimezone(to_tz)
# # Natijani chiqarish
# print("O'girilgan sana va vaqt:", converted_dt.strftime("%Y-%m-%d %H:%M (%Z)"))

# 5) Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
# import time

# # 1. Kelajak sana va vaqt
# future_str = input(
#     "Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
# future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

# while True:
#     now = datetime.now()
#     remaining = future_time - now

#     # Agar vaqt o'tib ketgan bo'lsa, siklni to'xtatish
#     if remaining.total_seconds() <= 0:
#         print("Vaqt tugadi!")
#         break

#     # Kun, soat, daqiqa, soniya hisoblash
#     days = remaining.days
#     hours, remainder = divmod(remaining.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     print(
#         f"Qolgan vaqt: {days} kun, {hours} soat, {minutes} daqiqa, {seconds} soniya", end="\r")

#     time.sleep(1)

# 6) Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re

# email = input("Email manzilingizni kiriting: ")

# # Xalqaro RFC 5322 standartiga yaqin regex
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# if re.match(pattern, email):
#     print("✅ Email manzili to'g'ri formatda!")
# else:
#     print("❌ Email manzili noto'g'ri!")

# 7) Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
phone = input("Telefon raqamingizni kiriting (faqat raqamlar): ")

# Faqat raqamlarni qoldirish
digits = "".join(filter(str.isdigit, phone))

if len(digits) == 10:
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print("❌ Telefon raqami 10 xonali bo'lishi kerak!")

# 8) Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
password = input("Parolingizni kiriting: ")

# Shartlar
min_length = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

if min_length and has_upper and has_lower and has_digit:
    print("✅ Parol kuchli!")
else:
    print("❌ Parol kuchsiz!")
    print("Shartlar:")
    print("- Kamida 8 ta belgidan iborat bo‘lishi kerak.")
    print("- Kamida bitta katta harf bo‘lishi kerak.")
    print("- Kamida bitta kichik harf bo‘lishi kerak.")
    print("- Kamida bitta raqam bo‘lishi kerak.")

# 9) Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
text = """
Python is a powerful programming language. 
Many people use Python for data analysis, machine learning, and web development.
Learning Python can be fun and rewarding.
"""

word = input("Qaysi so'zni qidirmoqchisiz? ").lower()

# Matnni so'zlarga bo‘lish va qidirish
words = text.lower().split()

occurrences = [i+1 for i, w in enumerate(words) if w.strip(".,") == word]

if occurrences:
    print(f"✅ \"{word}\" so'zi {len(occurrences)} marta uchradi.")
    print("Pozitsiyalari:", occurrences)
else:
    print(f"❌ \"{word}\" so'zi topilmadi.")

# 10) Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

# Foydalanuvchi matn kiritadi
text = input("Matnni kiriting: ")

# Sana formatlarini aniqlash (dd/mm/yyyy, dd-mm-yyyy, yyyy-mm-dd va h.k.)
date_pattern = r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b'

# Regex yordamida sanalarni topish
dates = re.findall(date_pattern, text)

if dates:
    print("Topilgan sanalar:")
    for d in dates:
        print("-", d)
else:
    print("Matnda sana topilmadi.")
