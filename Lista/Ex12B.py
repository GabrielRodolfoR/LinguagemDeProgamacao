filmes = []
jogos = []
livros = []
esportes = []
lista = ["filmes", "jogos", "livros", "esportes"]

for i in range(2):
    filmes.append(input("Adicionar algo a filmes: "))
    jogos.append(input("Adicionar algo a Jogos: "))
    livros.append(input("Adicionar algo a Livros: "))
    esportes.append(input("Adicionar algo a esportes: "))
print(f"{filmes}\n{jogos}\n{livros}\n{esportes}")

print(lista)

print(jogos[1])

del(esportes[0])
print(esportes)