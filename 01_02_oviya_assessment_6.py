# ASSESSMENT 6


'''1. Write a function in Python to read lines from a text file "notes.txt". 
Your function should find and display the occurrence of the word "the".													
                                                    
For example: If the content of the file is:													
India is the fastest-growing economy. India is looking for more investments around the globe. 
The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching.'''													

def func(file_path, search_word):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            print(content)
            word_count = content.count(search_word)
            print(word_count)
            return word_count
    except FileNotFoundError:
        return None

file_path = "notes.txt"
search_word = "the"
total_count = func(file_path, search_word)
print(f"Total count of the word '{search_word}' is {total_count}.")


'''2. Write a function display_words() in python to read lines from a text file "story.txt", and 
display those words, which are less than 4 characters.													
Input:													
A boy is playing there.													
There is a playground.													
An aeroplane is in the sky.													
Alphabets & numbers are allowed in password.													
This is Path Walla Website.													
Output :-													
Word with length smaller than 3 :-													                                                    
A													
boy													
is													
is													
a													
An													
is													
in													
the													
&													
are													
in													
is'''

def display_words(file_path):
    try:
        with open(file_path, 'r') as file:
            to_read = file.read()
            print(to_read)

            char_count = to_read.split()
            print(char_count)

            for word in char_count:
                if len(word) < 4:
                    print(word)
                
    except:
        print('error')

file_path = "story.txt"
result = display_words(file_path)

                                                    
'''3.Write a Python program to add the subject_mark and update for every students in the list of dictionary format.													
Input:  [{"name":"Arun","subject_mark":{"maths":98,"Science":89,"Social":79,"Tamil":98,"English":67}}, 
{"name":"Bhuvan","subject_mark":{"maths":90,"Science":97,"Social":89,"Tamil":78,"English":60}},
    {"name":"Rajesh","subject_mark":{"maths":70,"Science":94,"Social":99,"Tamil":85,"English":80}}]		
                                            
Output:													
[{'name': 'Arun', 'subject_mark': {'maths': 98, 'Science': 89, 'Social': 79, 'Tamil': 98, 'English': 67}, 'Total_mark': 431}, 
{'name': 'Bhuvan', 'subject_mark': {'maths': 90, 'Science': 97, 'Social': 89, 'Tamil': 78, 'English': 60}, 'Total_mark': 414}, 
{'name': 'Rajesh', 'subject_mark': {'maths': 70, 'Science': 94, 'Social': 99, 'Tamil': 85, 'English': 80}, 'Total_mark': 428}]'''													

students = [
    {"name": "Arun", "subject_mark": {"maths": 98, "Science": 89, "Social": 79, "Tamil": 98, "English": 67}},
    {"name": "Bhuvan", "subject_mark": {"maths": 90, "Science": 97, "Social": 89, "Tamil": 78, "English": 60}},
    {"name": "Rajesh", "subject_mark": {"maths": 70, "Science": 94, "Social": 99, "Tamil": 85, "English": 80}},]

def calculate_marks(student_list):
    for student in student_list:
        subject_marks = student["subject_mark"].values()
        print(subject_marks)

        total_mark = sum(subject_marks)
        print(total_mark)
        student["total_mark"] = total_mark

    return student_list

updated_students = calculate_marks(students)
print("updated students",updated_students)


'''4. Write a Python function called generate_random_passwords that takes two parameters: num_passwords (an integer representing the number of passwords to generate) and length (an integer representing the length of each password).
The function should generate random passwords with the following criteria:													                                                  
Passwords starting with numbers 100 to 105 should follow a specific pattern: the number followed by a mix of uppercase letters, lowercase letters, and digits.													
For the remaining passwords, generate them randomly with a mix of uppercase letters, lowercase letters, and digits.													
                                                    
Expected Output:													
Password 1: 100TwGDg													
Password 2: 101F5j3v													
Password 3: 102Kp7uL													
Password 4: 103Fv2A1													
Password 5: 104dRm9z	'''												

import random
import string

def generate_random_passwords(num_passwords, length):
    passwords = []

    for i in range(1, num_passwords + 1):
        if 100 <= i <= 105:
            password = f"{random.randint(100, 105)}" + ''.join(random.choice(string.ascii_letters) for i in range(length - 3))
        else:
            password = f"{random.randint(100, 105)}" + ''.join(random.choice(string.ascii_letters) for i in range(length - 3))

        passwords.append(password)

    return passwords

num_passwords = 5
password_length = 8
generated_passwords = generate_random_passwords(num_passwords, password_length)
for i, password in enumerate(generated_passwords, start=1):
    print(f"Password {i}: {password}")


'''5. Write a Python code to transform a list of lists in given input,  
into a dictionary of dictionaries named people_dict_of_dicts where each person is assigned a unique index, 
and a separate dictionary named people_indexed that categorizes individuals by their gender, listing the corresponding indices for males and females?													
Input: 													
people_list_of_lists = [													
    ['John', 25, 'Male'],													
    ['Jane', 30, 'Female'],													
    ['Alex', 22, 'Male'],													
    ['Emily', 28, 'Female'],													
    ['Michael', 35, 'Male'],													
    ['Sophia', 26, 'Female'],													
    ['Daniel', 31, 'Male'],													
    ['Olivia', 29, 'Female'],													
    ['William', 27, 'Male'],													
    ['Ava', 32, 'Female'],													
]													
                                                    
Output:													
a) people_dict_of_dicts = {"1":{"name": "John", "age": 25, "gender": "Male"},"2":{"name": "Jane", "age": 30, "gender": "Female"},"3":{"name": "Alex", "age": 22, "gender": "Male"},"4":{"name": "Emily", "age": 28, "gender": "Female"},"5":{"name": "Michael", "age": 35, "gender": "Male"},"6":{"name": "Sophia", "age": 26, "gender": "Female"},"7":{"name": "Daniel", "age": 31, "gender": "Male"},"8":{"name": "Olivia", "age": 29, "gender": "Female"},"9":{"name": "William", "age": 27, "gender": "Male"},"10":{"name": "Ava", "age": 32, "gender": "Female"}}													                                      
b) people_indexed = {"male":[1,5,7,9],"female":[2,4,6,8,10]}'''			

people_list_of_lists = [
    ['John', 25, 'Male'],
    ['Jane', 30, 'Female'],
    ['Alex', 22, 'Male'],
    ['Emily', 28, 'Female'],
    ['Michael', 35, 'Male'],
    ['Sophia', 26, 'Female'],
    ['Daniel', 31, 'Male'],                 
    ['Olivia', 29, 'Female'],
    ['William', 27, 'Male'],
    ['Ava', 32, 'Female'],
]

emp_dict = {}
people_indexed = {'male': [], 'female': []}

for i, person_info in enumerate(people_list_of_lists, start=1):
    name, age, gender = person_info
    person_dict = {'name': name, 'age': age, 'gender': gender}
    emp_dict[str(i)] = person_dict

    if gender.lower() == 'male':
        people_indexed['male'].append(i)
    elif gender.lower() == 'female':
        people_indexed['female'].append(i)
    else:
        print('error')

print("a) people_dict_of_dicts =", emp_dict)
print("b) people_indexed =", people_indexed)