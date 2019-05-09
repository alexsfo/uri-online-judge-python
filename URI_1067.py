num = int(input(""))
contador = 1

while contador <= num and num <= 1000:
    if num % 2 == 1:
        print(contador)
        contador = contador + 2
    elif num % 2 == 0:
        print(contador)
        contador = contador + 2



