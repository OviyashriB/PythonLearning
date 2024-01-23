# ASSESSMENT 1 


'''1. Write a code that takes a string as input and returns the reversed version of that string. 
For example expected output should be like reversed_output = "nohtyp"'''

def reverse_op(g_input):
    return g_input[::-1]

get_input = str(input("Enter the text: "))
output = reverse_op(get_input)
print("The reversed string is: ", output)


'''2. Given two different lists and tuples, write a Python code to merge these two different lists and tuples and
store the result in a new items called "combined_list." for each, expected output should be in combined lists and combined tuple format.'''

list_1 = [1, 2, 3]
list_2 = ['Python', 'Java', 'C']

combined_lists = list_1.extend(list_2)
print("Combined_lists: ", list_1)

tuple_1 = (10, 20, 30)
tuple_2 = (40, 50, 60)

combined_tuple = tuple_1 + tuple_2
print("Combined tuple: ", combined_tuple)


'''3. Write a code that takes a string and a target substring as input and returns the number of occurrences of the target substring in the given string. 
For example, if the input is "pythonpythonpython" and the target substring is "on," the output should be 3.'''

input_string = "pythononpythonpython"
target_substring = input_string.count('on')
print(target_substring)


'''4. write a python code to achieve the expected output below mentioned
text  = "#orange#strawberry#grapes#banana"
result = ['orange', 'strawberry', 'grapes', 'banana']'''

text  = "#orange#strawberry#grapes#banana"
output = text.split('#')
print("Output_1:", output)


# To remove the empty string
emp_list = []
for i in text.split('#'):
    if i:
        emp_list.append(i)
print("Output_2:",emp_list)
