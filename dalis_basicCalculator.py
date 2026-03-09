while True:
    print('\n-----Basic Calculator-----')
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiplication')
    print('4 - Division')
    print('5 - Exit')
    print('---------------------------')

    choice = input('Enter choice: ')

    if choice == '5':
        print('Exiting...')
        break

    num1 = float(input('Enter first number : '))
    num2 = float(input('Enter second number: '))

    if choice == '1':
        print('Sum:', num1 + num2)

    elif choice == '2':
        print('Difference:', num1 - num2)

    elif choice == '3':
        print('Product:', num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print('Quotient:', num1 / num2)
        else:
            print('Error: Cannot divide by zero')

    else:
        print('Invalid choice')