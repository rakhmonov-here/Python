# Homework. Lesson 6
# 1. Modify String with Underscores

my_txt = 'abcabcabcdeabcdefabcdef'

used_chars = ['a', 'e', 'i', 'o', 'u']

index = 2

while index < len(my_txt)-1 :
    if my_txt[index] not in used_chars:
         my_txt = my_txt[:index+1] + '_' + my_txt[index+1:]
         used_chars.append(my_txt[index])
         index += 4
    else:
        index += 1
        
print(my_txt)

# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

# Foydalanuvchidan son kiritishini so'raymiz
n = int(input("n sonini kiriting:"))

if n >= 1 and n <=20:  
    for i in list(range(n)):   
        if i >= 0 and i < n:
            print(i ** 2)
else:
    print("n soni 1 va 20 oralig'ida bo'lishi kerak")

# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using a while loop

cnt = 0

while cnt < 10:
    cnt += 1
    print(cnt)
    
# Exercise 2: Print the following pattern

n = 5  # qatordan iborat son

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number

# Foydalanuvchidan son kiritishini so'raymiz
num = int(input("ixtiyoriy son kiriting:"))

my_sum = 0

for i in list(range(num+1)):
    my_sum += i

print(my_sum)

# Exercise 4: Print multiplication table of a given number

# Foydalanuvchidan son kiritishini so'raymiz
number = int(input("Ixtiyoriy sonni kiriting: "))

for i in list(range(1,11)):
    print(i * number)

# Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i >= 100 and i <= 150:
        print(i)

# Exercise 6: Count the total number of digits in a number
number = int(input("ixtiyoriy son kiriting: "))

count = 0

while number != 0:
    number = number // 10
    count += 1

print("Raqamlar soni:", count)

# Exercise 7: Print reverse number pattern
n = 5 #qatordan iborat son

for i in reversed(range(1,n+1)):
    for j in reversed(range(1, i+1)):
        print(j, end=" ")
    print()

# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

for i in reversed(list1):
    print(i)

# Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10,0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution
for i in range(0, 5):
    print(i)
else:
    print("Done")


#Exercise 11: Print all prime numbers within a range

import math

for num in range(25, 50):
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Exercise 12: Display Fibonacci series up to 10 terms

n = 10

a, b = 0, 1  # Boshlang'ich 2 ta son

for x in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Exercise 13: Find the factorial of a given number

n = int(input("Istalgan sonni kiriting:"))

factorial = 1

if n > 0:
    for i in range(1, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")
else:
    print("Musbat son kiriting!")

# 4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter

list1 = [1, 1, 2] 
list2 = [2, 3, 4]

set1 =set(list1)
set2 = set(list2)

result = list(set1.symmetric_difference(set2))

print(result)