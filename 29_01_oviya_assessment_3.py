# ASSESSMENT 3


'''1.Develop a Python program to create a dictionary from a given string, where each key represents a unique character, 
and the corresponding values denote the count of occurrences.
Input: 'kovan labs'
Output: {'k': 1, 'o': 2, 'v': 1, 'a': 2, 'n': 1, ' ': 1, 'l': 1, 'b': 1, 's': 1}'''

input_strng = 'kovan labs'
from collections import Counter as c 

def count_character(input_strng):
    empty_dict = {}
    for i, j in c(input_strng).items():
        empty_dict[i] = j
    return empty_dict

result = count_character(input_strng)
print(result)


'''2. Create a Python program to find the key with the maximum value in a dictionary.
Input: 
my_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}
Output: 'orange' '''

my_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}

def max_value():
    max_value = 0 
    max_key = None
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

result = max_value()
print(result)


'''3.Create a Python function that counts the frequency of words in a sentence and returns a dictionary.
Input: 
sentence = "This is a sample sentence. This sentence has words."
Output: {'This': 2, 'is': 1, 'a': 1, 'sample': 1, 'sentence.': 2, 'has': 1, 'words.': 1}'''

sentence = "This is a sample sentence. This sentence has words."
splitted_words = sentence.split()
print("splitted_words", splitted_words)
unique_words = set(splitted_words)
print("unique_words", unique_words)

def count_words():
    word_counts = {}
    for word in unique_words:
        count = splitted_words.count(word)
        word_counts[word] = count
    return word_counts

result = count_words()
print(result)


'''4.  Write a Python function that takes a dictionary as input and returns a new dictionary where the keys are the original values, and the values are lists containing all corresponding keys.
Input: 
input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
Output: {1: ['a', 'c'], 2: ['b', 'd'], 3: ['e']}'''

input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3} 

def funct(input_dict):
    empty_dict = {}
    for key, value in input_dict.items():
        if value not in empty_dict:
            empty_dict[value] = [key]
        else:
            empty_dict[value].append(key)
    return empty_dict

result = funct(input_dict)
print(result)
