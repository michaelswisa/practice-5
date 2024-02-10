a = int(input("what is your age in years? "))
b = int(input("what is your weight in kg? "))
c = int(input("What is your height in cm? "))
ratio_1 = c / b >= 0.5 and c / b <= 2
ratio_2 = c / b >= 2 and c / b <= 3.5
ratio_3 = c / b >= 3.5 and c / b <= 5
age_1 = a >= 11 and a <= 20
age_2 = a >= 21 and a <= 40
age_3 = a >= 41 and a <= 120
if age_1 and ratio_1:
    print("A-Menu")
elif age_1 and ratio_2:
    print("B-Menu")
elif age_1 and ratio_3:
    print("C-Menu")
elif age_2 and ratio_1:
    print("A-Menu")
elif age_2 and ratio_2:
    print("B-Menu")
elif age_2 and ratio_3:
    print("C-Menu")
elif age_3 and ratio_1:
    print("A-Menu")
elif age_3 and ratio_2:
    print("B-Menu")
elif age_3 and ratio_3:
    print("C-Menu")
else:
    print("There is no corresponding menu in the database")
