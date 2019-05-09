selecao = (input().split())
A = int(selecao[0])
B = int(selecao[1])
C = int(selecao[2])
D = int(selecao[3])


if (((B > C) and (D > A)) and ((C + D) > (A + B)) and ((C and D) > 0) and ((A % 2) == 0)):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")
