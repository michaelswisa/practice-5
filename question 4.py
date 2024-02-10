a = int(input("type a whole number 1/3 "))
b = int(input("type a whole number 2/3 "))
c = int(input("type a whole number 3/3 "))
if b > a and c > b:
    print("The numbers are in ascending order")
elif b < a and c < b :
    print("The numbers are in descending order")
else:
    print("The numbers are in no particular order")
