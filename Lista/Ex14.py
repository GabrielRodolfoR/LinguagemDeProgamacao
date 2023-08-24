lista = ["azul", "verde", "amarelo", "marrom"]
print(lista)

elemento = input("Digite um elemento da lista: ")
for i in lista:
    if elemento in lista:
        print(f"Posição: {lista.index(elemento)}")