a = int(input("what is your age in years? "))
b = int(input("what is your weight in kg? "))
c = int(input("What is your height in cm? "))
if a >= 11 and a <= 120 and c / b >= 0.5 and c / b <= 2:
    print("A-Menu")
elif a >= 11 and a <= 40 and c / b >= 2 and c / b <= 3.5:
    print("B-Menu")
elif a >= 11 and a <= 20 and c / b >= 3.5 and c / b <= 5:
    print("C-Menu")
elif a >= 21 and a <= 40 and c / b >= 3.5 and c / b <= 5:
    print("C-Menu")
elif a >= 41 and a <= 120 and c / b >= 2 and c / b <= 3.5:
    print("B-Menu")
elif a >= 41 and a <= 120 and c / b >= 3.5 and c / b <= 5:
    print("C-Menu")
else:
    print("There is no corresponding menu in the database")
