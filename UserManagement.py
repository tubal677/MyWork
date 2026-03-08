user = []

while True:
    print("\n====== User Management System ======")
    print("1. Show Users")
    print("2. Add User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    choose = input(" Choose (1-5): ")

    if choose == "1":
        if len(user) != 0:
            print("\nUsers List: ", user)
        else:
            print("\nUser not found.")

    elif choose == "2":
        add = input("\nAdd new User: ")
        user.append(add)
        print("\nUser added.")
        print("User List:", user)

    elif choose == "3":
        update = input("\nEnter the user to update: ")
        if update in user:
            index = user.index(update)
            new_value = input("Enter the new user: ")
            user[index] = new_value
            print("User updated.")
        else:
            print("\nUser not found.")
        print("User List:", user)

    elif choose == "4":
        remove = input("\nEnter user to delete: ")
        if remove in user:
            user.remove(remove)
            print("User deleted.")
        else:
            print("User not found.")
        print("User List:", user)

    elif choose == "5":
        print("\n    Exiting in the Program...")
        break

    else:
        print("Invalid choice. Please choose between 1-5.")