import pandas as pd


data1 = {
    'a': 4,
    'b': 6,
    'c': 7
}
series_dict = pd.Series(data1)
print(series_dict)

data1 = {
    'Name': ['Darshan', 'Suresh', 'Kumar'],
    'Age': [22, 44, 32],
    'City': ['Bangalore', 'Mumbai', 'Delhi']
}
df1=pd.DataFrame(data1)
print(df1)

df = pd.read_csv('sales_data_sample.csv', encoding_errors='ignore')
print(df.tail())
print(df.dtypes)

