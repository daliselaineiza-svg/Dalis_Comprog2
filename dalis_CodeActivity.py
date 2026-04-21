while True:
    print("\n--- Simple Calculator ---\n")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exit")

    choice = input("Select an operation: ")

    if choice == '5':
        print("Program Exiting...")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))

            if choice == '1':
                print("Sum:", num1 + num2)
            elif choice == '2':
                print("Difference:", num1 - num2)
            elif choice == '3':
                print("Product:", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print("Quotient:", num1 / num2)

        except ValueError:
            print("Invalid number input")

    else:
        print("Invalid input")1
        