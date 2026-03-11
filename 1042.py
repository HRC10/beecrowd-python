a = input().split()
for i in range (3):
    a[i] = int(a[i])
novo = sorted(a)
print(*novo, sep="\n")
print()
print(*a, sep="\n")
