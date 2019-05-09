produto1 = (input().split(' '))
CP1 = int(produto1[0])
UP1 = int(produto1[1])
VP1 = float(produto1[2])
produto2= (input().split(' '))
CP2 = int(produto2[0])
UP2 = int(produto2[1])
VP2 = float(produto2[2])

valor = VP1 * UP1 + VP2 * UP2

print("VALOR A PAGAR: R$ %.2f" %valor)

