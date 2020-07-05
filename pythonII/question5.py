# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

empty_list = []

tuple1 = ('Nirvay', 'Chaudhary', '19')
empty_list.append(tuple1)

tuple2 = ('Yogesh', 'Bhattarai', '21')
empty_list.append(tuple2)

tuple3 = ('Nirmal', 'Pandey', '20')
empty_list.append(tuple3)

print("Unsorted List: \n")
print(empty_list)

empty_list.sort(key= lambda x:x[2])
print("sorted list: \n")
print(empty_list)

