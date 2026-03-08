def find_largest(A, B, C):

    if A == B == C:
        print("\nAll the values you entered are equal.")

    elif A > B and A > C:
        print("\nLetter A or", A, "is the largest number.")

    elif B > A and B > C:
        print("\nLetter B or", B, "is the largest number.")

    else:
        print("\nLetter C or", C, "is the largest number.")


print("\nInput 3 random numbers and I will find the largest number.")

A = int(input("A. Enter your number: "))
B = int(input("B. Enter your number: "))
C = int(input("C. Enter your number: "))

find_largest(A, B, C)
