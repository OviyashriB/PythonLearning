# ASSESSMENT 14


'''1.Given a DataFrame containing information about sales transactions, 
how would you find the total sales amount for each product category where the sales quantity is greater than 100?	
	
Output:	
  Product  Total_Sales_Amount	
0       A                 1100	
1       C                  750	'''

import pandas as pd
data = {'Product': ['A', 'B', 'A', 'C', 'B', 'C'],
        'Quantity': [150, 80, 200, 120, 90, 110],
        'Amount': [500, 300, 600, 400, 250, 350]}

df = pd.DataFrame(data)
filtered_df = df[df['Quantity'] > 100]
print(filtered_df)
res = filtered_df.groupby('Product')['Amount'].sum().reset_index()
res.rename(columns={'Amount': 'Total_Sales_Amount'}, inplace=True)
print(res)

	
'''2. Given a DataFrame with information about students and their test scores,
how would you find the average score for each subject, 
but only for students who scored above the mean score across all subjects?	

Output:	
   Subject  Average_Score	
0     Math           85.0	
1  Science           85.0	
2  English           85.0	'''

data = {'Student': ['A', 'B', 'C', 'D', 'E'],	
        'Math': [80, 70, 90, 60, 85],	
        'Science': [75, 85, 80, 70, 95],	
        'English': [65, 75, 70, 80, 90]}

df = pd.DataFrame(data)
# print(df)
mean_score = df[['Math', 'Science', 'English']].values.mean()
# print(mean_score)
above_mean_students = df[(df['Math'] > mean_score) & (df['Science'] > mean_score) & (df['English'] > mean_score)]
print(above_mean_students)
average_scores = above_mean_students[['Math', 'Science', 'English']].mean()
print(average_scores)
output = pd.DataFrame({"Subject": average_scores.index, "Average_Score": average_scores.values})
print(output)


'''3. Given a DataFrame with a time series index and a column representing stock prices, 
how would you identify the dates where the stock price increased by more than 10% compared to the previous day? 
(go through some timeseries topics in pandas) 	

Output:	
          Price	
2024-01-02    110	
2024-01-04    120	
2024-01-05    130	
2024-01-10    135	'''
	
# import pandas as pd
# dates = pd.date_range(start='2024-01-01', periods=10)
# prices = [100, 110, 105, 120, 130, 115, 112, 125, 130, 135]
# df = pd.DataFrame(prices, index=dates, columns=['Price'])
# print(df)
# df['Percent_change'] = df['Price'].pct_change()
# print(df['Percent_change'])
# increased_by_10_percent = df[df['Percent_change'] > 0.1]
# print(increased_by_10_percent)
# print(increased_by_10_percent[['Price']])


'''4. Given a DataFrame with information about sales transactions and another DataFrame with information about discounts, 
how would you calculate the total discounted amount for each product sold, considering both the quantity and discount rate?	

Output:	
  Product  Total_Discounted_Amount	
0       A                     500	
1       B                    1000	
2       C                    1900	'''

sales_data = {'Product': ['A', 'B', 'A', 'C', 'B', 'C'],	
              'Quantity': [10, 20, 30, 40, 50, 60],	
              'Amount': [500, 600, 700, 800, 900, 1000]}	
	
discount_data = {'Product': ['A', 'B', 'C'],	
                 'Discount_Rate': [0.1, 0.2, 0.15]}	

import pandas as pd
sales_df = pd.DataFrame(sales_data)
# print(sales_df)
discount_df = pd.DataFrame(discount_data)
# print(discount_df)

to_merge_df = pd.merge(sales_df, discount_df, on='Product', how = 'left')
# print(to_merge_df)

def calculate_discounted_amount(row):
    return row['Amount'] * (1 - row['Discount_Rate'])

to_merge_df['Discounted_Amount'] = to_merge_df.apply(calculate_discounted_amount, axis=1)
print(to_merge_df['Discounted_Amount'])

ttl_discounted_amounts = to_merge_df.groupby('Product')['Discounted_Amount'].sum().reset_index()
ttl_discounted_amounts.columns = ['Product', 'Total_Discounted_Amount']
print(ttl_discounted_amounts)


'''5. Given a DataFrame with information about customer orders,
how would you find the total number of orders placed by customers who have made more than one order?	
	
Output:	
  Total_Orders	
0             3	'''

import pandas as pd
data = {'Customer': ['A', 'B', 'A', 'C', 'B', 'C'],
        'Order_ID': [1, 2, 3, 4, 5, 6]}

df = pd.DataFrame(data)

orders_per_customer = df.groupby('Customer')['Order_ID'].count()
print(orders_per_customer)
more_than_one_order = orders_per_customer[orders_per_customer > 1]
print(more_than_one_order)
total_orders = more_than_one_order.count()
res = pd.DataFrame({'Total_Orders': [total_orders]})
print(res)


'''6.  Given a DataFrame with a column containing JSON strings representing nested data, how would you extract a specific value nested within the JSON for each row?	
	
Output:	
ID  Nested_Value	
0 1 10	
1 2 20	
2 3 30	'''

data = {'ID': [1, 2, 3],	
        'Nested_Data': ['{"key1": {"key2": {"key3": 10}}}',	
                        '{"key1": {"key2": {"key3": 20}}}',	
                        '{"key1": {"key2": {"key3": 30}}}']}	

import json
import pandas as pd
df = pd.DataFrame(data)

def to_extract_nested_value(df):
    data1 = json.loads(df) 
    return data1['key1']['key2']['key3']

# Apply the function to extract nested value for each row
df['Nested_Value'] = df['Nested_Data'].apply(to_extract_nested_value)
print(df[['ID', 'Nested_Value']])


'''7.  Given a DataFrame with duplicate rows, how would you remove the duplicate rows based on a subset of columns 
while keeping only the row with the maximum value in another column?	
	
Output:	
   ID  Value   Timestamp	
1   1     20  2024-01-01	
3   2     40  2024-01-02	
4   3     50  2024-01-03'''	

import pandas as pd
data = {'ID': [1, 1, 2, 2, 3],
        'Value': [10, 20, 30, 40, 50],
        'Timestamp': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03']}

df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # converted to dttime 
idx = df.groupby('ID')['Value'].idxmax()
res = df.loc[idx]
print(res)