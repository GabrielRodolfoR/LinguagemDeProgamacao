cidade = 5
dados = []

for i in range(cidade):
    print(f"Digite os dados da cidade {i+1}:")
    codigo = input("Código da cidade: ")
    veiculos = int(input("Número de veículos de passeio (em 1999): "))
    acidentes = int(input("Número de acidentes de trânsito com vítimas (em 1999): "))
    dados.append((codigo, veiculos, acidentes))

maior = -1
menor = float('inf')
maiorC = ""
menorC = ""

total = 0

for cidade, veiculos, acidentes in dados:
    indice = acidentes / veiculos

    if indice > maior:
        maior = indice
        maiorC = cidade

    if indice < menor:
        menor = indice
        menorC = cidade

    total += veiculos

media = total / cidade

print(f"O maior índice de acidentes de trânsito foi {maior:.2f} na cidade {maiorC}.")
print(f"O menor índice de acidentes de trânsito foi {menor:.2f} na cidade {menorC}.")
print(f"A média de veículos nas cinco cidades juntas é {media:.2f}.")