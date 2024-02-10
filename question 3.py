a = int(input("type a whole number "))
b = input("type the invoice operation you want to do ")
c = int(input("type a whole number "))
if b == "%":
    print(a % c)
elif b == "/":
    print(a / c)
elif b == "*":
    print(a * c)
elif b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
else:
    print("Sorry, I don't know this operator. Please type one of the following - (%, /, *, +, -) ")

