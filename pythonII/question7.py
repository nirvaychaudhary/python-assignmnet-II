# 7. Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

empty_list = []
tuple1 = ('Nirvay', 'Chaudhary', 19)
empty_list.append(tuple1)

tuple2 = ('Sandesh', 'Khadka', 55)
empty_list.append(tuple2)

tuple3 = ('Ram', 'Singh', None)
empty_list.append(tuple3)

print(empty_list)
avg = []
for i in empty_list:
    if i[2] != None:
        avg.append(i[2])
print(avg)

total = str(sum(avg)/len(avg))
print("The average is: " + total)

for x in avg:
    if x > 50:
        print(avg[1],'is aged')
    elif x < 15 :
        print(avg[0],"you are too young")
    elif x > 15 and x < 50:
        print('You are young')
