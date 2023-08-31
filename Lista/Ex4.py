dado = input("Digite algo: ")

print(f"{type(dado)}\nNumero: {dado.isnumeric()}\nLetra: {dado.isalpha()}\nAlfanumérico: {dado.isalnum()}"
f"\nMinusculo: {dado.islower()}\nMaiusculo: {dado.isupper()}\nEspaço Vazio: {dado.isspace()}\nTitulo {dado.istitle()}")
