# ASSESSMENT 10


'''1. Write a Python class BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and 
methods like deposit, withdraw, and check_balance.

Expected Output:

Customer Details:
Name: Toninho Takeo
Account Number: 2345
Date of opening: 01-01-2011
Balance: $1000

Name: Astrid Rugile
Account Number: 1234
Date of opening: 11-03-2011
Balance: $2000

Name: Orli Kerenza
Account Number: 2312
Date of opening: 12-01-2009
Balance: $3000

Name: Luciana Chika
Account Number: 1395
Date of opening: 01-01-2011
Balance: $3000

Name: Toninho Takeo
Account Number: 6345
Date of opening: 01-05-2011
Balance: $4000

Name: Luciana Chika
Account Number: 1395
Date of opening: 01-01-2011
Balance: $3000

$1000 has been deposited in your account.
Current balance is $4000.
Insufficient balance.
$3400 has been withdrawn from your account.
Current balance is $600.'''

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} has been deposited in your account.")
        self.check_balance()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} has been withdrawn from your account.")
        else:
            print("Insufficient balance.")
        self.check_balance()

    def check_balance(self):
        print(f"Current balance is ${self.balance}.\n")

accounts = [
    BankAccount(2345, 1000, "01-01-2011", "Toninho Takeo"),
    BankAccount(1234, 2000, "11-03-2011", "Astrid Rugile"),
    BankAccount(2312, 3000, "12-01-2009", "Orli Kerenza"),
    BankAccount(1395, 3000, "01-01-2011", "Luciana Chika"),
    BankAccount(6345, 4000, "01-05-2011", "Toninho Takeo"),
    BankAccount(1395, 3000, "01-01-2011", "Luciana Chika")]

print("Customer Details:")
for account in accounts:
    print(f"Name: {account.customer_name}")
    print(f"Account Number: {account.account_number}")
    print(f"Date of opening: {account.date_of_opening}")
    print(f"Balance: ${account.balance}")
    account.check_balance()

accounts[2].deposit(1000)
accounts[2].withdraw(5400)
accounts[2].withdraw(3400)


'''2. Write a Python class Inventory with attributes like item_id, item_name, stock_count, and price, and 
methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id and the value is a dictionary containing the item_name, stock_count, and price

Output:
Item Details:
Product Name: Laptop, Stock Count: 100, Price: 500.0
Product Name: Mobile, Stock Count: 110, Price: 450.0
Product Name: Desktop, Stock Count: 120, Price: 500.0
Product Name: Tablet, Stock Count: 90, Price: 550.0

Update the price of item code - 'I001':
Product Name: Laptop, Stock Count: 100, Price: 505.0

Update the stock of item code - 'I003':
Product Name: Desktop, Stock Count: 115, Price: 500.0'''

class Inventory:
    def __init__(self):
        self.item_details = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.item_details[item_id] = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }

    def update_item(self, item_id, **kwargs):
        if item_id in self.item_details:
            for key, value in kwargs.items():
                if key in self.item_details[item_id]:
                    self.item_details[item_id][key] = value
            print("Update successful")
        else:
            print("Item not found")

    def check_item_details(self, item_id):
        if item_id in self.item_details:
            details = self.item_details[item_id]
            print(f"Product Name: {details['item_name']}, Stock Count: {details['stock_count']}, Price: {details['price']}")
        else:
            print("Item not found")

inventory = Inventory()

inventory.add_item('I001', 'Laptop', 100, 500.0)
inventory.add_item('I002', 'Mobile', 110, 450.0)
inventory.add_item('I003', 'Desktop', 120, 500.0)
inventory.add_item('I004', 'Tablet', 90, 550.0)

print("Item Details:")
for item_id, details in inventory.item_details.items():
    print(f"Product Name: {details['item_name']}, Stock Count: {details['stock_count']}, Price: {details['price']}")

inventory.update_item('I001', price=505.0)
inventory.check_item_details('I001')
inventory.update_item('I003', stock_count=115)
inventory.check_item_details('I003')


'''3. Write a Python class to convert a Roman numeral to an integer.

Input and Expected output:
Input: "III", Output: 3 (III represents 3 in Roman numerals)
Input: "IV", Output: 4 (IV represents 4 in Roman numerals)
Input: "IX", Output: 9 (IX represents 9 in Roman numerals)
Input: "LVIII", Output: 58 (LVIII represents 58 in Roman numerals)
Input: "MCMXCIV", Output: 1994 (MCMXCIV represents 1994 in Roman numerals)'''

class RomanToInteger:
    def __init__(self):
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s: str) -> int:
        result = 0
        prev_value = 0

        for char in s[::-1]:
            value = self.roman_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value

        return result

