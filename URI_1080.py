b = list(input().split())

posicao = int((b.index(min(b))))
menor = int((min(b)))

print("Menor valor: %d" % menor)
print("Posicao: %d" % posicao)

