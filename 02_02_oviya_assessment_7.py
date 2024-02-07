'''1. Write a function to eliminate all special characters for each of strings in a list and just return back alpha strings for each in a list		
Output:													
['nB23', 'Gh45vD9zL', 'qW3yU1r7X', 'p8JmVcBn6F', 'k2oT7sPmQl']'''										
												
input1=['nB~!@#$%^23', 'Gh&*45vD9zL', 'qW@3yU%1r+7X', 'p$*8JmVcBn6F', 'k!2oT&7sPmQ"(l']											
import re                                                    
def to_eliminate_splchars(input1):
    emp_list = []
    for i in input1:
        alphanum = re.sub(r'[^a-zA-Z0-9]', '', i)
        emp_list.append(alphanum)
    return emp_list

result = to_eliminate_splchars(input1)
print(result)


'''2. Write a function to manipulate the values of list of dictionary. 
for example, if its int, multiply with 2, str means reverse it, float means, round to nearby number,																								
Output:													
[{'a': 10, 'b': 'olleh', 'c': 3}, {'x': 20, 'y': 'dlrow', 'z': 8}]	'''												

list_of_dicts = [													
    {'a': 5, 'b': 'hello', 'c': 3.14},													
    {'x': 10, 'y': 'world', 'z': 7.5}]	

def to_manipulate_values(list_of_dicts):
    emp_list = []

    for i in list_of_dicts:
        emp_dict = {}

        for key, value in i.items():
            if isinstance(value, int):
                emp_dict[key] = value * 2
            elif isinstance(value, str):
                emp_dict[key] = value[::-1]
            elif isinstance(value, float):
                emp_dict[key] = round(value)
        emp_list.append(emp_dict)

    return emp_list

result = to_manipulate_values(list_of_dicts)
print(result)


'''3. Write a function to manipulate the values of below input as expected								
Output: {'word1': 'oll*h', 'word2': 'l*v*l - palindrome', 'word3': '*lpmax*', 'word4': 'rac*car - palindrome'}	'''												

input_dict = {													
    'word1': 'hello',													
    'word2': 'level',													
    'word3': 'example',													
    'word4': 'racecar'													
}	

def to_manipulate(input_dict):
    emp_dict = {}
    for key, value in input_dict.items():
        reverse_val = value[::-1]
        reverse_val1 = reverse_val.replace('e', '*')

        palindrome_cnt = ""
        if value == reverse_val1:
            palindrome_cnt = "- palindrome"
        manipulate_value = f'{reverse_val1} {palindrome_cnt}'
        emp_dict[key] = manipulate_value
    return emp_dict

res = to_manipulate(input_dict)
print(res)


'''4. Given a dictionary with string keys and integer values, transform it into a new dictionary where the keys are the lengths of the original keys, 
and the values are lists of keys of that length. 													
Input:													
original_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4, 'grape': 5}													
Output:													
transformed_dict = {4: ['kiwi'], 5: ['apple', 'grape'], 6: ['banana', 'orange']}'''	

original_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4, 'grape': 5}

def transform_dict(original_dict):
    emp_dict = {}

    for key, value in original_dict.items():
        key_len = len(key) 

        if key_len not in emp_dict: 
            emp_dict[key_len] = [key] 
        else:
            emp_dict[key_len].append(key)

    return emp_dict

result = transform_dict(original_dict)
print(result)


'''5. Given a list of dictionaries representing student information, 
where each dictionary has keys 'name', 'subject', and 'marks', 
write a Python function to transform the list into a dictionary where each subject is a key, 
and the value is a list of students who scored the highest marks in that subject.													
Input:													
student_data = [													
    {'name': 'Alice', 'subject': 'Math', 'marks': 90},													
    {'name': 'Bob', 'subject': 'Math', 'marks': 85},													
    {'name': 'Alice', 'subject': 'Physics', 'marks': 88},													
    {'name': 'Bob', 'subject': 'Physics', 'marks': 92},													
    {'name': 'Alice', 'subject': 'Chemistry', 'marks': 78},													
    {'name': 'Bob', 'subject': 'Chemistry', 'marks': 88}													
]													
Output:													
highest_scorers = {													
    'Math': ['Alice'],													
    'Physics': ['Bob'],													
    'Chemistry': ['Bob']}'''									

student_data = [
    {'name': 'Alice', 'subject': 'Math', 'marks': 90},
    {'name': 'Bob', 'subject': 'Math', 'marks': 85},
    {'name': 'Alice', 'subject': 'Physics', 'marks': 88},
    {'name': 'Bob', 'subject': 'Physics', 'marks': 92},
    {'name': 'Alice', 'subject': 'Chemistry', 'marks': 78},
    {'name': 'Bob', 'subject': 'Chemistry', 'marks': 88}
]

def find_highest_scorers(student_data):
    highest_scorers = {}

    for student in student_data:
        subject = student['subject']
        marks = student['marks']
        name = student['name']

        if subject in highest_scorers:
            if marks > highest_scorers[subject]['marks']:
                highest_scorers[subject] = {'marks': marks, 'students': [name]}
            elif marks == highest_scorers[subject]['marks']:
                highest_scorers[subject]['students'].append(name)
        else:
            highest_scorers[subject] = {'marks': marks, 'students': [name]}

    
    result = {subject: highest_scorers[subject]['students'] for subject in highest_scorers}
    return result

res = find_highest_scorers(student_data)
print(res)

