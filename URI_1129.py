resposta = ["A", "B", "C", "D", "E"]

while (True):
    tamanho = int(input())

    if tamanho == 0:
        break

    for i in range(tamanho):
        questao = input().split()
        escolha = []

        for j in range(len(questao)):
            if int(questao[j]) <= 127:
                escolha.append(j)

        if len(escolha) == 1:
            print(resposta[escolha[0]])
        else:
            print("*")
