def switch(operation, num1, num2):

    dict={
        1: (lambda x, y : x + y),
        2: (lambda x, y : x - y),
        3: (lambda x, y : x * y),
        4: (lambda x, y : x / y),
        5: (lambda x, y : x // y),
        6: (lambda x, y : x % y)

    }
    return dict.get(operation, 'Invalid Operation')(num1, num2)

num1= int(input('Enter the first number: '))
num2= int(input('Enter the second number: '))

print('''Press 1 for Addition
Press 2 for Subtraction
Press 3 for Multiplication
Press 4 for real number Division
Press 5 for integer Division
Press 6 for finding the remainder after division''')
num= int(input('Enter a number of your choice: '))

print('Result is: ', switch(num, num1, num2))
