while True:
    try:

        n = int(input())
        vlesmas = input().split()
        lista = list(vlesmas)

        maior = int(max(lista, key=int))

        if maior < 10:
            nivel = 1
        elif 10 <= maior < 20:
            nivel = 2
        elif maior >= 20:
            nivel = 3

        print(nivel)
    except EOFError:
        break
