valores = input().split()
N1, N2, N3, N4 = valores

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

notaExame = 0.0
media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print("Media: %.1f" %media)

if (media >= 7.0):
    print("Aluno aprovado.")

if (media < 5.0):
    print("Aluno reprovado.")

if (media >= 5.0 and media <= 6.9):
    print("Aluno em exame.")
    notaExame = float(input())
    print("Nota do exame: %.1f" %notaExame)
    media = (media + notaExame) /2

    if (media >=5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print('Media final: %.1f' %media)
