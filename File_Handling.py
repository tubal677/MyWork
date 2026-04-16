# Simple Messaging App

def Create_File():
    try:
        file = open("message.txt", "x")
        file.close()
        print("File Created Successfully.")

    except FileExistsError:
        print("File already exist!")

def Send_Message():
    try:
        message = input("Enter your Message: ")
        with open("message.txt", "a") as file:
            file.write(message + "\n")
        print("Message Sent.")

    except Exception as error:
        print("\nError Message: ", error)

def View_Message():
    try:
        with open("message.txt", "r") as file:
            messages = file.read()
            print("\n=== Message ===")
            print(messages if messages else "No Messages yet.")

    except FileNotFoundError:
        print("\nFile not found.")

def Menu():
    while True:
        print("\n=== Welcome to our Messaging App ===")
        print("1. Send Message")
        print("2. View Message")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                Send_Message()

            elif choice == 2:
                View_Message()

            elif choice == 3:
                print("\nExiting the progaram...")
                break

            else:
                print("\nInvalid Input. Please choose only 1-3.")

        except ValueError:
            print("\nPlease input a valid number.")

Create_File()
Menu()
