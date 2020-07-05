# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.
def anagrams(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return 0
    
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(0, n1):
        if(str1[i] != str2[i]):
            return 0

    return 1

str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"

if anagrams(str1, str2):
    print("Two strings are anagram of eac other")
else:
    print("Two string are not anagram of each other")