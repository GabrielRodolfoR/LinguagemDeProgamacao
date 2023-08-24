n = int(input("1-Somar 2 Números"
                  "\n2-Diferença entre 2 números"
                  "\n3-Produto de 2 números"
                  "\n4-Divisão de 2 números"
                  "\nSelecione a opção: "))

n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))

if n == 1:
    res = n1+n2
elif n == 2:
    if n1>n2:
        res = n1-n2
    else:
        res = n2-n1
elif n == 3:
    res = n1*n2
elif n == 4 and (n1>0 or n1<0) and (n2>0 or n2<0):
    res = n1/n2

else:
    print("inválido")

print(f"resultado: {res}")