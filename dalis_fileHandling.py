# DALIS - Week 8: FILE HANDLING ACTIVITY

# Create file using "x" mode
try:
    with open("message.txt", "x"):
        print("File successfully created")
except FileExistsError:
    print("Error: File already exists")

# Menu
while True:
    print("\nWelcome to Messaging App")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")

#User input
    choice = input("Enter choice: ")

    if choice == '1':
        try:
            message = input("Enter your message: ")
            if message.strip() == "":
                print("Message cannot be empty.")
            else:
                with open("message.txt", "a") as file:
                    file.write(message + "\n")
                print("Message sent!")
        except Exception as e:
            print("Error in writing....", e)

    elif choice == '2':
        try:
            with open("message.txt", "r") as file:
                print("\n--- Messages ---")
                content = file.read()
                if content.strip() == "":
                    print("No messages")
                else:
                    print(content)
        except Exception as e:
            print("Error in reading:", e)

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid input. Please try again.")