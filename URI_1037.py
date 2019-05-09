num = float(input())

if num >= 0 and num <= 25.0000:
    print("Intervalo [0,25]")
if num >= 25.00001 and num <= 50.0000000:
    print("Intervalo (25,50]")
if num >= 50.00001 and num <= 75.0000000:
    print("Intervalo (50,75]")
if num >= 75.00001 and num <= 100.000000:
    print("Intervalo (75,100]")

else:
    print("Fora de intervalo")
