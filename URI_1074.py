n = int(input())
x = 0
lista = []

while len(lista) < n:
    lista.append(int(input()))
    if lista[x] > 0 and lista[x] % 2 == 0:
        print("EVEN POSITIVE")
    if lista[x] > 0 and lista[x] % 2 != 0:
        print("ODD POSITIVE")
    if lista[x] < 0 and lista[x] % 2 == 0:
        print("EVEN NEGATIVE")
    if lista[x] < 0 and lista[x] % 2 != 0:
        print("ODD NEGATIVE")
    if lista[x] == 0:
        print("NULL")
    x += 1
