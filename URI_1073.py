num = int(input(""))
contador = 0
numagora = 0
while contador < num and num <= 2000:

    if num % 2 == 0:
        contador += 2
        numagora = contador ** 2
        print("{n1}^2 = {n2}".format(n1=contador, n2=numagora))

    if num % 2 == 1 and numagora == num - 1:
        contador += 2
        numagora = contador ** 2

        print("{n1}^2 = {n2}".format(n1=contador, n2=numagora))


"""
MODO SIMPLES:

valor = int(input())

contador = 2

while(contador <= valor):
    print("%d^2 = %d" %(contador,(contador**2)))
    contador += 2

"""