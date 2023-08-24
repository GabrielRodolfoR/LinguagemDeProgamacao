def main():
    while True:
        print("a. Lojas Tabajara")
        
        total = 0.0
        produtos = []
        
        while True:
            valor = float(input(f"b. Produto {len(produtos) + 1}: R$ "))
            if valor == 0:
                break
            total += valor
            produtos.append(valor)
        
        print("c. Produto 3: R$ 0")
        
        print(f"d. Total: R$ {total:.2f}")
        
        dinheiro = float(input("e. Dinheiro: R$ "))
        troco = dinheiro - total
        
        print(f"f. Troco: R$ {troco:.2f}")
        
        nova_compra = input("Realizar nova compra? (s/n): ")
        if nova_compra.lower() != "s":
            break

main()