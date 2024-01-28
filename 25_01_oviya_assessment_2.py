# ASSESSMENT 2


'''1.Turn every item of a list into its square .Given a list of numbers write a program to turn every item of a list into its square. 
Try to write it in function using both list comprehension, for loop methods separately.
Input : numbers = [1, 2, 3, 4, 5] 
Expected Output : [1, 4, 9, 16, 25]'''

numbers = [1, 2, 3, 4, 5] 
# Loop method
emp_list = []
for i in numbers:
    a = i ** 2
    emp_list.append(a)
print(emp_list)

# List comprehension
output = [i**2 for i in numbers]
print(output)


'''2. Concatenate two lists in the following order
Input: list1 = ["Hello ", "take "], list2 = ["Dear", "Sir"]
Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

emp_list = []
for list in list1:
    a = str(list) + str(list2[0])
    b = str(list) + str(list2[1])
    emp_list.append(a)
    emp_list.append(b)
print(emp_list)

'''3. Remove empty strings from the list of strings
Input:    ["Mike", "", "Emma", "Kelly", "", "Brad"]
output: ['Mike', 'Emma', 'Kelly', 'Brad']'''

input = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Method 1
emp_list = []
for i in input:
    if i != "":
        emp_list.append(i)
print(emp_list)

# Method 2
emp_list = []
for i in input:
    if i:
        emp_list.append(i)
print(emp_list)


'''4. Convert two lists into a dictionary
Input : 
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]
Output:  {'Ten': 10, 'Twenty': 20, 'Thirty': 30}'''

keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]
output = dict(zip(keys,values))
print(output)


'''5.  Delete a list of keys from a dictionary
Input : 
sample_dict =          {"name": "Kelly",     "age": 25,     "salary": 8000,     "city": "New York"}
Output:       {'age': 25, 'city': 'New York'}'''

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
remove = ["name", "salary"]
emp_dict = {}
for key,value in sample_dict.items():
    if key not in remove:
        emp_dict[key] = value
print(emp_dict)