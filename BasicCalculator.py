while True:
    print("\n=== Basic Calculator ===")
    print("\nChoose an Operationt:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1" or choice == "2" or choice == "3" or choice == "4":

        num1 = int(input("\nEnter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == "1":
            print(f"Answer: {num1} + {num2} = {num1 + num2}")

        elif choice == "2":
            print(f"Answer: {num1} - {num2} = {num1 - num2}")

        elif choice == "3":
            print(f"Answer: {num1} * {num2} = {num1 * num2}")

        elif choice == "4":
            if num2 != 0:
                print(f"Answer: {num1} / {num2} = {num1 / num2}")
            else:
                print(f"Error... {num1} Cannot divide by zero.")

    elif choice == "5":
        print("\n=== Exiting... BYE MATSALAM! ===")
        break

    else:
        print("\n=== Invalid choice. Please select only (1-5). ===")
