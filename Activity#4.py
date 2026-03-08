while True:
    print("\n=== Password must contain at least one letter and number. ===")
    password = input("\nInput a password: ")

    has_letter = False
    has_number = False

    if len(password) != 2:
        print("\nPassword must be exactly 2 characters.")
        continue

    for i in password:
        if i.isalpha():
            has_letter = True
        if i.isdigit():
            has_number = True

    if has_letter and has_number:
        print("\nPassword accepted.")
        break
    
    else:
        print("\nInvalid password. Try again.")