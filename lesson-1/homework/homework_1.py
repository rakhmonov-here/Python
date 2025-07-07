# Homework. Lesson 1
# 1) Given a side of square. Find its perimeter and area.

import math  # math kutubxonasidan pi sonini import qilish
side = int(input("Kvadratning tomonini kiriting: "))
perimeter = 4 * side  # Kvadratning perimetrini hisoblash
area = side**2  # Kvadratning yuzini hisoblash
print("Kvadratning perimetri: ", perimeter)
print("Kvadratning yuzi: ", area)

# 2) Given diameter of circle. Find its length.

diameter = int(input("Aylananing diametrini kiriting: "))
length = math.pi * diameter  # Aylananing uzunligini hisoblash
print("Aylananing uzunligi: ", length)

# 3)Given two numbers a and b. Find their mean.

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
mean = (a + b)/2  # Ikki sonning o'rtacha qiymatini topish
print("Ikki sonning o'rtacha qiymati: ", mean)

# 4) Given two numbers a and b. Find their sum, product and square of each number.

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
sum = a + b  # Ikki sonning yig'indisi
product = a * b  # Ikki sonning ko'paytmasi
asquare = a**2  # Birinchi sonning kvadrati
bsquare = b**2  # Ikkinchi sonning kvadrati
print("Ikki sonning yig'indisi: ", sum)
print("Ikki sonning ko'paytmasi: ", product)
print("Birinchi sonning kvadrati: ", asquare)
print("Ikkinchi sonning kvadrati: ", bsquare)
