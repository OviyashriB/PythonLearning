# ASSESSMENT 5


'''1. Write a program to iterate the first 5 numbers, and in each iteration, print the sum of the current and previous number at the end.
Expected Output:
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7'''

def to_get_nums():
    for current_number in range(1,5): 
        if current_number == 0:
            previous_number = 0
        else:
            previous_number = current_number - 1
            
        current_sum = current_number + previous_number
        print(f"Current Number {current_number} Previous Number {previous_number} Sum: {current_sum}")
to_get_nums()


'''
for current_number in range(5):
    previous_number = current_number - 1 if current_number > 0 else 0
    current_sum = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {current_sum}")
'''


'''2. Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.'''

num = 7536
print(type(num))

def extract_digits(num):
    rvrsd_str = str(num)[::-1]
    for digit in rvrsd_str:
        print(digit, end =" ")

extract_digits(num)


'''3. Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
Input:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

def new_list(l1, l2):
    odd_elements_l1 = l1[1::2]
    print(odd_elements_l1)

    evenelements_l2 = l2[0::2]
    print(evenelements_l2)

    l3 = odd_elements_l1  + evenelements_l2
    print(l3)

new_list(l1, l2)


'''4. Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string.
Input:
str1 = "Emma25 is Data scientist50 and AI Expert"
Output:
Emma25
scientist50'''

input_string = "Emma25 is Data scientist50 and AI Expert"
def find_words(input_string):
    words = input_string.split()

    result = []
    for word in words:
        is_alpha = any(char.isalpha() for char in word)
        is_digit = any(char.isdigit() for char in word)

        if is_alpha and is_digit:
            result.append(word)
    return result

result = find_words(input_string)
print(result)


'''5. Write a Python program to find the second maximum and second minimum elements in a given list of numbers. 
Assume that the list has at least two distinct elements.
Input:
[55, 23, 78, 12, 67, 34, 89, 9, 43]
Output:
Second Maximum: 78
Second Minimum: 12'''

li1 = [55, 23, 78, 12, 67, 34, 89, 9, 43]

def find_second_max_min(li1):
    sorted_nums = sorted(li1)
    print("Sorted nums:", sorted_nums)
    second_max = sorted_nums[-2]
    second_min = sorted_nums[1]

    return second_max, second_min

second_max, second_min = find_second_max_min(li1)
print("Second Max:", second_max)
print("Second Min:", second_min)
