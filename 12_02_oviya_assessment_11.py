'''1. Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price.
Expected Output:
Current Items in Cart:
Papaya - 100
Guava - 200
Orange - 150
Total Quantity: 450

Updated Items in Cart after removing Orange:
Papaya - 100
Guava - 200
Total Quantity: 300'''

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def calculate_total_price(self):
        total_price = sum(self.items.values())
        return total_price

    def display_cart(self):
        for item, price in self.items.items():
            print(f"{item} - {price}")
        print("Total Quantity:", sum(self.items.values()))

cart = ShoppingCart()
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)
print("Current items in cart:")
cart.display_cart()

cart.remove_item("Orange")
# updated one
print("\nUpdated items in cart after removing orange:")
cart.display_cart()


'''2. Design a class Calculator that performs basic arithmetic operations. 
The class should have the following methods like add, subtract, multiply and 
divide, square, square root, power, absolute value, factorial, percentage

Expected Output:
calc = Calculator()
print(calc.add(5, 3))            
# Expected output: 8
print(calc.subtract(10, 4))       
# Expected output: 6
print(calc.multiply(2, 6))        
# Expected output: 12
print(calc.divide(15, 4))         
# Expected output: 3.75
print(calc.square(4))             
# Expected output: 16
print(calc.square_root(9))        
# Expected output: 3.0
print(calc.power(2, 3))           
# Expected output: 8
print(calc.absolute_value(-5))    
# Expected output: 5
print(calc.factorial(5))          
# Expected output: 120
print(calc.percentage(30, 50)) '''

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def square(self, x):
        return x ** 2

    def square_root(self, x):
        return x ** 0.5

    def power(self, x, y):
        return x ** y

    def absolute_value(self, x):
        return abs(x)

    def factorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.factorial(x - 1)

    def percentage(self, x, y):
        return (x / y) * 100

calc = Calculator()
print(calc.add(5, 3))             
print(calc.subtract(10, 4))        
print(calc.multiply(2, 6))         
print(calc.divide(15, 4))         
print(calc.square(4))              
print(calc.square_root(9))         
print(calc.power(2, 3))            
print(calc.absolute_value(-5))     
print(calc.factorial(5))           
print(calc.percentage(30, 50))     