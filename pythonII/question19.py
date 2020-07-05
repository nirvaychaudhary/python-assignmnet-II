# Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

class brackets:
    def parenthesese(self, str1):
        list1, paren_char = [], {"(": ")", "{": "}", "[": "]"}

        for x in str1:
            if x in paren_char:
                list1.append(x)

            elif len(list1) == 0 or paren_char[list1.pop()] != x:
                return False

        return len(list1) == 0

print(brackets().parenthesese("(){}[]"))
print(brackets().parenthesese("()[{)}"))
print(brackets().parenthesese("()"))