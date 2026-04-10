# Simple Money Withdrawal System

# Initial balance
balance = 5000.0

while True:
    print("\n=== WITHDRAWAL MENU ===")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    # WITHDRAW
    if choice == "1":
        while True: # withdrawal loop
            # try block
            try:
                amount = float(input("Enter amount to withdraw: ₱ ")) # try will check this.

                if amount <= 0:
                    print("\nInvalid amount. Please enter a positive number.")
                    continue

                if amount > balance:
                    print("\nInsufficient funds.")

                    print("\nOptions:")
                    print("1. Try Again")
                    print("2. Check Balance")
                    print("3. Exit")

                    option = input("Choose an option: ")

                    if option == "1":
                        continue
                    elif option == "2":
                        print(f"\nCurrent Balance: ₱ {balance:.2f}")
                    elif option == "3":
                        print("\nExiting Program, Thank you for using the Withdrawal System!!\n")
                        exit()
                    else:
                        print("\nInvalid option.")

                else:
                    balance -= amount  # balance = balance - amount
                    print("\nWithdrawal successful!")
                    print(f"Remaining Balance: ₱ {balance:.2f}")
                    break

            # except 
            except ValueError: # error if the user input a letters or symbol instead of numbers.
                print("\nInvalid input. Please enter a valid number.")

    # CHECK BALANCE
    elif choice == "2":
        print(f"\nCurrent Balance: ₱ {balance:.2f}")

    # EXIT
    elif choice == "3":
        print("\nExiting Program, Thank you for using the Withdrawal System!!\n")
        break

    else:
        print("\nInvalid choice. Please select from 1 to 3.")
