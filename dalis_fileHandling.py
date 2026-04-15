# DALIS - Week 8: FILE HANDLING ACTIVITY

# Create file using file mode "x"
try:
    with open("message.txt", "x") as file:
        print("File successfully created")
except FileExistsError:
    print("Error: File already exists")

# Menu
while True:
    print("\n--- Welcome to Messaging App ---\n")
    print("1 - Send a Message")
    print("2 - View All Messages")
    print("3 - Exit")
    
    choice = input("Enter choice: ")

    if choice == '1':
        try:
            message = input("Enter a message: ")
            if message.strip() == "":
                print("Message cannot be empty...")
            else:
                with open("message.txt", "a") as file:
                    file.write(message + "\n")
                print("Message sent!")
        except Exception as e:
            print("Error in writing:", e)

    elif choice == '2':
        try:
            with open("message.txt", "r") as f:
                print("\n--- Messages ---")
                content = f.read()
                if content.strip() == "":
                    print("No messages")
                else:
                    print(content)
        except Exception as e:
            print("Error in reading:", e)

    elif choice == '3':
        print("Exiting....")
        break

    else:
        print("Invalid input")