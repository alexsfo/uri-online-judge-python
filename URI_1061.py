diainicial = int(input().split()[1])
hora = input().split(" : ")
horainicial = int(hora[0])
minutoinicial = int(hora[1])
seginicial = int(hora[2])

diafinal = int(input().split()[1])
hora = input().split(" : ")
horafinal = int(hora[0])
minutofinal = int(hora[1])
segfinal = int(hora[2])
               
dias = diafinal - diainicial
horas = horafinal - horainicial

if horas < 0:
     horas += 24
     dias -= 1
minutos = minutofinal - minutoinicial

if minutos < 0:
     minutos += 60
     horas -= 1
segundos = segfinal - seginicial

if segundos < 0:
     segundos += 60
     minutos -= 1

print("%d dia(s)" %dias)
print("%d hora(s)" %horas)
print("%d minuto(s)" %minutos)
print("%d segundo(s)" %segundos)
     
