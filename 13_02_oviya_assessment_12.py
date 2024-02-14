# ASSESSMENT 11


'''1. Run this below code in your terminal,
import json
import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_json(depth):
    if depth <= 0:
        return random.choice([None, random.randint(0, 100), generate_random_string(random.randint(5, 10))])

    result = {}
    for _ in range(random.randint(10, 20)):
        key = generate_random_string(random.randint(3, 7))
        result[key] = generate_random_json(depth - 1)

    return result

random_json = generate_random_json(3)

with open("random_data.json", "w") as json_file:
    json.dump(random_json, json_file, indent=4)

print("Random JSON data stored in 'random_data.json'")


you can see an random json data created in the directory, now use that given random data, find out the total number of keys, values, null values,

Expected output should be like below with each :
Total number of keys: 
Total number of values:
Total number of null values:'''

import json
with open('random_data.json') as f:
    data = json.load(f)
    print(data)
def count_metrics(data):
    total_keys = 0
    total_values = 0
    total_null_values = 0
    
    for key, value in data.items():
        total_keys += 1
        
        if isinstance(value, dict):
            sub_keys, sub_values, sub_null_values = count_metrics(value)
            total_keys += sub_keys
            total_values += sub_values
            total_null_values += sub_null_values
        elif value is None:
            total_null_values += 1
        else:
            total_values += 1
    
    return total_keys, total_values, total_null_values

total_keys, total_values, total_null_values = count_metrics(data)

print("Total number of keys:", total_keys)
print("Total number of values:", total_values)
print("Total number of null values:", total_null_values)


'''2.Write a program to build a simple Student Management System using Python which can perform the following operations:

Accept
Display
Search
Delete
Update

Expected Output:


Operations used,

a.Accept Student details
b.Display Student Details
c.Search Details of a Student
d.Delete Details of Student
e.Update Student Details
f.Exit



List of Students

Name   :  A
RollNo :  1
Marks1 :  100
Marks2 :  100


Name   :  B
RollNo :  2
Marks1 :  90
Marks2 :  90


Name   :  C
RollNo :  3
Marks1 :  80
Marks2 :  80



Student Found,
Name   :  B
RollNo :  2
Marks1 :  90
Marks2 :  90


List after deletion
Name   :  A
RollNo :  1
Marks1 :  100
Marks2 :  100


Name   :  C
RollNo :  3
Marks1 :  80
Marks2 :  80


List after updation
Name   :  A
RollNo :  1
Marks1 :  100
Marks2 :  100


Name   :  C
RollNo :  2
Marks1 :  80
Marks2 :  80
'''

class Student:
    def __init__(self, name, roll_no, marks1, marks2):
        self.name = name
        self.roll_no = roll_no
        self.marks1 = marks1
        self.marks2 = marks2

    def display_details(self):
        print("Name   :", self.name)
        print("RollNo :", self.roll_no)
        print("Marks1 :", self.marks1)
        print("Marks2 :", self.marks2)

def accept_details():
    name = input("Enter Name: ")
    roll_no = int(input("Enter RollNo: "))
    marks1 = int(input("Enter Marks1: "))
    marks2 = int(input("Enter Marks2: "))
    return Student(name, roll_no, marks1, marks2)

def display_students(students):
    print("\nList of Students")
    for student in students:
        student.display_details()

def search_student(students, roll_no):
    for student in students:
        if student.roll_no == roll_no:
            student.display_details()
            return student
    return None

def delete_student(students, roll_no):
    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            print("List after deletion")
            display_students(students)
            return

def update_student(students, roll_no):
    for student in students:
        if student.roll_no == roll_no:
            print("Enter new details:")
            student.name = input("Enter Name: ")
            student.marks1 = int(input("Enter Marks1: "))
            student.marks2 = int(input("Enter Marks2: "))
            print("List after updation")
            display_students(students)
            return

def main():
    students = []

    while True:
        print("\nOperations used,")
        print("a.Accept Student details")
        print("b.Display Student Details")
        print("c.Search Details of a Student")
        print("d.Delete Details of Student")
        print("e.Update Student Details")
        print("f.Exit")

        choice = input("Enter choice: ").lower()

        if choice == 'a':
            students.append(accept_details())
        elif choice == 'b':
            display_students(students)
        elif choice == 'c':
            roll_no = int(input("Enter RollNo to search: "))
            search_student(students, roll_no)
        elif choice == 'd':
            roll_no = int(input("Enter RollNo to delete: "))
            delete_student(students, roll_no)
        elif choice == 'e':
            roll_no = int(input("Enter RollNo to update: "))
            update_student(students, roll_no)
        elif choice == 'f':
            break
        else:
            print("Invalid choice! Please enter again.")

if __name__ == "__main__":
    main()