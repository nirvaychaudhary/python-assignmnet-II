# Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]

import csv
csv_columns_name = ['name', 'address', 'age']
dict_data = [
    {'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
    {'name':'John', 'address': '54 Love Ave', 'age': 21}
] 

csv_file_name = 'info.csv'

try:
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= csv_columns_name)
        writer.writeheader
        for data in dict_data:
            writer.writerow(data)

except IOError:
    print("Input/Output Error")

