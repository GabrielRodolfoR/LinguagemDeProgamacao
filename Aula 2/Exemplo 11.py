while True:
    a = input("Curso (abreviação): ")
    if a.upper == "INF":
        print("informatica")
    elif a.upper == "ADM":
        print("Administração")
    elif a.upper == "ELT":
        print("Eletrotécnica")
    else:
        break