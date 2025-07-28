# Homework. Lesson 9
# 1) Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
from datetime import datetime
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        # Return the area of the circle
        return math.pi * (self.radius ** 2)

    def circle_perimeter(self):
        # Return the perimeter of the circle
        return 2 * math.pi * self.radius


# Example usage
r = float(input("Enter the radius of the circle:"))
c = Circle(r)

print(f"Area: {c.circle_area():.2f}")
print(f"Perimeter: {c.circle_perimeter():.2f}")

# 2) Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
       # date_of_birth in format 'YYYY-MM-DD'
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def get_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        # Adjust age if birthday hasn't occurred yet this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


# Example usage
name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")

person = Person(name, country, dob)

print(f"\nName: {person.name}")
print(f"Country: {person.country}")
print(f"Age: {person.get_age()} years old")

# 3) Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b


# Example usage:
calc = Calculator()

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print(f"Addition: {calc.add(x, y)}")
print(f"Subtraction: {calc.subtract(x, y)}")
print(f"Multiplication: {calc.multiply(x, y)}")
print(f"Division: {calc.divide(x, y)}")

# 4) Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

# Base class


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass for Circle


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Subclass for Triangle (assuming sides are known)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Subclass for Square


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# Example usage
circle = Circle(5)
print("Circle -> Area:", circle.area(), "Perimeter:", circle.perimeter())

triangle = Triangle(3, 4, 5)
print("Triangle -> Area:", triangle.area(), "Perimeter:", triangle.perimeter())

square = Square(6)
print("Square -> Area:", square.area(), "Perimeter:", square.perimeter())

# 5) Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # If value == current.value, do nothing (no duplicates)

    def search(self, value):
        """Search for a value in the BST. Returns True if found, False otherwise."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if value == current.value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)


# Example usage:
bst = BinarySearchTree()
values = [10, 5, 15, 3, 7, 12, 18]
for v in values:
    bst.insert(v)

# Searching
print("Search 7:", bst.search(7))    # True
print("Search 20:", bst.search(20))  # False

# 6) Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)


# Example usage:
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())     # 30
print("Popped:", stack.pop())           # 30
print("Popped:", stack.pop())           # 20
print("Is stack empty?", stack.is_empty())  # False
print("Popped:", stack.pop())           # 10
print("Popped:", stack.pop())           # Stack is empty

# 7) Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Initially the list is empty

    def insert(self, data):
        """Insert a new node with given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node  # List is empty
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node

    def delete(self, key):
        """Delete the first node with the given data."""
        current = self.head
        prev = None

        while current:
            if current.data == key:
                if prev is None:
                    self.head = current.next  # Deleting head
                else:
                    prev.next = current.next
                return True  # Node deleted
            prev = current
            current = current.next

        return False  # Node not found

    def display(self):
        """Print all elements in the linked list."""
        current = self.head
        if current is None:
            print("Linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Initial list:")
ll.display()

print("\nDeleting 20:")
ll.delete(20)
ll.display()

print("\nDeleting 40 (not in list):")
deleted = ll.delete(40)
print("Deleted?", deleted)
ll.display()

# 8) Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Store items as {item_name: (price, quantity)}

    def add_item(self, name, price, quantity=1):
        """Add an item to the cart or update its quantity."""
        if name in self.items:
            current_price, current_qty = self.items[name]
            self.items[name] = (price, current_qty + quantity)
        else:
            self.items[name] = (price, quantity)

    def remove_item(self, name):
        """Remove an item from the cart."""
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} is not in the cart.")

    def total_price(self):
        """Calculate and return the total cost of items in the cart."""
        return sum(price * qty for price, qty in self.items.values())

    def show_cart(self):
        """Display all items in the cart."""
        if not self.items:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        for name, (price, qty) in self.items.items():
            print(f"- {name}: ${price:.2f} x {qty} = ${price * qty:.2f}")
        print(f"Total: ${self.total_price():.2f}")


# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 0.99, 3)
cart.add_item("Milk", 2.50, 1)
cart.add_item("Bread", 1.75, 2)

cart.show_cart()

print("\nRemoving 'Milk' from the cart...")
cart.remove_item("Milk")
cart.show_cart()

# 9) Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        removed = self.items.pop()
        print(f"Popped: {removed}")
        return removed

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for item in reversed(self.items):
                print(item)

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()

# 10) Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        removed = self.items.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    def display(self):
        """Display all items in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue (front to rear):")
            for item in self.items:
                print(item)

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0


# Example usage
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

queue.display()

queue.dequeue()
queue.display()

# 11) Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.


class Customer:
    def __init__(self, name, account_number, balance=0.0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(
                f"Deposited ${amount:.2f} into account {self.account_number}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}")

    def display(self):
        print(
            f"Name: {self.name}, Account: {self.account_number}, Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, account_number, initial_balance=0.0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = Customer(
                name, account_number, initial_balance)
            print(f"Account created for {name} with number {account_number}")

    def deposit(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            customer.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        customer = self.customers.get(account_number)
        if customer:
            customer.withdraw(amount)
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        customer = self.customers.get(account_number)
        if customer:
            print(f"Account {account_number} balance: ${customer.balance:.2f}")
        else:
            print("Account not found.")

    def display_all_customers(self):
        if not self.customers:
            print("No customers in the bank.")
        else:
            print("Customer List:")
            for customer in self.customers.values():
                customer.display()


# Example usage
bank = Bank()
bank.create_account("Alice", "1001", 500.0)
bank.create_account("Bob", "1002", 300.0)

bank.deposit("1001", 150)
bank.withdraw("1002", 100)

bank.check_balance("1001")
bank.display_all_customers()
