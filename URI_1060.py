lista = []

lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
lista.append(float(input()))
soma = float(0)


x = float(0)
for v in lista:
    if v > 0:
        soma += v
        x += 1


div = float(soma / x)
print("%.0f valores positivos" % x)
print("%.1f"% div)