x = int(input())
c = 0

while c < 6:
    if x % 2 == 1 and c < 6:
        x = x + 2
        print(x)
        c = c + 1

    elif x % 2 == 0 and c < 6:
        x = x + 1
        print(x)
        c = c + 1