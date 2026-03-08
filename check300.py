ex_nimo = 300

print ("\nFind the closest number to 300")

A = int(input("A. Enter your number: "))
B = int(input("B. Enter your number: "))
C = int(input("C. Enter your number: "))

num1 = abs(ex_nimo - A)
num2 = abs(ex_nimo - B)
num3 = abs(ex_nimo - C)

if num1 == num2 == num3:
    print("\nAll the value that you input is equal.")
elif num1 <= num2 and num1 <= num3:
    print("\nLetter A or", A, "is the closest number to 300.")
elif num2 <= num1 and num2 <= num3:
    print("\nLetter B or", B, "is the closest number to 300.")
else:
    print("\nLetter C or", C, "is the closest number to 300.")