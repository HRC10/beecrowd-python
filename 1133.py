a = input()
b = input()
a = int(a)
b = int(b)
if a > b:
    while b < a:
        b += 1
        if (b % 5 == 2) or ( b % 5 == 3):
            print(b)
else:
    while a < b:
        a += 1
        if (a % 5 == 2) or (a % 5 == 3):
            print(a)
