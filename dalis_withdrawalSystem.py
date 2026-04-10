def main():
    balance = 1000 

    while True:
        print("\n=== Money Withdrawal System ===")  
        print("1 - Withdraw Money")
        print("2 - Check Balance")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:  
                try:
                    amount = float(input("Enter amount to withdraw: "))

                    if amount <= 0:
                        print("Invalid amount. Please enter a positive value.")
                        continue

                    elif amount > balance:
                        print("Insufficient funds!")

                        while True:
                            print("\nWhat would you like to do?")
                            print("1 - Re-enter amount")
                            print("2 - Check balance")
                            print("3 - Exit")

                            error_choice = input("Enter choice: ")

                            if error_choice == "1":
                                break  
                            elif error_choice == "2":
                                print(f"Current balance: {balance}")
                            elif error_choice == "3":
                                print("Exiting program...")
                                return
                            else:
                                print("Invalid option. Try again.")


                    else:
                        balance -= amount  
                        print(f"Withdrawal successful! Remaining balance: {balance}")
                        break 
                

                except ValueError:
                    print("Invalid input! Please enter a numeric value.")

        elif choice == "2":
            print(f"Current balance: {balance}")

        elif choice == "3":
            print("Exiting...\nThank you for using the system!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


main()

