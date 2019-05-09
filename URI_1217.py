n = int(input())
cont = 0
frutas = [1,n]
kgpordia = 0
valordia = 0
dia = 1
if 1 <= n <= 365:
    while cont < n:
        valordia += float(input())
        frutas.append(input().split)
        cont+=1
        kgpordia += len(frutas)

        mediafrutas = (kgpordia / cont)
        mediapreco = valordia / cont



        print("day %d: %d kg" % (dia, (len(frutas))))
        dia += 1

print("%.2f kg by day" % mediafrutas)
print("R$ %.2f by day" % mediapreco)


