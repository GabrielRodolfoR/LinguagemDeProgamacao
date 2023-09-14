def soma(*n):
    soma = sum(n)
    tamanho = len(n)
    print(f"Valores: {n}, Soma: {soma}, quantidade de itens: {tamanho}")
    for i in n:
        print(i)
soma(2,4,5,6)
soma(2,3)