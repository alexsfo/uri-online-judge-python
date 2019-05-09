lista = input().split()

A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

lista[0] = float(A)
lista[1] = float(B)
lista[2] = float(C)
lista.sort(reverse=True)

if (A >= B + C):
    print("NAO FORMA TRIANGULO")

if (A ** 2 == (B ** 2) + (C ** 2)):
    print("TRIANGULO RETANGULO")

if (A ** 2 > (B ** 2) + (C ** 2)):
    print("TRIANGULO OBTUSANGULO")

if (A ** 2 < (B ** 2) + (C ** 2)):
    print("TRIANGULO ACUTANGULO")

if (A == B and B == C):
    print("TRIANGULO EQUILATERO")

if ((A == B or B == C) and not (A == B and B == C)):
    print("TRIANGULO ISOSCELES")
