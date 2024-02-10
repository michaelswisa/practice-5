a = int(input("type a whole number 1/3 "))
b = int(input("type a whole number 2/3 "))
c = int(input("type a whole number 3/3 "))
if a >= b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