res = RomanToInteger()
print(res.romanToInt("III"))      
print(res.romanToInt("IV"))    
print(res.romanToInt("IX"))    
print(res.romanToInt("LVIII"))  
print(res.romanToInt("MCMXCIV"))  


'''4.'''
library_data = {
    "library_name": "City Library",
    "location": "City XYZ",
    "books": [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Classic Fiction",
            "availability": True,
            "borrowers": []
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "genre": "Literary Fiction",
            "availability": False,
            "borrowers": [
                {"name": "Alice", "borrow_date": "2023-01-15", "due_date": "2023-02-15"},
                {"name": "Alice", "borrow_date": "2023-02-01", "due_date": "2023-03-01"},
                {"name": "Bob", "borrow_date": "2023-02-15", "due_date": "2023-03-15"},
                {"name": "Bob", "borrow_date": "2023-03-16", "due_date": "2023-04-16"}
            ]
        },
        {
            "title": "Harry Potter and the Philosopher's Stone",
            "author": "J.K. Rowling",
            "genre": "Fantasy",
            "availability": True,
            "borrowers": [
                {"name": "Charlie", "borrow_date": "2023-01-01", "due_date": "2023-01-31"},
                {"name": "Eve", "borrow_date": "2023-02-10", "due_date": "2023-03-10"},
                {"name": "Alice", "borrow_date": "2023-02-20", "due_date": "2023-03-20"}
            ]
        },
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "genre": "Classic Fiction",
            "availability": False,
            "borrowers": [
                {"name": "Alice", "borrow_date": "2023-03-01", "due_date": "2023-03-31"},
                {"name": "Bob", "borrow_date": "2023-03-15", "due_date": "2023-04-15"}
            ]
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "genre": "Dystopian Fiction",
            "availability": True,
            "borrowers": []
        }
    ]
}

'''a) Create a function that calculates the total number of books borrowed each month from the City Library. 
The function should return a dictionary where each key is a month (in the format "YYYY-MM") and 
the corresponding value is the total number of books borrowed in that month. 

Expected Output:
{'2023-01': 2, '2023-02': 4, '2023-03': 3}'''

def to_cal_borrowed_books_per_mon(library_data):
    borrowed_books_per_month = {}

    for book in library_data['books']:
        for borrower in book['borrowers']:
            borrow_date = borrower['borrow_date'][:7]
            if borrow_date not in borrowed_books_per_month:
                borrowed_books_per_month[borrow_date] = 1
            else:
                borrowed_books_per_month[borrow_date] += 1
                
    return borrowed_books_per_month

res = to_cal_borrowed_books_per_mon(library_data)
print(res)


'''b) Develop a function that identifies the most borrowed author from the City Library.
If there's a tie, return all authors with the highest number of borrowings.
Expected Output:
['Harper Lee']'''

def most_borrowed_author(library_data):
    author_borrow_counts = {}

    for book in library_data['books']:
        author = book['author']
        print(author)
        borrowers_count = len(book['borrowers'])
        print(borrowers_count)
        if author in author_borrow_counts:
            author_borrow_counts[author] += borrowers_count
        else:
            author_borrow_counts[author] = borrowers_count

    max_borrow_count = max(author_borrow_counts.values())
    print(max_borrow_count, '- max_borrow_count')
   
    most_borrowed_authors = []
    for author, count in author_borrow_counts.items():
        if count == max_borrow_count:
            most_borrowed_authors.append(author)

    return most_borrowed_authors

res = most_borrowed_author(library_data)
print(res)


'''c) Write a function that calculates the average duration (in days) books of each genre are borrowed from the City Library.
The function should return a dictionary where each key is a genre and the corresponding value is the average borrowing duration.
keep an eye on output, if the int ended with .5, return same, else round the decimal to nearest
Expected Output:
{'Literary Fiction': 29.5, 'Fantasy': 29, 'Classic Fiction': 30.5}'''

from datetime import datetime
def calculate_average_duration(library_data):
    genre_duration = {}
    genre_counts = {}

    for book in library_data['books']:
        for borrower in book['borrowers']:
            borrow_date = datetime.strptime(borrower['borrow_date'], "%Y-%m-%d")
            due_date = datetime.strptime(borrower['due_date'], "%Y-%m-%d")
            duration = (due_date - borrow_date).days
            print(duration)

            if book['genre'] not in genre_duration:
                genre_duration[book['genre']] = duration
                genre_counts[book['genre']] = 1
            else:
                genre_duration[book['genre']] += duration
                genre_counts[book['genre']] += 1

    average_durations = {}
    for genre, total_duration in genre_duration.items():
        count = genre_counts[genre]
        print('count', count)
        average_duration = total_duration / count
        print(average_duration)
        if average_duration % 1 == 0.5:
            average_durations[genre] = average_duration
        else:
            average_durations[genre] = round(average_duration)

    return average_durations

result = calculate_average_duration(library_data)
print(result)
