pos= 0
neg = 0
imp= 0
par= 0
lista = []

lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))



for v in lista:
    if v % 2 != 0:
        imp +=1
    else:
         par += 1

    if v > 0:
        pos += 1
    else:
        if v < 0:
            neg += 1

print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %imp)
print("%d valor(es) positivo(s)" %pos)
print("%d valor(es) negativo(s)" %neg)

