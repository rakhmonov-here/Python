# Homework. Lesson 10
# 1) Homework 1. ToDo List Application
from datetime import datetime


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = False  # False = Incomplete, True = Complete

    def mark_complete(self):
        self.status = True

    def __str__(self):
        status = "✓ Done" if self.status else "⏳ Incomplete"
        return f"{self.title} - {self.description} | Due: {self.due_date.date()} | Status: {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            return True
        return False

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. {task}")

    def display_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.status]
        if not incomplete:
            print("All tasks are completed!")
        for idx, task in enumerate(incomplete):
            print(f"{idx + 1}. {task}")


def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Show Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Task title: ")
            description = input("Description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            try:
                task = Task(title, description, due_date)
                todo.add_task(task)
                print("Task added successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            todo.list_all_tasks()
            index = int(input("Enter task number to mark complete: ")) - 1
            if todo.mark_task_complete(index):
                print("Task marked as complete.")
            else:
                print("Invalid task number.")

        elif choice == "3":
            print("\nAll Tasks:")
            todo.list_all_tasks()

        elif choice == "4":
            print("\nIncomplete Tasks:")
            todo.display_incomplete_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# 2) Homework 2. Simple Blog System


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nDate: {self.timestamp.strftime('%Y-%m-%d %H:%M')}\nContent: {self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        if not self.posts:
            print("No posts found.")
        for idx, post in enumerate(self.posts):
            print(f"{idx + 1}. {post}")

    def posts_by_author(self, author):
        filtered = [p for p in self.posts if p.author.lower() ==
                    author.lower()]
        if not filtered:
            print(f"No posts found by {author}.")
        for post in filtered:
            print(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            print("Post deleted successfully.")
        else:
            print("Invalid index.")

    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content
            print("Post updated.")
        else:
            print("Invalid index.")

    def latest_posts(self, count=3):
        latest = sorted(self.posts, key=lambda p: p.timestamp,
                        reverse=True)[:count]
        print(f"\nLatest {len(latest)} post(s):")
        for post in latest:
            print(post)


def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Post title: ")
            content = input("Content: ")
            author = input("Author: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added.")

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.posts_by_author(author)

        elif choice == "4":
            blog.list_posts()
            index = int(input("Enter post number to delete: ")) - 1
            blog.delete_post(index)

        elif choice == "5":
            blog.list_posts()
            index = int(input("Enter post number to edit: ")) - 1
            new_title = input("New title: ")
            new_content = input("New content: ")
            blog.edit_post(index, new_title, new_content)

        elif choice == "6":
            blog.latest_posts()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Show Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            title = input("Post title: ")
            content = input("Content: ")
            author = input("Author: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added.")

        elif choice == "2":
            blog.list_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            blog.posts_by_author(author)

        elif choice == "4":
            blog.list_posts()
            index = int(input("Enter post number to delete: ")) - 1
            blog.delete_post(index)

        elif choice == "5":
            blog.list_posts()
            index = int(input("Enter post number to edit: ")) - 1
            new_title = input("New title: ")
            new_content = input("New content: ")
            blog.edit_post(index, new_title, new_content)

        elif choice == "6":
            blog.latest_posts()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

# 3) Homework 3. Simple Banking System


class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Account Number: {self.account_number}, Holder: {self.holder_name}, Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def check_balance(self, acc_number):
        account = self.get_account(acc_number)
        return account.balance if account else None

    def deposit(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            return account.deposit(amount)
        return False

    def withdraw(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            return account.withdraw(amount)
        return False

    def transfer(self, from_acc, to_acc, amount):
        from_account = self.get_account(from_acc)
        to_account = self.get_account(to_acc)
        if from_account and to_account and from_account.withdraw(amount):
            to_account.deposit(amount)
            return True
        return False

    def display_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        for acc in self.accounts.values():
            print(acc)


def main():
    bank = Bank()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Money")
        print("6. Display All Accounts")
        print("7. Exit")

        choice = input("Choose an option (1–7): ")

        if choice == "1":
            acc_no = input("Account Number: ")
            name = input("Holder Name: ")
            balance = float(input("Initial Balance: "))
            acc = Account(acc_no, name, balance)
            bank.add_account(acc)
            print("Account added successfully.")

        elif choice == "2":
            acc_no = input("Enter Account Number: ")
            account = bank.get_account(acc_no)
            if account:
                print(f"Balance: ${account.balance:.2f}")
            else:
                print("Account not found.")

        elif choice == "3":
            acc_no = input("Enter Account Number: ")
            amount = float(input("Amount to deposit: "))
            if bank.deposit(acc_no, amount):
                print("Deposit successful.")
            else:
                print("Deposit failed.")

        elif choice == "4":
            acc_no = input("Enter Account Number: ")
            amount = float(input("Amount to withdraw: "))
            if bank.withdraw(acc_no, amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed (insufficient funds?).")

        elif choice == "5":
            from_acc = input("From Account: ")
            to_acc = input("To Account: ")
            amount = float(input("Amount to transfer: "))
            if bank.transfer(from_acc, to_acc, amount):
                print("Transfer successful.")
            else:
                print("Transfer failed.")

        elif choice == "6":
            bank.display_all_accounts()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
