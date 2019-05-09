x = 0
lista = [0,0,0,0,0]
pares = 0
while x < 5:
    lista[x] = int(input(""))
    if lista[x] % 2 == 0:
        pares += 1
    x += 1
print("%d valores pares" %pares)