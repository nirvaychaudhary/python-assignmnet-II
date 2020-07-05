# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

pos = -1
list1 = [5, 12, 15, 6, 24, 1, 20]
new_list = sorted(list1)
n = int(input("Enter any number to search: "))
def binarysearch(new_list, n):
    lower_bound = 0
    upper_bound = len(new_list)-1

    while lower_bound <=  upper_bound:
       mid = (lower_bound + upper_bound) // 2

       if new_list[mid] == n:
           globals()['pos'] = mid
           return True 

       else:

            if new_list[mid] < n:
                lower_bound = mid + 1

            else:
                upper_bound = mid - 1

    return False

if binarysearch(new_list, n):
    print("found at" , pos + 1)

else:
    print("Not Found")

