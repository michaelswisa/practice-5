age = int(input("what is your age in years? "))
b = int(input("what is your weight in kg? "))
c = int(input("What is your height in cm? "))
bmi = c / b
Binary_relation = bmi >= 3.5 and bmi <= 5
age_range = age >= 11 and age <= 120
if (age_range and bmi >= 0.5 and bmi <= 2) or (age >= 21 and age <= 40 and Binary_relation):
    print("A-Menu")
elif age_range and bmi >= 2 and bmi <= 3.5 or age >= 41 and age <= 120:
    print("B-Menu")
elif age_range and Binary_relation:
    print("C-Menu")
else:
    print("There is no corresponding menu in the database")
