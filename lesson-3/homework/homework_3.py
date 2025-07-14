#Homework. Lesson 3
#1)Create and Access List Elements. Create a list containing five different fruits and print the third fruit.

fruit_list = ['apple','banana','orange','grapes','strawberry']

print("The third fruit is:",fruit_list[2])

#2)Concatenate Two Lists. Create two lists of numbers and concatenate them into a single list.

first_list = [1,3,5,7,9]
second_list = [2,4,6,8]

first_list += second_list

print(first_list)

#3)Extract Elements from a List. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

numbers_list = [1,3,5,7,13,17,20]

first = numbers_list[0]
middle = numbers_list[len(numbers_list)//2]
last = numbers_list[-1]

new_list = [first,middle,last]

print(new_list)

#4)Convert List to Tuple. Create a list of your five favorite movies and convert it into a tuple.

my_movies = ['Ted Lasso','Squid Game','Deha','Inception','The Lion King']

my_tuple = tuple(my_movies)

print(my_tuple)

#5)Check Element in a List. Given a list of cities, check if "Paris" is in the list and print the result.

city_list = ['Madrid','London','Tashkent','Moscow','Kokand']

if city_list.count('Paris') == 1:
    print('Paris is in the list')
else: 
    print('Paris is not in the list')

#6)Duplicate a List Without Using Loops. Create a list of numbers and duplicate it without using loops.

numbers = [1,8,15,97,875]

duplicated = numbers * 2

print("Duplicated list:", duplicated)

#7)Swap First and Last Elements of a List. Given a list of numbers, swap the first and last elements.

nums = [15,45,90,105]

nums[0], nums[-1] = nums[-1], nums[0]

print("After swap:",nums)

#8)Slice a Tuple. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers_tuple = (1,2,3,4,5,6,7,8,9,10)

slice_tuple = numbers_tuple[3:7]

print("Slice tuple:", slice_tuple)

#9) Count Occurrences in a List. Create a list of colors and count how many times "blue" appears in the list.

colors = ["red", "blue", "green", "blue", "yellow", "blue","orange","gray","blue"]

num_blue = colors.count("blue")

print("Number of times 'blue' appears:",num_blue)

#10)Find the Index of an Element in a Tuple. Given a tuple of animals, find the index of "lion".

animals = ("lion", "tiger", "elephant", "giraffe", "zebra")

in_lion = animals.index("lion")

print("The index of lion:",in_lion)

#11)Merge Two Tuples. Create two tuples of numbers and merge them into a single tuple.

first_tuple = (1,2,7)
second_tuple = (5,11,8)

first_tuple += second_tuple

print(first_tuple)

#12)Find the Length of a List and Tuple. Given a list and a tuple, find and print their lengths.

list_1 = [1,3,65,8]
tuple_1 = ("Real","Madrid","Spain",15,36,"UCL")

length_list = len(list_1)
length_tuple = len(tuple_1)

print(length_list)
print(length_tuple)

#13)Convert Tuple to List. Create a tuple of five numbers and convert it into a list.

tuple_five = (1,2,3,4,5)

list_five = list(tuple_five)

print(list_five)

#14)Find Maximum and Minimum in a Tuple. Given a tuple of numbers, find and print the maximum and minimum values.

num_tuple = (1,4,19,87,35,54)

max_nums = max(num_tuple)
min_nums = min(num_tuple)

print("Maximum value:",max_nums)
print("Minimum value:",min_nums)

#15)Reverse a Tuple. Create a tuple of words and print it in reverse order.

words = ("John","reads","book")

reverse_word = words[::-1]

print(reverse_word)