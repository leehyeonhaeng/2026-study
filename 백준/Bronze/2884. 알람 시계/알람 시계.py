a, b = map(int, input().split())

if (b - 45) < 0 :
    a = a - 1
    if a < 0 : a += 24
    b = 60 + (b - 45)
else : b = b - 45

if a > 23 : a = a - 24
print(f"{a} {b}")