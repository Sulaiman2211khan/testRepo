''' Software Construction & Development
        Author: Muhammad Sulaiman'''

'''Online Selling bookstore Management System.'''
# Admin Class
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_book(self, book, inventory):
        book.inventory = inventory
        books.append(book)

    def remove_book(self, book):
        if book in books:
            books.remove(book)

# User Class
class User:
    def __init__(self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance
        self.cart = ShoppingCart()
        self.purchase_history = []

    def add_purchase(self, book, quantity, total_price):
        self.purchase_history.append((book, quantity, total_price))
        self.balance -= total_price

# Book Class
class Book:
    def __init__(self, title, author, price, inventory):
        self.title = title
        self.author = author
        self.price = price
        self.inventory = inventory

# ShoppingCart Class
class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, book, quantity=1):
        if book.inventory >= quantity:
            if book in self.cart:
                self.cart[book] += quantity
            else:
                self.cart[book] = quantity
            book.inventory -= quantity
            return True
        else:
            print("Sorry, the book is out of stock.")
            return False

    def view_cart(self):
        return self.cart

    def checkout(self):
        total_price = sum(book.price * quantity for book, quantity in self.cart.items())
        return total_price

# Define an empty list to store books
books = []

# Initial book data
books.append(Book("The Catcher in the Rye", "J.D. Salinger", 20.0, 10))
books.append(Book("To Kill a Mockingbird", "Harper Lee", 15.0, 15))
books.append(Book("1984", "George Orwell", 25.0, 5))

# Function to handle user registration
def user_registration(users):
    while True:
        username = input("Enter a username for registration: ")
        if username in users:
            print("Username already exists. Please choose another one.")
        else:
            password = input("Enter a password: ")
            balance = float(input("Enter your initial balance in Rs: "))
            users[username] = User(username, password, balance)
            print("Registration successful. Welcome, {}!".format(username))
            return username

# Define an empty dictionary to store admin instances
admins = {
    # "admin1": Admin("admin1", "adminpass")
}

users={
    # "user1": User("khan", "khan123",3433)
} 

# Function to handle user login
def user_login(users):
    while True:
        userName = input("Enter your username (or type 'register' to register): ")
        if userName == 'register':
            username = user_registration(users)
            if username:
                return username
        else:
            Password = input("Enter your password: ")
            if userName in users and users[userName].password == Password:
                print("Login successful. Welcome, {}!".format(userName))
                confirmation = input("Confirm login (yes/no): ")
                if confirmation.lower() == 'yes':
                    return userName
                else:
                    print("Login not confirmed.")
            else:
                print("Invalid username or password. Please try again.")

# Function to handle admin registration
def admin_registration(admins):
    username = input("Enter an admin username for registration: ")
    if username in admins:
        print("Admin username already exists.")
    else:
        password = input("Enter an admin password: ")
        admins[username] = Admin(username, password)
        print("Admin registration successful. Welcome, {}!".format(username))
        return username

# Function to handle admin login
def admin_login(admins):
    while True:
        userName = input("Enter your admin username (or type 'register' to register as admin): ")
        if userName == 'register':
            username = admin_registration(admins)
            if username:
                return username
        else:
            Password = input("Enter your admin password: ")
            if userName in admins and admins[userName].password == Password:
                print("Admin login successful. Welcome, {}!".format(userName))
                return userName
            else:
                print("Invalid admin username or password. Please try again.")

# Function to perform admin-specific actions
def admin_features(books, users):
    admin = admin_login(admins)
    if admin:
        while True:
            choice = input(
                "Select an admin feature:\n1. Add a book\n2. Remove a book\n3. View Books\n4. View User Book History\n5. Back\nEnter your choice: ")

            if choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                price = float(input("Enter book price in Rs: "))
                inventory = int(input("Enter book inventory: "))
                new_book = Book(title, author, price, inventory)
                books.append(new_book)
                print("Book added successfully.")

            elif choice == '2':
                print("Current Books:")
                for index, book in enumerate(books):
                    print(
                        f"{index + 1}. {book.title} by {book.author}, Price: Rs {book.price}, Inventory: {book.inventory}")
                book_number = int(input("Enter the number of the book to remove: ")) - 1
                if 0 <= book_number < len(books):
                    books.remove(books[book_number])
                    print("Book removed successfully.")
                else:
                    print("Invalid book number. Please try again.")

            elif choice == '3':
                print("Available Books:")
                for book in books:
                    print(
                        f"Title: {book.title}, Author: {book.author}, Price: Rs {book.price}, Inventory: {book.inventory}")

            elif choice == '4':
                print("User Book History:")
                for username, user in users.items():
                    print(f"Username: {username}")
                    for book, quantity, total_price in user.purchase_history:
                        print(f"Book: {book.title}, Quantity: {quantity}, Total Price: Rs {total_price}")

            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

# Function to handle the main menu
def main():
    while True:
        print("Welcome to the Online Book Store")
        print("1. Login")
        print("2. Admin")
        print("3 Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = user_login(users)
            if username:
                user = users[username]  # Get the user object for the logged-in user

                while True:
                    # Display available books
                    print("Available Books:")
                    for index, book in enumerate(books):
                        print(
                            f"{index + 1}. {book.title} by {book.author}, Price: Rs {book.price}, Inventory: {book.inventory}")

                    user_choice = input(
                        "Enter '1' to select a book, '2' to view your cart, or '3' to Go Back: ")

                    if user_choice == '1':
                        book_number = int(input("Enter the number of the book to select (1-N): ")) - 1
                        if 0 <= book_number < len(books):
                            selected_book = books[book_number]
                            quantity = int(
                                input(f"Enter the quantity you want to purchase of {selected_book.title}: "))
                            if user.balance >= selected_book.price * quantity:
                                if user.cart.add_to_cart(selected_book, quantity):
                                    user.balance -= selected_book.price * quantity
                                    print(
                                        f"{quantity} {selected_book.title} added to your cart.")
                                else:
                                    print("Failed to add to cart.")
                            else:
                                print("Insufficient balance.")
                        else:
                            print("Invalid book number. Please try again.")
                    elif user_choice == '2':
                        cart = user.cart
                        cart_contents = cart.view_cart()
                        if cart_contents:
                            print("Shopping Cart Contents:")
                            for book, quantity in cart_contents.items():
                                print(f"{book.title} - Quantity: {quantity}")
                            checkout = input(
                                "Proceed to checkout (yes/no): ").lower()
                            if checkout == 'yes':
                                total_price = cart.checkout()
                                user.balance -= total_price
                                print(f"Total Price: Rs {total_price}")
                                print(f"Remaining Balance: Rs {user.balance}")
                                for book, quantity in cart_contents.items():
                                    user.add_purchase(book, quantity, book.price * quantity)
                                cart.cart.clear()
                                print("Your cart is empty.")
                            else:
                                print("Cart checkout canceled.")
                        else:
                            print("Your cart is empty.")
                    elif user_choice == '3':
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '2':
            admin_features(books, users)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
