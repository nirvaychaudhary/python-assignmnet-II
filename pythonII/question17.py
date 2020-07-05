# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

def main():
    print('1: addition')
    print('2: Multiplication')
    print('3: Subtraction')
    print('4: Divison')

def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def subtract(x,y):
    return x - y

def divide(x,y):
    return x / y

while True:
    main()
    choice = input("Enter your choice: ")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter any number: "))
        num2 = float(input("Enter any Number: "))

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))           
            break
        elif choice == '2':
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '3':
            print(num1, '-', num2, '=', subtract(num1, num2))

        elif choice == '4':
            print(num1, '/', num2, '=', divide(num1, num2))
        break

    else:
        print('Invalid Choice')


    



