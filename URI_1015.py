ponto1 = (input().split(' '))
x1 = float(ponto1[0])
y1 = float(ponto1[1])

ponto2 = (input().split(' '))
x2 = float(ponto2[0])
y2 = float(ponto2[1])


distancia = (((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))**(1/2))

print("%.4f" % distancia)
