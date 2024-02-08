'''1. Given a complex JSON structure representing a hierarchical organization with employees and their departments, 
write a program to extract the names of all employees who hold a managerial position in any department. 
Ensure that the output is a sorted list of unique names. Extract the names of all employees holding a managerial position.																						
                                                    
Output:													
['Bob', 'Eve']'''													
# python to json - used dumps
inp_1 = {													
    "organization": {													
    "departments": [													
        {													
        "name": "Engineering",												
        "employees": [													
            {"name": "Alice", "position": "Engineer"},													
            {"name": "Bob", "position": "Manager"},													
            {"name": "Charlie", "position": "Engineer"}													
        ]													
        },													
        {													
        "name": "Sales",													
        "employees": [													
            {"name": "David", "position": "Salesperson"},													
            {"name": "Eve", "position": "Manager"}													
        ]													
        }													
    ]													
    }													
}				

import json
def extract_managerial_employees(inp_1):

    managerial_employees = [
        employee["name"]
        for department in inp_1.get("organization", {}).get("departments",[])
        for employee in department.get("employees",[])
        if employee.get("position") == "Manager"
    ]

    return json.dumps(sorted(set(managerial_employees)))

result = extract_managerial_employees(inp_1)
print(result)

'''2. Given a nested JSON structure representing a file system, write a program to find the total size occupied by files in a specific directory 
and its subdirectories.																				
                                                    
Output:													
The total size of files in the specified directory and its subdirectories is: 1984 bytes.	'''												
													
json_data = {													
    "name": "root",													
    "type": "directory",													
    "size": None,													
    "contents": [													
    {													
        "name": "folder1",													
        "type": "directory",													
        "size": None,													
        "contents": [													
        {"name": "file1.txt", "type": "file", "size": 1024},													
        {"name": "file2.txt", "type": "file", "size": 512}													
        ]													
    },													
    {													
        "name": "folder2",													
        "type": "directory",													
        "size": None,													
        "contents": [													
        {"name": "file3.txt", "type": "file", "size": 256},													
        {"name": "file4.txt", "type": "file", "size": 128}													
        ]													
    },													
    {"name": "file5.txt", "type": "file", "size": 64}													
    ]													
}						       

def to_calculate_file_size(json_data):
    total_size = 0

    for i in json_data.get("contents", []):
        if i["type"] == "file":
            total_size += i["size"]
        elif i["type"] == "directory":
            total_size += to_calculate_file_size(i)

    return total_size

targrt_dir = json_data["contents"][0]
result = to_calculate_file_size(json_data)
print(f"The total size of files in the specified directory and its subdirectories is: {result} bytes.")


'''3. Write a program to transform a JSON structure representing a list of students and their grades into a report card, 
including the average grade for each student and the class average. ALso sort the order of average from highest to lowest inside report card	
                                                    
Output:													
Report Card:													
[{'name': 'Charlie', 'average_grade': 92.0}, {'name': 'Alice', 'average_grade': 89.0}, {'name': 'Bob', 'average_grade': 87.0}]													
Class Average: 89	'''												

student_grades_json = {
  "students": [
    {"name": "Alice", "grades": [90, 85, 92]},
    {"name": "Bob", "grades": [78, 88, 94]},
    {"name": "Charlie", "grades": [92, 95, 89]}
  ]
}

student_grades = student_grades_json["students"]

report_card = []
for student in student_grades:
    name = student["name"]
    grades = student["grades"]
    average_grade = sum(grades) / len(grades)

    report_card.append({"name": name, "average_grade": average_grade})

report_card.sort(key=lambda x: x["average_grade"], reverse=True)

total_average_grades = sum(student["average_grade"] for student in report_card)
class_average = total_average_grades / len(report_card)

for student in report_card:
    student["average_grade"] = round(student["average_grade"], 1)

class_average = round(class_average)

print("Report Card:")
print(report_card)

print("Class Average:", class_average)


'''4. You are given two lists: one containing names and the other containing corresponding birth years.
 Your task is to manipulate these lists and generate key-value pairs with the name as the key and age as the value. 
Calculate the age based on the given birth year and today's date. Then, create a JSON structure to represent this information. 
Additionally, calculate the average age of the individuals and include it in the JSON output.																								
                                                    
Output should be in json format:													
{													
    "above_40": {													
    "Alice": 44,													
    "Bob": 46,													
    "David": 53													
    },													
    "below_40": {													
    "Charlie": 33,													
    "Eve": 29													
    },													
    "statistics": {													
    "count_above_40": 3,													
    "count_below_40": 2													
    }													
}			'''						
				
from datetime import datetime
names = ["Alice", "Bob", "Charlie", "David", "Eve"]													
birth_years = [1980, 1978, 1991, 1971, 1995]		

current_yr = datetime.now().year

above_40 = {}
below_40 = {}

count_above_40 = 0
count_below_40 = 0

for name, birth_yr in zip(names, birth_years):
    age = current_yr - birth_yr
    if age > 40:
        above_40[name] = age
        count_above_40 += 1
    else:
        below_40[name] = age
        count_below_40 += 1

total_age_above_40 = sum(above_40.values())
total_age_below_40 = sum(below_40.values())

average_age_above_40 = total_age_above_40 / count_above_40 if count_above_40 > 0 else 0
average_age_below_40 = total_age_below_40 / count_below_40 if count_below_40 > 0 else 0

output = {
    "above_40": above_40,
    "below_40": below_40,
    "statistics": {
        "count_above_40": count_above_40,
        "count_below_40": count_below_40,
        "average_age_above_40": round(average_age_above_40, 2),
        "average_age_below_40": round(average_age_below_40, 2)
    }
}

result = json.dumps(output, indent=2)
print(result)


'''5. You are provided with a JSON structure representing a list of employees in a company. 
Each employee has information such as name, department, and salary. 
Write a program to identify the highest-paid employee in each department and generate a new JSON structure with the department names and 
the corresponding highest-paid employee details.													
                                                    											
Output:													
{													
    "highest_paid_employees": [													
    {"department": "HR", "highest_paid_employee": {"name": "Charlie", "salary": 70000}},													
    {"department": "Engineering", "highest_paid_employee": {"name": "Eve", "salary": 90000}},													
    {"department": "Sales", "highest_paid_employee": {"name": "David", "salary": 75000}}													
    ]													
}'''	

inp_json = {
    "employees": [
        {"name": "Alice", "department": "HR", "salary": 60000},
        {"name": "Bob", "department": "Engineering", "salary": 80000},
        {"name": "Charlie", "department": "HR", "salary": 70000},
        {"name": "David", "department": "Sales", "salary": 75000},
        {"name": "Eve", "department": "Engineering", "salary": 90000}] }
        
dept_emplys = {}
for employee in inp_json["employees"]:
    department = employee["department"]
    if department not in dept_emplys:
        dept_emplys[department] = []
    dept_emplys[department].append(employee)

highest_paid_emplys = []
for dept, employees in dept_emplys.items():
    highest_paid_emplye = max(employees, key=lambda x: x["salary"])
    
    department_info = {"department": dept, "highest_paid_employee": highest_paid_emplye}
    
    highest_paid_emplys.append(department_info)

res = {"highest_paid_employees": highest_paid_emplys}
print(json.dumps(res))