# Homework. Lesson 5
#1) Determines whether a given year is a leap year.

# Tekshiriladigan yilni so'raymiz
year = input("Tekshiriladigan yilni kiriting:")

# Kiritilgan qiymat integer yoki integer emasligini tekshiramiz
x = year.isdigit()

# Agar integer bo'lsa hisoblashni amalga oshiramiz
if x == True:
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0):
        print(f"{year} - kabisa yili")
    else:
        print(f"{year} - kabisa yili emas")

# Aks holda "Year must be an integer" xabarini chiqaramiz       
else:
    print("ValueError:","Year must be an integer")

# Conditional Statements Exercise
# 2) Given an integer, n, perform the following conditional actions:

'''If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''

# Son kiritishni so'raymiz
n = int(input("n sonini kiriting: "))

# Kiritiladigan son cheklovga mos kelishini tekshiramiz
if (n >= 1 and n <= 100):

# Agar mos kelsa, quyidagi shartlar bajarilsin
    if n % 2 == 1:
        print("Weird")
    elif (n % 2 == 0) and (n >= 2 and n <= 5):
        print("Not Weird")
    elif (n % 2 == 0) and (n >= 6 and n <= 20):
        print("Weird")
    elif (n % 2 == 0) and (n > 20):
        print("Not Weird")

# Aks holda, ushbu xabar yuborilsin 
else:
    print("Kiritilgan raqam 1 <= n <= 100 ushbu shartni qanoatlantirishi kerak")

# 3)Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

# Ikkita son kiritishni so'raymiz
a = int(input("a sonini kiriting:"))
b = int(input("b sonini kiriting:"))

# Solution 1
start = min(a, b)
end = max(a, b)

# Juft sonlar ro'yxatini to'plash
numbers = range(start, end + 1)

# Har bir elementni filter bilan ajratamiz
even_numbers = list(filter(lambda x: x % 2 == 0 if True else False, numbers))
    
print("Juft sonlar:", even_numbers)

# Solution 2
start = min(a, b) + (min(a, b) % 2)        # Agar toq bo‘lsa, keyingi juftdan boshlaydi
end = max(a, b)

even_numbers = list(range(start, end + 1, 2))  # 2 qadam bilan yuradi

print("Juft sonlar:", even_numbers)