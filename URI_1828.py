nc = int(input())
x = 0
while x < nc:
    esc = input().split()
    if esc[0] == esc[1]:
        resultado = "De novo!"
    elif esc[0] == "tesoura" and esc[1] == "papel":
        resultado = "Bazinga!"
    elif esc[0] == "papel" and esc[1] == "pedra":
        resultado = "Bazinga!"
    elif esc[0] == "pedra" and esc[1] == "lagarto":
        resultado = "Bazinga!"
    elif esc[0] == "lagarto" and esc[1] == "Spock":
        resultado = "Bazinga!"
    elif esc[0] == "Spock" and esc[1] == "tesoura":
        resultado = "Bazinga!"
    elif esc[0] == "tesoura" and esc[1] == "lagarto":
        resultado = "Bazinga!"
    elif esc[0] == "lagarto" and esc[1] == "papel":
        resultado = "Bazinga!"
    elif esc[0] == "papel" and esc[1] == "Spock":
        resultado = "Bazinga!"
    elif esc[0] == "Spock" and esc[1] == "pedra":
        resultado = "Bazinga!"
    elif esc[0] == "pedra" and esc[1] == "tesoura":
        resultado = "Bazinga!"
    else:
        resultado = "Raj trapaceou!"
    x += 1
    print("Caso #%d: %s" % (x, resultado))