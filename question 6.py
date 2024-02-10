ROUND_DOWN = 1
ROUND_UP = 2
ROUND = 3
program = int(input("Floor round .1\n
Ceiling round .2\n
Round to the nearest whole number .3\n"))
number = float(input("Write the number you want to round\n"))
decimal_part = number * 10 % 10
if program == ROUND_DOWN:
    print(int(number))
elif program == ROUND_UP:
    if decimal_part > 0:
        print(int(number) + 1)
    elif decimal_part == 0:
        print(number)
elif program == ROUND:
    if decimal_part < 5:
        print(int(number))
    elif decimal_part >= 5:
        print(int(number) + 1)
else:
    print("ERROR")