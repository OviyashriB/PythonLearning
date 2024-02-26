# ASSESSMENT 15


'''1. Consider the following data as dataframe.								
a) What code should you use to add a new column named Word_Count to df which contains the number of words in each text entry?			
			
Expected Output:			
       Text  Word_Count			
0  Hello world           2			
1 Python is  awesome     3			
2 Data science is fun   4	'''		


data = {'Text': ['Hello world', 'Python is awesome', 'Data science is fun']}	
#a 
import pandas as pd
df = pd.DataFrame(data)

def count_words(df):
    return len(df.split())

df['Word_Count'] = df['Text'].apply(count_words)
print(df)


'''b) Write code to find the most common word in the 'Text' column.			
			
Expected Output:			
is'			'''

data = {'Text': ['Hello world', 'Python is awesome', 'Data science is fun']}	
			
texts = data['Text']
print('Values', texts)

word_counts = {}

for text in texts:
    words = text.split()
    print('Words', words)
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

most_common_word = None
max_count = 0
for word, count in word_counts.items():
    if count > max_count:
        most_common_word = word
        max_count = count
print(most_common_word)


'''c) Write code to replace each word in the 'Text' column with its length. 
For example, in given input 1st index is Hello WOrld, both words has 5 letters, so it is replaced with 5, 5 in 1st index in below output.			
			
Expected Output:			
                   Text			
0             5 5			
1        6 2 7			
2  4 7 2 5 2 3	'''		

data = {'Text': ['Hello world', 'Python is awesome', 'Data science is fun']}	
df = pd.DataFrame(data)
print(df)

def word_length(df):
    word_lengths = []
    for word in df.split():
        word_lengths.append(str(len(word)))
    return ' '.join(word_lengths)


df['Text'] = df['Text'].apply(word_length)
print(df)


'''2. Write code to find the count of individuals in each department.					
			
Expected Output:			
Marketing    2			
Sales        2			
HR           1			
Name: Department, dtype: int64		'''	
			
import pandas as pd

data = {'ID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Age': [25, 30, 35, 40, 45],
        'Department': ['Sales', 'Marketing', 'Sales', 'HR', 'Marketing']}

df = pd.DataFrame(data)
# print(df)
counts= df['Department'].value_counts()  #Returns the number of unique rows
print(counts)


'''3. You're provided with a dataset containing information about hotel bookings. 
The dataset includes categorical columns for "Hotel_Name", "Booking_Status", and "Payment_Method". 
Your task is to analyze the booking status distribution for each hotel, focusing on payments made through credit cards. 
Write a Python function to achieve this.									
			
Output:			
  Hotel_Name Booking_Status  Count			
0    Hotel A      Cancelled      1			
1    Hotel A      Confirmed      2			
2    Hotel B      Confirmed      1	'''		

data = {
    'Hotel_Name': ['Hotel A', 'Hotel B', 'Hotel A', 'Hotel B', 'Hotel A', 'Hotel B'],
    'Booking_Status': ['Confirmed', 'Cancelled', 'Confirmed', 'Confirmed', 'Cancelled', 'Confirmed'],
    'Payment_Method': ['Credit Card', 'Debit Card', 'Credit Card', 'Credit Card', 'Credit Card', 'Debit Card']
}

import pandas as pd

def analyze_booking_status(data):
    df = pd.DataFrame(data)
    print(df)
    credit_card_bookings = df[df['Payment_Method'] == 'Credit Card']
    print('Credit card bookings', credit_card_bookings)
    booking_status_counts = credit_card_bookings.groupby(['Hotel_Name', 'Booking_Status']).size().reset_index(name='Count')
    return booking_status_counts

res = analyze_booking_status(data)
print(res)

			
'''4. You've been given a dataset containing information about electrical appliances in a store. 
The dataset includes categorical columns for "Appliance_Name", "Type", and "Availability".
Your task is to create a dictionary where each key is an appliance type and 
the corresponding value is a list containing the names of appliances belonging to that type along with their availability status. 
Write a Python function to accomplish this.	Use pandas.				
		
Expected Output:			
{			
    'Large Appliance': [('Refrigerator', 'In Stock'), ('Dishwasher', 'In Stock')],			
    'Small Appliance': [('Microwave', 'Out of Stock'), ('Vacuum Cleaner', 'Out of Stock'), ('Toaster', 'In Stock'), ('Blender', 'Out of Stock')]			
}			'''

data = {			
    'Appliance_Name': ['Refrigerator', 'Microwave', 'Dishwasher', 'Vacuum Cleaner', 'Toaster', 'Blender'],			
    'Type': ['Large Appliance', 'Small Appliance', 'Large Appliance', 'Small Appliance', 'Small Appliance', 'Small Appliance'],			
    'Availability': ['In Stock', 'Out of Stock', 'In Stock', 'Out of Stock', 'In Stock', 'Out of Stock']			
}

import pandas as pd

def create_appliance_dict(data):
    df = pd.DataFrame(data)
    print('dataframe', df)

    result = {}
    for appliance_type in df['Type'].unique():
        filtered_df = df[df['Type'] == appliance_type]
        print('fil', filtered_df)
        appliance_list = list(zip(filtered_df['Appliance_Name'], filtered_df['Availability']))
        print('app', appliance_list)
        result[appliance_type] = appliance_list
    return result

res = create_appliance_dict(data)
print(res)
