step1 = str(input())
step2 = str(input())
step3 = str(input())

if step1 == "vertebrado":
    if step2 == "ave":
        if step3 == "carnivoro":
            print("aguia")
        if step3 == "onivoro":
            print("pomba")

    if step2 == "mamifero":
        if step3 == "onivoro":
            print("homem")
        if step3 == "herbivoro":
            print("vaca")

if step1 == "invertebrado":
    if step2 == "inseto":
        if step3 == "hematofago":
            print("pulga")
        if step3 == "herbivoro":
            print("lagarta")

    if step2 == "anelideo":
        if step3 == "hematofago":
            print("sanguessuga")
        if step3 == "onivoro":
            print("minhoca")
            



