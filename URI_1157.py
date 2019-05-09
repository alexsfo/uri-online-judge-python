n = int(input())
x = int(n)
while x != 0:

    if n > 0 and n >= x:

        if n % x == 0 or n % x == n:
            valor = n // x
            print(valor)
            x -= 1

        elif n % x != 0:
            x -= 1