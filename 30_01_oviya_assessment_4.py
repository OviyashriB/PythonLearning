# ASSESSMENT 4


'''1. Write a Python program to filter a dictionary based on values.										
Input:										
Original Dictionary:										
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}										
Output:										
Marks greater than 170:										
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}'''										

input_dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}

def filter_dict(input_dict):
    emp_dict = {}
    for key, value in input_dict.items():
        if value > 170:
            emp_dict[key] = value
    return emp_dict

result = filter_dict(input_dict)
print(result)

# Dictionary Comprehension
comp = {key: value for key, value in input_dict.items() if value > 170}
print(comp)


'''2. Write a Python program to convert more than one list to a nested dictionary.										
Input : 										
Original strings:										
['S001', 'S002', 'S003', 'S004']										
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']										
[85, 98, 89, 92]										
Output:										
Nested dictionary:										
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]'''										

keys = ['S001', 'S002', 'S003', 'S004']										
values_1 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']										
values_2 = [85, 98, 89, 92]	       

def nested_dict(keys, values_1, values_2):
    if len(keys) != len(values_1) or len(keys) != len(values_2):
        print("Length aren't same")

    empty_lst = []
    for i in range(len(keys)):
        key = keys[i]                 # assigning value at index in the lst - keys
        value1 = values_1[i]
        value2 = values_2[i]  

        nested_dict = {key: {value1 : value2}}
        empty_lst.append(nested_dict)
    return empty_lst

result = nested_dict(keys, values_1, values_2)
print(result)


'''3. Write a Python program to extract and print the phone number of a specific employee from a nested dictionary.										
Input:										
employee_data = {										
    'Alice': {'position': 'Manager', 'phone': '123-456-7890'},										
    'Bob': {'position': 'Developer', 'phone': '987-654-3210'},										
    'Charlie': {'position': 'Analyst', 'phone': '555-123-4567'}										
}										
Expected Output:										
Phone number for Bob: 987-654-3210'''						

employee_data = {										
    'Alice': {'position': 'Manager', 'phone': '123-456-7890'},										
    'Bob': {'position': 'Developer', 'phone': '987-654-3210'},										
    'Charlie': {'position': 'Analyst', 'phone': '555-123-4567'}										
}	

def get_phone_num (employee_data, employee_name):
    if employee_name in employee_data:
        phone_num = employee_data[employee_name].get('phone')
        print(f"Phone number for Bob:", phone_num)
    else:
        return None

result = get_phone_num(employee_data, 'Bob')


'''4. You are given a nested dictionary representing a catalog of products in an online store. Each product has various attributes such as name, price, and availability. 
Write a Python program to find and print the names of products that are both affordable (price less than $50) and currently available.										
Input:										
product_catalog = {										
    'Laptop': {'price': 1200, 'availability': True},										
    'Headphones': {'price': 30, 'availability': True},										
    'Smartphone': {'price': 600, 'availability': False},										
    'Tablet': {'price': 40, 'availability': True},										
    'Camera': {'price': 150, 'availability': False}										
}										
Expected Output:										
Affordable and Available Products:										
['Headphones', 'Tablet']'''									


product_catalog = {										
    'Laptop': {'price': 1200, 'availability': True},										
    'Headphones': {'price': 30, 'availability': True},										
    'Smartphone': {'price': 600, 'availability': False},										
    'Tablet': {'price': 40, 'availability': True},										
    'Camera': {'price': 150, 'availability': False}										
}	

def func(product_catalog):
    emp_list = []
    for product, attributes in product_catalog.items():
        price = attributes.get('price')
        if price < 50:
            emp_list.append(product)
    return emp_list

result = func(product_catalog)
print(result)


