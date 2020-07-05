# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?
empty_list = []
list1 = ['Nirvay', 'Nirmal', 'Aman', 'Pramit', 'Yogesh']   
for i in list1:
    empty_list.append(i)
print(empty_list)
empty_list.sort()
print(empty_list)

print(empty_list[0],"is the first item on list")
print(empty_list[1],"is the second item on list")

