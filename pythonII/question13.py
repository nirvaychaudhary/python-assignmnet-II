# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv
def main():
    file_name = input("Enter the filename only without .csv extension: ")
    tuples_list = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
    writer_to_csv(file_name, tuples_list)
def writer_to_csv(file_name, tuples_list):
    with open(file_name+str(".csv"), 'w') as file:
        write = csv.writer(file)
        write.writerow(['name', 'address', 'age'])
        for each in tuples_list:
            write.writerow(each)
if __name__ == "__main__":
    main()