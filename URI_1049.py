animal = input()

if animal == "vertebrado":
    categoria = input()
    if categoria == "ave":
        tipo = input()
        if tipo == "carnivoro":
            print("aguia")
        elif tipo == "onivoro":
            print("pomba")

    elif categoria == "mamifero":
        tipo = input()
        if tipo == "onivoro":
            print("homem")
        elif tipo == "herbivoro":
            print("vaca")

if animal == "invertebrado":
    categoria = input()
    if categoria == "inseto":
        tipo = input()
        if tipo == "hematofago":
            print("pulga")
        elif tipo == "herbivoro":
            print("lagarta")
    if categoria == "anelideo":
        tipo = input()
        if tipo == "hematofago":
            print("sanguessuga")
        elif tipo == "onivoro":
            print("minhoca")