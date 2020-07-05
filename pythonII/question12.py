word = str(input("Enter any word to check palindrome: "))

def is_palindrome(string1):
    rev = string1[::-1]

    if string1 == rev:
        print("The word is palindrome")
    else:
        print("The word is not palindrome")

    return rev
print(is_palindrome(word))