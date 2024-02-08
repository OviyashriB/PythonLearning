'''1. Given a JSON structure representing employees and their skills, 
write a Python program to generate a new JSON structure mapping each skill to the employees possessing that skill.'''

input_data = {
  "employees": [
    {"name": "Alice", "skills": ["Python", "Java"]},
    {"name": "Bob", "skills": ["C++", "Python", "JavaScript"]},
    {"name": "Charlie", "skills": ["Java", "JavaScript"]},
    {"name": "David", "skills": ["Python", "C#"]},
    {"name": "Eve", "skills": ["JavaScript", "HTML", "CSS"]}
  ]
}

'''out_put = {
  "skill_mapping": {
    "Python": ["Alice", "Bob", "David"],
    "Java": ["Alice", "Charlie"],
    "C++": ["Bob"],
    "JavaScript": ["Bob", "Charlie", "Eve"],
    "C#": ["David"],
    "HTML": ["Eve"],
    "CSS": ["Eve"]
  }
}'''

def generate_skill_mapping(input_data):
    skill_mapping = {}
    
    for employee in input_data["employees"]:
        name = employee["name"]
        skills = employee["skills"]
        
        for i in skills:
            if i not in skill_mapping:
                skill_mapping[i] = []
            skill_mapping[i].append(name)
    return {"skill_mapping": skill_mapping}

res = generate_skill_mapping(input_data)
print(res,'test')


# 2
json_data = {
  "company": "InnovateTech",
  "location": "Metropolis",
  "departments": [
    {
      "name": "Engineering",
      "manager": "Amit Sharma",
      "employees": [
        {
          "id": 1,
          "name": "Sunita Patel",
          "position": "Software Engineer",
          "salary": 95000,
          "projects": [
            {
              "name": "AI Chatbot Development",
              "status": "In Progress"
            },
            {
              "name": "Data Analytics Dashboard",
              "status": "Completed"
            }
          ]
        },
        {
          "id": 2,
          "name": "Rahul Singh",
          "position": "DevOps Engineer",
          "salary": 105000,
          "projects": [
            {
              "name": "Continuous Integration Pipeline",
              "status": "In Progress"
            }
          ]
        },
        {
          "id": 3,
          "name": "Deepa Sharma",
          "position": "Frontend Developer",
          "salary": 90000,
          "projects": [
            {
              "name": "User Interface Redesign",
              "status": "Completed"
            }
          ]
        }
      ]
    },
    {
      "name": "Marketing",
      "manager": "Neha Verma",
      "employees": [
        {
          "id": 4,
          "name": "Aryan Khan",
          "position": "Marketing Manager",
          "salary": 110000,
          "campaigns": [
            {
              "name": "Product Launch Campaign",
              "status": "In Progress"
            }
          ]
        },
        {
          "id": 5,
          "name": "Neha Gupta",
          "position": "Digital Marketer",
          "salary": 80000,
          "campaigns": [
            {
              "name": "Social Media Campaign",
              "status": "Completed"
            }
          ]
        }
      ]
    }
  ]
}

'''a) Given the JSON data provided, write a function that returns the total number of completed projects across all departments.
Expected output: Total number of completed projects: 2'''

import json

def count_completed_projects(json_data):
    total_completed_projects = 0
    departments = json_data.get("departments", [])
    for department in departments:
        employees = department.get("employees", [])
        for employee in employees:
            projects = employee.get("projects", [])
            for project in projects:
                if project["status"] == "Completed":
                    total_completed_projects += 1
    return total_completed_projects

result = count_completed_projects(json_data)
print("Total number of completed projects:", result)


'''b) Using the JSON data, generate a report that lists all employees along with their positions and salaries, sorted in descending order of salaries.
Expected Output: 
Employee Report:
Name: Aryan Khan, Position: Marketing Manager, Salary: 110000
Name: Rahul Singh, Position: DevOps Engineer, Salary: 105000
Name: Sunita Patel, Position: Software Engineer, Salary: 95000
Name: Deepa Sharma, Position: Frontend Developer, Salary: 90000
Name: Neha Gupta, Position: Digital Marketer, Salary: 80000'''

all_employees = []
for dept in json_data["departments"]:
    for employee in dept["employees"]:
        all_employees.append((employee["name"], employee["position"], employee["salary"]))

sorted_employees = sorted(all_employees, key=lambda x: x[2], reverse=True)
print("Employee Report:")
for employee in sorted_employees:
    print(f"Name: {employee[0]}, Position: {employee[1]}, Salary: {employee[2]}")


'''c) Extend the JSON data to include a new department called "Finance" with a manager named "Rajesh Kumar". 
Then, write a function to update the JSON with a new employee in the Finance department. The new employee's details are:

Name: Priya Mehta
Position: Financial Analyst
Salary: 95000
Expected output: given details should be added to existing json and print the updated json in terminal.'''
new_employee = {
    "id": 6,
    "name": "Priya Mehta",
    "position": "Financial Analyst",
    "salary": 95000
}

new_department = {
    "name": "Finance",
    "manager": "Rajesh Kumar",
    "employees": [new_employee]
}

json_data["departments"].append(new_department)
print(json.dumps(json_data, indent=2))


'''d) Utilizing the provided JSON, create a report that lists all ongoing projects, along with the department they belong to and their respective managers.

Expected Output:
Ongoing Projects Report:
Project: AI Chatbot Development, Department: Engineering, Manager: Amit Sharma
Project: Continuous Integration Pipeline, Department: Engineering, Manager: Amit Sharma
Project: Product Launch Campaign, Department: Marketing, Manager: Neha Verma'''

print("Ongoing Projects Report:")
for dept in json_data["departments"]:
    manager = dept["manager"]
    for employee in dept["employees"]:
        projects = employee.get("projects", [])  
        for project in projects:
            if project["status"] == "In Progress":
                project_name = project["name"]
                dept_name = dept["name"]
                print(f"Project: {project_name}, Department: {dept_name}, Manager: {manager}")

'''e) Given the JSON structure, write a function that calculates the average salary for each department.
Expected Output:
Average Salaries for Each Department:
Engineering: 96833.33333333333
Marketing: 95000.0
Finance: 95000.0'''


import statistics
def calculate_average_salaries(json_data):
    average_salaries = {}
    
    for dept in json_data["departments"]:
        dept_name = dept["name"]
        salaries = [employee["salary"] for employee in dept["employees"]]
        average_salary = statistics.mean(salaries)
        average_salaries[dept_name] = average_salary
    return average_salaries

res =  calculate_average_salaries(json_data)
print(res,'res')
for dept, average_salary in res.items():  
    print(f"{dept}: {average_salary}")